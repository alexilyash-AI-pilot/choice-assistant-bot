# Glovo Integration

## Overview

Glovo supports live updates for item availability and pricing. Modifier option changes require a manual sync trigger — they do NOT sync automatically.

## Connection

1. In Choice admin, go to **Marketplace** → **Glovo**
2. Enter the Glovo store credentials (provided by Glovo account manager)
3. Sync menu
4. Verify items appear on Glovo app

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

## Live Update Speeds

| Update type | Speed |
|------------|-------|
| Item availability (86/sold out) | ~1 minute |
| Price change | ~1 minute |
| Modifier options | **Manual only** — does NOT auto-sync |
| New menu section/item | Manual sync recommended |

Live updates ARE working for Glovo for items and prices. **Modifier options require a manual sync** — they will not update automatically.

## Discounts

All discount types are supported:
- **% discount**
- **Amount discount**
- **Free delivery** discount

> Platform-funded promotions (Glovo's own campaigns) are NOT passed to Choice.

## Modifiers

- Price and availability sync at **item level**
- **IMPORTANT**: Modifier changes require manual sync — changes do NOT push automatically to Glovo
- To update modifiers: make changes in Choice → go to Glovo integration settings → click **Sync modifiers** (or full sync)

## Packaging

1. Create packaging in Delivery settings
2. Assign to dishes
3. In Glovo integration settings → enable **"Use delivery package"**
4. Re-sync menu

## Order Flow

1. Customer places order on Glovo
2. Order appears in Choice Business app
3. Restaurant accepts the order (timeout: ~10 minutes)
4. Glovo dispatches courier
5. Order status updates in Choice Business

## Time-Restricted Menu Sections

- After adding a new section with time restrictions, disconnect and reconnect the integration
- New section takes effect the **next day**

## Known Issues & Fixes

### Modifier price/availability not updated on Glovo
- This is by design — modifiers do NOT auto-sync on Glovo
- Solution: go to Glovo settings in Choice admin → trigger manual sync for modifiers
- After manual sync, allow 1–2 minutes for Glovo to process

### Item availability not updating (sold-out item still showing)
- Live push should work within ~1 min
- If delayed: check device internet connection
- If persistent: try manual sync from Choice admin

### Item image not appearing on Glovo
- Images must be in Glovo's accepted format (JPG/PNG, specific dimensions)
- Re-upload image in Choice and re-sync
- Glovo can take up to 30 minutes to process new images

### Menu section not visible on Glovo
- Check if section is active
- For new time-restricted sections: reconnect integration, takes effect next day
- Check that items in the section are also active

### Order not appearing in Choice Business
- Verify device is online and app is running
- Check that the venue is active on Glovo

### Restaurant paused on Glovo but not in Choice
- Glovo allows pausing directly in their partner portal
- This state is not reflected in Choice admin
- Re-open from both Choice and Glovo partner portal if needed

## Contact

- **Glovo support**: via Glovo Partner Portal
- **Integration issues**: Choice support team
