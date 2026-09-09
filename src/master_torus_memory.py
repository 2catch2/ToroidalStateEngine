# =====================================================================
# UNIFIED MASTER SYSTEM TEMPLATE: GLOBAL RESET & CONCENTRIC POWER ADAPT
# =====================================================================

class MasterTorusMemoryBlock:
    def __init__(self, size=8):
        self.size = size
        self.past_ring = ["00"] * size
        self.ring_index = 0
        self.angle_map = {"000":0,"001":1,"010":2,"011":3,"100":4,"101":5,"110":6,"111":7}

    def execute_clock_cycle(self, incoming_data, microcode_opcode, stack_en=1, cpu_address="000", read_en=0, reset_n=1):

        if reset_n == 0:
            self.past_ring = ["00"] * self.size
            self.ring_index = 0
            return "Hi-Z", "⚡ [GLOBAL RESET_N ACTIVE] All slots flushed to '00' (Neutral Potentials)"

        target_slot = self.angle_map.get(cpu_address, 0) if stack_en == 0 else self.ring_index
        current_past = self.past_ring[target_slot]

        if incoming_data == "11" or current_past == "11":
            neighbor_index = (target_slot - 1) % self.size
            next_state = self.past_ring[neighbor_index]
        else:
            if microcode_opcode == "00":
                next_state = incoming_data if current_past == "00" else current_past
            elif microcode_opcode == "01":
                next_state = incoming_data
            elif microcode_opcode == "11":
                next_state = current_past
            else:
                next_state = current_past

        self.past_ring[target_slot] = next_state

        if read_en == 1:
            read_slot = self.angle_map.get(cpu_address, 0) if stack_en == 0 else target_slot
            output_bus = self.past_ring[read_slot]
            telemetry = f"📋 READ Slot {read_slot} Value: {output_bus}"
        else:
            output_bus = "Hi-Z"
            telemetry = "💤 READ BUS DISABLED (High-Impedance Mode)"

        if stack_en == 1:
            self.ring_index = (self.ring_index + 1) % self.size

        return output_bus, telemetry

