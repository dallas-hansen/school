FULL_TANK = 14

class FancyCar:
    def __init__(self, make="Old Clunker", mpg=24.0):
        # Complete the constructor.
        self.make = make
        self.mpg = mpg
        self.odometer = 5
        self.gas_tank = FULL_TANK
        self.engine_on = False
        

    # Return car model
    def get_model(self):
        # Update the return statment.
        
        return self.make

    # Return car odometer
    def check_odometer(self):
        # Update the return statment.
        
        return self.odometer

    # Return miles per gallon (MPG)
    def get_mpg(self):
        # Update the return statment.
        
        return self.mpg

    # Return amount of gas in tank
    def check_gas_gauge(self):
        # Update the return statment.
        
        return self.gas_tank

    # Honk horn
    def honk_horn(self):
        # Type your code here.
        print(f'The {self.make} says beep beep!')

    # Drive car requested miles but check for enough,
    # checking that miles_to_drive is positive
    def drive(self, miles_to_drive):
        # Type your code here and remove the return statement
        if miles_to_drive > 0:
            self.odometer = self.odometer + miles_to_drive
            self.gas_tank -= (miles_to_drive / self.mpg)

    # Add gas to tank. Check for positive value of amount to add
    def add_gas(self, amount_to_add):
        # Type your code here and remove the return statement
        amount_to_add = float(amount_to_add)
        if amount_to_add > 0:
            if self.gas_tank + amount_to_add <= FULL_TANK:
                self.gas_tank += amount_to_add

    # Set boolean variable to True
    def start_engine(self):
        # Type your code here and remove the return statement
        self.engine_on = True

    # Set boolean variable to False
    def stop_engine(self):
        # Type your code here and remove the return statement
        self.engine_on = False

if __name__ == '__main__':
    my_car = FancyCar()

    # Just for initial testing
    print(f"make={my_car.get_model()}")
    print(f"mpg={my_car.get_mpg()}")
    print(f"odometer={my_car.check_odometer()}")
    print(f"gas_tank={my_car.check_gas_gauge()}")