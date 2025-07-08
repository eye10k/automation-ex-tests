# Test Automation Framework

A comprehensive test automation framework combining UI testing with Playwright and API testing with requests library. The framework includes advanced logging, HTML reporting, and Allure integration for detailed test analytics.

## Features

- **UI Testing**: Playwright-based web application testing
- **API Testing**: RESTful API testing using requests library
- **Reporting**: Dual reporting system with HTML and Allure reports
- **Logging**: Comprehensive logging system for test execution tracking
- **Page Object Model**: Structured page objects for maintainable UI tests
- **Configuration Management**: Centralized configuration handling
- **Utilities**: Helper functions for common test operations

### Configuration Files:
- .gitignore - Git ignore rules
- pytest.ini - Pytest configuration
- requirements.txt - Python dependencies
- README.md - This file

## Installation & Setup

### Prerequisites:
- Python 3.8+
- pip package manager

### Installation Steps:

#### 1. Clone the repository
```bash
git clone <repository-url>
cd <repository-directory>
```

#### 2. Install dependencies
```bash
pip install -r requirements.txt
```

#### 3. Install Playwright browsers
```bash
playwright install
```
## Running Tests

### UI Tests:
```bash
# Run all UI tests
pytest tests/test_ui.py

# Run with HTML report
pytest tests/test_ui.py --html=reports/ui_report.html

# Run with Allure report
pytest tests/test_ui.py --alluredir=reports/allure-results
```

### API Tests:
```bash
# Run all API tests
pytest tests/test_api.py

# Run with HTML report
pytest tests/test_api.py --html=reports/api_report.html

# Run with Allure report
pytest tests/test_api.py --alluredir=reports/allure-results
```

### Run All Tests:
```bash
# Run complete test suite
pytest

# Run with both HTML and Allure reports
pytest --html=reports/full_report.html --alluredir=reports/allure-results
```

## Configuration

### pytest.ini:
Main pytest configuration file containing:
- Test discovery patterns
- Markers definition
- Default command line options

### conf.ini:
Application configuration including:
- Base URLs
- Web elements locators

### Contributing Steps:
1. Fork the repository
2. Create a feature branch (git checkout -b feature/amazing-feature)
3. Commit your changes (git commit -m 'Add amazing feature')
4. Push to the branch (git push origin feature/amazing-feature)
5. Open a Pull Request
