# Uber Eats Integration

## Overview

Uber Eats supports live menu updates. Key difference from other platforms: modifier **availability** syncs at the **modifier set (group) level**, not the individual item level.

## Connection

1. In Choice admin, go to **Marketplace** → **Uber Eats**
2. Enter the Uber venue UUID (from Uber Eats Manager portal)
3. Sync menu
4. Verify items appear in Uber Eats app

## What Gets Synchronized

| Feature | Synced | Notes |
|---------|--------|-------|
| Menu items | ✅ | Name, description, image, price |
| Modifier groups | ✅ | |
| Modifier prices | ✅ | Item level |
| Modifier availability | ✅ | **Set (group) level only** |
| Item availability (86) | ✅ | Live, ~1 min |
| Packaging | ✅ | Enable "Use delivery package" in settings |
| Restaurant open/closed | ✅ | |

## Live Update Speeds

| Update type | Speed |
|------------|-------|
| Item availability (86/sold out) | ~1 minute |
| Price change | ~1 minute |
| Modifier options | ~15 min or manual |
| New menu section/item | Manual sync recommended |

Live updates ARE working for Uber Eats.

## Critical: Modifier Availability Behavior

**Uber Eats syncs modifier availability at the modifier SET level, not the individual item level.**

This means:
- If you mark a single modifier option as unavailable in Choice, Uber Eats will hide/show the **entire modifier group** rather than just that one option
- Example: if you have "Sauces" group with 5 options and mark "Ketchup" as unavailable, Uber may hide all sauces
- Plan accordingly when 86-ing individual modifiers on Uber

## Discounts

All discount types are supported:
- **% discount**
- **Amount discount**
- **Free delivery** discount

> Platform-funded promotions (Uber's own campaigns — first order, Happy Hours) are NOT passed to Choice.

## Modifiers

- Modifier **prices** sync at item level
- Modifier **availability** syncs at **set (group) level**
- Modifier changes: ~15 min or use manual sync
- Min/max quantity on groups is supported

## Packaging

1. Create packaging in Delivery settings
2. Assign to dishes
3. In Uber Eats integration settings → enable **"Use delivery package"**
4. Re-sync menu

## Order Flow

1. Customer places order on Uber Eats
2. Order appears in Choice Business app
3. Restaurant must accept within **~5 minutes** — if not accepted, Uber automatically cancels
4. Uber dispatches courier
5. Courier tracking visible in Choice Business app

### Critical: Order Acceptance Timeout

**Uber Eats cancels unaccepted orders after ~5 minutes.** Staff must monitor Choice Business app.

## Time-Restricted Menu Sections

- Time restrictions sync to Uber Eats
- Adding a new time-restricted section: disconnect and reconnect integration; takes effect the **next day**

## Known Issues & Fixes

### Modifier availability not working as expected
- Remember: Uber syncs at **set level**, not item level
- If only some options in a group should be unavailable, the entire group may be affected
- Workaround: restructure modifier groups so each unavailable option is in its own group if needed

### Modifier prices not updated
- Modifier changes can take up to 15 minutes
- Use manual sync from Choice admin to force update

### Menu item not appearing on Uber Eats
- Verify item is active and assigned to correct menu
- Images must meet Uber's requirements (minimum resolution, correct format)
- Trigger manual sync from Choice admin
- Allow 2–3 min for Uber to process

### Orders being cancelled immediately
- Likely due to timeout — restaurant did not accept within 5 minutes
- Ensure Choice Business app is open on a monitored device
- Check device internet connection

### "Restaurant not found" when connecting
- Verify Uber venue UUID is correct (found in Uber Eats Manager portal)
- Venue must be live and active on Uber Eats

### Price mismatch between Choice and Uber
- Uber caches prices for up to 15 minutes
- If mismatch persists: trigger manual full sync
- If still wrong after sync: check for currency/rounding settings

## Contact

- **Uber Eats support**: via Uber Eats Manager portal (manager.uber.com)
- **Integration issues**: Choice support team
