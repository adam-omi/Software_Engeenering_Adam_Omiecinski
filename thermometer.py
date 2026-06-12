import tkinter as tk
import random


class TemperatureSensor:
    def read_data(self):
        """Mocked sensor: return temperature from -20 to +40 celsius"""
        return random.uniform(-20.0, 40.0)

class UnitConverter:
    @staticmethod
    def celsius_to_fahrenheit(celsius):
        """Converts Celsius to Fahrenheit"""
        return (celsius * 9/5) + 32

class ThermometerSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Digital Thermometer")
        self.root.geometry("350x250")
        self.root.resizable(False, False)
        
        self.sensor = TemperatureSensor()
        self.is_celsius = True
        self.current_temp_c = 0.0
        
        self.title_label = tk.Label(root, text="Current Temperature:", font=("Arial", 12))
        self.title_label.pack(pady=(20, 5))

        self.temp_label = tk.Label(root, text="--.- °C", font=("Arial", 40, "bold"))
        self.temp_label.pack(pady=5)
        
        self.alert_label = tk.Label(root, text="", font=("Arial", 16, "bold"), fg="red")
        self.alert_label.pack(pady=5)
        
        self.toggle_btn = tk.Button(
            root, 
            text="Switch Unit (C/F)", 
            command=self.toggle_unit, 
            font=("Arial", 12),
            cursor="hand2"
        )
        self.toggle_btn.pack(pady=10)
        
        self.update_temperature()
        
    def toggle_unit(self):
        self.is_celsius = not self.is_celsius
        self.update_display()
        
    def update_temperature(self):
        """Reads data from the sensor and schedules the next update (REQ-1.3)"""
        self.current_temp_c = self.sensor.read_data()
        
        self.update_display()
        
        self.root.after(2000, self.update_temperature)
        
    def update_display(self):
        """Updates the display and checks alarm conditions"""
        if self.current_temp_c > 30.0:
            self.alert_label.config(text="HOT!")
        else:
            self.alert_label.config(text="")
            
        if self.is_celsius:
            display_val = self.current_temp_c
            unit_str = "°C"
        else:
            display_val = UnitConverter.celsius_to_fahrenheit(self.current_temp_c)
            unit_str = "°F"
            
        self.temp_label.config(text=f"{display_val:.1f} {unit_str}")


if __name__ == "__main__":
    app_window = tk.Tk()
    app = ThermometerSystem(app_window)
    app_window.mainloop()