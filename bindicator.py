import automationhat
from binlogic import determine_bin_status


# Channel each light is wired to
RECYCLING_CHANNEL = 0
GARDEN_CHANNEL = 1
WASTE_CHANNEL = 2

def set_bin_lights(recycling, waste, garden):
    """Sets the automation hat outputs based on bin status."""
    automationhat.output[RECYCLING_CHANNEL].write(recycling)
    automationhat.output[WASTE_CHANNEL].write(waste)
    automationhat.output[GARDEN_CHANNEL].write(garden)
    print(f"RECYCLING = {recycling}")
    print(f"WASTE = {waste}")
    print(f"GARDEN = {garden}")


# Main logic
if __name__ == "__main__":
    recycling, waste, garden = determine_bin_status()
    set_bin_lights(recycling, waste, garden)
