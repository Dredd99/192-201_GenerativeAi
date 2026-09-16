from rental import Vehicle, Renter, ElectricCar, Motorbike


# Create vehicles
car = Vehicle("Toyota", "Yaris", "1AB234")
electric = ElectricCar("Tesla", "Model 3", "EV123", 60)
bike = Motorbike("Honda", "CBR500R", "2AB345", 500)

# Create a renter
renter = Renter("John", 12345)

# Print vehicles
print(car)
print(electric)
print(bike)

# Rent and return a vehicle
car.rent()
print(car)

car.return_vehicle()
print(car)

# Test invalid renter information
try:
    bad_renter = Renter("", 12345)
except ValueError as e:
    print("Error:", e)

try:
    bad_renter = Renter("John", 0)
except ValueError as e:
    print("Error:", e)

# Polymorphism: different vehicle types in one list
vehicles = [car, electric, bike]

for vehicle in vehicles:
    print(vehicle)
