# Simulation Flow

## microcode_engine.py
Runs a 16‑cycle overwrite simulation demonstrating:
- ring traversal
- opcode effects
- overwrite vs hold
- end‑of‑loop snapshots

## master_torus_memory.py
Implements the unified toroidal memory‑process block:
- angle‑map addressing
- stack‑pointer traversal
- tri‑state bus output
- neighbor‑healing logic
- global reset behavior

## test_bench.py
Provides a hardware‑style execution trace.
