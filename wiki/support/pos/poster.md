# Poster POS Integration

## Overview

| Feature | Supported |
|---------|-----------|
| Table ordering | YES |
| Takeaway | YES |
| Delivery | YES |
| QR payments | YES |
| Table booking | — |

## How to Connect

Integration with POS is disabled by default — must be enabled in backoffice per profile.

1. Admin panel → **Features** → **POS terminal**
2. In the **Provider** field, select **Poster**
3. In the **Poster (Provider Account ID)** field, enter the client's Poster account number
4. Click **Activate**
5. You'll be redirected to Poster to authorize — enter the account URL, login, and password
6. After authorization, you're redirected back to Choice — integration is active

## Critical Rules

- All dishes without a POS ID will **not be displayed** in the menu when POS integration is active
- If a POS ID is incorrect, the order is **automatically cancelled** by Poster
- All products, categories, tables, and options must have matching POS IDs
- **Menu sync does not work if the "one menu" function is enabled**

## POS IDs Required On

- All menu items (dishes + modifiers/options)
- Areas (tables, takeaway, delivery)
- Packaging items

## Menu Synchronization

1. In Choice admin → **Features** → **POS terminal** → **Menu Synchronization**
2. Click to start sync — Choice pulls menu from Poster
3. Items receive POS IDs from Poster automatically

### What Syncs

| Data | Synced |
|------|--------|
| Item name | ✅ |
| Price | ✅ |
| POS ID | ✅ |
| Modifiers/options | First sync only |
| Images | ❌ (not synced from Poster) |
| Categories | ✅ |

**Important:**
- Modifiers are linked to dishes **only on the first sync** — subsequent syncs do not re-link modifiers
- After sync, new items receive a **"New"** badge — this disappears automatically after 24 hours

## Discounts

Choice discounts are passed to Poster as a **discounted price** (not as a separate discount line).

### How it works
- Choice calculates the discount and sends the final discounted price to Poster
- The discount amount is **distributed across all dishes** in the order proportionally
- Delivery charges, packaging, and tips are **excluded** from the discount distribution

### Limitations

| Scenario | Behavior |
|----------|----------|
| Choice discount applied | ✅ Passed to Poster as reduced price |
| Poster-side discount | ❌ Not accepted back into Choice |
| Client is in a Poster client group with a group discount | ❌ Choice discount will NOT apply — Poster group discount takes priority |

> If a customer belongs to a Poster loyalty/client group that has a discount, the Choice discount is ignored. This is a Poster-side behavior.

## Working with Orders

Two modes available:

### Mode 1: Via Choice Business (default — recommended)

**How to enable:** In Features → POS terminal, turn **OFF** the "Send direct to POS" option.

**Workflow:**
1. Order arrives → appears in **Choice Business** app
2. Staff review and accept the order in Choice Business
3. After acceptance, order is sent to Poster
4. Order appears in Poster for kitchen/fulfillment

**Before using this mode:**
- Synchronize Poster staff — employee names must match between Poster and Choice Business
- Employees who will handle orders must have the required access rights in Poster

**What's different in this mode:**
- Online paid orders can be **automatically closed** in Poster so staff don't need to select payment method again
- For unpaid orders, payment handling must still be completed on the Poster side
- Delivery charges are sent through the integration and do not need a separate delivery dish

### Mode 2: Direct to Poster

**How to enable:** In Features → POS terminal → turn **ON** the "Send direct to POS" option.

**Workflow:**
1. Order is placed by customer → goes directly to Poster without appearing in Choice Business first
2. No acceptance step in Choice Business

**Important differences:**
- Online paid orders appear in Poster as **already paid** — the payment type cannot be changed after the fact
- This mode removes the Choice Business acceptance step entirely
