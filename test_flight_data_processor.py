import unittest
from flight_data_processor import FlightDataProcessor


class TestFlightDataProcessor(unittest.TestCase):
    def setUp(self):
        """Initialize a FlightDataProcessor instance before each test."""
        self.processor = FlightDataProcessor()
        self.sample_data = [
            {"flight_number": "AZ001", "departure_time": "2025-02-19 15:30", "arrival_time": "2025-02-20 03:45", "status": "ON_TIME"},
            {"flight_number": "AZ002", "departure_time": "2025-02-21 11:00", "arrival_time": "2025-02-21 16:00", "status": "DELAYED"},
            {"flight_number": "AZ003", "departure_time": "2025-02-22 10:00", "arrival_time": "2025-02-22 22:00", "status": "CANCELLED"},
        ]
        for flight in self.sample_data:
            self.processor.add_flight(flight)

    def test_add_flight(self):
        """Test adding a flight and preventing duplicates."""
        new_flight = {"flight_number": "AZ004", "departure_time": "2025-02-23 08:00", "arrival_time": "2025-02-23 12:00", "status": "ON_TIME"}
        self.processor.add_flight(new_flight)
        self.assertEqual(len(self.processor.flights), 4)
        self.processor.add_flight(new_flight)
        self.assertEqual(len(self.processor.flights), 4)

    def test_remove_flight(self):
        """Test removing a flight by flight number."""
        self.processor.remove_flight("AZ002")
        self.assertEqual(len(self.processor.flights), 2)
        self.assertFalse(any(f["flight_number"] == "AZ002" for f in self.processor.flights))

    def test_flights_by_status(self):
        """Test retrieving flights by status."""
        delayed_flights = self.processor.flights_by_status("DELAYED")
        self.assertEqual(len(delayed_flights), 1)
        self.assertEqual(delayed_flights[0]["flight_number"], "AZ002")

    def test_get_longest_flight(self):
        """Test retrieving the longest non-cancelled flight."""
        longest_flight = self.processor.get_longest_flight()
        self.assertEqual(longest_flight["flight_number"], "AZ001")

    def test_get_longest_flight_excludes_cancelled(self):
        """Test that get_longest_flight() ignores cancelled flights."""
        self.processor.update_flight_status("AZ001", "CANCELLED")
        longest_flight = self.processor.get_longest_flight()
        self.assertNotEqual(longest_flight["flight_number"], "AZ001")

    def test_update_flight_status(self):
        """Test updating the flight status."""
        self.processor.update_flight_status("AZ001", "DELAYED")
        updated_flight = next(f for f in self.processor.flights if f["flight_number"] == "AZ001")
        self.assertEqual(updated_flight["status"], "DELAYED")


if __name__ == "__main__":
    unittest.main()

# python3 -m unittest test_flight_data_processor.py