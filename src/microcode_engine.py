# ========================================================
# MICROCODE STATE ENGINE SIMULATION WITH OVERWRITE LOOPS
# ========================================================

def run_microcode_matrix_simulation():
    past_ring = ["00"] * 8
    ring_index = 0

    future_stream = [
        "01","10","01","01","10","00","01","10",
        "10","10","00","10","01","01","00","01"
    ]

    microcode_opcodes = [
        "00","00","00","00","00","00","00","00",
        "01","11","01","00","01","11","00","01"
    ]

    print("=== STARTING MULTI-CYCLE OVERWRITE SIMULATION ===")

    for cycle in range(16):
        incoming = future_stream[cycle]
        current_past = past_ring[ring_index]
        opcode = microcode_opcodes[cycle]

        if opcode == "00":
            next_state = incoming if current_past == "00" else current_past
        elif opcode == "01":
            next_state = incoming
        elif opcode == "11":
            next_state = current_past
        else:
            next_state = current_past

        action_taken = "OVERWRITE" if next_state != current_past and current_past != "00" else "WRITE/HOLD"
        past_ring[ring_index] = next_state

        print(f"Cycle {cycle:02d} | Opcode: {opcode} | In: {incoming} | Past: {current_past} -> Next: {next_state} [{action_taken}]")
        if (cycle + 1) % 8 == 0 or cycle == 15:
            print(f"--> End of Loop Wave Ring State: {past_ring}\n")

        ring_index = (ring_index + 1) % len(past_ring)

    print("=== SIMULATION SEQUENCE COMPLETE ===")


if __name__ == "__main__":
    run_microcode_matrix_simulation()

