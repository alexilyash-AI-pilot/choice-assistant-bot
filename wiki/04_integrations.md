# Choice Integrations

## Delivery Marketplace Integrations

Choice integrates with all major food delivery platforms via **Collection Point** (Smart & Pro plans).

| Platform | Type | What it enables |
|----------|------|----------------|
| **Wolt** | Marketplace | Orders, menu management, analytics from one tablet |
| **Bolt Food** | Marketplace | Orders consolidated in Choice Business app |
| **Glovo** | Marketplace | Orders + menu management unified |
| **Uber Eats** | Marketplace | Orders, expand reach, no separate tablet needed |
| **Foodora** | Marketplace | Orders and menu managed from Choice |
| **Just Eat / Pyszne.pl / Bistro.sk** | Marketplace | Orders consolidated (PL, SK) |
| **LOKO** | Marketplace | Orders consolidated (UA, LT) |

### Country Availability

| Platform | CZ | SK | PL | UA | EE | LT | LV | HU | RO | PT |
|----------|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| Wolt | ✓ | ✓ | ✓ | — | ✓ | ✓ | ✓ | ✓ | ✓ | — |
| Bolt Food | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | — |
| Foodora | ✓ | ✓ | — | — | — | — | — | ✓ | — | — |
| Glovo | — | — | ✓ | ✓ | — | — | — | — | ✓ | ✓ |
| Uber Eats | ✓* | — | ✓ | — | — | — | — | — | — | — |
| Just Eat / Pyszne.pl | — | — | ✓ | — | — | — | — | — | — | — |
| Bistro.sk | — | ✓ | — | — | — | — | — | — | — | — |
| LOKO | — | — | — | ✓ | — | ✓ | — | — | — | — |

*CZ: coming soon

### How Marketplace Integration Works
1. Restaurant connects marketplace account in Choice admin panel (provides Store ID)
2. Choice menu syncs to marketplace automatically — old menu deactivated
3. Customer orders on Wolt/Glovo/etc. → order appears in Choice Business app
4. Staff confirms in Choice → syncs to POS
5. All marketplace analytics available in Choice dashboard

---

## On-Demand Courier Services

| Service | Type | Notes |
|---------|------|-------|
| **Wolt Drive** | Courier dispatch | Primary — fixed price per delivery, no % commission |
| **Foodora Go** | Courier dispatch | On-demand Foodora courier for direct orders |
| **Stuart** | Courier dispatch | On-demand courier for direct orders |
| **Glovo on-demand** | Courier dispatch | Glovo courier for non-Glovo orders |
| **Uber Direct** | Courier dispatch | Uber courier for direct orders |
| **Uklon** | Courier dispatch | Ukraine only |
| **Byteberry** | Advanced dispatch | Advanced courier management and dispatching system for larger operations |

Available on all plans (Basic and up).

**Own couriers:** restaurants can also connect their own courier fleet through Choice — orders are dispatched and managed directly from the platform.

Available on all plans (Basic and up).

---

## POS System Integrations

| POS System | Priority | Notes |
|------------|----------|-------|
| **Dotykačka** | ⭐ Primary | Most reliable — recommended first |
| **Storyous** | ⭐ Primary | Most reliable — recommended first |
| **Poster** | Secondary | Full integration |
| **Syrve (iiko)** | Secondary | Full integration |
| **Servio** | Secondary | Full integration |
| **R-Keeper** | Secondary | Full integration |
| **Profit** | Secondary | Full integration |
| **Restis** | Secondary | Full integration |
| **Compucash** | Secondary | Full integration |
| **ID POS** | Secondary | Full integration |
| **POS ID sync** | Secondary | Full integration |

**Open API:** Choice offers an open API with 50+ integrations available. Restaurants and partners can also connect their own custom systems via the API.

> **Note:** Dotykačka and Storyous are the most stable integrations — always offer these first. Other POS integrations exist but are less stable; discuss with an experienced colleague before selling them.

**Important QR distinction:**
- **QR orders** can work **without POS integration** — orders come to the Choice Business tablet, staff manually mark them in the POS.
- **QR payments require POS integration** — items must be marked in the POS first, then the bill is automatically transferred to the QR code for the guest to pay. Only Dotykačka and Storyous are recommended for QR payments.

### What POS Integration Does
- Orders from Choice (website, QR table, marketplace) flow automatically to POS
- No manual re-entry at the counter
- Kitchen display system (KDS) receives orders instantly
- Payments sync automatically
- Menu changes in Choice can sync to POS

---

## Payment Integrations

| Processor | Region | Methods |
|-----------|--------|---------|
| **Adyen** | Global | Card, Apple Pay, Google Pay, 3DS |
| **LiqPay** | Ukraine | Card, bank transfer |

Supported payment methods: **All major cards (Visa, Mastercard, Amex, Maestro), Apple Pay, Google Pay, Cash** (Smart & Pro plans).

---

## Marketing & Analytics Integrations

| Tool | What it connects |
|------|----------------|
| **Google Analytics** | Website traffic and conversion tracking |
| **Google Tag Manager** | Tag management for all tracking scripts |
| **Google Search Console** | SEO performance monitoring |
| **Google Maps** | Automatic positive review forwarding |
| **Google Reservations** | Table booking widget synced with Google Search / Maps |
| **Google My Business Feed** | Menu and info sync to Google listing |
| **Facebook Page** | Menu and ordering integrated with Facebook presence |
| **Facebook Pixel** | Ad conversion tracking and retargeting |
| **TripAdvisor** | Review sharing |

---

## AI / LLM Integrations

Choice is AI-native and integrates with leading AI models to power its smart features (menu management, marketing content, analytics assistant, review replies, translations).

| Provider | Models |
|----------|--------|
| **Anthropic** | Claude |
| **OpenAI** | GPT-4 and family |
| **Google** | Gemini |

---

## Communication Integrations

| Tool | Use |
|------|-----|
| **Telegram** | Real-time review and order notifications to manager |
| **Email (SMTP)** | Reservation confirmations, marketing campaigns |
| **SMS** | Marketing, retention, reservation reminders (Smart & Pro) |
| **Push Notifications** | Mobile app and web push for promotions |

---

## Calendar Integrations

| Tool | Use |
|------|-----|
| **Google Calendar** | Reservation sync for staff (Standard+ plan) |

---

## Summary by Plan

| Integration Category | Basic | Standard | Smart | Pro |
|---------------------|-------|----------|-------|-----|
| Courier services (Wolt Drive, Stuart, etc.) | ✓ | ✓ | ✓ | ✓ |
| Marketplace orders (Collection Point) | Add-on €40 | Add-on €40 | ✓ | ✓ |
| Basic POS integration | ✓ | ✓ | ✓ | ✓ |
| Advanced POS (Storyous, etc.) | — | — | — | ✓ |
| Google Analytics / Pixel | ✓ | ✓ | ✓ | ✓ |
| SMS Marketing | — | — | ✓ | ✓ |
| Google Calendar | — | ✓ | ✓ | ✓ |
