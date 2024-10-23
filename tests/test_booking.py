import pytest
from api.booking_api import BookingAPI
from utils.data_provider import DataProvider

booking_api = BookingAPI()
data_provider = DataProvider()

@pytest.fixture
def log_all_bookings():
    response = booking_api.create_booking(data_provider.generate_booking_data())
    booking_id = response.json()['bookingid']
    return [booking_id]

def test_create_booking():
    booking_data = data_provider.generate_booking_data(total_price=500, deposit_paid=True, additional_needs="Lunch")
    response = booking_api.create_booking(booking_data)
    assert response.status_code == 200

def test_modify_booking(log_all_bookings):
    booking_id = log_all_bookings[0]
    modified_data = data_provider.generate_booking_data(total_price=1000, deposit_paid=False, additional_needs="Dinner")
    response = booking_api.update_booking(booking_id, modified_data)
    assert response.status_code == 200

def test_delete_booking(log_all_bookings):
    booking_id = log_all_bookings[0]
    response = booking_api.delete_booking(booking_id)
    assert response.status_code == 201
