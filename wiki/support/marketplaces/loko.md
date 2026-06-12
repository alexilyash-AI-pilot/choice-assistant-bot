# LOKO Integration

## Overview

LOKO is a marketplace available in Czech Republic and Ukraine (LOKO UA). Both variants use live updates and have similar integration behavior. Live updates are working with ~1 minute delay for items and ~20 minutes for modifier options.

## Variants

| Variant | Market | Notes |
|---------|--------|-------|
| LOKO | Czech Republic / Slovakia | Primary variant |
| LOKO UA | Ukraine | Separate integration, same features |

## Connection

1. In Choice admin, go to **Marketplace** → **LOKO** (or **LOKO UA**)
2. Enter the LOKO venue credentials
3. Sync menu
4. Verify items appear on LOKO app

## What Gets Synchronized

| Feature | Synced | Notes |
|---------|--------|-------|
| Menu items | ✅ | Name, description, image, price |
| Modifier groups | ✅ | |
| Modifier prices | ✅ | |
| Modifier availability | ✅ | Item level |
| Item availability (86) | ✅ | Live, ~1 min |
| Packaging | ✅ | Enable "Use delivery package" |
| Restaurant open/closed | ✅ | |

## Live Update Speeds

| Update type | Speed |
|------------|-------|
| Item availability (86/sold out) | ~1 minute |
| Price change | ~1 minute |
| Modifier options | ~20 min or manual |
| New menu section/item | Manual sync recommended |

Live updates ARE working for LOKO.

## Discounts

All discount types are supported:
- **% discount**
- **Amount discount**
- **Free delivery** discount

> Platform-funded promotions (LOKO's own campaigns) are NOT passed to Choice.

## Modifiers

- Price and availability sync at **item level**
- Modifier changes: ~20 min or use manual sync

## Packaging

1. Create packaging in Delivery settings
2. Assign to dishes
3. In LOKO integration settings → enable **"Use delivery package"**
4. Re-sync menu

## Order Flow

1. Customer places order on LOKO
2. Order appears in Choice Business app
3. Restaurant accepts the order
4. LOKO dispatches courier
5. Order status updates in Choice Business

## Time-Restricted Menu Sections

- Time restrictions sync to LOKO
- Adding a new time-restricted section: disconnect and reconnect integration; takes effect the **next day**

## LOKO UA Specifics

LOKO UA is a separate integration for the Ukrainian market:
- Connected separately from LOKO CZ
- Uses UAH currency
- Same feature set and sync behavior
- Separate credentials required

## Known Issues & Fixes

### Modifier options not updating on LOKO
- Modifier option changes take up to 20 minutes to sync
- Use manual sync from Choice admin to force update
- If still not updated after 30 min: contact Choice support

### Item availability not syncing
- Live push should work within ~1 min
- Check internet connection on device
- Try manual sync if persistent

### Connecting LOKO UA instead of LOKO CZ
- Make sure to use the correct marketplace section in Choice admin
- LOKO and LOKO UA are listed as separate integration options
- Credentials differ between markets — use credentials from the respective LOKO market account

### Menu not visible on LOKO after sync
- Verify all items are active
- Check that images meet LOKO's requirements
- Trigger manual sync and wait 2–3 min

## Contact

- **LOKO support**: via LOKO Partner Portal
- **LOKO UA support**: via LOKO Ukraine partner contact
- **Integration issues**: Choice support team
