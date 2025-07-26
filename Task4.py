# Make a class called Car
class Car:
    # This runs when a new Car is made
    def __init__(self, model, color):
        self.model = model
        self.color = color

    # This shows the car's details
    def show_details(self):
        print(f"Car Model: {self.model}")
        print(f"Car Color: {self.color}")

    # This acts like the car is driving
    def drive(self):
        print(f"{self.model} is now driving!")

# Make two cars using the Car class
car1 = Car("Tesla Model S", "Red")
car2 = Car("BMW X5", "Black")

# Show the first car’s info and make it drive
car1.show_details()
car1.drive()

print()  # Adds a blank line

# Show the second car’s info and make it drive
car2.show_details()
car2.drive()