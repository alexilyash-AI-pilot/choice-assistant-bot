# Marketplace Integrations

Overview of all delivery marketplace integrations supported by Choice platform.

## Supported Marketplaces

| Marketplace | Live Updates | Item Speed | Options Speed | Notes |
|-------------|-------------|-----------|---------------|-------|
| [Wolt](wolt.md) | ✅ Working | ~1 min | 15 min or manual | Most reliable |
| [Bolt Food](bolt.md) | ❌ Not working | 5 min auto-sync | 5 min auto-sync | No live push |
| [Glovo](glovo.md) | ✅ Working | ~1 min | Manual only | |
| [Foodora](foodora.md) | ❌ Not working | 5 min auto-sync | 5 min auto-sync | No live push |
| [Uber Eats](uber.md) | ✅ Working | ~1 min | 15 min or manual | Option availability syncs at set level |
| [Just Eat / Pyszne / Bistro](just_eat.md) | ✅ Working | ~5 min | 20 min or manual | No min/max qty |
| [LOKO](loko.md) | ✅ Working | ~1 min | 20 min or manual | UA variant available |

## Key Concepts

### Live Updates vs Auto-Sync
- **Live updates**: changes in Choice push to marketplace in near-real-time (availability, sold-out, price)
- **Auto-sync**: marketplace re-fetches data from Choice every 5 minutes; no immediate push

### What Gets Synchronized
- Menu items (names, descriptions, images, prices)
- Modifier groups and options
- Availability (86 / sold-out)
- Packaging
- Restaurant open/closed status

### Modifier Sync Matrix

| Platform | Price | Availability | Level |
|----------|-------|-------------|-------|
| Wolt | ✅ | ✅ | Item level |
| Bolt | ✅ | ✅ | Item level |
| Glovo | ✅ | ✅ | Item level |
| Foodora | ✅ | ✅ | Item level |
| Uber Eats | ✅ | ✅ | **Set level** (not item) |
| Just Eat | ✅ | ✅ | Item level (no min/max qty) |
| LOKO | ✅ | ✅ | Item level |

### Discounts

| Platform | % Discount | Amount Discount | Free Delivery | Platform promos |
|----------|-----------|----------------|---------------|-----------------|
| Wolt | ✅ | ✅ | ✅ | ❌ not passed to Choice |
| Bolt | ✅ | ✅ | ✅ | ❌ not passed to Choice |
| Glovo | ✅ | ✅ | ✅ | ❌ not passed to Choice |
| Foodora | ✅ | ✅ | ✅ | ❌ not passed to Choice |
| Uber Eats | ✅ | ✅ | ✅ | ❌ not passed to Choice |
| Just Eat | ✅ | ✅ | ✅ | ❌ not passed to Choice |
| LOKO | ✅ | ✅ | ✅ | ❌ not passed to Choice |

> **Note**: Restaurant-funded discounts (created in Choice) transfer automatically. Platform-funded promotions (first order bonuses, free delivery promotions) are NOT passed to Choice — these are platform-side only.

### Packaging Setup (All Marketplaces)

1. Go to **Delivery** function in Choice admin
2. Create packaging item(s)
3. Assign packaging to dishes
4. In marketplace settings, enable **"Use delivery package"**
5. Sync menu to marketplace

### Order Acceptance Timeouts

Critical — if order is not accepted within this time, it is automatically cancelled:

| Platform | Timeout |
|----------|---------|
| Wolt | 3–5 minutes |
| Uber Eats | ~5 minutes |
| Just Eat / Pyszne | ~3 minutes |
| Bolt | ~10 minutes |
| Glovo | ~10 minutes |

## Common Issues

- **Menu not updating on marketplace**: check if live updates are working (see individual pages); for Bolt/Foodora wait up to 5 min for auto-sync
- **New time-restricted menu section not appearing**: after adding a new section with time restrictions, disconnect and reconnect marketplace (takes effect the next day)
- **Modifier not syncing**: verify modifier is assigned to item in Choice; for Uber check at set level not item level
- **Packaging not applied**: confirm "Use delivery package" is enabled in marketplace settings and menu was re-synced
- **Order arrives then immediately cancels**: order acceptance timeout exceeded — ensure staff monitors Choice Business app
