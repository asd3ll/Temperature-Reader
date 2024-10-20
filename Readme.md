# Temperature Reader Application

## Description
This is a simple Python GUI application that reads temperature data from a text file and displays the most recent temperature. The application updates the temperature at a set interval and allows the user to customize the font size and background color.

## Features
- Select a temperature log file.
- Automatically display the latest temperature reading.
- Customize font size and background color.
- Auto-updates every 3 minutes.

## Installation
1. Clone or download this repository.
2. Ensure Python 3.x is installed on your system.
3. Run the following command to install required libraries (if necessary):

pip install tk


## Usage
1. Run the `TemperatureReader.py` file.
2. Use the "Menu" to:
- Select a temperature file
- Update the temperature reading
- Change font size
- Change background color
3. The temperature will update automatically every 3 minutes.

### Example Data Format
The application expects the temperature log file to follow this format:

```plaintext
2024-10-20 12:00:00;Location1;20.5
2024-10-20 12:05:00;Location1;21.0
2024-10-20 12:10:00;Location1;21.3


Each line contains the following values separated by semicolons (;):

Date and time (e.g., 2024-10-20 12:00:00)
Location (e.g., Location1)
Temperature in Celsius (e.g., 20.5)
If the file format is incorrect, the application will display an error message.

Author
[R]

License
This project is licensed under the MIT License - see the LICENSE file for details.