LENGTH_TO_METERS = {
    "mm": 0.001, "cm": 0.01, "m": 1.0, "km": 1000.0,
    "inch": 0.0254, "ft": 0.3048, "mile": 1609.34,
}

WEIGHT_TO_GRAMS = {
    "mg": 0.001, "g": 1.0, "kg": 1000.0,
    "oz": 28.3495, "lb": 453.592,
}


def convert_length(value, from_unit, to_unit):
    meters = value * LENGTH_TO_METERS[from_unit]
    return meters / LENGTH_TO_METERS[to_unit]


def convert_weight(value, from_unit, to_unit):
    grams = value * WEIGHT_TO_GRAMS[from_unit]
    return grams / WEIGHT_TO_GRAMS[to_unit]


def convert_temperature(value, from_unit, to_unit):
    if from_unit == "C":
        celsius = value
    elif from_unit == "F":
        celsius = (value - 32) * 5 / 9
    elif from_unit == "K":
        celsius = value - 273.15
    else:
        raise ValueError("Unknown temperature unit")

    if to_unit == "C":
        return celsius
    elif to_unit == "F":
        return celsius * 9 / 5 + 32
    elif to_unit == "K":
        return celsius + 273.15
    else:
        raise ValueError("Unknown temperature unit")