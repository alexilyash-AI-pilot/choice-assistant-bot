# Compocash POS Integration

## Overview

Compocash is a POS system available primarily in Slovakia.

| Feature | Supported |
|---------|-----------|
| Table ordering | YES |
| Takeaway | YES |
| Delivery | YES |
| Collection point | YES |
| QR payments | Partial (check with support) |
| Discounts / Promo codes / Loyalty | YES |

## How to Connect

1. Contact Compocash to request the integration be activated for the venue
2. In Choice admin, go to **Features** → **POS terminal** → select **Compocash**
3. Generate the API token in the Choice backoffice (or Compocash will provide a connection link)
4. Compocash generates a connection link — open this link to authorize the integration
5. Enter the token from Choice into the connection form
6. Save and verify the connection is active

> The entire initial setup involves Compocash's team — they configure their side and provide the connection link.

## Menu Synchronization

Menu sync with Compocash is **manual only** — there is no automatic sync.

Two methods:
1. **Export from Compocash** — export the menu file from Compocash and import it into Choice
2. **Manual entry** — add each dish from Compocash manually into Choice with the correct POS ID

There is no live or scheduled automatic sync. After any menu changes on the Compocash side, you must manually update Choice accordingly.

## Working with Orders

Compocash supports two integration modes:

### Mode 1: Via Choice Business (default)
1. Order arrives in **Choice Business** app
2. Staff accept the order in Choice Business
3. After acceptance, the order is sent to Compocash POS
4. Staff then process the order on the Compocash terminal

### Mode 2: Direct to Compocash
- Orders go straight to Compocash without appearing in Choice Business first
- No acceptance step in Choice Business app

### Supported Order Types

| Order type | Supported |
|------------|-----------|
| Delivery | ✅ |
| Takeaway | ✅ |
| Table orders | ✅ |
| Collection point | ✅ |
| QR payments | Partial |

### What Transfers from Choice to Compocash

| Data | Notes |
|------|-------|
| Discounts / promo codes / loyalty | Fixed discount amount is shown on the order |
| Order comments | Transferred as-is |
| Payment status | Paid / not paid |
| Delivery address | Passed to Compocash |
| Table number | For table orders |
| Preorders | Supported |
