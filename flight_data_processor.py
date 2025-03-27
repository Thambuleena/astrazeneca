from typing import List, Dict
from datetime import datetime


class FlightDataProcessor:
    def __init__(self) -> None:
        self.flights: List[Dict] = []

    def add_flight(self, data: Dict) -> None:
        """Add flight details"""
        if not any(f["flight_number"] == data["flight_number"] for f in self.flights):            
            data["duration_minutes"] = self._calculate_duration(data["departure_time"], data["arrival_time"])
            self.flights.append(data)

    def remove_flight(self, flight_number: str) -> None:
        """Remove flight by flight_number"""
        self.flights = [f for f in self.flights if f["flight_number"] != flight_number]

    def flights_by_status(self, status: str) -> List[Dict]:
        """Search flights by status"""
        return [f for f in self.flights if f["status"] == status]

    def get_longest_flight(self) -> Dict:
        """Search non cancelled logest duration flights"""
        valid_flights = [f for f in self.flights if f["status"] != "CANCELLED"]
        return max(valid_flights, key=lambda f: f.get("duration_minutes", 0), default={})

    def update_flight_status(self, flight_number: str, new_status: str) -> None:
        """Update status of flights by flight number"""
        for flight in self.flights:
            if flight["flight_number"] == flight_number:
                flight["status"] = new_status
                break

    def _calculate_duration(self, departure: str, arrival: str) -> int:
        """Transform depature and arrival date to standard format and convert to minutes"""
        fmt = "%Y-%m-%d %H:%M"
        dep_time = datetime.strptime(departure, fmt)
        arr_time = datetime.strptime(arrival, fmt)
        return int((arr_time - dep_time).total_seconds() // 60)
