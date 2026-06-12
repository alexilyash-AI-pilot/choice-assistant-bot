# Just Eat / Pyszne.pl / Bistro.sk Integration

## Overview

Just Eat operates under different brand names in different markets:
- **Just Eat** — UK, Netherlands, and other markets
- **Pyszne.pl** — Poland
- **Bistro.sk** — Slovakia

All use the same underlying integration. Live updates are working but slower than Wolt/Uber. Critical limitation: **min/max quantity for modifier groups is not supported**.

## Connection

1. In Choice admin, go to **Marketplace** → **Just Eat** (or Pyszne / Bistro depending on market)
2. Enter the venue credentials provided by Just Eat/Pyszne/Bistro account manager
3. Sync menu
4. Verify items appear on the platform

## What Gets Synchronized

| Feature | Synced | Notes |
|---------|--------|-------|
| Menu items | ✅ | Name, description, image, price |
| Modifier groups | ✅ | |
| Modifier prices | ✅ | |
| Modifier availability | ✅ | Item level |
| Item availability (86) | ✅ | Live, ~5 min |
| Packaging | ✅ | Enable "Use delivery package" |
| Restaurant open/closed | ✅ | |
| Min/max quantity on modifiers | ❌ | **Not supported** |

## Live Update Speeds

| Update type | Speed |
|------------|-------|
| Item availability (86/sold out) | ~5 minutes |
| Price change | ~5 minutes |
| Modifier options | ~20 min or manual |
| New menu section/item | Manual sync recommended |

Live updates ARE working but slower than Wolt/Uber/Glovo.

## Critical Limitation: No Min/Max Quantity for Modifiers

**Just Eat does not support `min_quantity` / `max_quantity` on modifier groups.**

This means:
- If a modifier group in Choice has a required selection (min: 1) or limited selection (max: 2), this constraint will NOT be enforced on Just Eat
- Customers on Just Eat can skip required modifiers or select more options than allowed
- This is a platform limitation — not possible to fix without Just Eat implementing the feature

## Discounts

All discount types are supported:
- **% discount**
- **Amount discount**
- **Free delivery** discount

> Platform-funded promotions (Just Eat's own campaigns) are NOT passed to Choice.

## Modifiers

- Price and availability sync at **item level**
- **Min/max quantity NOT supported**
- Modifier changes: ~20 min or use manual sync

## Packaging

1. Create packaging in Delivery settings
2. Assign to dishes
3. In Just Eat/Pyszne/Bistro integration settings → enable **"Use delivery package"**
4. Re-sync menu

## Order Flow

1. Customer places order on Just Eat / Pyszne / Bistro
2. Order appears in Choice Business app
3. Restaurant must accept within **~3 minutes** — if not accepted, order is automatically cancelled
4. Platform dispatches courier
5. Order status updates in Choice Business

### Critical: Order Acceptance Timeout

**Just Eat / Pyszne cancels unaccepted orders after ~3 minutes.** This is one of the shortest timeouts among all platforms. Staff must monitor Choice Business app closely.

## Time-Restricted Menu Sections

- Time restrictions sync to the platform
- Adding a new time-restricted section: disconnect and reconnect integration; takes effect the **next day**

## Known Issues & Fixes

### Required modifier not enforced on Just Eat
- Expected behavior — Just Eat does not support min/max quantity
- No fix available; this is a platform limitation
- If critical: contact Just Eat account manager to request feature support

### Menu update slow to appear (more than 5 min)
- Just Eat has a slower sync cycle than Wolt/Uber
- Normal delay is 5 min for items, up to 20 min for modifiers
- For urgent changes: trigger manual sync from Choice admin
- Contact Just Eat support if not updated after 30 minutes

### Orders cancelled immediately after placement
- Very likely due to the 3-minute acceptance window being missed
- Ensure Choice Business app is permanently open on a monitored device
- Check device internet connection

### Items appearing in wrong order on platform
- Just Eat may have its own ordering logic in addition to Choice's menu order
- Re-sync menu from Choice admin
- Contact Just Eat if ordering is consistently wrong

### Integration shows as connected but orders not coming through
- Verify the correct platform variant is connected (Just Eat vs Pyszne vs Bistro)
- Check that the venue is marked active on the platform's partner portal
- Test by placing a test order

## Market-Specific Notes

### Pyszne.pl (Poland)
- Polish-language support in Choice admin
- Menu items can include Polish characters
- PLN currency

### Bistro.sk (Slovakia)
- Slovak-language support
- EUR currency

## Contact

- **Just Eat support**: via Just Eat Partner Centre
- **Pyszne.pl support**: via Pyszne Partner Portal
- **Bistro.sk support**: via Bistro Partner Portal
- **Integration issues**: Choice support team
