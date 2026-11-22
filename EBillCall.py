
fix_30 = 80
fix_60 = 210
fix_90 = 400
fix_120 = 1000
fix_180 = 1500

unit0_30 = 5
unit31_60 = 9
unit61_90 = 20
unit91_120 = 28
unit121_180 = 44
unitab180 = 32.5


def calculate(unit):

    if unit == 0:
        return fix_30

    elif unit <= 30:
        bill = fix_30 + unit * unit0_30

    elif unit <= 60:
        bill = fix_60 + (unit - 30) * unit31_60 + 30 * unit0_30

    elif unit <= 90:
        bill = fix_90 + (unit - 60) * unit61_90 + 30 * unit0_30 + 30 * unit31_60

    elif unit <= 120:
        bill = fix_120 + (unit - 90) * unit91_120 + 30 * unit0_30 + 30 * unit31_60 + 30 * unit61_90

    elif unit <= 180:
        bill = fix_180 + (unit - 120) * unit121_180 + 30 * unit0_30 + 30 * unit31_60 + 30 * unit61_90 + 30 * unit91_120

    else:
        bill = fix_180 + (unit - 180) * unitab180 + 30 * unit0_30 + 30 * unit31_60 + 30 * unit61_90 + 30 * unit91_120 + 60 * unit121_180

    return round(bill, 2)


while True:

    try:
        # Read previous meter reading
        try:
            with open("meter_reading.txt", "r") as file:
                saved_reading = file.read().strip()

            if saved_reading:
                FormerEBordNumber = int(saved_reading)
                first_time = False
            else:
                first_time = True

        except FileNotFoundError:
            first_time = True

        # Input new meter reading
        while True:
            NewEBordNumber = int(input("\nEnter your EB meter reading: "))

            if NewEBordNumber < 0:
                print("Error: Meter reading cannot be negative.")

            elif not first_time and NewEBordNumber < FormerEBordNumber:
                print("Error: New reading cannot be smaller than previous reading.")

            else:
                break

        # First reading
        if first_time:

            with open("meter_reading.txt", "w") as file:
                file.write(str(NewEBordNumber))

            print("First meter reading saved successfully!")

        # Calculate bill
        else:

            num_of_unit = NewEBordNumber - FormerEBordNumber

            price = calculate(num_of_unit)

            print(f"\nUnits consumed: {num_of_unit}")
            print(f"Your electricity bill is Rs. {price:.2f}")

            # Update saved reading
            with open("meter_reading.txt", "w") as file:
                file.write(str(NewEBordNumber))

            print("New meter reading saved successfully!")

        # Continue or exit
        while True:
            try:
                choice = int(input("\nDo you want to continue?\n1) Yes\n2) No\nEnter choice: "))

                if choice == 1 or choice == 2:
                    break

                else:
                    print("Please enter 1 or 2.")

            except ValueError:
                print("Please enter a valid number.")

        if choice == 2:
            print("Program ended.")
            break

    except ValueError:
        print("Please enter a valid whole number.")

    except OSError:
        print("File error: Unable to access meter_reading.txt")
        break
