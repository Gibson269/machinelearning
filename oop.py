### Vehicle Management System

class Vehicle:
    #Creating the instant variable
    def __init__(self, brand, model, year):
        self.brand=brand
        self.model=model
        self.year=int(year)
        #return
    
    def display_info (self):
        print(f"Your car info is Brand : {self.brand}, Model : {self.model}, year: {self.year}")

class Car (Vehicle):
    # Inheriting everything from Vehicle
    def __init__(self, brand, model, year, fuel_type):
        super().__init__(brand, model, year)
        self.fuel_type=fuel_type

    def display_info(self):
        print(f"Vehicle Brand: {self.brand}, Model : {self.model}, year: {self.year}, Fuel Type: {self.fuel_type}")        
    
class Bike (Vehicle):
    def __init__(self, brand, model, year, type_of_bike):
        super().__init__(brand, model, year)
        self.type_of_bike=type_of_bike

    def display_info(self):
        super().display_info()
        print(f"Vehicle Brand : {self.brand}, Model : {self.model}, year: {self.year}, Type of Bike : {self.type_of_bike}")
        
def add_info ():
    brand = input("Please add car brand")
    model = input ("Enter Car Model ")
    Year = int(input("Enter year of manufacturing:  "))
    
    vehicle_type = input("Is it a Car or Bike? ").lower()

    if vehicle_type == "car":
        fuel_type = input("Enter the fuel type: ")
        vehicle = Car(brand, model, Year, fuel_type)
    elif vehicle_type == "bike":
        type_of_bike = input("Enter the type of bike: ")
        vehicle = Bike(brand, model, Year, type_of_bike)
    else:
        print("Invalid vehicle type! Please choose Car or Bike.")
        return

    vehicle.display_info()

def main ():
    while True:
        print ("\n Vehicle Management System ")
        print (" 1. Add Car Info ")
        print (" 2. View Vehicle Information")
        print (" 3. Exit ")
        
        emp_type = input("Select an option (1-3): ")
        if emp_type == "1":
            add_info()
       # elif emp_type == "2":
            
        elif emp_type == "3":
            print("Exiting now, Bye .... ")
            break
        else:
            print("Invalid Choice! Please try again")
    
if __name__ == "__main__":
    main()

    
    
