# Playwright + Python + Pytest Automation Framework

[![CI](https://github.com/aishwaryyaa12/playwright-python-pytest-framework/actions/workflows/ci.yml/badge.svg)](https://github.com/aishwaryyaa12/playwright-python-pytest-framework/actions)
[![Python](https://img.shields.io/badge/Python-3.11+-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Playwright](https://img.shields.io/badge/Playwright-1.40+-2EAD33?logo=playwright&logoColor=white)](https://playwright.dev/python/)
[![Pytest](https://img.shields.io/badge/Pytest-7.4+-0A9EDC?logo=pytest&logoColor=white)](https://docs.pytest.org/)

A modular UI and API test automation framework built with Python, Playwright, and Pytest following the Page Object Model (POM) pattern. Configured for parallel execution, headless/headed browser switching, and GitHub Actions CI/CD.

**Author:** [Aishwarya Shanmugam](https://linkedin.com/in/aishwaryyaa12) (QA Automation Engineer)

---

## Why I Built This & Architectural Decisions

Having spent several years building and maintaining Selenium suites in enterprise environments (including at Capgemini and Bettermile), I built this framework to address three recurring pain points in UI automation:

1. **Flaky Tests & Hydration Delays (Playwright vs. Selenium):**  
   In modern React/Vue applications, tests often fail because elements exist in the DOM before their JavaScript event listeners are hydrated. In Selenium, teams frequently fall back on `time.sleep()` or brittle `WebDriverWait` wrappers. I chose Playwright here because its built-in auto-waiting mechanism checks element visibility, stability, and actionable state before firing clicks, virtually eliminating timing-related flakiness.

2. **Decoupled Page Object Architecture:**  
   Locators and actions are strictly encapsulated in page classes (`pages/login_page.py`, `pages/inventory_page.py`). Test functions only express user intent (`login_page.login(user, pwd)`), never raw CSS/XPath selectors. If the DOM structure changes, only the Page Object requires updates.

3. **Hybrid UI + API Testing in One Suite:**  
   Instead of testing everything through slow browser interactions, the framework includes API tests (`tests/test_api_products.py`). This allows pre-seeding test state or verifying backend data contracts directly without spinning up a browser context.

---

## Repository Structure

```text
├── .github/workflows/
│   └── ci.yml               # GitHub Actions CI workflow (installs Playwright browsers & runs tests)
├── pages/
│   ├── base_page.py         # Base class encapsulating Playwright actions & explicit assertions
│   ├── login_page.py        # Login Page Object (locators & auth actions)
│   └── inventory_page.py    # Inventory/Products Page Object (catalog & cart interactions)
├── tests/
│   ├── test_ui_login.py     # UI E2E tests (positive login, invalid password error, cart increment)
│   └── test_api_products.py # REST API contract & latency tests against live endpoints
├── utils/
│   └── config.py            # Centralized environment URLs, credentials, and timeout configurations
├── conftest.py              # Pytest fixtures managing session-scoped browser contexts & tabs
├── pytest.ini               # Test run configuration, CLI flags, and custom markers
└── requirements.txt         # Pinned project dependencies
```

---

## Edge Cases & Engineering Notes

* **Viewport Stability:** Standardized browser context at `1280x720` in `conftest.py` to prevent responsive navigation menus from collapsing into hamburger icons, which often causes false-negative locator timeouts in headless Linux runners.
* **API Latency SLA Check:** The API suite asserts that response times remain below 2.0 seconds (`response.elapsed.total_seconds() < 2.0`), catching server degradations during regression runs.
* **Graceful Environment Handling:** `conftest.py` checks whether Playwright browser binaries are present before launching UI tests, cleanly skipping rather than crashing if run in lightweight development environments.

---

## Setup & Local Execution

### 1. Prerequisites
* Python 3.10+
* Git

### 2. Installation
```bash
# Clone the repository
git clone https://github.com/aishwaryyaa12/playwright-python-pytest-framework.git
cd playwright-python-pytest-framework

# Create and activate virtual environment
python -m venv venv
source venv/bin/activate       # On Windows: venv\Scripts\activate

# Install dependencies and Playwright browser binaries
pip install -r requirements.txt
playwright install --with-deps
```

### 3. Running Tests
```bash
# Run full suite (UI + API) with verbose output
pytest -v

# Run only UI smoke tests
pytest -m smoke

# Run only REST API contract tests
pytest -m api

# Run headed mode (watch browser execution)
pytest --headed

# Run tests in parallel across multiple workers
pytest -n auto
```

---

## Continuous Integration (GitHub Actions)

The pipeline (`.github/workflows/ci.yml`) runs automatically on every `push` and `pull_request` to `main`:
1. Checks out repository and installs Python 3.11.
2. Caches `pip` dependencies and installs Playwright Chromium/Firefox/WebKit binaries.
3. Executes the full test suite and uploads execution logs and HTML reports as build artifacts.
