# State Transition Diagrams

This document gives simple ASCII state‑transition views for the
ToroidalStateEngine under different microcode behaviors.

## 1. Passive Collapse (00) — Write‑If‑Empty

Initial ring (slots 0–7):

[0] 0   [1] 0   [2] 1   [3] 0
[4] 0   [5] 0   [6] 0   [7] 0

Incoming value at pointer: 1  
Rule: write only if slot == 0

Cycle 0 (pointer at 2): slot 2 already 1 → hold  
Cycle 1 (pointer at 3): slot 3 = 0 → becomes 1  
Cycle 2 (pointer at 4): slot 4 = 0 → becomes 1  

Resulting wave:

[0] 0   [1] 0   [2] 1   [3] 1
[4] 1   [5] 0   [6] 0   [7] 0

## 2. Forced Overwrite (01) — Write‑Always

Initial ring:

[0] 0   [1] 0   [2] 1   [3] 0
[4] 0   [5] 0   [6] 0   [7] 0

Incoming value at pointer: 1  
Rule: always overwrite

Cycle 0 (pointer at 2): slot 2 → 1 (unchanged)  
Cycle 1 (pointer at 3): slot 3 → 1  
Cycle 2 (pointer at 4): slot 4 → 1  
Cycle 3 (pointer at 5): slot 5 → 1  

Resulting front:

[0] 0   [1] 0   [2] 1   [3] 1
[4] 1   [5] 1   [6] 0   [7] 0

## 3. Protected History (11) — Hold‑Always

Initial ring:

[0] 0   [1] 0   [2] 1   [3] 1
[4] 1   [5] 0   [6] 0   [7] 0

Incoming value at pointer: 0  
Rule: never overwrite

Pointer moves, but slots marked as protected history do not change:

Cycle 0 (pointer at 2): slot 2 stays 1  
Cycle 1 (pointer at 3): slot 3 stays 1  
Cycle 2 (pointer at 4): slot 4 stays 1  

Result:

[0] 0   [1] 0   [2] 1   [3] 1
[4] 1   [5] 0   [6] 0   [7] 0

These diagrams show how different microcode “physics” produce distinct
propagation and stability behaviors on the same toroidal ring.
