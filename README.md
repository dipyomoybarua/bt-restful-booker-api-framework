### Project Overview

This Python-based automation framework tests the Restful Booker API (https://restful-booker.herokuapp.com) by performing CRUD operations on bookings (create, update, retrieve, delete). It is modular, scalable, and maintainable, offering:

- Dynamic test data generation with Faker.
- Secure authentication handling.
- Detailed logging and automated HTML report generation.
- Easy-to-understand test case structure.

**Key Components**:
## api/: Core API logic
- ```bash base_api.py: Common API interactions (requests, authentication).```

- ```bash booking_api.py: Booking-specific actions (create, update, delete).```

- ```bash auth_provider.py: Secure authentication management.```

## config/: Configuration files
- ```bash config.yaml: API URLs and authentication settings. ```

## tests/: API test cases
- ```bash test_booking.py: CRUD tests for bookings.```

## utils/: Utilities
- ```bash logger.py: Logs test execution.```

- ```bash data_provider.py: Faker-based dynamic data generation. ```

## reports/: Test reporting
- ```bash report_generator.py: Generates HTML reports from test logs.```

## conftest.py:
- ```bash Provides shared fixtures for tests, including API client setup, authentication management, and any other common test configurations.```

### Prerequisites
Before setting up this project, ensure that you have the following installed:

- Python 3.8 or higher
- `pip` package manager

For generating HTML reports:
- Jinja2 (for templating)

### Setup Instructions
To get the project running on your local machine, follow these steps:

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/yourusername/restful-booker-api-framework.git
   cd restful-booker-api-framework
   ```
2. **Create a Virtual Environment**
    ```bash
    python -m venv venv
    On Windows: venv\Scripts\activate
    ```
3. **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```
4. **Run all the Tests & generate logs for results**
    ```bash
    pytest
    ```