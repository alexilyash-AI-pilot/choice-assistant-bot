# ID POS Integration

## Overview

Full-featured POS integration with support for tables, QR payments, and discounts.

| Feature | Supported |
|---------|-----------|
| Table ordering | YES |
| Takeaway / Delivery | YES |
| QR payments | YES |
| Discounts | YES |
| Preorders | YES |

## How to Connect

1. Obtain from ID POS:
   - **Client ID**
   - **API key**
   - **API URL** (example: `https://aws-prod4.idpos.pl:10446/api/v1/gateway`)
2. In Choice admin → **Features** → **POS terminal** → select **ID POS**
3. Enter Client ID, API key, and API URL
4. Click **Activate**
5. Verify the connection is active

## General Settings

After connecting, configure these settings in Choice admin → **Features** → **POS terminal** → ID POS:

| Setting | Description |
|---------|-------------|
| Branch | Select the correct branch/location |
| Terminal | Select the POS terminal to use |
| User | Select the POS user account orders will be created under |
| Price list | Select the active price list (only one can be active at a time) |

> If multiple price lists exist in ID POS, only one should be active. Make sure the one selected in Choice matches what is active in ID POS.

## Menu Synchronization

Two methods to sync menu:

### Method 1: Download Menu File
1. In ID POS back-office → export the menu file
2. In Choice admin → **Features** → **POS terminal** → ID POS → **Download Menu file**
3. Upload the exported file
4. Verify items have POS IDs assigned

### Method 2: Menu Sync Button
1. In Choice admin → **Features** → **POS terminal** → ID POS
2. Click **Menu sync**
3. Choice will fetch items from ID POS API and assign POS IDs automatically
4. Review items and ensure correct mapping

> Items without POS IDs will not appear in the menu when POS integration is active.

## Tables Setup

1. In ID POS → export the **Areas file** (contains table/area layout)
2. In Choice admin → **Features** → **Tables** → import areas
3. Create areas and tables matching the ID POS layout
4. Copy the **POS IDs** from ID POS for each table and paste them into Choice

> Area and table POS IDs must match exactly between ID POS and Choice for orders to route correctly.

## Working with Orders

Two modes available:

### Mode 1: Via Choice Business (default)
1. Order comes in → appears in **Choice Business** app
2. Staff accept in Choice Business
3. After acceptance, order is sent to ID POS
4. ID POS processes the order

### Mode 2: Direct to ID POS
- Orders go directly to ID POS without appearing in Choice Business first
- Enable this in Features → POS terminal → ID POS → turn on **direct to POS** option

### Important Rules

- **Sales types must match** — the sales type set in Choice (delivery, takeaway, table) must have a corresponding type configured in ID POS; mismatched types cause order failures
- **Delivery address** is passed in the order comment field (not a structured field)
- **Payment types must match** — payment method names in Choice must correspond to payment types in ID POS; mismatches cause payment processing errors
- **Auto-close option** — if enabled, orders are automatically closed in ID POS after payment without staff action

## QR Payment Orders

QR payment at tables is supported with the following limitations:

| Feature | Notes |
|---------|-------|
| Split payments | ❌ Not supported |
| Partial payments | ❌ Not supported |
| Full table payment | ✅ |

### Tips Setup

1. Create a tip type on the **ID POS side** first
2. In Choice admin → **Features** → **POS terminal** → select the tip type
3. If you add a new tip type later → you must **reactivate** the integration for it to take effect

### Global Tips

1. Sync waiters between ID POS and Choice (waiter accounts must exist in both systems)
2. In Choice admin → configure **Global Tips links**
3. Each waiter gets a unique QR/link for tips

## Discounts

1. Create the discount in **ID POS** first (Choice cannot create discounts in POS)
2. In Choice admin → **Features** → **POS terminal** → ID POS → select the discount from the list
3. The discount works for all discount types: percentage, fixed amount, promo code

> Discounts flow from Choice → ID POS. Discounts created only in ID POS are not automatically applied via Choice.
