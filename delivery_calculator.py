from datetime import datetime
import math
import calendar


# Returns the surcharge in Euros from a cart under a 10€ order.
def surcharge(cart):
    if cart < 10:
        return round(10 - cart, 2)
    return 0


# Returns the delivery fee in Euros from the distance in meters travelled.
def travel_fee(dist):
    return 2 + round(math.ceil((dist - 1000) / 500), 2)


# Returns the surcharge in Euros from the number of items ordered.
def item_surcharge(amount):
    fee = 0
    if amount >= 12:
        fee += 1.2
    if amount >= 5:
        fee += (amount - 4) * 0.5
    return fee


# Returns True if there is a Friday rush.
def is_rush(date_and_time):
    formatted_time = date_and_time.replace("Z", "")
    date_time_obj = datetime.fromisoformat(formatted_time)
    date_obj = date_time_obj.date()

    week_day = calendar.day_name[date_obj.weekday()]
    hours = date_time_obj.hour

    if week_day == "Friday" and 15 <= hours < 19:
        return True
    return False
