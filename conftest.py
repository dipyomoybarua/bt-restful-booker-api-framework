import pytest
from reports.report_generator import ReportGenerator
import logging

# Create a logger for test results
logging.basicConfig(
    filename="logs/booking_test_results.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    # Log test result (pass/fail) with more details
    if report.when == "call":
        if report.outcome == "passed":
            logging.info(f"Test {item.name} passed.")
        else:
            logging.error(f"Test {item.name} failed. Reason: {report.longrepr}")

# Run after the entire test session completes
def pytest_sessionfinish(session, exitstatus):
    if exitstatus == 0:  # All tests passed
        logging.info("All tests passed. Generating report...")
    else:
        logging.error(f"Some tests failed (exit status: {exitstatus}).")

    # Generate the HTML report after tests finish
    report_gen = ReportGenerator(log_file="logs/booking_test_results.log")
    report_gen.generate_html_report()
