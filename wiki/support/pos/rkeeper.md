# R-Keeper POS Integration

## Overview

Integration with R-Keeper requires coordination with the client's local R-Keeper dealer or integrator. The dealer handles all R-Keeper-side configuration and must be involved in the setup process.

## Required Licenses

One of the following (12-month preferred to avoid expiry issues):

| License | Notes |
|---------|-------|
| R-Keeper module XML-interface for the application, 12 months | Preferred |
| R-Keeper module XML interface for the application, 1 month | Short-term |
| Write XML Order, lifetime version | No renewal needed |

Integrator pricing varies — typically around 100 USD for setup work (charged by local partner).

## Connection Flow

### Step 1 — Get dealer/integrator contact
Ask the client for the contact details of their local R-Keeper dealer or integrator.

### Step 2 — Confirm version and license
Contact the dealer/integrator to confirm:
- R-Keeper version
- Active license type
- Whether the current setup supports Choice integration
- Integrator's setup fee

### Step 3 — Prepare information for the integrator
Send the integrator:
- R-Keeper configuration instructions (EN manual or RU Google Doc)
- The activation link from Choice admin (generated in Step 5)
- Required connection data: 2 URLs and a token

### Step 4 — Integrator completes R-Keeper-side setup
The integrator must:
1. Install the R-Keeper plugin (from Google Drive folder)
2. Configure R-Keeper per the setup instructions
3. Open the activation link from Choice admin
4. Fill in the first block (default values) and select the correct license type

**For lifetime license:** integrator reviews settings and clicks **Confirm**.

**For 1-month or 12-month license**, the integrator must enter:
- **Dealer ID** — numeric dealer ID (not email)
- **Dealer password**
- **Dealer restaurant code**
- **Dealer R-Keeper token** — must be requested from R-Keeper at integrations@rkeeper.ru (token format: `f6f82954-3567-48bd-814e-d6dd398f516c`)

### Step 5 — Generate activation link in Choice admin
1. Choice admin → Admin → Integration → POS terminal
2. Select **R-Keeper**
3. Click **Activate**
4. A browser page opens with the activation link
5. Send this link to the dealer/integrator

### Step 6 — Post-connection setup
After successful connection:
- Import the menu
- Fill in all required POS IDs
- Connect Choice Business app
- Staff can start processing orders

## Operational Requirements

- Staff need a tablet or phone with the **Choice Business app**
- Device should be placed near the POS terminal
- **Keep device on lock screen near POS** — otherwise staff miss sound notifications

## Working with Orders

### Two Operating Modes

**Mode 1: Via Choice Business (default)**
1. Order arrives → appears in Choice Business app
2. Staff accept the order in Choice Business
3. Order is sent to R-Keeper after acceptance

**Mode 2: Direct to R-Keeper (ChB mode)**
- Orders go directly to R-Keeper without requiring acceptance in Choice Business

### Tables
- **All orders must be connected to tables** in R-Keeper — this is a system requirement
- For takeaway: set the takeaway POS ID in **Features → POS terminal** settings
- For delivery: set the delivery POS ID in **Features → POS terminal** settings

### Marketplace Orders
- For marketplace orders (Wolt, Bolt, etc.): set the marketplace-specific POS settings in **Features → POS terminal** per marketplace

### Order Type Codes
R-Keeper uses order type codes to categorize orders. These must be configured correctly in Choice POS settings to match the codes in R-Keeper.

### Payment Types
- Custom payment settings can be configured per payment method
- Payment type in Choice must match the payment type code in R-Keeper

### Auto-Close Orders
- Option available to automatically close orders in R-Keeper after payment
- Enable in Features → POS terminal → R-Keeper settings

### Discounts
- Discounts require **open price** to be enabled on the dish in R-Keeper
- A **round discount POS ID** must be set in POS settings (for rounding purposes)
- Without open price + round discount ID, discounts will not process correctly

### QR Payments
- QR table payments are supported with R-Keeper integration

## Menu Sync

1. In Choice admin → **Features** → **POS terminal** → R-Keeper
2. Click **Menu synchronization**
3. Choice fetches the menu from R-Keeper via the XML interface
4. Items receive POS IDs from R-Keeper
5. Verify all items, modifiers, and categories have correct POS IDs

> Items without POS IDs are hidden when POS integration is active.

## Errors

### Error: "Invalid license check digit"
**Cause:** Subscription license does NOT work if a physical security key (dongle) is installed on the cash server.
**Fix:** A **virtual security key** is required instead of the physical one. Contact the R-Keeper dealer to switch to a virtual key.

### Error 504 Timeout

**Cause:** The service tries to connect while the R-Keeper process is running — the search takes too long and times out.

**Fix (must be done in exact sequence):**
1. **Stop** the R-Keeper service on the cash server
2. Immediately go to **Choice admin** → connect the integration (click Connect/Activate)
3. **Start** the R-Keeper service right after initiating the connection — do this **before** the connection search finishes
4. The connection should establish successfully

> The key is the timing: connect from Choice side while R-Keeper is starting up. If you start R-Keeper first and wait for it to fully load, the 504 error recurs.
