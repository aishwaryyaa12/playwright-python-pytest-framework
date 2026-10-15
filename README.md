# Production-Ready Playwright + Python + Pytest Automation Framework

[![Playwright Tests](https://github.com/aishwaryaas/playwright-python-pytest-framework/actions/workflows/ci.yml/badge.svg)](https://github.com/aishwaryaas/playwright-python-pytest-framework/actions)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/)
[![Playwright](https://img.shields.io/badge/Playwright-v1.40+-green.svg)](https://playwright.dev/python/)

An end-to-end Web & API Test Automation Framework engineered in **Python** using **Playwright**, **Pytest**, and **Page Object Model (POM)** architecture, integrated with **GitHub Actions CI/CD** and HTML reporting.

Developed by **[Aishwarya Shanmugam](https://linkedin.com/in/aishwaryaas)** (QA Engineer).

---

## 🌟 Framework Architecture & Highlights

- **Page Object Model (POM)**: Decoupled UI page locators and user interactions from test assertions.
- **Pytest Fixture Management**: Modular `conftest.py` supporting parallel test execution, headless/headed browser toggling, and multi-browser configurations (Chromium, Firefox, WebKit).
- **API & UI Dual Capability**: Integrated REST API verification (`playwright.request`) alongside UI end-to-end regression suites.
- **CI/CD Pipeline Integration**: Automated execution on GitHub Actions triggered on every Pull Request or push commit.
- **Allure & HTML Reporting**: Automated test execution reports, failure screenshots, and trace viewer recordings.

---

## 🛠️ Project Structure

```text
├── .github/workflows/
│   └── ci.yml               # GitHub Actions CI pipeline configuration
├── pages/
│   ├── base_page.py         # Abstract Base Page with common Playwright interactions
│   ├── login_page.py        # Login Page Object
│   └── inventory_page.py    # Product Inventory Page Object
├── tests/
│   ├── test_ui_login.py     # UI E2E Test Suite
│   └── test_api_products.py # REST API Test Suite
├── utils/
│   └── config.py            # Environment & Test Data Configuration
├── conftest.py              # Pytest fixtures for Playwright browser setup & tracing
├── pytest.ini               # Pytest configuration settings
└── requirements.txt         # Dependencies
```

---

## 🚀 Getting Started

### 1. Prerequisites
- Python 3.10 or higher
- Git

### 2. Installation
```bash
# Clone repository
git clone https://github.com/aishwaryaas/playwright-python-pytest-framework.git
cd playwright-python-pytest-framework

# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies and Playwright browsers
pip install -r requirements.txt
playwright install
```

### 3. Running Tests
```bash
# Run all tests headlessly
pytest

# Run tests in headed mode
pytest --headed

# Run parallel tests (e.g. 4 workers)
pytest -n 4

# Generate HTML report
pytest --html=report.html
```

---

## 📊 CI/CD GitHub Actions Integration

The pipeline runs headless Chromium tests on Ubuntu runners for every push to `main` or `develop` branches:

```yaml
name: Playwright Test Automation CI

on:
  push:
    branches: [ main, develop ]
  pull_request:
    branches: [ main, develop ]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.11'
      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt
          playwright install --with-deps
      - name: Run Playwright Tests
        run: pytest --html=report.html --self-contained-html
      - name: Upload Test Report
        if: always()
        uses: actions/upload-artifact@v4
        with:
          name: playwright-report
          path: report.html
```

---

## 👩‍💻 Author
**Aishwarya Shanmugam** — QA Engineer | Test Automation Specialist  
📍 Steinenbronn (Stuttgart Region), Germany  
🔗 [LinkedIn Profile](https://linkedin.com/in/aishwaryaas)
