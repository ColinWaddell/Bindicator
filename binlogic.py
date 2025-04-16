import datetime


# Start and end week numbers for garden waste collection
GARDEN_WASTE_WEEKS = (11, 46)

now = datetime.datetime.now()

def update_now(new_now):
    """Updates the current datetime for testing purposes."""
    global now
    now = new_now

def is_after_lunchtime_wednesday_or_before_lunchtime_thursday():
    """Checks if it's after Wednesday lunchtime or before Thursday lunchtime."""
    lunchtime = datetime.time(12, 0)

    if now.weekday() == 2 and now.time() >= lunchtime:  # After Wednesday afternoon
        return True
    if now.weekday() == 3 and now.time() < lunchtime:  # Before Thursday lunchtime
        return True
    return False


def is_odd_week():
    """Returns True if the current week number is odd."""
    return now.isocalendar()[1] % 2 != 0


def is_garden_waste_collection_period():
    """Checks if the current week is within the garden waste collection period."""
    week_number = now.isocalendar()[1]
    return GARDEN_WASTE_WEEKS[0] <= week_number <= GARDEN_WASTE_WEEKS[1]


def determine_bin_status():
    """Determines which bins should be out based on the current week and schedule."""
    recycling_enabled = (
        not is_odd_week() and is_after_lunchtime_wednesday_or_before_lunchtime_thursday()
    )
    waste_enabled = (
        is_odd_week() and is_after_lunchtime_wednesday_or_before_lunchtime_thursday()
    )
    garden_enabled = (
        is_odd_week()
        and is_garden_waste_collection_period()
        and is_after_lunchtime_wednesday_or_before_lunchtime_thursday()
    )
    return recycling_enabled, waste_enabled, garden_enabled

# Main logic
if __name__ == "__main__":
    # Define the number of past and future days to consider
    past_days = 3
    future_days = 3

    # Get the current date
    current_date = datetime.date.today()

    print("| Date       | Recycling | Waste | Garden |")
    print("|------------+-----------+-------+--------|")

    # Loop over the past and future days
    for i in range(-past_days, future_days + 1):
        # Calculate the date to consider
        date = current_date + datetime.timedelta(days=i)
        
        # Update the current datetime for testing purposes
        update_now(datetime.datetime.combine(date, now.time()))
        
        # Determine the bin status for the current date
        recycling, waste, garden = determine_bin_status()
        
        # Print the bin status for the current date
        print(f"| {date.isoformat()} |  ", end="")
        print("   x     |" if recycling else "         |", end="")
        print("   x   |" if waste else "       |", end="")
        print("    x   |" if garden else "        |")
