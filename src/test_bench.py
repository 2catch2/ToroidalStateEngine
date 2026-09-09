from master_torus_memory import MasterTorusMemoryBlock

def run_master_test_bench():
    engine = MasterTorusMemoryBlock()

    execution_profile = [
        ("01","01",1,"000",1,1),
        ("10","01",1,"000",1,1),
        ("01","01",1,"000",1,1),
        ("00","11",1,"000",0,0),
        ("01","00",1,"000",1,1),
        ("10","01",1,"000",1,1),
    ]

    print("=== EXECUTING UNIFIED MASTER SIMULATION PROFILE ===\n")
    for cycle, (incoming, opcode, stack_en, cpu_addr, read_en, reset_n) in enumerate(execution_profile):
        bus_out, log = engine.execute_clock_cycle(incoming, opcode, stack_en, cpu_addr, read_en, reset_n)
        print(f"Cycle {cycle:02d} | Hardware Pin Output: [{bus_out}]")
        print(f"         ├─ Tracker: {log}")
        print(f"         └─ Memory Ring Grid Array: {engine.past_ring}\n")

    print("=====================================================")


if __name__ == "__main__":
    run_master_test_bench()
