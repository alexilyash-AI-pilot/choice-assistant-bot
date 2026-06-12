# Restis POS Integration

## Overview

| Feature | Supported |
|---------|-----------|
| Table ordering | YES |
| Takeaway | YES |
| Delivery | YES |
| QR payments | NO |
| Table booking | NO |
| Choice Business app | **Mandatory for all functions** |
| Availability | No restrictions |

## How to Connect

Restis integration is set up by their IT contact — do not attempt self-setup.

**Contact:**
- Petr Adamus
- adamus@rapid-system.cz
- +420 777 730 909

Provide Petr with the customer's profile details and ask him to configure the integration.

## POS IDs Required On

- All menu items (including options/modifiers)
- Areas: **for takeaway and delivery, the area POS ID field must be empty**
- Packaging (for takeaway and delivery)
- Cost of delivery — optional (must be created as an item in the register)

## Order Scenario (Takeaway / Delivery)

1. Confirmation in Choice Business → order sent to cash register → order printed
2. All order statuses must be manually moved in the app
3. Order is finished in the app
4. In the cash register, the order remains open — staff enter the payment method (cash or online) → order closed → receipt printed

## Receipt Data

- Order number (from Choice)
- Customer name
- Pick-up time (ASAP or specific time)
- Payment method (chosen in register while closing)
- **Note: Tips are NOT displayed** (can only be checked in the app)

## Known Limitations

- QR payments only feature is not available
- Choice Business app is mandatory — without it, the integration does not work
