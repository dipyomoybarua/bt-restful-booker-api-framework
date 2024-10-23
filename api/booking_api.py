from .base_api import BaseAPI
import requests

class BookingAPI(BaseAPI):
    def create_booking(self, booking_data):
        response = requests.post(f"{self.base_url}/booking", json=booking_data, headers=self.get_headers())
        return response

    def update_booking(self, booking_id, booking_data):
        response = requests.put(f"{self.base_url}/booking/{booking_id}", json=booking_data, headers=self.get_headers())
        return response

    def delete_booking(self, booking_id):
        response = requests.delete(f"{self.base_url}/booking/{booking_id}", headers=self.get_headers(is_json=False))
        return response
