| **Opcode** | **Name** | **Behavior Summary** | **Detailed Effect** |
| --- | --- | --- | --- |
| **[00 — Passive Collapse](ca://s?q=Explain_passive_collapse_opcode)** | Passive Collapse | Write only if the slot is empty | The cell adopts the incoming value *only* when its current state is ``0``. If the slot is occupied, it holds its value. This creates gentle, non‑destructive propagation. |
| **[01 — Forced Overwrite](ca://s?q=Explain_forced_overwrite_opcode)** | Forced Overwrite | Always overwrite the slot | The incoming value replaces whatever is present, regardless of state. This produces strong overwrite waves and shock‑front propagation. |
| **[11 — Protected History](ca://s?q=Explain_protected_history_opcode)** | Protected History | Never overwrite; always hold | The cell refuses incoming writes. It preserves its state across cycles, forming invariants and “memory anchors” inside the toroidal fabric. |
