# Syrve (Iiko) POS Integration

## Overview

| Feature | Supported |
|---------|-----------|
| Table ordering | YES |
| Takeaway / Delivery | YES |
| QR payments | YES (only with Plugin) |
| Discounts | YES (only with Plugin) |
| Better addresses | YES (only with Plugin) |
| Stop list | YES (only with Plugin) |

The ChoiceQR Plugin is strongly recommended — always connect it.

## Required Licenses

Must be purchased by the customer from their Syrve/Iiko integrators (~200 UAH / 8 USD per license per month):

1. **iikoTransport** — for delivery, self-delivery, order to table, payment at table
2. **ApiPayments** — for delivery, self-delivery, order to table, payment at table
3. **iikoDelivery** — **only if the client wants to use delivery or takeaway on Choice** (not required otherwise)

## How to Connect

### Option A: With Plugin (recommended)

1. In Choice admin → **Integrations** → **POS Integrations** → enable Syrve/Iiko integration
2. Download the ChoiceQR plugin for Syrve: `Resto.Front.Api.ChoiceQRPlugin.V8.1.0.21.zip`
3. Install the plugin on the Syrve front — copy the extracted folder into the Syrve front plugins directory
4. Configure the plugin config file (see **Plugin Setup** section below)
5. Restart the Syrve front
6. In Choice admin → **Integrations** → **Access to application** → **Create access** → enter the generated code in the Choice Business app
7. Verify the connection is active and test an order

### Option B: Without Plugin

1. In Choice admin → **Integrations** → **POS Integrations** → enable Syrve/Iiko integration
2. Enter the Syrve API credentials:
   - **API URL**: `https://api-eu.iiko.services/api/1`
   - **Organization ID** (from Syrve back-office)
   - **API login / API key**
3. Connect Choice Business app: admin → **Integrations** → **Access to application** → **Create access** → enter code in the app
4. Sync menu and verify items appear

> Without the plugin: QR payments, discounts, better addresses, and stop list are NOT available.

## Plugin Setup

The plugin config file is located in the Syrve front plugins folder. Edit the config with the following keys:

| Key | Description |
|-----|-------------|
| `WebSocketAddress` | WebSocket URL for communication with Choice backend |
| `AuthHeaderValue` | Authorization header value (token) |
| `MinQuantityBeforeSoldOut` | Set to `0` — marks item as sold out when stock reaches 0 |
| `FlexibleDiscountId` | POS ID of the flexible discount (for Choice discounts) |
| `FlexibleSurchargeId` | POS ID of the flexible surcharge |
| `DiscountIdForExternalDeliveryOrder` | POS ID of the discount used for external delivery orders |

### How to Find Discount and Surcharge POS IDs

1. Navigate to: `%appdata%\iiko\CashServer\logs\plugin-ChoiceQr`
2. Open the most recent log file
3. Search for `FlexibleDiscount` or `Surcharge` — the IDs are logged when the plugin starts
4. Copy the relevant IDs into the config file

## Testing the Integration

1. Download the Choice Business app
2. Admin panel → **Integrations** → **Access to application** → **Create access** → enter code in the app
3. Admin panel → **Integrations** → **POS Integrations** → confirm integration is enabled
4. Test order to table: scan table QR → place order → accept in Choice Business → order appears in iiko under "IikoTransport" waiter

## Menu Sync

1. In Choice admin → **Features** → **POS terminal**
2. Click **Menu synchronization** (or **Download Menu file** depending on version)
3. Wait for sync to complete — items get POS IDs from Syrve
4. Items marked as **"New"** after sync — the "New" badge disappears after 24 hours automatically
5. Modifiers are linked to dishes **only on the first sync** — after the first sync, modifiers are not re-linked automatically

> If the "one menu" function is enabled, menu sync does not work. Disable it first.

## Adding Delivery Cost POS ID (via Postman)

Use this guide when you need to set a POS ID for the delivery cost item in Syrve.

### Prerequisites
- Postman installed
- Syrve API credentials (login + API key)
- API base URL: `https://api-eu.iiko.services/api/1`

### Step-by-step

1. Open Postman → create a new POST request to:
   `https://api-eu.iiko.services/api/1/access_token`
   Body (JSON): `{"apiLogin": "YOUR_API_LOGIN"}`
2. Run the request → copy the `token` value from the response
3. Create a new POST request to:
   `https://api-eu.iiko.services/api/1/organizations`
   Header: `Authorization: Bearer YOUR_TOKEN`
   Body: `{}`
4. Run → copy the organization ID (`id` field) from the response
5. Create a new POST request to:
   `https://api-eu.iiko.services/api/1/nomenclature`
   Header: `Authorization: Bearer YOUR_TOKEN`
   Body: `{"organizationId": "YOUR_ORG_ID"}`
6. Run → search through the response for the delivery cost item (search for "delivery" or the item name in Russian/local language)
7. Copy the `id` value of the delivery cost item — this is the POS ID
8. In Choice admin → **Features** → **POS terminal** → paste this ID into the **Delivery cost POS ID** field
9. Save settings

> The token from step 2 expires after 1 hour — if requests start failing, repeat step 1–2 to get a fresh token.

## Discounts and Tips Setup

Both discounts and tips require `FlexibleDiscountId` and `FlexibleSurchargeId` to be configured in the plugin config.

### Finding the IDs

1. Go to `%appdata%\iiko\CashServer\logs\plugin-ChoiceQr`
2. Open the latest log — search for `FlexibleDiscount` and `Surcharge`
3. The IDs appear in the log output when the plugin initializes

### Configuring in Choice

1. Admin → **Features** → **POS terminal** → open Syrve settings
2. Enter `FlexibleDiscountId` in the **Discount POS ID** field
3. Enter `FlexibleSurchargeId` in the **Surcharge POS ID** field
4. For external delivery orders (marketplace): enter `DiscountIdForExternalDeliveryOrder`
5. Save and test with a discount order
