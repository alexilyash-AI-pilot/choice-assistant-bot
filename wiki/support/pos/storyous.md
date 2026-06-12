# Storyous POS Integration

## Overview

| Feature | Supported |
|---------|-----------|
| Table ordering | YES |
| Takeaway | YES |
| Delivery | YES |
| QR payments | YES (no notification or receipt in POS) |
| Table booking | NO (in progress) |
| Collection Point | YES |
| Choice Business app | Optional (mandatory for QR payments) |
| Availability | No restrictions |

## How to Connect

1. In backoffice, enable **"POS terminal"** for the profile
2. Contact Storyous support at **pomoc@storyous.cz** to get API keys (provide company name + ID number)
   - Keys needed: **Merchant ID** and **Place ID**
3. Enter Merchant ID and Place ID in the integration settings
4. Click **Activate**

## Settings After Connection

| Setting | What it does |
|---------|-------------|
| **Autoclose table order** | After order sent to register, automatically closes the bill (table orders only) |
| **Send order direct to POS** | Order sent directly to register without needing confirmation in Choice Business |

## POS IDs Required On

- All menu items (including options/modifiers)
- Areas (takeaway, delivery, tables) — POS ID is **mandatory for all areas** (most common for takeaway/delivery: table "CD")
- Packaging (for takeaway and delivery)
- Cost of delivery — **automatic** ("delivery fee"), no POS ID needed

## Order Scenarios (Takeaway / Delivery / Table)

All scenarios are identical in behavior for all order types:

- **Choice Business + autoclose** → confirm in app → notification in register, order auto-confirmed → customer sees "in preparation" → dispatch to register when ready → customer sees "ready" → after delivery, close in register (add payment in register for cash/by-card orders)
- **Choice Business without autoclose** → confirm in app → notification in register, confirm there → customer sees "in preparation" → dispatch when ready → after delivery, close in register
- **Without Choice Business + autoclose** → notification in register, auto-confirmed → customer sees "in preparation" → dispatch when ready → close in register
- **Without Choice Business and without autoclose** → auto-confirmed in app → notification in register, confirm there → customer in preparation → dispatch when ready → close in register

## Receipt Data

Configurable in Storyous admin:
- Order number
- Customer name + phone number
- Pick-up time (ASAP or specific time)
- Payment method (paid in advance or by pick-up)
- Cost of delivery (automatic, no POS ID)
- Tips (cashTips and cardTips on closure in Storyous — **not shown on bill detail/PDF**)
- Discounts — not shown in open bill, **should appear in closed bill**
- Customer's comment
- Cutlery
- **Note: Comment to delivery address is NOT displayed**

## Known Limitations

- QR payments work without notification or receipt in POS
- Table booking not yet supported
- Tips not visible on bill detail or PDF (only in the app)
- Delivery address comment not shown on receipt
