from faker import Faker

fake = Faker()

class DataProvider:
    def generate_booking_data(self, total_price=500, deposit_paid=True, additional_needs="Breakfast"):
        return {
            "firstname": fake.first_name(),
            "lastname": fake.last_name(),
            "totalprice": total_price,
            "depositpaid": deposit_paid,
            "bookingdates": {
                "checkin": fake.date(),
                "checkout": fake.date()
            },
            "additionalneeds": additional_needs
        }
