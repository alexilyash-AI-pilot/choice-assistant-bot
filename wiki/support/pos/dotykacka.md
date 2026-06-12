# Dotykačka POS Integration

## Overview

| Feature | Supported |
|---------|-----------|
| Table ordering | YES |
| Takeaway | YES |
| Delivery | YES |
| QR payments | YES |
| Table booking | YES (requires Choice Business app) |
| Choice Business app | Optional (mandatory for table booking) |
| Availability | Only on tariff **Dotykačka NAPLNO** and **NEOMEZENĚ** |

## How to Connect

1. In backoffice, enable **"POS terminal"** for the profile
2. Click **Activate** — client is redirected to their Dotykačka admin
3. A pop-up appears asking to grant access to Choice — client must approve and select their **cloud** (if multiple clouds exist)
4. Integration is complete

## Settings After Connection

| Setting | What it does |
|---------|-------------|
| **Branch ID** | Select which cash register receives orders/bookings (find name in Dotykačka admin) |
| **Autoclose table order** | After order sent to register, automatically closes the bill (table orders only) |
| **Autoclose takeaway/delivery order** | Same for takeaway/delivery |
| **Send order direct to POS** | Order sent directly to register without needing confirmation in Choice Business |
| **Booking support** | Enable reservation integration |

## POS IDs Required On

- All menu items (including options/modifiers)
- Areas (takeaway, delivery, tables) — takeaway/delivery POS ID is optional (can be empty)
- Packaging (for takeaway and delivery)
- Cost of delivery — optional (must be created as an item in the register)

## Order Scenarios

### Takeaway / Delivery
- **Choice Business + autoclose** → confirm in app → notification + payment pops up in register → receipt printed
- **Choice Business without autoclose** → confirm in app → order appears in "Open bills" (otevřené účty) without notification → must close bill in register manually + issue in app for customer to see ready status
- **Without Choice Business + autoclose** → order appears in register, notification pops up, closed regardless of payment
- **Without Choice Business and without autoclose** → auto-confirmed in app → appears in "Open bills" without notification (online payment shows notification)

### Order to Table
- **Choice Business + autoclose** → confirm in app → notification + payment in register → receipt printed
- **Choice Business without autoclose** → confirm in app → order in "Open bills" + table lights up green → close bill in register after preparation
- **Without Choice Business + autoclose** → notification in register, auto-closed
- **Without Choice Business and without autoclose** → auto-confirmed → appears in "Open bills" + table lights up green → must close manually

### QR Payment
- Waiter puts items on table, must **leave "table edit"** for items to appear to customer
- Customer pays in Choice → notification with completed payment in register → receipt printed → paid items disappear from open bill (if all paid, bill closes)

## Receipt Data

Configurable in Dotykačka print settings per register:
- Order number (from Choice and from Dotykačka)
- Customer name + phone number
- Pick-up time (ASAP or specific time)
- Payment method (must be selected in register if autoclose is not applied)
- Customer's comment
- Comment to delivery address
- Cutlery
- **Note: Tips are NOT displayed** (can only be checked in the app)

## Errors with POS IDs

**Problem:** "Cost 0 is not acceptable" / "Delivery fee 0 is not acceptable" / other POS ID issues

**Fix — How to find modifier POS IDs in Dotykačka:**
1. Check if you have the same modifier categories in Dotykačka as in Choice (if not, add them in Dotykačka first)
2. Dotykačka → Dashboard → Item Management → search for the dish name
3. Press **Details** → left side menu → **Customization**
4. Choose the modifier category → press **Add group**
5. Edit the group (pencil icon) — if modifications are free and required, set "All items are free"
6. Repeat for all dishes with modifiers

**Fix — How to get POS IDs from the exported menu:**
1. Admin panel → Integrations → POS Integrations → **Menu** button (downloads the file)
2. Open in Excel / Google Sheets
3. Ctrl+F (⌘+F on Mac) → search for the dish name → find modifiers
4. Copy the POS ID → paste into the corresponding option in Choice dish edit

Repeat for all modifiers.

## Advantages vs Storyous

- Tariff NAPLNO: 890 CZK (includes mobile waiter + stocks) vs Storyous 680 CZK + mobile waiter 1000 CZK + stocks 1000 CZK → ~3× cheaper
- Orders go to cash register/printer first, then to cloud (Storyous is reversed — longer delay)
