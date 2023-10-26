import datetime

def advance_time(character, hours):
    current_day, current_time = character['time']
    hours_to_add = current_time.hour + hours

    # Calculate days to add
    days_to_add = hours_to_add // 24

    # Calculate the new hour
    new_hour = (current_time.hour + hours) % 24

    # Update the day and hour
    current_day += days_to_add
    current_time = current_time.replace(hour=new_hour)

    # Update character's time
    character['time'] = (current_day, current_time)
