# TableauKalkül-SAT
Einfacher SAT - Tableau Kalkül Solver in Python. Gedacht um sich die Schritte zu visualisieren.

```Bash
Checking [(A -> B) -> ((B -> C) -> (A -> C))]:
### Checking if formula is a tautology: ((A → B) → ((B → C) → (A → C))) ###
Negating formula: ¬(((A → B) → ((B → C) → (A → C))))
Current Branch: ¬(((A → B) → ((B → C) → (A → C))))
Current Branch: ¬(((B → C) → (A → C))), (A → B)
Current Branch: (A → B), (B → C), ¬((A → C))
Current Branch: A, (A → B), (B → C), ¬(C)
  Current Branch: A, ¬(A), (B → C), ¬(C)
  ⊗ (Closed)
  Current Branch: A, B, (B → C), ¬(C)
    Current Branch: A, ¬(B), B, ¬(C)
    ⊗ (Closed)
    Current Branch: A, B, ¬(C), C
    ⊗ (Closed)
✅ Tautology (All branches closed).
True
Checking moderate SAT formula:
Current Branch: ((A ∨ B) ∧ ((¬(A) ∨ C) ∧ ((B ∨ ¬(C)) ∧ (¬(B) ∨ A))))
Current Branch: ((¬(A) ∨ C) ∧ ((B ∨ ¬(C)) ∧ (¬(B) ∨ A))), (A ∨ B)
Current Branch: (A ∨ B), (¬(A) ∨ C), ((B ∨ ¬(C)) ∧ (¬(B) ∨ A))
Current Branch: (B ∨ ¬(C)), (A ∨ B), (¬(B) ∨ A), (¬(A) ∨ C)
  Current Branch: A, (B ∨ ¬(C)), (¬(B) ∨ A), (¬(A) ∨ C)
    Current Branch: A, (¬(B) ∨ A), (¬(A) ∨ C), B
      Current Branch: A, (¬(A) ∨ C), B, ¬(B)
      ⊗ (Closed)
      Current Branch: A, (¬(A) ∨ C), B
        Current Branch: A, B, ¬(A)
        ⊗ (Closed)
        Current Branch: A, B, C
        ✓ (Open Branch)
Assignment: {'A': True, 'B': True, 'C': True}
True
Checking unsatisfiable SAT formula:
Current Branch: ((¬(A) ∨ B) ∧ ((¬(B) ∨ C) ∧ ((¬(C) ∨ A) ∧ (A ∧ ¬(A)))))
Current Branch: (¬(A) ∨ B), ((¬(B) ∨ C) ∧ ((¬(C) ∨ A) ∧ (A ∧ ¬(A))))
Current Branch: (¬(A) ∨ B), (¬(B) ∨ C), ((¬(C) ∨ A) ∧ (A ∧ ¬(A)))
Current Branch: (¬(C) ∨ A), (¬(A) ∨ B), (¬(B) ∨ C), (A ∧ ¬(A))
Current Branch: ¬(A), (¬(B) ∨ C), A, (¬(C) ∨ A), (¬(A) ∨ B)
⊗ (Closed)
False
```
