# SauceDemo UI – Smoke Test Checklist

## Overview

This document contains a **UI smoke test checklist** for the SauceDemo application.
The checklist covers critical user flows that must work for the application
to be considered stable.

Smoke tests are designed to provide fast feedback and validate
core functionality before deeper functional or regression testing.

---

## Preconditions

- Application URL is accessible: https://www.saucedemo.com
- Supported browser is installed (Chromium / Chrome)
- Test user credentials are available:
  - `standard_user / secret_sauce`

---

## Smoke Checklist

### Authentication

- [ ] Login page is displayed correctly
- [ ] User can log in with valid credentials
- [ ] Inventory page is visible after successful login
- [ ] Error message is displayed for invalid credentials
- [ ] Locked-out user cannot log in

---

### Inventory / Products

- [ ] Product list is displayed on inventory page
- [ ] Product items contain name, price, and image
- [ ] User can add a product to the cart
- [ ] Cart icon updates after adding a product
- [ ] User can remove a product from inventory page

---

### Cart

- [ ] Cart page opens successfully
- [ ] Added products are displayed in cart
- [ ] Product quantity is displayed correctly
- [ ] User can remove items from cart
- [ ] User can proceed to checkout from cart

---

### Checkout

- [ ] Checkout information page is displayed
- [ ] User can enter first name, last name, and postal code
- [ ] User can continue to checkout overview page
- [ ] Checkout overview displays correct products and total
- [ ] User can complete the checkout successfully

---

### Order Completion

- [ ] Checkout complete page is displayed
- [ ] Success message is visible
- [ ] User can return to inventory page after checkout

---

## Notes

- This checklist represents **high-priority business-critical flows**.
- Smoke scenarios are good candidates for automation.
- Full regression and edge cases are covered by automated Playwright tests.
- The checklist is intentionally lightweight to keep execution fast.

---

## Automation Reference

The majority of smoke scenarios listed above are automated using
Playwright and pytest:

- Login scenarios → `tests/test_login.py`
- Cart scenarios → `tests/test_cart.py`
- Checkout E2E flow → `tests/test_checkout.py`
