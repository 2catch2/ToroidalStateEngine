# Toroidal Geometry

Below is a conceptual ASCII diagram of the 8‑slot toroidal ring:

        [0] — [1] — [2] — [3]
          |               |
        [7] — [6] — [5] — [4]

The ring pointer moves around this loop, driving execution.
# Toroidal Geometry — ASCII Layout

Below is a conceptual ASCII diagram of the 8‑slot toroidal ring used
in the current prototypes:

        [0] ── [1] ── [2] ── [3]
         │                 │
        [7] ── [6] ── [5] ── [4]

The ring pointer circulates through these indices:

0 → 1 → 2 → 3 → 4 → 5 → 6 → 7 → 0 → ...

Each slot can hold:
- state values
- microcode tags
- history / protected invariants
- 
