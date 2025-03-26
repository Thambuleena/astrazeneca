# Flight Data Processor

## Overview
The **Flight Data Processor** is a Python class designed to handle flight information efficiently. It provides functionality to add, remove, filter, and analyze flight data while ensuring data integrity and data transformations.

## Features
- Add flights while preventing duplicates.
- Remove flights by flight number.
- Retrieve flights based on status (ON_TIME, DELAYED, CANCELLED).
- Find the longest flight based on duration.
- Update flight status dynamically.
- Implements unit testing using `unittest`.

## Technologies Used
- Python 3.8+
- `datetime` module for handling timestamps.
- `unittest` for testing.

## Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/Thambuleena/astrazeneca.git
   ```
2. Navigate to the project folder:
   ```bash
   cd astrazeneca
   ```

## Usage
### Running the Script
```bash
python3 flight_data_processor.py
```

### Running Unit Tests
```bash
python3 -m unittest test_flight_data_processor.py
```

## Example Flight Data
```json
[
    {
        "flight_number": "AZ001",
        "departure_time": "2025-02-19 15:30",
        "arrival_time": "2025-02-20 03:45",
        "status": "ON_TIME"
    },
    {
        "flight_number": "AZ002",
        "departure_time": "2025-02-21 11:00",
        "arrival_time": "2025-02-21 16:00",
        "status": "DELAYED"
    }
]
```

## File Structure
```
asterazenica/
│── flight_data_processor.py  # Main script containing FlightDataProcessor class
│── test_flight_data_processor.py  # Unit tests
│── README.md  # Project documentation
```
