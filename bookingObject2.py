# main.py (or bookingObject.py)

from bookingClass import booking

# Define a list of reservation types
reservation_types = ["Standard", "Premium", "VIP", "Family", "Business"]

# Function to display reservation types and get a valid choice
def get_reservation_type():
    print("Please select a reservation type from the following options:")
    for i, type in enumerate(reservation_types, 1):
        print(f"{i}. {type}")
    while True:
        try:
            choice = int(input("Enter the number corresponding to your choice: "))
            if 1 <= choice <= len(reservation_types):
                return reservation_types[choice - 1]
            else:
                print("Invalid choice. Please select a number from the list.")
        except ValueError:
            print("Invalid input. Please enter a number.")

# Collect input from the user
name = input("Enter name: ")
reservationType = get_reservation_type()
numberOfGuests = input("Enter number of guests: ")
Time = input("Enter time of appointment: ")

# Create an instance of the booking class with the provided inputs
booking_instance = booking(name, reservationType, numberOfGuests, Time)

# Open the file in append mode
with open("Reservations.txt", "a") as Booked:
    # Write the booking information to the file
    Booked.write(f"Name: {booking_instance.name}\n")
    Booked.write(f"Reservation Type: {booking_instance.reservationType}\n")
    Booked.write(f"Number of Guests: {booking_instance.numberOfGuests}\n")
    Booked.write(f"Time: {booking_instance.Time}\n")
    Booked.write("\n")  # Add a newline for better readability