# Admin Logs (Global Logs)

The Global Logs feature records all actions taken in the admin panel — useful for troubleshooting, auditing changes, and tracking who changed what and when.

---

## Where to find it

Admin panel → **Settings** → **Global Logs**

---

## What it tracks

- All admin panel actions across all sections
- Which user performed each action
- Timestamp of each action
- What was changed (for supported fields: shows `prevValue` with before/after values)

**Examples of what you can track:**
- Dish price changes (before and after values)
- Option/addition changes
- Integration settings changes
- User permission changes
- Menu enable/disable actions

---

## Filters

| Filter | Options |
|--------|---------|
| **Date range** | Set start and end date |
| **User** | Filter by specific admin user |
| **Section** | Filter by area (menu, integrations, settings, etc.) |

---

## How to use it for troubleshooting

**"Who changed this dish price?"**
→ Filter by section = Menu, look for the dish name in the log entries. The `prevValue` field shows what the value was before the change.

**"When was this integration modified?"**
→ Filter by section = Integrations, set date range when the issue started.

**"Did a staff member disable the menu?"**
→ Filter by section = Menu, look for enable/disable actions with timestamps.

---

## Escalating issues using logs

When escalating a support ticket involving notifications or orders in Choice Business app, **always include logs** from the relevant time period. The support team or developers can use logs to trace exactly what happened at the system level.

See: [Troubleshooting guide](troubleshooting.md) for full escalation guidelines.
