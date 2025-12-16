# QA UI Automation - Playwright + Python (SauceDemo)
A UI automation testing framework built with Playwright and pytest, focusing on end-to-end user flows, Page Object Model (POM), and reusable test architecture.

---

# 1. Project Overview

This project implements a **UI automation framework** for the SauceDemo web application using **Playwright (Python)** and **pytest**, following the **Page Object Model (POM)** design pattern.

The framework covers:
- Positive and negative login scenarios
- Add-to-cart functionality
- Full checkout end-to-end flow
- Reusable auto-login fixtures
- Clean separation between test logic and page structure

The main goal is to demonstrate **real-world QA Automation practices**, including maintainable architecture, readable tests, and scalable design suitable for CI pipelines.

---

# 2. Application Under Test

**Application:** SauceDemo  
**URL:** https://www.saucedemo.com  

SauceDemo is a demo e-commerce application commonly used for QA automation practice.  
It includes login, product listing, cart management, and checkout functionality.

Test users provided by the application:
- `standard_user`
- `locked_out_user`
- `problem_user`
- Password for all users: `secret_sauce`

---

# 3. Test Architecture (POM)

The project follows the **Page Object Model** pattern.

### Core Page Objects
| Page Object                     | Description                                      |
|--------------------------------|--------------------------------------------------|
| `BasePage`                     | Common functionality (navigation, waits)         |
| `LoginPage`                    | Login form interactions and error handling       |
| `InventoryPage`                | Product list and add-to-cart actions             |
| `CartPage`                     | Cart validation and checkout entry               |
| `CheckoutPage`                 | User information form                            |
| `CheckoutOverviewPage`         | Order overview and confirmation                  |
| `CheckoutCompletePage`         | Order success verification                      |

Each Page Object defines:
- element selectors
- supported user actions
- page-level validations

---

# 4. Fixtures and Test Setup

### Auto-Login Fixture

A reusable pytest fixture is used to:
- open the application
- perform login
- return a ready-to-use Inventory page

This removes duplication and ensures all tests start from a **known, valid state**.

Example:
```python
def test_add_item_to_cart(inventory_page):
    inventory_page.add_first_item_to_cart()
```
---

# 5. Test Coverage

### **5.1 Login Tests**

#### **Successful Login**
- User logs in with valid credentials
- Inventory page is loaded successfully
- Product list is visible

#### **Negative Login (Invalid Password)**
- User attempts login with incorrect password
- Login is rejected
- Error message is displayed

These tests validate authentication logic and basic security controls.

### **5.2 Cart Tests**

#### **Add Item to Cart**
- User adds a product from inventory
- Cart icon updates
- Cart page displays the correct number of items

This ensures that core shopping cart functionality works as expected.

### **5.3 Checkout End-to-End Flow**

A full end-to-end (E2E) scenario covering the complete purchase flow:

1. User logs in (via auto-login fixture)
2. Product is added to the cart
3. Cart is opened
4. Checkout process is started
5. User information is entered
6. Order is reviewed
7. Purchase is completed successfully

This test validates that the entire business flow works correctly from start to finish.

---

# 6. Assertions Strategy

Assertions are designed to validate both **UI state** and **business logic**.

Examples include:
- Inventory page visibility after login
- Correct number of items in cart
- Presence of checkout success confirmation
- Error message visibility for invalid login attempts

Assertions are placed strategically to fail fast and provide clear feedback.

---

# 7. Key Design Decisions

### Page Object Model (POM)
- UI selectors are isolated inside Page Objects
- Tests remain readable and focused on business logic
- Changes in UI require updates in one place only

### Fixtures for State Management
- Auto-login fixture ensures consistent test starting state
- Eliminates repeated login steps across tests
- Improves test stability and maintainability

### Clean Test Design
- Tests describe **what** is being validated
- Page Objects define **how** interactions happen

---

# 8. How to Run the Project

### 1 Create and activate virtual environment
```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

### 2 Install dependencies
```powershell
pip install -r requirements.txt
python -m playwright install
```

### 3 Run tests
```powershell
pytest -v
```

---

# 9. Folder Structure

``` md
project/
│
├── pages/                          # Page Object Model (POM)
│   ├── __init__.py
│   ├── base_page.py
│   ├── login_page.py
│   ├── inventory_page.py
│   ├── cart_page.py
│   ├── checkout_page.py
│   ├── checkout_overview_page.py
│   └── checkout_complete_page.py
│
├── tests/                          # UI test cases
│   ├── test_login.py
│   ├── test_cart.py
│   └── test_checkout.py
│
├── __pycache__/                    # Python cache (auto-generated)
├── .pytest_cache/                  # pytest cache (auto-generated)
│
├── venv/                           # Virtual environment (local)
│
├── conftest.py                     # pytest fixtures (auto-login, base_url)
├── pytest.ini                      # pytest configuration
├── requirements.txt                # Project dependencies
├── README.md                       # Project documentation
└── .gitignore                      # Git ignore rules
```

---

# 10. Key Skills Demonstrated

- UI Automation with Playwright (Python)
- pytest fixtures and test lifecycle management
- Page Object Model (POM) architecture
- End-to-End (E2E) testing
- Positive and negative test scenarios
- Clean and scalable automation framework design

---

## Author

**Dmytro Litvinov**

LinkedIn:  
[Dmytro Litvinov](https://www.linkedin.com/in/dmytro-litvinov-2b319b235)

---

## License

This project is released under the MIT License.  
You are free to use, modify, and distribute it with attribution.