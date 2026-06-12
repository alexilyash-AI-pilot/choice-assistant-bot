# POS ID Sync

A tool in the Choice admin panel for assigning POS IDs to existing menu items without editing each item manually.

## What It Covers

Assigns POS IDs to:
- Dishes
- Additions (modifiers/options)
- Tables
- Utilities: packs, cutlery

## Requirements

- **Active POS integration** must be connected
- **Only works on desktop and tablet** — not supported on mobile

## How It Works

1. When a menu is set up and POS is connected, an indicator appears showing how many items are missing POS IDs (or confirming all are synced)
2. Click the indicator to open a detailed screen listing all items by section/category

### First Use

The first time you enter, the system prompts you to **"Request the latest data from your POS"**. This step must be completed to unlock all functionality. After requesting, you see counters per section showing how many items are missing POS IDs.

### Editing POS IDs

1. Click the POS ID field for an item
2. System suggests matching items from POS based on name
3. Select the correct item from the list
4. If the correct option is not shown: type the name or POS ID manually — new suggestions appear
5. **Must select from the suggestion list** — typing a raw value without selecting does not sync

### If the item still doesn't appear

- Verify the item exists in your POS system
- Request the latest data from POS again

### Filtering Unsynced Items

Check the **"Unsynced"** filter box to show only items missing POS IDs.

## Notes

- Automatic name-based search is available for all POS IDs across the admin panel
- This tool applies to all POS systems that require POS IDs (Dotykačka, Storyous, Poster, R-Keeper, Restis, etc.)
