# Profit POS Integration

## Overview

Profit integrates via OpenAPI. The entire setup is handled on the Profit side.

| Feature | Supported |
|---------|-----------|
| Table ordering | YES |
| Takeaway | YES |
| Delivery | YES |
| QR payments | YES (table payment) |

## How to Connect

1. Write to **Roman** at https://t.me/rom_romaha and ask him to connect the integration
2. Wait for Profit to complete the setup — no configuration needed on the Choice side

**Note:** The setup takes place entirely on the Profit side.

## Important

- **Menu sync does not work if the "one menu" function is enabled**

## Table Payment

Table payment via QR code requires setup on both the Profit side and the Choice side.

### Prerequisites

- QR codes must be placed on tables — request these from your **personal manager** at Profit
- **Choice Business app** installed and active on a staff device
- **Access code** obtained from Profit for the integration

### Workflow

1. Guest arrives and scans the QR code on their table
2. Guest browses the menu and places an order via Choice
3. Waiter creates an **invoice** on the Profit POS terminal linked to the guest's table
4. Guest scans the table QR code again (or receives a link) and sees their bill
5. Guest pays online through Choice
6. Staff device receives a **push notification** confirming payment
7. Staff close the order on the Profit POS terminal

### Setup Steps

1. Contact your Profit personal manager → request table QR codes for the venue
2. Install Choice Business app on a staff device
3. In Choice admin → obtain the access code
4. Provide the access code to Profit to finalize the integration
5. Place QR codes on tables
6. Test the full flow: scan → order → invoice on POS → payment → push notification → close on POS
