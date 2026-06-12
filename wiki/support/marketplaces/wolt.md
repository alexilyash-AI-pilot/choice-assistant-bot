# Wolt Integration

## Overview

Wolt is the most fully-featured marketplace integration in Choice. It supports live menu updates, full modifier sync, all discount types, and automatic courier tracking.

## Connection

1. In Choice admin, go to **Marketplace** → **Wolt**
2. Enter the Wolt venue ID (provided by Wolt account manager)
3. Sync menu
4. Verify items appear on Wolt

> If the venue ID is unknown, ask the restaurant to check their Wolt Partner Portal or contact their Wolt account manager.

## What Gets Synchronized

| Feature | Synced | Notes |
|---------|--------|-------|
| Menu items | ✅ | Name, description, image, price |
| Modifier groups | ✅ | |
| Modifier prices | ✅ | |
| Modifier availability | ✅ | Item level |
| Item availability (86) | ✅ | Live, ~1 min |
| Packaging | ✅ | Enable "Use delivery package" in settings |
| Restaurant open/closed | ✅ | |
| Time-restricted sections | ✅ | See note below |

## Live Update Speeds

| Update type | Speed |
|------------|-------|
| Item availability (86/sold out) | ~1 minute |
| Price change | ~1 minute |
| Modifier options | ~15 min or manual trigger |
| New menu section/item | Manual sync recommended |

Live updates ARE working for Wolt — changes push immediately without waiting for auto-sync.

## Discounts

All discount types are supported:
- **% discount** (e.g. 20% off entire menu)
- **Amount discount** (e.g. -50 CZK on order)
- **Free delivery** discount
- **Minimum order amount** for discount

> Platform-funded promotions (Wolt's own first-order bonus, free delivery campaigns) are NOT passed to Choice. These show on the Wolt app but do not affect Choice-side discount calculations.

## Modifiers

- Price and availability sync at **item level**
- Wolt supports `min_quantity` and `max_quantity` on modifier groups
- Modifier changes: ~15 min or use manual sync

## Packaging

1. Create packaging in Delivery settings
2. Assign to dishes
3. In Wolt integration settings → enable **"Use delivery package"**
4. Re-sync menu

## Order Flow

1. Customer places order on Wolt
2. Order appears in Choice Business app
3. Restaurant must accept within **3–5 minutes** — if not accepted, Wolt automatically cancels the order
4. After acceptance, Wolt dispatches a courier
5. Courier tracking is visible in Choice Business app (Wolt Drive)

### Critical: Order Acceptance Timeout

**Wolt cancels unaccepted orders after 3–5 minutes.** Staff must monitor Choice Business app and accept promptly.

## Wolt Drive (Courier Tracking)

When using Wolt's own courier service (Wolt Drive):
- Courier location is tracked and visible in Choice Business app
- Estimated delivery time updates in real time
- Issues with Wolt Drive couriers → contact Wolt support directly

## Time-Restricted Menu Sections

- Time restrictions set in Choice sync to Wolt
- **Adding a new time-restricted section**: disconnect and reconnect the Wolt integration; the new section takes effect the **next day**
- Existing sections with time restrictions update normally

## Known Issues & Fixes

### Items not appearing on Wolt after menu sync
- Check that items are marked as **active** in Choice
- Check that items are assigned to the correct menu
- Wait 1–2 minutes and refresh Wolt Partner Portal
- If still missing: trigger manual sync from Choice admin

### Modifier prices not updated on Wolt
- Modifier changes can take up to 15 minutes
- Use manual sync button in Choice admin to force update

### Order not received in Choice Business
- Check that Choice Business app is open and logged in
- Check internet connection on the tablet/device
- Verify the correct venue is selected in Choice Business

### "Venue not found" error when connecting
- Verify the Wolt venue ID is correct
- The venue must be live on Wolt (not in test mode)
- Contact Wolt support if the ID appears correct but connection fails

### Discount not applying on Wolt
- Discount must be active and within validity dates
- Platform-funded Wolt promotions do not sync — these are Wolt-side only
- Restaurant discounts created in Choice sync correctly

## Contact

- **Wolt support**: via Wolt Partner Portal
- **Integration issues**: Choice support team
