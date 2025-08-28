"""
Vehicle Movement Simulator
Demonstrating polymorphism with different move() implementations for various vehicles
"""

class Vehicle:
    """Base class for all vehicles"""
    
    def __init__(self, brand, model, vehicle_type, fuel_type):
        self.brand = brand
        self.model = model
        self.vehicle_type = vehicle_type
        self.fuel_type = fuel_type
        self.speed = 0
        self.engine_on = False
    
    def move(self):
        """Base move method to be overridden by subclasses"""
        raise NotImplementedError("Subclasses must implement move() method")
    
    def start_engine(self):
        """Start the vehicle's engine"""
        if not self.engine_on:
            self.engine_on = True
            return f"🔑 {self.brand} {self.model} engine started!"
        return "⚠️ Engine is already running!"
    
    def stop_engine(self):
        """Stop the vehicle's engine"""
        if self.engine_on:
            self.engine_on = False
            self.speed = 0
            return f"🔑 {self.brand} {self.model} engine stopped!"
        return "⚠️ Engine is already off!"
    
    def accelerate(self, amount):
        """Increase vehicle speed"""
        if self.engine_on:
            self.speed += amount
            return f"🚀 Accelerating to {self.speed} km/h!"
        return "❌ Cannot accelerate - engine is off!"
    
    def brake(self, amount):
        """Decrease vehicle speed"""
        if self.speed > 0:
            self.speed = max(0, self.speed - amount)
            return f"🛑 Braking to {self.speed} km/h!"
        return "⚠️ Vehicle is already stopped!"
    
    def get_status(self):
        """Get current vehicle status"""
        status = f"\n{self.brand} {self.model} Status:"
        status += f"\nType: {self.vehicle_type}"
        status += f"\nFuel: {self.fuel_type}"
        status += f"\nEngine: {'ON' if self.engine_on else 'OFF'}"
        status += f"\nSpeed: {self.speed} km/h"
        return status
    
    def __str__(self):
        return f"{self.brand} {self.model} ({self.vehicle_type})"

class Car(Vehicle):
    """Car class - moves by driving on roads"""
    
    def __init__(self, brand, model, fuel_type, doors=4):
        super().__init__(brand, model, "Car", fuel_type)
        self.doors = doors
        self.wheels = 4
    
    def move(self):
        if self.engine_on:
            return f"🚗 {self.brand} {self.model} is driving on the road at {self.speed}km/h!"
        return "❌ Car cannot move - start the engine first!"
    
    def honk(self):
        return "🚨 Honk! Honk!"
    
    def open_trunk(self):
        return "📦 Trunk opened!"
    
    def get_specs(self):
        return f"Car specs: {self.doors} doors, {self.wheels} wheels, {self.fuel_type} fuel"

class Motorcycle(Vehicle):
    """Motorcycle class - moves by riding on roads"""
    
    def __init__(self, brand, model, fuel_type, engine_size):
        super().__init__(brand, model, "Motorcycle", fuel_type)
        self.engine_size = engine_size
        self.wheels = 2
    
    def move(self):
        if self.engine_on:
            return f"🏍️ {self.brand} {self.model} is riding on the road at {self.speed}km/h!"
        return "❌ Motorcycle cannot move - start the engine first!"
    
    def do_wheelie(self):
        if self.speed > 30:
            return "🎯 Performing an awesome wheelie! 🤘"
        return "❌ Too slow for a wheelie! Need more speed!"
    
    def ring_bell(self):
        return "🔔 Ring ring!"
    
    def get_specs(self):
        return f"Motorcycle specs: {self.engine_size}cc engine, {self.wheels} wheels"

class Airplane(Vehicle):
    """Airplane class - moves by flying in the air"""
    
    def __init__(self, brand, model, fuel_type, max_altitude):
        super().__init__(brand, model, "Airplane", fuel_type)
        self.max_altitude = max_altitude
        self.altitude = 0
        self.wingspan = "30m"  # Example wingspan
    
    def move(self):
        if self.engine_on and self.altitude > 0:
            return f"✈️ {self.brand} {self.model} is flying at {self.altitude} feet, speed: {self.speed}km/h!"
        elif self.engine_on:
            return f"✈️ {self.brand} {self.model} is taxiing on runway at {self.speed}km/h!"
        return "❌ Airplane cannot move - start the engine first!"
    
    def take_off(self):
        if self.engine_on and self.speed > 200:
            self.altitude = 1000
            return "🛫 Airplane taking off! Climbing to 1000 feet!"
        return "❌ Not enough speed for takeoff! Need to accelerate more!"
    
    def land(self):
        if self.altitude > 0:
            self.altitude = 0
            self.speed = 50
            return "🛬 Airplane landing! Descending to runway!"
        return "⚠️ Airplane is already on ground!"
    
    def increase_altitude(self, feet):
        if self.engine_on and self.altitude > 0:
            self.altitude = min(self.max_altitude, self.altitude + feet)
            return f"📈 Climbing to {self.altitude} feet!"
        return "❌ Must be airborne to change altitude!"
    
    def get_specs(self):
        return f"Airplane specs: Max altitude {self.max_altitude}ft, Wingspan {self.wingspan}"

class Boat(Vehicle):
    """Boat class - moves by sailing on water"""
    
    def __init__(self, brand, model, fuel_type, boat_type):
        super().__init__(brand, model, "Boat", fuel_type)
        self.boat_type = boat_type
        self.anchor_down = True
    
    def move(self):
        if self.engine_on and not self.anchor_down:
            return f"🚢 {self.brand} {self.model} is sailing on water at {self.speed} knots!"
        elif self.engine_on:
            return "⚠️ Boat cannot move - raise the anchor first!"
        return "❌ Boat cannot move - start the engine first!"
    
    def raise_anchor(self):
        if self.anchor_down:
            self.anchor_down = False
            return "⚓ Anchor raised! Ready to sail!"
        return "⚠️ Anchor is already raised!"
    
    def drop_anchor(self):
        if not self.anchor_down:
            self.anchor_down = True
            self.speed = 0
            return "⚓ Anchor dropped! Boat secured!"
        return "⚠️ Anchor is already down!"
    
    def blow_horn(self):
        return "📯 Boat horn sounding! Whoo whoo!"
    
    def get_specs(self):
        return f"Boat specs: Type: {self.boat_type}, Fuel: {self.fuel_type}"

class Bicycle(Vehicle):
    """Bicycle class - moves by pedaling (human-powered)"""
    
    def __init__(self, brand, model, gears):
        super().__init__(brand, model, "Bicycle", "Human Power")
        self.gears = gears
        self.wheels = 2
        # Bicycles don't have engines in the traditional sense
        self.engine_on = True  # Always "on" since it's human-powered
    
    def move(self):
        if self.speed > 0:
            return f"🚴 {self.brand} {self.model} is pedaling on the road at {self.speed}km/h!"
        return "🚴 Bicycle is stationary - start pedaling!"
    
    def start_engine(self):
        return "✅ Bicycle is ready to pedal! No engine needed!"
    
    def stop_engine(self):
        return "✅ Bicycle stopped! No engine to turn off!"
    
    def ring_bell(self):
        return "🔔 Ring ring! Bicycle bell!"
    
    def change_gear(self, gear):
        if 1 <= gear <= self.gears:
            return f"⚙️ Changed to gear {gear} of {self.gears}"
        return f"❌ Invalid gear! Choose between 1-{self.gears}"
    
    def get_specs(self):
        return f"Bicycle specs: {self.gears} gears, {self.wheels} wheels, Human-powered"

class Helicopter(Vehicle):
    """Helicopter class - moves by hovering and flying"""
    
    def __init__(self, brand, model, fuel_type, rotor_diameter):
        super().__init__(brand, model, "Helicopter", fuel_type)
        self.rotor_diameter = rotor_diameter
        self.altitude = 0
        self.rotor_spinning = False
    
    def move(self):
        if self.rotor_spinning and self.altitude > 0:
            return f"🚁 {self.brand} {self.model} is flying at {self.altitude} feet, speed: {self.speed}km/h!"
        elif self.rotor_spinning:
            return f"🚁 {self.brand} {self.model} is ready for takeoff on helipad!"
        return "❌ Helicopter cannot move - start the rotors first!"
    
    def start_engine(self):
        self.engine_on = True
        self.rotor_spinning = True
        return f"🔑 {self.brand} {self.model} engine started! Rotors spinning! 🚁"
    
    def stop_engine(self):
        self.engine_on = False
        self.rotor_spinning = False
        self.altitude = 0
        self.speed = 0
        return f"🔑 {self.brand} {self.model} engine stopped! Rotors stopped! 🚁"
    
    def take_off(self):
        if self.rotor_spinning:
            self.altitude = 500
            return "🛫 Helicopter taking off! Hovering at 500 feet!"
        return "❌ Rotors not spinning! Start engine first!"
    
    def hover(self):
        if self.altitude > 0:
            self.speed = 0
            return "🚁 Hovering in place! Maintaining altitude!"
        return "❌ Must be airborne to hover!"
    
    def get_specs(self):
        return f"Helicopter specs: Rotor diameter {self.rotor_diameter}m, Fuel: {self.fuel_type}"

def demonstrate_vehicle_movement():
    """
    Function to demonstrate polymorphism with vehicle move() method
    """
    print("=" * 60)
    print("VEHICLE MOVEMENT SIMULATOR")
    print("=" * 60)
    print("Demonstrating Polymorphism with move() method\n")
    
    # Create various vehicles
    vehicles = [
        Car("Toyota", "Camry", "Gasoline", 4),
        Motorcycle("Harley-Davidson", "Sportster", "Gasoline", 1200),
        Airplane("Boeing", "747", "Jet Fuel", 35000),
        Boat("Yamaha", "242X", "Gasoline", "Speedboat"),
        Bicycle("Trek", "FX 2", 21),
        Helicopter("Bell", "407", "Aviation Fuel", 10.7)
    ]
    
    # Demonstrate each vehicle's movement
    print("🚗 VEHICLES IN ACTION 🚗")
    print("-" * 30)
    
    for vehicle in vehicles:
        print(f"\n{vehicle}")
        print(vehicle.start_engine())
        
        # Vehicle-specific actions
        if isinstance(vehicle, Car):
            print(vehicle.accelerate(60))
            print(vehicle.honk())
        
        elif isinstance(vehicle, Motorcycle):
            print(vehicle.accelerate(80))
            print(vehicle.ring_bell())
        
        elif isinstance(vehicle, Airplane):
            print(vehicle.accelerate(250))
            print(vehicle.take_off())
            print(vehicle.increase_altitude(5000))
        
        elif isinstance(vehicle, Boat):
            print(vehicle.raise_anchor())
            print(vehicle.accelerate(30))
            print(vehicle.blow_horn())
        
        elif isinstance(vehicle, Bicycle):
            print(vehicle.accelerate(20))
            print(vehicle.change_gear(5))
            print(vehicle.ring_bell())
        
        elif isinstance(vehicle, Helicopter):
            print(vehicle.take_off())
            print(vehicle.accelerate(100))
            print(vehicle.hover())
        
        # Demonstrate polymorphism - same method, different behavior
        print(f"Movement: {vehicle.move()}")
        print(vehicle.get_status())
        print(vehicle.get_specs())
        print("-" * 40)
    
    print("=" * 60)
    
    # Demonstrate polymorphism explicitly
    print("🌟 POLYMORPHISM DEMONSTRATION 🌟")
    print("-" * 35)
    print("Calling move() on different vehicles without knowing their specific types:\n")
    
    for vehicle in vehicles:
        movement = vehicle.move()
        print(f"{vehicle.__class__.__name__}: {movement}")
    
    print("\n" + "=" * 60)
    
    # Stop all vehicles
    print("🛑 STOPPING ALL VEHICLES 🛑")
    print("-" * 25)
    
    for vehicle in vehicles:
        print(vehicle.stop_engine())
        print(vehicle.get_status())
        print()

def vehicle_race_challenge():
    """
    Race challenge between different types of vehicles
    """
    print("\n" + "=" * 60)
    print("🏁 VEHICLE RACE CHALLENGE! 🏁")
    print("=" * 60)
    
    # Create racing vehicles
    race_vehicles = [
        Car("Ferrari", "488", "Gasoline", 2),
        Motorcycle("Ducati", "Panigale", "Gasoline", 1100),
        Airplane("Cessna", "172", "Avgas", 10000),
        Boat("Formula", "350", "Gasoline", "Racing Boat")
    ]
    
    print("RACE PARTICIPANTS:")
    for i, vehicle in enumerate(race_vehicles, 1):
        print(f"{i}. {vehicle}")
    
    print("\n🏁 RACE START! 🏁")
    for vehicle in race_vehicles:
        print(f"\n{vehicle}:")
        print(vehicle.start_engine())
        
        if isinstance(vehicle, Car):
            print(vehicle.accelerate(200))
        elif isinstance(vehicle, Motorcycle):
            print(vehicle.accelerate(180))
            print(vehicle.do_wheelie())
        elif isinstance(vehicle, Airplane):
            print(vehicle.accelerate(300))
            print(vehicle.take_off())
        elif isinstance(vehicle, Boat):
            print(vehicle.raise_anchor())
            print(vehicle.accelerate(80))
        
        print(vehicle.move())
    
    print("\n🏆 And the winners are... 🏆")
    print("Each vehicle excels in its own environment! 🎉")

# Main execution
if __name__ == "__main__":
    demonstrate_vehicle_movement()
    vehicle_race_challenge()
    
    print("\n" + "=" * 60)
    print("THANK YOU FOR USING THE VEHICLE MOVEMENT SIMULATOR!")
    print("=" * 60)