# Adyen Payments

How Adyen processes payments, when money arrives, subscription charges, and setup guide.

---

## When does money from a customer reach the restaurant?

### Standard cards (Visa, Mastercard, Apple Pay, Google Pay, P24)

| Day | What happens |
|-----|-------------|
| Monday | Customer pays |
| Monday → Tuesday | 24-hour hold (fraud prevention) |
| Tuesday–Wednesday | T+2 settlement period (2 business days) |
| **Thursday 00:00** | **Funds available for payout** |

If the T+2 period includes weekends or public holidays, it extends by the number of non-working banking days.

### BLIK (Poland)

No hold period — T+2 starts immediately on the day of payment.

- Payment on Monday → funds available **Wednesday 00:00**

---

## Subscription Charge Flow

### How it works automatically

1. **Invoice generated** — 5 days before the payment due date
2. **Attempt 1** — system charges the saved credit card
3. **Attempt 2** — if card fails, charges from Adyen balance
4. **Attempt 3 (fallback)** — if both fail: payouts are blocked, and subscription fee is deducted from incoming revenue daily at midnight until paid
5. **Confirmation** — client receives email confirmation after successful charge

**Important notes:**
- Automation only works for system-generated invoices. Manually created invoices must be charged manually.
- All subscriptions are charged monthly, even for longer subscription periods — divided into monthly payments.
- Clients without Adyen connected: credit card and manual invoices only.

### When payouts are blocked

The system retries the Adyen balance charge every night at midnight. Options to resolve:
- Card charged successfully → payouts resume
- Balance accumulates enough → auto-charge succeeds → payouts resume
- Partial payment arrangement → charge part now, rest later
- Cancel the invoice and resume payouts manually

### Subscription charge in payout reports

Subscription deductions appear as separate line items in the payout report.

---

## Adyen Setup Guide

### How to set up Adyen for a restaurant

1. In the restaurant's backoffice → select **Adyen** as online payment provider
2. Click **"Manage client"** to start creating the Adyen profile
3. You'll be redirected to the Adyen backoffice — fill in **legal information for the representative**:
   - Full name, date of birth (correct format required)
   - Phone number (correct format required)
   - All fields are mandatory
4. Complete business information, documents, and bank account details
5. After approval, online payments via Adyen are active

### Enabling auto-charge for subscriptions

In the backoffice: find the client → enable the switcher **"Allow charge invoices from Adyen"** → click **Activate**.

---

## FAQ

**Why are payouts blocked?**
Most likely a subscription invoice failed to charge — card declined and Adyen balance insufficient. Check the subscription status and invoice in the backoffice.

**How long does a refund take?**
Refunds go back through Adyen. Typically 3–10 business days depending on the customer's bank.

**Where to find payout reports?**
Admin panel → Clients → Payouts. Reports available in PDF or Excel. Issued by the 10th of each month for the previous month.
