# POS Integrations

Reference for all POS systems supported by Choice — setup, order flow, and error troubleshooting.

## Supported POS Systems

| POS | Countries | Table | Takeaway | Delivery | QR Pay | Booking |
|-----|-----------|-------|----------|----------|--------|---------|
| [Poster](poster.md) | UA, PL, others | YES | YES | YES | YES | — |
| [Dotykačka](dotykacka.md) | CZ, SK | YES | YES | YES | YES | YES |
| [Storyous](storyous.md) | CZ, SK | YES | YES | YES | YES | in progress |
| [Syrve (Iiko)](syrve.md) | UA, others | YES | YES | YES | YES (plugin) | — |
| [R-Keeper](rkeeper.md) | UA, others | YES | YES | YES | — | — |
| [Restis](restis.md) | CZ | YES | YES | YES | NO | NO |
| [Compocash](compocash.md) | SK | YES | YES | YES | — | — |
| [ID POS](idpos.md) | — | YES | YES | YES | YES | — |
| [Servio](servio.md) | — | — | — | — | — | — |
| [Profit](profit.md) | UA | — | — | — | — | — |

## Common POS Rules

1. When POS integration is active, **all items without a POS ID are hidden from the menu**.
2. If a dish or modifier has an **incorrect POS ID**, the order is automatically cancelled by the POS.
3. All products, categories, tables, and options must have a POS ID matching the POS system.
4. **Menu sync does not work if the "one menu" function is enabled** (Poster, Profit).

## POS ID Sync Tool

- Use the [POS ID Sync](pos_id_sync.md) feature to assign POS IDs from within the Choice admin panel.
- Only available on desktop and tablet (not mobile).
- Requires an active POS integration.
