from collections import defaultdict
from functools import lru_cache

class Formula:
    def __repr__(self) -> str:
        return str(self)

class Var(Formula):
    def __init__(self, name: str) -> None:
        self.name: str = name

    def __repr__(self) -> str:
        return self.name

class Not(Formula):
    def __init__(self, formula: Formula) -> None:
        self.formula: Formula = formula

    def __repr__(self) -> str:
        return f"¬({self.formula})"

class And(Formula):
    def __init__(self, left: Formula, right: Formula) -> None:
        self.left: Formula = left
        self.right: Formula = right

    def __repr__(self) -> str:
        return f"({self.left} ∧ {self.right})"

class Or(Formula):
    def __init__(self, left: Formula, right: Formula) -> None:
        self.left: Formula = left
        self.right: Formula = right

    def __repr__(self) -> str:
        return f"({self.left} ∨ {self.right})"

class Implies(Formula):
    def __init__(self, left: Formula, right: Formula) -> None:
        self.left: Formula = left
        self.right: Formula = right

    def __repr__(self) -> str:
        return f"({self.left} → {self.right})"

@lru_cache(maxsize=None)
def expand_tableau(formula_set: frozenset, depth: int = 0) -> bool:
    formula_sorted = sorted(
        formula_set,
        key=lambda f: (
            isinstance(f, Var),
            isinstance(f, Not) and isinstance(f.formula, Var),
            isinstance(f, Not) and isinstance(f.formula, Implies),
            isinstance(f, Not) and isinstance(f.formula, Or),
            isinstance(f, And),
            isinstance(f, Or) or isinstance(f, Implies),
            -len(str(f))
        ),
        reverse=True
    )

    print("  " * depth + f"Current Branch: {', '.join(map(str, formula_set))}")
    
    ## is there a confluct on the current branch?
    if any(isinstance(f, Not) and f.formula in formula_set for f in formula_set):
        print("  " * depth + "⊗ (Closed)")
        return False

    new_branches = []
    for f in formula_sorted:
        if isinstance(f, Not) and isinstance(f.formula, Not):
            new_branches.append(frozenset(formula_set - {f} | {f.formula.formula}))
            break
        elif isinstance(f, And):
            new_branches.append(frozenset(formula_set - {f} | {f.left, f.right}))
            break
        elif isinstance(f, Or):
            new_branches.append(frozenset(formula_set - {f} | {f.left}))
            new_branches.append(frozenset(formula_set - {f} | {f.right}))
            break
        elif isinstance(f, Implies):
            new_branches.append(frozenset(formula_set - {f} | {Not(f.left)}))
            new_branches.append(frozenset(formula_set - {f} | {f.right}))
            break
        elif isinstance(f, Not) and isinstance(f.formula, And):
            new_branches.append(frozenset(formula_set - {f} | {Or(Not(f.formula.left), Not(f.formula.right))}))
            break
        elif isinstance(f, Not) and isinstance(f.formula, Or):
            new_branches.append(frozenset(formula_set - {f} | {Not(f.formula.left), Not(f.formula.right)}))
            break
        elif isinstance(f, Not) and isinstance(f.formula, Implies):
            new_branches.append(frozenset(formula_set - {f} | {f.formula.left, Not(f.formula.right)}))
            break

    if not new_branches:
        print("  " * depth + "✓ (Open Branch)")
        assignment = compute_assignment(formula_set)
        print("  " * depth + f"Assignment: {assignment}")
        return True

    return any(expand_tableau(branch, depth + 1) for branch in new_branches)

def compute_assignment(formula_set: frozenset) -> dict:
    assignment = {}
    for f in formula_set:
        if isinstance(f, Not) and isinstance(f.formula, Var):
            assignment[f.formula.name] = False
        elif isinstance(f, Var):
            assignment[f.name] = True
    return assignment

def is_satisfiable(formula: Formula) -> bool:
    return expand_tableau(frozenset([formula]))

def is_tautology(formula: Formula) -> bool:
    negated_formula = Not(formula)
    print(f"### Checking if formula is a tautology: {formula} ###")
    print(f"Negating formula: {negated_formula}")
    result = is_satisfiable(negated_formula)
    if result:
        print("❌ Not a tautology (Counterexample found).")
    else:
        print("✅ Tautology (All branches closed).")
    return not result

A = Var("A")
B = Var("B")
C = Var("C")
D = Var("D")

large_formula = And(
    Or(A, B),
    And(
        Or(Not(B), C),
        And(
            Implies(A, C),
            And(
                Implies(C, D),
                And(
                    Or(Not(A), Not(D)),
                    And(
                        Or(Not(C), D),
                        And(
                            Implies(Not(B), A),
                            And(
                                Or(C, D),
                                And(
                                    Implies(Not(C), A),
                                    Or(Not(D), Not(A))
                                )
                            )
                        )
                    )
                )
            )
        )
    )
)

print("Checking large SAT formula:")
print(is_satisfiable(large_formula))

unsat_formula = And(
    Or(Not(A), B),
    And(
        Or(Not(B), C),
        And(
            Or(Not(C), A),
            And(
                A,
                Not(A)
            )
        )
    )
)

print("Checking unsatisfiable SAT formula:")
print(is_satisfiable(unsat_formula))
