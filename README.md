# Test Automation Framework

A comprehensive test automation framework combining BDD testing with Behave and REST API testing.  
The framework includes Allure reporting for detailed analytics and a flexible structure for UI and API tests.

## Features

- **BDD Testing**: Behavior-driven testing with Behave
- **API Testing**: RESTful API testing integrated into BDD scenarios
- **Reporting**: Allure report integration for detailed execution analytics
- **Logging**: Centralized logging for debugging and traceability
- **Page Object Model**: Structured page objects for UI scenarios
- **Data Generation**: Test data simulation using Faker
- **Models**: POCO-style models for user and payment card entities
- **Configuration Management**: Centralized configuration via `behave.ini` and `config.py`
- **Utilities**: Helper modules for assertions, logging, and user management
- 
### Configuration Files:
- `.gitignore` – Git ignore rules  
- `behave.ini` – Behave configuration  
- `requirements.txt` – Python dependencies  
- `README.md` – This file  e

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
behave -t=@ui    

# Run UI tests with Allure report
behave -t=@ui -f allure_behave.formatter:AllureFormatter -o allure-results-bdd```

### API Tests:
```bash
# Run all API tests
behave -t=@api 

# Run with Allure report
behave -t=@api -f allure_behave.formatter:AllureFormatter -o allure-results-bdd
```

### Run All Tests:
```bash
# Run complete test suite
behave

# Run with both HTML and Allure reports
behave -f allure_behave.formatter:AllureFormatter -o allure-results-bdd
```
### Generate Allure Report:
```bash
allure serve allure-results-bdd
```
## Configuration

### behave.ini:
[behave]
paths = features
show_snippets = false
show_skipped = false
format = pretty
logging_level = INFO


### config.py:
Application configuration including:
- Base URLs
- API_BASE_URL

### Contributing Steps:
1. Fork the repository
2. Create a feature branch (git checkout -b feature/amazing-feature)
3. Commit your changes (git commit -m 'Add amazing feature')
4. Push to the branch (git push origin feature/amazing-feature)
5. Open a Pull Request
