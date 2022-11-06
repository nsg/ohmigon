import math


def temp_to_kilo_ohm(temperature, table):

    # I found the values at page 26 at the Elomax 250 installation
    # and service document. The outdoor sensor has a different range
    # compared to the other sensors.

    lookup = {
        "outdoor": {
            -35: 64.2,
            -30: 47,
            -25: 34.7,
            -20: 25.9,
            -15: 19.5,
            -10: 14.8,
            -5: 11.4,
            0: 8.8,
            5: 6.8,
            10: 5.3,
            15: 4.2,
            20: 3.4,
            25: 2.7,
            30: 2.2,
        }
    }

    # The temperatures are undefined outside this range, for our use
    # it's just fine to set the maximum or minimum values.
    if temperature > 30:
        temperature = 30
    elif temperature < -35:
        temperature = -35

    if lookup[table].get(temperature):
        # Number found in the lookup table, just return it

        return lookup[table][temperature]
    else:
        # Calculate the number between two values, this assumes a
        # linear graph, with is not true, but with these small steps
        # this is a acceptable approximation for my use case.

        t_upper = math.ceil(temperature / 5) * 5
        t_lower = math.floor(temperature / 5) * 5
        t_range = (temperature - t_lower) / 5

        ohm_upper = temp_to_kilo_ohm(t_upper, table)
        ohm_lower = temp_to_kilo_ohm(t_lower, table)

        ohm_diff = ohm_lower - ohm_upper
        return round(temp_to_kilo_ohm(t_lower, table) - ohm_diff * t_range, 2)
