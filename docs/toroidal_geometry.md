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
# Toroidal Geometry — ASCII Expansion

The ToroidalStateEngine uses an 8‑slot toroidal ring as its core
memory‑process manifold. This ASCII layout shows the ring, its
neighbor relationships, and the circulation path of the pointer.

        [0] ── [1] ── [2] ── [3]
         │                 │
        [7] ── [6] ── [5] ── [4]

Pointer traversal follows a continuous loop:

0 → 1 → 2 → 3 → 4 → 5 → 6 → 7 → 0 → ...

Each slot can hold:
- state values
- microcode tags
- protected history invariants

## Neighbor Map

Each slot has two direct neighbors:

- 0 ↔ 1 and 7  
- 1 ↔ 0 and 2  
- 2 ↔ 1 and 3  
- 3 ↔ 2 and 4  
- 4 ↔ 3 and 5  
- 5 ↔ 4 and 6  
- 6 ↔ 5 and 7  
- 7 ↔ 6 and 0

This neighbor structure enables:
- overwrite wave propagation  
- [neighbor healing](ca://s?q=Explain_neighbor_healing)  
- [shock‑front movement](ca://s?q=Explain_shock_front_behavior)  
- [protected invariant anchoring](ca://s?q=Explain_protected_invariant_behavior)

## Pointer Movement Timeline

Cycle progression (example):

Cycle 00 → pointer at slot 0  
Cycle 01 → pointer at slot 1  
Cycle 02 → pointer at slot 2  
Cycle 03 → pointer at slot 3  
Cycle 04 → pointer at slot 4  
Cycle 05 → pointer at slot 5  
Cycle 06 → pointer at slot 6  
Cycle 07 → pointer at slot 7  
Cycle 08 → pointer wraps to slot 0

This geometric traversal replaces the traditional instruction pointer
with a circulating spatial index.

