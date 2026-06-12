# Bolt Food Integration

## Overview

Bolt Food integration works via auto-sync — Choice does NOT push live updates to Bolt. Menu data is re-fetched by Bolt every ~5 minutes.

## Connection

1. In Choice admin, go to **Marketplace** → **Bolt Food**
2. Enter the Bolt venue credentials (provided by Bolt account manager)
3. Sync menu
4. Verify items appear on Bolt Food app

## What Gets Synchronized

| Feature | Synced | Notes |
|---------|--------|-------|
| Menu items | ✅ | Name, description, image, price |
| Modifier groups | ✅ | |
| Modifier prices | ✅ | |
| Modifier availability | ✅ | Item level |
| Item availability (86) | ✅ | Via 5 min auto-sync |
| Packaging | ✅ | Enable "Use delivery package" in settings |
| Restaurant open/closed | ✅ | |

## Live Update Speeds

| Update type | Speed |
|------------|-------|
| Item availability (86/sold out) | ~5 min (auto-sync) |
| Price change | ~5 min (auto-sync) |
| Modifier options | ~5 min (auto-sync) |

**Live updates are NOT working for Bolt Food.** Changes are picked up by Bolt's auto-sync every 5 minutes. There is no way to push changes immediately.

## Discounts

All discount types are supported:
- **% discount**
- **Amount discount**
- **Free delivery** discount

> Platform-funded promotions (Bolt's own campaigns) are NOT passed to Choice.

## Modifiers

- Price and availability sync at **item level**
- Min/max quantity on modifier groups is supported
- Changes reflected after next auto-sync (~5 min)

## Packaging

1. Create packaging in Delivery settings
2. Assign to dishes
3. In Bolt integration settings → enable **"Use delivery package"**
4. Re-sync menu (takes effect on next auto-sync cycle)

## Order Flow

1. Customer places order on Bolt Food
2. Order appears in Choice Business app
3. Restaurant accepts the order (timeout: ~10 minutes)
4. Bolt dispatches courier
5. Order status updates in Choice Business

## Time-Restricted Menu Sections

- After adding a new section with time restrictions, disconnect and reconnect the integration
- New section takes effect the **next day**

## Known Issues & Fixes

### Menu change not reflected on Bolt after 5 minutes
- Wait a full 5-minute cycle — Bolt's sync can be slightly delayed
- Check that the change was saved in Choice admin
- Trigger manual sync from Choice admin if available
- If still not updated after 10–15 min: contact Choice support

### Items marked 86/sold-out still showing as available on Bolt
- This is expected behavior — Bolt does not support live push
- The sold-out status will sync on the next 5-min cycle
- Inform customer that there is a ~5 min delay for availability changes

### Cannot immediately take an item off the menu
- Due to no live push, there is inherent delay
- Workaround: mark item as unavailable in Choice → wait up to 5 min for sync
- For immediate action: pause the restaurant directly in Bolt Partner Portal

### Order not received in Choice Business
- Check that Choice Business app is running and device is online
- Verify correct venue is selected

### Discount not working on Bolt
- Confirm discount is active and dates are correct
- Platform Bolt promotions (Bolt's own campaigns) do not sync to Choice

## Contact

- **Bolt support**: via Bolt Food Partner Portal
- **Integration issues**: Choice support team
