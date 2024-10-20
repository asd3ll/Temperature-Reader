"""
Temperature Reader Application

Description:
This program is a simple GUI application built using Tkinter. It allows the user to select a text file 
that contains temperature readings, displays the most recent temperature in the file, and updates the 
temperature automatically at regular intervals. The user can customize the font size and background color
of the temperature display.

Features:
- Select a temperature log file.
- Display the latest temperature reading.
- Auto-update temperature at a user-defined interval (default: 3 minutes).
- Change font size and background color dynamically through the menu.

Author: [R]
Version: 1.0
Date: October 20, 2024
"""

import tkinter as tk
from tkinter import filedialog, messagebox, Menu
from tkinter.simpledialog import askinteger, askstring


class TemperatureReader:
    def __init__(self, root):
        # Initialize the main window and default settings
        self.root = root
        self.root.title("Temperature Reader")

        # Store the file path as a StringVar, which will update the UI if changed
        self.file_path = tk.StringVar()
        # Set the update interval to 3 minutes (180,000 milliseconds)
        self.update_interval = 3 * 60 * 1000  
        # Default font size for temperature display
        self.font_size = 10  
        # Default background color for the display
        self.bg_color = 'white'  
        
        # Create and display the necessary widgets
        self.create_widgets()
        # Create and configure the application menu
        self.create_menu()
        
    
    def create_widgets(self):
        # Create a label to display the temperature, initially set to "--" (no data)
        self.temperature_label = tk.Label(self.root, text="--", font=("Helvetica", self.font_size))
        # Expand the label to fill both horizontal and vertical space
        self.temperature_label.pack(expand=True, fill='both')
    
    def create_menu(self):
        # Create a menu bar for the application
        menu_bar = tk.Menu(self.root)
        self.root.config(menu=menu_bar)
        
        # Create a drop-down menu for file and application settings
        file_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Menu", menu=file_menu)

        # Add commands to the menu for selecting a file, updating temperature, changing font size, etc.
        file_menu.add_command(label="Select File", command=self.select_file)
        file_menu.add_command(label="Update Temperature", command=self.update_temperature)
        file_menu.add_command(label="Change Font Size", command=self.change_font_size)
        file_menu.add_command(label="Change Background Color", command=self.change_bg_color)

        # Add a separator and exit command to the menu
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.root.quit)
    
    def select_file(self):
        # Open a file dialog for selecting a text file
        file_selected = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
        if file_selected:
            # Store the selected file path and immediately update the temperature
            self.file_path.set(file_selected)
            self.update_temperature()  
    
    def update_temperature(self):
        # Get the current file path for reading temperature data
        file = self.file_path.get()
        if not file:
            # Show an error message if no file has been selected
            messagebox.showerror("Error", "Please select a file first")
            return
        
        # Read the latest temperature from the file
        latest_temp = self.read_latest_temperature(file)
        if latest_temp is not None:
            # Update the temperature label with the formatted temperature (2 decimal points)
            self.temperature_label.config(text=f"{latest_temp:.2f}") 
        else:
            # Reset the label if temperature could not be read
            self.temperature_label.config(text="--")
            messagebox.showerror("Error", "Failed to read temperature data.")
        
        # Schedule the next temperature update after the interval
        self.schedule_update()  
    
    def schedule_update(self):
        # Use the after method to schedule the update_temperature method to run after the interval
        self.root.after(self.update_interval, self.update_temperature)
    
    def read_latest_temperature(self, file):
         # Try reading the latest temperature from the file
        try:
            with open(file, 'r') as f:
                lines = f.readlines()
                if lines:
                    # Get the last line and extract the temperature part
                    latest_line = lines[-1].strip()
                    parts = latest_line.split(';')
                    if len(parts) == 3:
                        try:
                            # Convert the temperature string to a floating-point number
                            temperature = float(parts[2])   
                            return temperature
                        except ValueError:
                            # Handle invalid temperature value
                            print(f"Invalid temperature value: {parts[2]}")
                            return None
                print("No valid lines found in the file.")
                return None
        except FileNotFoundError:
            print("File not found.")
            return None
        except IOError as e:
            print(f"File error: {e}")
            return None
        except Exception as e:
            print(f"Unexpected error: {e}")
            return None
    
    def change_font_size(self):
        # Ask the user to input a new font size, with a minimum value of 1
        new_size = askinteger("Font Size", "Enter new font size:", initialvalue=self.font_size, minvalue=1)
        if new_size is not None:
            # Update the font size and reconfigure the temperature label
            self.font_size = new_size
            self.temperature_label.config(font=("Helvetica", self.font_size))

    def change_bg_color(self):
        # Ask the user to input a new background color (e.g., 'black' or '#000000')
        color = askstring("Background Color", "Enter new background color:", initialvalue=self.bg_color)
        if color:
            # Update the background color and reconfigure both the label and root window
            self.bg_color = color
            self.temperature_label.config(bg=self.bg_color)
            self.root.configure(bg=self.bg_color)
            
if __name__ == "__main__":
    # Initialize the Tkinter root window
    root = tk.Tk()
     # Instantiate the TemperatureReader class
    app = TemperatureReader(root)
     # Set the initial size of the window and the minimum size
    root.geometry("200x100")  
    root.minsize(10, 10)
      # Start the Tkinter main event loop
    root.mainloop()

