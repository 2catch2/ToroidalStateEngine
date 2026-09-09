import sys
from src.microcode_engine import run_microcode_matrix_simulation
from src.test_bench import run_master_test_bench

def main():
    print("=== ToroidalStateEngine Launcher ===")
    print("Select a simulation to run:\n")
    print("1. Microcode Overwrite Simulation")
    print("2. Master Torus Memory Block Test Bench\n")

    choice = input("Enter 1 or 2: ").strip()

    if choice == "1":
        print("\nLaunching Microcode Overwrite Simulation...\n")
        run_microcode_matrix_simulation()

    elif choice == "2":
        print("\nLaunching Master Torus Memory Block Test Bench...\n")
        run_master_test_bench()

    else:
        print("\nInvalid selection. Exiting.")
        sys.exit(1)

if __name__ == "__main__":
    main()
