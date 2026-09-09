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

# Pointer Movement Timeline

The ToroidalStateEngine uses a circulating pointer instead of a
traditional instruction counter. Each cycle advances the pointer
to the next slot on the ring.

Below is the 8‑slot toroidal ring:

        [0] ── [1] ── [2] ── [3]
         │                 │
        [7] ── [6] ── [5] ── [4]

## Cycle-by-Cycle Pointer Movement

Cycle 00 → pointer at slot [0]  
Cycle 01 → pointer at slot [1]  
Cycle 02 → pointer at slot [2]  
Cycle 03 → pointer at slot [3]  
Cycle 04 → pointer at slot [4]  
Cycle 05 → pointer at slot [5]  
Cycle 06 → pointer at slot [6]  
Cycle 07 → pointer at slot [7]  
Cycle 08 → pointer wraps to slot [0]  
Cycle 09 → pointer at slot [1]  
Cycle 10 → pointer at slot [2]  
...continues indefinitely

## Visual Timeline

Cycle:   00  01  02  03  04  05  06  07  08  09  10  
Pointer:  0 → 1 → 2 → 3 → 4 → 5 → 6 → 7 → 0 → 1 → 2

This geometric traversal defines execution order.  
Every microcode rule is applied at the pointer’s current slot.

## Why This Matters

- It creates **deterministic circulation**  
- It ensures **every slot participates**  
- It produces **wave-like propagation**  
- It replaces the CPU’s “program counter” with **geometry-driven execution**

Pointer movement is the heartbeat of the ToroidalStateEngine.
