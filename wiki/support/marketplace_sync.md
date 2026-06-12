# Marketplace Sync

How menu changes sync to delivery platforms (Wolt, Bolt, Foodora, Glovo, Uber, Just Eat/Pyszne, LOKO).

---

## Live Update Speeds

| Platform | Live Updates | Speed | Notes |
|----------|-------------|-------|-------|
| **Wolt** | YES | ~1 min for items | Categories take ~15 min. Options sync in 15 min or via manual sync. |
| **Glovo** | YES | ~1 min for items | Categories take ~15 min. Sections/Categories/Options availability must be synced manually. |
| **Uber Eats** | YES | ~1 min for items | Categories take ~15 min. Options sync in 15 min or via manual sync. |
| **Foodora** | NO | Auto-sync every 5 min | Options can only sync every 5 min or via manual sync. |
| **Bolt** | NO | Auto-sync every 5 min | Options can only sync every 5 min or via manual sync. |

**To manually sync:** Admin panel → Menu → Synchronization → click "Sync Menu"

---

## What modifier fields sync per platform

| Platform | Price | Availability | Min/Max Quantity | Notes |
|----------|-------|-------------|-----------------|-------|
| **Bolt** | ✅ | ✅ | — | Items and options |
| **Wolt** | ✅ | ✅ | — | Items and options |
| **Glovo** | ✅ | ✅ | — | Sets/combos only |
| **Foodora** | ✅ | ✅ | — | Items and options |
| **Uber Eats** | ✅ (items) | ✅ (sets) | — | Price syncs for items; availability for sets |
| **Just Eat / Pyszne / Bistro** | ✅ | ✅ | ❌ (no min/max) | Min/max quantity not supported |
| **LOKO** | ✅ | ✅ | — | Items and options |

---

## Packaging fee on marketplaces

1. Set up packaging first: Admin panel → Features → Takeaway or Delivery → "Cost of Packaging"
2. Click "Add New Pack" → set name, price, and assign to the whole menu / a category / a specific item
3. One package per item maximum
4. To apply packaging to a marketplace: enable "Use Delivery Package" for each marketplace separately
5. After enabling — **manually sync the menu**

Packaging works for all marketplaces: Wolt, Bolt, Foodora, Uber, Glovo.

The "POS id" field in packaging is only needed if a POS system is connected.

---

## New items not appearing on a marketplace

New items are not pushed automatically — you must sync them:

1. Admin panel → Menu → Synchronization
2. Select the items or categories under "ITEMS"
3. Click Save → then manually sync if needed

If items still don't appear after sync:
- Check if the dish photo meets the marketplace's requirements
- Verify the dish is enabled and marked as available for that marketplace in Choice
- Contact the marketplace's support if the issue persists after syncing
