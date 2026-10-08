from converters import (
    convert_length, convert_weight, convert_temperature,
    LENGTH_TO_METERS, WEIGHT_TO_GRAMS,
)


def show_menu():
    print("\n=== Unit Converter ===")
    print("1. Length")
    print("2. Weight")
    print("3. Temperature")
    print("4. Quit")


def handle_length():
    print(f"Available units: {', '.join(LENGTH_TO_METERS.keys())}")
    from_unit = input("From unit: ").strip().lower()
    to_unit = input("To unit: ").strip().lower()
    if from_unit not in LENGTH_TO_METERS or to_unit not in LENGTH_TO_METERS:
        print("Invalid unit(s).")
        return
    value = float(input("Value: "))
    result = convert_length(value, from_unit, to_unit)
    print(f"{value} {from_unit} = {result:.4f} {to_unit}")


def handle_weight():
    print(f"Available units: {', '.join(WEIGHT_TO_GRAMS.keys())}")
    from_unit = input("From unit: ").strip().lower()
    to_unit = input("To unit: ").strip().lower()
    if from_unit not in WEIGHT_TO_GRAMS or to_unit not in WEIGHT_TO_GRAMS:
        print("Invalid unit(s).")
        return
    value = float(input("Value: "))
    result = convert_weight(value, from_unit, to_unit)
    print(f"{value} {from_unit} = {result:.4f} {to_unit}")


def handle_temperature():
    print("Available units: C, F, K")
    from_unit = input("From unit: ").strip().upper()
    to_unit = input("To unit: ").strip().upper()
    if from_unit not in ("C", "F", "K") or to_unit not in ("C", "F", "K"):
        print("Invalid unit(s).")
        return
    value = float(input("Value: "))
    result = convert_temperature(value, from_unit, to_unit)
    print(f"{value}°{from_unit} = {result:.2f}°{to_unit}")


def main():
    handlers = {"1": handle_length, "2": handle_weight, "3": handle_temperature}

    while True:
        show_menu()
        choice = input("Choose an option: ").strip()

        if choice == "4":
            print("Goodbye!")
            break
        if choice not in handlers:
            print("Invalid option.")
            continue

        try:
            handlers[choice]()
        except ValueError as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()