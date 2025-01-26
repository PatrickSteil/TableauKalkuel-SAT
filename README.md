# TableauKalk-l-SAT
Einfacher SAT - Tableau Kalkül Solver in Python

```Bash
Checking moderate SAT formula:
Current Branch: ((A ∨ B) ∧ ((¬(A) ∨ C) ∧ ((B ∨ ¬(C)) ∧ (¬(B) ∨ A))))
  Current Branch: (A ∨ B), ((¬(A) ∨ C) ∧ ((B ∨ ¬(C)) ∧ (¬(B) ∨ A)))
    Current Branch: ((B ∨ ¬(C)) ∧ (¬(B) ∨ A)), (¬(A) ∨ C), (A ∨ B)
      Current Branch: (¬(B) ∨ A), (B ∨ ¬(C)), (¬(A) ∨ C), (A ∨ B)
        Current Branch: (¬(B) ∨ A), (B ∨ ¬(C)), (¬(A) ∨ C), A
          Current Branch: (B ∨ ¬(C)), (¬(A) ∨ C), ¬(B), A
            Current Branch: B, (¬(A) ∨ C), ¬(B), A
            ⊗ (Closed)
            Current Branch: (¬(A) ∨ C), ¬(B), A, ¬(C)
              Current Branch: ¬(A), ¬(B), A, ¬(C)
              ⊗ (Closed)
              Current Branch: C, ¬(B), A, ¬(C)
              ⊗ (Closed)
          Current Branch: (B ∨ ¬(C)), (¬(A) ∨ C), A
            Current Branch: B, (¬(A) ∨ C), A
              Current Branch: B, ¬(A), A
              ⊗ (Closed)
              Current Branch: B, C, A
              ✓ (Open Branch)
              Assignment: {'B': True, 'C': True, 'A': True}
True
Checking unsatisfiable SAT formula:
Current Branch: ((¬(A) ∨ B) ∧ ((¬(B) ∨ C) ∧ ((¬(C) ∨ A) ∧ (A ∧ ¬(A)))))
  Current Branch: ((¬(B) ∨ C) ∧ ((¬(C) ∨ A) ∧ (A ∧ ¬(A)))), (¬(A) ∨ B)
    Current Branch: ((¬(C) ∨ A) ∧ (A ∧ ¬(A))), (¬(B) ∨ C), (¬(A) ∨ B)
      Current Branch: (¬(C) ∨ A), (A ∧ ¬(A)), (¬(B) ∨ C), (¬(A) ∨ B)
        Current Branch: (¬(B) ∨ C), (¬(C) ∨ A), A, ¬(A), (¬(A) ∨ B)
        ⊗ (Closed)
False
```
