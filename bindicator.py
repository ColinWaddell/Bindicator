import automationhat
from datetime import datetime, time

RECYCLING = 0
WASTE = 1
GARDEN = 2

GARDEN_WEEKS = (11, 49) # start and end week numbers

def is_after_lunchtime_wednesday_or_before_lunchtime_friday():
    now = datetime.now()
    current_day = now.weekday()
    current_time = now.time()
    
    # Define lunchtime as 12:00 PM
    lunchtime = time(12, 0)

    # Check conditions
    if (current_day == 2 and current_time >= lunchtime):  # Wednesday afternoon onwards
        return True
    elif (current_day == 4 and current_time < lunchtime):  # Before Friday lunchtime
        return True
    return False

def is_odd_week():
    week_number = datetime.now().isocalendar()[1]  # ISO week number
    return week_number % 2 != 0


def is_garden_waste_period():
    week_number = datetime.now().isocalendar()[1]  # ISO week number
    return GARDEN_WEEKS[0] <= week_number <= GARDEN_WEEKS[1]
    

# Check which bins should be out
recycling_enabled = not is_odd_week()
waste_enabled = is_odd_week()
garden_enabled = is_odd_week() and is_garden_waste_period()

# Set lights
automationhat.output[RECYCLING].write(recycling_enabled)
automationhat.output[WASTE].write(waste_enabled)
automationhat.output[GARDEN].write(garden_enabled)

# Report status
print(f"RECYCLING = {recycling_enabled}")
print(f"WASTE = {waste_enabled}")
print(f"GARDEN = {garden_enabled}")