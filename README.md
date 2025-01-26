# TableauKalk-l-SAT
Einfacher SAT - Tableau Kalkül Solver in Python

```Bash
Checking moderate SAT formula:
Current Branch: ((A ∨ B) ∧ ((¬(A) ∨ C) ∧ ((B ∨ ¬(C)) ∧ (¬(B) ∨ A))))
Current Branch: (A ∨ B), ((¬(A) ∨ C) ∧ ((B ∨ ¬(C)) ∧ (¬(B) ∨ A)))
Current Branch: ((B ∨ ¬(C)) ∧ (¬(B) ∨ A)), (¬(A) ∨ C), (A ∨ B)
Current Branch: (B ∨ ¬(C)), (¬(A) ∨ C), (A ∨ B), (¬(B) ∨ A)
  Current Branch: (B ∨ ¬(C)), A, (¬(A) ∨ C), (¬(B) ∨ A)
    Current Branch: A, (¬(A) ∨ C), (¬(B) ∨ A), B
      Current Branch: A, ¬(A), (¬(B) ∨ A), B
      ⊗ (Closed)
      Current Branch: C, A, (¬(B) ∨ A), B
        Current Branch: C, ¬(B), B, A
        ⊗ (Closed)
        Current Branch: C, B, A
        ✓ (Open Branch)
        Assignment: {'C': True, 'B': True, 'A': True}
True
Checking unsatisfiable SAT formula:
Current Branch: ((¬(A) ∨ B) ∧ ((¬(B) ∨ C) ∧ ((¬(C) ∨ A) ∧ (A ∧ ¬(A)))))
Current Branch: ((¬(B) ∨ C) ∧ ((¬(C) ∨ A) ∧ (A ∧ ¬(A)))), (¬(A) ∨ B)
Current Branch: (¬(A) ∨ B), ((¬(C) ∨ A) ∧ (A ∧ ¬(A))), (¬(B) ∨ C)
Current Branch: (¬(C) ∨ A), (¬(A) ∨ B), (A ∧ ¬(A)), (¬(B) ∨ C)
Current Branch: (¬(C) ∨ A), (¬(A) ∨ B), A, ¬(A), (¬(B) ∨ C)
⊗ (Closed)
False
```
