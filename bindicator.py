import automationhat
from datetime import datetime, time

# Channel each light is wired to
RECYCLING_CHANNEL = 0
WASTE_CHANNEL = 1
GARDEN_CHANNEL = 2

# Start and end week numbers for garden waste collection
GARDEN_WASTE_WEEKS = (11, 49)


def is_after_lunchtime_wednesday_or_before_lunchtime_friday():
    """Checks if it's after Wednesday lunchtime or before Friday lunchtime."""
    now = datetime.now()
    lunchtime = time(12, 0)

    if now.weekday() == 2 and now.time() >= lunchtime:  # Wednesday afternoon
        return True
    if now.weekday() == 4 and now.time() < lunchtime:  # Before Friday lunchtime
        return True
    return False


def is_odd_week():
    """Returns True if the current week number is odd."""
    return datetime.now().isocalendar()[1] % 2 != 0


def is_garden_waste_collection_period():
    """Checks if the current week is within the garden waste collection period."""
    week_number = datetime.now().isocalendar()[1]
    return GARDEN_WASTE_WEEKS[0] <= week_number <= GARDEN_WASTE_WEEKS[1]


def determine_bin_status():
    """Determines which bins should be out based on the current week and schedule."""
    recycling_enabled = (
        not is_odd_week() and is_after_lunchtime_wednesday_or_before_lunchtime_friday()
    )
    waste_enabled = (
        is_odd_week() and is_after_lunchtime_wednesday_or_before_lunchtime_friday()
    )
    garden_enabled = (
        is_odd_week()
        and is_garden_waste_collection_period()
        and is_after_lunchtime_wednesday_or_before_lunchtime_friday()
    )
    return recycling_enabled, waste_enabled, garden_enabled


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
