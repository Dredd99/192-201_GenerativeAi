class Vehicle:
    def __init__(self, make, model, plate):
        self.make = make
        self.model = model
        self.plate = plate
        self.is_rented = False

    def rent(self):
        self.is_rented = True

    def return_vehicle(self):
        self.is_rented = False

    def __str__(self):
        status = "rented" if self.is_rented else "available"
        return f"{self.make} {self.model} ({self.plate}) [{status}]"
