from jinja2 import Template
import os

class ReportGenerator:
    def __init__(self, log_file="logs/booking_test_results.log"):
        self.log_file = log_file

    def generate_html_report(self, output_file="reports/report.html"):
        if not os.path.exists(self.log_file):
            print(f"Log file {self.log_file} not found.")
            return

        log_content = self._parse_log_file()

        template = Template("""
        <html>
        <head>
            <title>Booking API Test Results</title>
            <style>
                body { font-family: Arial, sans-serif; }
                h1 { color: #333; }
                table { width: 100%; border-collapse: collapse; }
                th, td { border: 1px solid #ddd; padding: 8px; text-align: left; }
                .pass { color: green; }
                .fail { color: red; }
                th { background-color: #f2f2f2; }
            </style>
        </head>
        <body>
            <h1>Booking API Test Results</h1>
            
            <h2>Passed Tests</h2>
            <table>
                {% for test in passed_tests %}
                    <tr>
                        <td>{{ test[0] }}</td>
                        <td class="pass">{{ test[1] }}</td>
                        <td>{{ test[2] }}</td>
                    </tr>
                {% endfor %}
            </table>

            <h2>Failed Tests</h2>
            <table>
                {% for test in failed_tests %}
                    <tr>
                        <td>{{ test[0] }}</td>
                        <td class="fail">{{ test[1] }}</td>
                        <td>{{ test[2] }}</td>
                    </tr>
                {% endfor %}
            </table>
        </body>
        </html>
        """)

        report_content = template.render(passed_tests=log_content['passed'], failed_tests=log_content['failed'])
        
        self._create_output_directory(output_file)
        with open(output_file, 'w') as f:
            f.write(report_content)

        print(f"Report generated successfully: {output_file}")

    def _parse_log_file(self):
        with open(self.log_file, 'r') as f:
            lines = f.readlines()

        passed_tests = []
        failed_tests = []

        for line in lines:
            if 'passed' in line:
                parts = line.split(' - ')
                if len(parts) >= 3:
                    passed_tests.append((parts[2].strip(), "Passed", ""))
            elif 'failed' in line:
                parts = line.split(' - ')
                if len(parts) >= 3:
                    error_details = line.split(' Reason: ')[-1]
                    failed_tests.append((parts[2].split(' Reason')[0].strip(), "Failed", error_details.strip()))

        return {'passed': passed_tests, 'failed': failed_tests}

    @staticmethod
    def _create_output_directory(file_path):
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
