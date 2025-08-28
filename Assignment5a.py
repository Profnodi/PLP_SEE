"""
Smartphone Class Implementation with OOP Concepts
Demonstrating: Classes, Constructors, Inheritance, Polymorphism, and Encapsulation
"""

class Smartphone:
    """
    Base class representing a smartphone with core functionality.
    Demonstrates encapsulation through private attributes and public methods.
    """
    
    # Class attribute (shared by all instances)
    device_count = 0
    
    def __init__(self, brand, model, imei, storage_gb=64, ram_gb=4, os="Android"):
        """
        Constructor to initialize smartphone with unique values
        """
        # Instance attributes (unique to each object)
        self._brand = brand                    # Encapsulated attribute
        self._model = model                    # Encapsulated attribute
        self._imei = imei                      # Encapsulated attribute
        self._storage_gb = storage_gb          # Encapsulated attribute
        self._ram_gb = ram_gb                  # Encapsulated attribute
        self._os = os                          # Encapsulated attribute
        
        # Device state attributes
        self._powered_on = False
        self._battery_level = 100
        self._screen_locked = True
        self._current_call = None
        
        # Content storage
        self._installed_apps = []
        self._contacts = {}
        self._photos = []
        self._messages = []
        
        # Update class attribute
        Smartphone.device_count += 1
    
    # Getter methods for encapsulated attributes (properties)
    @property
    def brand(self):
        return self._brand
    
    @property
    def model(self):
        return self._model
    
    @property
    def full_name(self):
        return f"{self._brand} {self._model}"
    
    @property
    def battery_level(self):
        return self._battery_level
    
    @property
    def imei(self):
        return self._imei
    
    @property
    def specs(self):
        return f"{self._storage_gb}GB Storage, {self._ram_gb}GB RAM, {self._os}"
    
    def power_on(self):
        """Power on the smartphone"""
        if not self._powered_on and self._battery_level > 5:
            self._powered_on = True
            return f"📱 {self.full_name} powered ON"
        return "❌ Cannot power on - low battery"
    
    def power_off(self):
        """Power off the smartphone"""
        if self._powered_on:
            self._powered_on = False
            self._screen_locked = True
            return f"📱 {self.full_name} powered OFF"
        return "❌ Device already off"
    
    def unlock(self, pin="1234"):
        """Unlock the screen"""
        if self._powered_on and self._screen_locked:
            self._screen_locked = False
            return f"🔓 {self.full_name} unlocked"
        return "❌ Cannot unlock"
    
    def lock(self):
        """Lock the screen"""
        self._screen_locked = True
        return f"🔒 {self.full_name} locked"
    
    def charge(self, percentage):
        """Charge the battery"""
        if self._battery_level < 100:
            self._battery_level = min(100, self._battery_level + percentage)
            return f"⚡ Charging... {self._battery_level}%"
        return "✅ Battery full"
    
    def _use_battery(self, amount):
        """Private method for battery usage (encapsulation)"""
        self._battery_level = max(0, self._battery_level - amount)
        if self._battery_level <= 10:
            return f"⚠️ Low battery! {self._battery_level}% left"
        return f"🔋 Battery: {self._battery_level}%"
    
    def make_call(self, number):
        """Make a phone call"""
        if not self._powered_on:
            return "❌ Cannot call - device off"
        if self._battery_level < 5:
            return "❌ Cannot call - low battery"
        
        self._current_call = number
        self._use_battery(3)
        return f"📞 Calling {number}..."
    
    def end_call(self):
        """End current call"""
        if self._current_call:
            number = self._current_call
            self._current_call = None
            return f"📞 Ended call with {number}"
        return "❌ No active call"
    
    def send_message(self, number, message):
        """Send a text message"""
        if not self._powered_on:
            return "❌ Cannot send message - device off"
        if self._battery_level < 3:
            return "❌ Cannot send message - low battery"
        
        self._messages.append({"to": number, "message": message})
        self._use_battery(1)
        return f"✉️ Message sent to {number}"
    
    def install_app(self, app_name, size_mb=100):
        """Install an application"""
        if not self._powered_on:
            return "❌ Cannot install app - device off"
        
        # Check storage (simplified)
        used_storage = len(self._installed_apps) * 100
        available = (self._storage_gb * 1024) - used_storage
        
        if size_mb <= available:
            self._installed_apps.append(app_name)
            self._use_battery(2)
            return f"📦 Installed {app_name}"
        return f"❌ Not enough storage for {app_name}"
    
    def take_photo(self):
        """Take a photo"""
        if not self._powered_on:
            return "❌ Cannot take photo - device off"
        if self._battery_level < 2:
            return "❌ Cannot take photo - low battery"
        
        self._photos.append(f"photo_{len(self._photos) + 1}.jpg")
        self._use_battery(1)
        return f"📸 Photo taken! Total: {len(self._photos)}"
    
    def add_contact(self, name, number):
        """Add a contact"""
        self._contacts[name] = number
        return f"👤 Added contact: {name}"
    
    def get_status(self):
        """Get current device status"""
        status = f"\n{self.full_name} Status:\n"
        status += f"Specs: {self.specs}\n"
        status += f"Power: {'ON' if self._powered_on else 'OFF'}\n"
        status += f"Screen: {'Locked' if self._screen_locked else 'Unlocked'}\n"
        status += f"Battery: {self._battery_level}%\n"
        status += f"In call: {self._current_call if self._current_call else 'No'}\n"
        status += f"Apps: {len(self._installed_apps)} installed\n"
        status += f"Contacts: {len(self._contacts)} saved\n"
        status += f"Photos: {len(self._photos)} taken"
        return status
    
    def perform_action(self):
        """Polymorphic method to be overridden by subclasses"""
        return "📱 Performing smartphone functions"


class GamingPhone(Smartphone):
    """
    Specialized smartphone for gaming - demonstrates inheritance
    """
    
    def __init__(self, brand, model, imei, gpu_model, refresh_rate=60, 
                 storage_gb=128, ram_gb=8, os="Android Gaming"):
        # Initialize parent class
        super().__init__(brand, model, imei, storage_gb, ram_gb, os)
        
        # Gaming-specific attributes
        self._gpu_model = gpu_model
        self._refresh_rate = refresh_rate
        self._game_mode = False
        self._current_game = None
    
    @property
    def gaming_specs(self):
        return f"{self._gpu_model} GPU, {self._refresh_rate}Hz"
    
    def enable_game_mode(self):
        """Enable gaming performance mode"""
        self._game_mode = True
        return "🎮 Game mode ENABLED - Maximum performance!"
    
    def disable_game_mode(self):
        """Disable gaming mode"""
        self._game_mode = False
        return "🎮 Game mode DISABLED"
    
    def play_game(self, game_name):
        """Play a game"""
        if not self._powered_on:
            return "❌ Cannot play game - device off"
        
        battery_usage = 15 if self._game_mode else 10
        if self._battery_level < battery_usage:
            return "❌ Cannot play game - low battery"
        
        self._current_game = game_name
        self._use_battery(battery_usage)
        return f"🎮 Playing {game_name} at {self._refresh_rate}Hz"
    
    def perform_action(self):
        """Override parent method - polymorphism"""
        if self._current_game:
            return f"🎮 Gaming: {self._current_game}"
        return "🎮 Ready for gaming action!"


class CameraPhone(Smartphone):
    """
    Specialized smartphone for photography - demonstrates inheritance
    """
    
    def __init__(self, brand, model, imei, camera_mp, aperture, 
                 storage_gb=256, ram_gb=6, os="Android Camera"):
        # Initialize parent class
        super().__init__(brand, model, imei, storage_gb, ram_gb, os)
        
        # Camera-specific attributes
        self._camera_mp = camera_mp
        self._aperture = aperture
        self._camera_mode = "Auto"
        self._flash_enabled = False
    
    @property
    def camera_specs(self):
        return f"{self._camera_mp}MP, f/{self._aperture}"
    
    def enable_flash(self):
        """Enable camera flash"""
        self._flash_enabled = True
        return "📸 Flash ENABLED"
    
    def disable_flash(self):
        """Disable camera flash"""
        self._flash_enabled = False
        return "📸 Flash DISABLED"
    
    def set_camera_mode(self, mode):
        """Set camera mode"""
        self._camera_mode = mode
        return f"📸 Camera mode set to {mode}"
    
    def take_photo(self):
        """Override parent method with enhanced camera functionality"""
        if not self._powered_on:
            return "❌ Cannot take photo - device off"
        if self._battery_level < 3:
            return "❌ Cannot take photo - low battery"
        
        flash_status = "with flash" if self._flash_enabled else "without flash"
        self._photos.append(f"hq_photo_{len(self._photos) + 1}.jpg")
        self._use_battery(2)
        return f"📸 High-quality photo taken {flash_status} in {self._camera_mode} mode!"
    
    def perform_action(self):
        """Override parent method - polymorphism"""
        return f"📸 Camera ready: {self.camera_specs}"


def demonstrate_smartphones():
    """
    Function to demonstrate smartphone functionality and OOP concepts
    """
    print("=" * 60)
    print("SMARTPHONE CLASS DEMONSTRATION")
    print("=" * 60)
    
    # Create different smartphone instances with unique values
    phone1 = Smartphone("Samsung", "Galaxy S23", "SAM123456789", 256, 8, "Android 14")
    phone2 = GamingPhone("ASUS", "ROG Phone 6", "ASUSGAMER123", "Adreno 730", 144, 512, 16)
    phone3 = CameraPhone("Google", "Pixel 8", "PIXELCAM123", 50, 1.7, 128, 8)
    
    smartphones = [phone1, phone2, phone3]
    
    print(f"\nTotal devices created: {Smartphone.device_count}")
    print("\n" + "=" * 40)
    
    # Demonstrate polymorphism
    print("\nPOLYMORPHISM DEMONSTRATION:")
    print("-" * 30)
    for phone in smartphones:
        action = phone.perform_action()
        print(f"{phone.full_name}: {action}")
    
    print("\n" + "=" * 40)
    
    # Demonstrate each smartphone's unique features
    print("\nUNIQUE FEATURES DEMONSTRATION:")
    print("-" * 35)
    
    # Regular smartphone
    print(f"\n{phone1.full_name}:")
    print(phone1.power_on())
    print(phone1.unlock())
    print(phone1.install_app("WhatsApp"))
    print(phone1.make_call("555-0123"))
    print(phone1.send_message("555-0123", "Hello!"))
    print(phone1.take_photo())
    
    # Gaming phone
    print(f"\n{phone2.full_name}:")
    print(phone2.power_on())
    print(phone2.enable_game_mode())
    print(phone2.play_game("Call of Duty Mobile"))
    print(phone2.install_app("Game Launcher", 500))
    
    # Camera phone
    print(f"\n{phone3.full_name}:")
    print(phone3.power_on())
    print(phone3.enable_flash())
    print(phone3.set_camera_mode("Portrait"))
    print(phone3.take_photo())
    print(phone3.take_photo())
    
    print("\n" + "=" * 40)
    
    # Show status of all devices
    print("\nDEVICE STATUS SUMMARY:")
    print("-" * 25)
    for phone in smartphones:
        print(phone.get_status())
        print("-" * 30)
    
    # Demonstrate battery usage and charging
    print("\nBATTERY MANAGEMENT:")
    print("-" * 20)
    for phone in smartphones:
        print(f"{phone.full_name}: {phone.battery_level}%")
        if phone.battery_level < 50:
            print(phone.charge(30))
    
    print("\n" + "=" * 40)
    
    # Power off all devices
    print("\nPOWERING OFF DEVICES:")
    print("-" * 22)
    for phone in smartphones:
        print(phone.power_off())


# Main execution
if __name__ == "__main__":
    demonstrate_smartphones()