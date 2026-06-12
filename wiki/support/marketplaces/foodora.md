# Foodora Integration

## Overview

Foodora integration works via auto-sync — Choice does NOT push live updates to Foodora. Menu data is re-fetched by Foodora every ~5 minutes. Behavior is similar to Bolt Food.

## Connection

1. In Choice admin, go to **Marketplace** → **Foodora**
2. Enter the Foodora venue credentials (provided by Foodora account manager)
3. Sync menu
4. Verify items appear on Foodora app

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

**Live updates are NOT working for Foodora.** All changes are picked up by Foodora's auto-sync every 5 minutes. There is no way to push changes immediately.

## Discounts

All discount types are supported:
- **% discount**
- **Amount discount**
- **Free delivery** discount

> Platform-funded promotions (Foodora's own campaigns) are NOT passed to Choice.

## Modifiers

- Price and availability sync at **item level**
- Min/max quantity on modifier groups is supported
- Changes reflected after next auto-sync (~5 min)

## Packaging

1. Create packaging in Delivery settings
2. Assign to dishes
3. In Foodora integration settings → enable **"Use delivery package"**
4. Re-sync menu (takes effect on next auto-sync cycle)

## Order Flow

1. Customer places order on Foodora
2. Order appears in Choice Business app
3. Restaurant accepts the order
4. Foodora dispatches courier
5. Order status updates in Choice Business

## Time-Restricted Menu Sections

- After adding a new section with time restrictions, disconnect and reconnect the integration
- New section takes effect the **next day**

## Known Issues & Fixes

### Menu change not reflected on Foodora
- Wait up to 5 minutes for auto-sync cycle
- Check that the change was saved in Choice admin
- Trigger manual sync from Choice admin if available
- If still not updated after 10–15 min: contact Choice support

### Item availability delay (sold-out still showing)
- Expected behavior — Foodora does not support live push
- Availability change will reflect on next 5-min auto-sync
- For immediate removal: pause restaurant in Foodora Partner Portal

### Cannot immediately remove item from Foodora
- No live push available, inherent ~5 min delay
- Workaround for urgent situations: pause venue in Foodora Partner Portal directly

### Order not received in Choice Business
- Check that Choice Business app is running and device is online
- Verify correct venue is selected

## Contact

- **Foodora support**: via Foodora Partner Portal
- **Integration issues**: Choice support team
