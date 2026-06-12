# Analytics Setup

Technical setup guides for GTM, GA4, Google E-commerce, Meta Conversion API, Google Consent Mode v2, and UTM tracking.

---

## GA4 Measurement Protocol

**Where to configure:** Admin panel → Template → Analytics

### Purchase event data structure

When a purchase completes, Choice sends a GA4 Measurement Protocol event with:

| Field | Value |
|-------|-------|
| `event_name` | `purchase` |
| `session_id` | current session ID |
| `currency` | order currency (e.g. CZK, EUR) |
| `value` | order total |
| `transaction_id` | unique order ID |
| `items` | array of ordered items |
| UTM params | `utm_source`, `utm_medium`, `utm_campaign`, `utm_content`, `utm_term` |

UTM parameters are passed through from the original visit and included in the event.

---

## UTM Tag Tracking (iframe)

Choice website and ordering widget can be embedded as an iframe. UTM parameters from the parent page are passed into the iframe using `URLSearchParams`.

### How it works

1. Parent page URL contains UTM parameters (e.g. `?utm_source=google&utm_medium=cpc`)
2. Parameters are read and passed to the iframe via `postMessage`
3. The iframe picks them up and stores them for use in analytics events

### postMessage events sent from the iframe

| Event | When fired |
|-------|-----------|
| `initialized` | iframe loads and is ready |
| `dateUpdated` | user selects a date (reservations) |
| `bookingCreated` | reservation confirmed |

### GTM configuration

In GTM, listen for `message` events from the iframe and use the data to fire GA4 or other analytics tags. Set up a custom event trigger for the `message` event type, then read `event.data` fields.

---

## Meta Conversion API (server-side)

Sends conversion events server-side to Meta (Facebook) — avoids browser tracking limitations (ad blockers, iOS restrictions).

### Setup overview (7 steps via Google Cloud Platform + server-side GTM)

1. **Create server-side GTM container** in Google Tag Manager
2. **Deploy to Google Cloud Run** (or App Engine) — gives you a server-side tagging endpoint
3. **Set up Meta Pixel** (client-side) on your website for basic event tracking
4. **Create a Conversion API token** in Meta Events Manager → Data Sources → your Pixel → Settings → Conversions API
5. **Add Meta CAPI tag** in server-side GTM container using the token
6. **Configure event forwarding** — map client-side events (PageView, Purchase, etc.) to server-side CAPI
7. **Verify in Meta Events Manager** → Test Events tab — events should appear as "Server" source

### Key benefit
Events received via CAPI are deduplicated with browser Pixel events using `event_id`. Both sources send the same `event_id` — Meta counts it once, improving attribution accuracy.

---

## Google Consent Mode v2

Required for compliance with EU cookie laws and to maintain GA4 / Google Ads data quality when users decline cookies.

### Default state (before user consent)

Set all parameters to `denied` by default in GTM:

```
ad_storage: denied
analytics_storage: denied
ad_user_data: denied
ad_personalization: denied
```

### Implementation in GTM

1. Add a **Consent Initialization trigger** tag (fires before all other tags)
2. Set default consent state to `denied` for all four parameters
3. Add a **consent banner** (CookieYes, Cookiebot, or custom) that updates consent state on user choice
4. Configure GTM to **update consent** when the banner fires:
   - Accept all → set all to `granted`
   - Reject all → leave as `denied`
   - Partial → set individual parameters per user choice

### What happens with denied consent

- GA4 still fires in **cookieless/pingless mode** — no cookies set, no cross-site tracking
- Google Ads still models conversions using behavioral modeling
- No personal data collected until user consents

---

---

## Google Tag Manager Setup

### Add GTM to Choice website

In the Choice admin panel, add the **GTM container code** to the designated field. **Do not** also add the Google Analytics tag directly through the admin panel — this causes data duplication. Add GA4 through GTM only.

### GTM variables to enable

In GTM → Variables → Built-In Variables → Configure. Keep only:
- **Click Element** (Data Layer Variable)
- **Page URL** (URL)
- **Event** (Special event)

### Create GA4 Configuration Tag

1. Tags → New → name it **"GA4 - Configuration"**
2. Tag Type: **Google Analytics: GA4 Configuration**
3. Measurement ID: paste your GA4 Measurement ID from Google Analytics
4. Enable **"Send a page view event when this configuration loads"**
5. Trigger: **All Pages**
6. Save

### Create Conversion Trigger (order_created)

Choice uses a special page `/order-created` that fires immediately after a successful payment (before the user is redirected to `/order-status`). Use this as a conversion trigger.

1. Triggers → New → name it **"order_created"**
2. Trigger Type: **Page View**
3. Fire on: **Some Page Views**
4. Condition: **Page URL → Contains → /order-created**
5. Save

### Create Conversion Tag

1. Tags → New → name it **"order_created"**
2. Tag Type: **Google Analytics: GA4 Event**
3. Configuration Tag: select **GA4 - Configuration**
4. Event Name: `order_created`
5. Trigger: select **order_created** trigger
6. Save

### Publish GTM

Changes only take effect after publishing. Tags → Submit → add a version name → Publish.

GA4 data appears after 1–2 days. Then go to GA4 Admin → Events → find `order_created` → mark as conversion.

---

## Google E-commerce Tracking

Choice pushes standard GA4 e-commerce events via the data layer. To receive them in GA4:

1. Create a **Trigger** in GTM for all e-commerce events:
   - Type: Custom Event
   - Event name: `view_item_list|select_item|share|add_to_cart|remove_from_cart|add_to_wishlist|view_cart|begin_checkout|add_shipping_info|add_payment_info|purchase|search|select_promotion|view_promotion|earn_virtual_currency|spend_virtual_currency|login|booking_request`
   - Enable **"Use regex matching"** and **"All custom events"**

2. Create a **Tag** to send data to GA4:
   - Tag Type: Google Analytics: GA4 Event
   - Configuration Tag: GA4 - Configuration
   - Enable **"Send e-commerce data"**
   - Trigger: the e-commerce all events trigger above

### Full list of Choice e-commerce events

| Event | When fired |
|-------|-----------|
| `view_item_list` | User views menu category |
| `select_item` | User clicks on a dish |
| `add_to_cart` | User adds dish to cart |
| `remove_from_cart` | User removes dish from cart |
| `view_cart` | User opens cart ("To order" button) |
| `begin_checkout` | User proceeds to checkout |
| `add_shipping_info` | User enters delivery address |
| `add_payment_info` | User reaches payment step |
| `purchase` | Order completed successfully |
| `search` | User searches in menu |
| `login` | User logs in |
| `booking_request` | User submits reservation request |
| `share` | User shares menu/dish |
| `select_promotion` / `view_promotion` | Promotional banners |
| `earn_virtual_currency` / `spend_virtual_currency` | Loyalty points |

### booking_request event data structure

```javascript
window.dataLayer.push({
  'event': 'booking_request',
  'ecommerce': {
    'bookingDetails': {
      'persons': 4,       // number of guests
      'zone': 'terrace',  // preferred zone
      'deposit': 20.00,   // deposit amount
      'duration': 90      // visit duration in minutes
    }
  }
});
```

---

## UTM Tracking for Restaurants

UTM parameters let you track which marketing campaigns drive orders.

### How it works in Choice

1. Restaurant creates a UTM-tagged link (e.g. `https://yourrestaurant.com/?utm_source=facebook&utm_medium=post&utm_campaign=new_menu`)
2. When a guest clicks and places an order, UTM parameters are stored with the order
3. In admin panel → **Customers → Orders**: a **UTM Source** column shows which source drove each order
4. Click any order for full UTM detail (source, medium, campaign, content, term)
5. In XLSX export: 5 new columns at the end of the file for each UTM parameter

### Creating UTM links

Use utmbuilder.net to generate links. Fields:
- **Website URL** *(required)* — your restaurant or menu URL
- **UTM Source** *(required)* — where the link will be placed (facebook, instagram, email, telegram)
- **UTM Medium** *(optional)* — type of placement (post, banner, newsletter)
- **UTM Campaign** *(optional)* — campaign name (summer_promo, new_menu)
- **UTM Content** *(optional)* — page or placement label
- **UTM Term** *(optional)* — any additional filtering parameter

**Example:** `https://pizza.com/?utm_source=facebook&utm_medium=post_september&utm_campaign=new_menu&utm_content=main_page`

---

## All analytics features in summary

| Feature | Where to configure |
|---------|-------------------|
| GTM container | Admin panel → add GTM container code |
| GA4 Measurement Protocol | Admin panel → Template → Analytics |
| Google E-commerce events | GTM → e-commerce trigger + GA4 Event tag |
| Conversion tracking | GTM → `/order-created` page trigger |
| UTM tracking | UTM-tagged links → visible in Orders + export |
| UTM passing to iframe | Automatic via URLSearchParams; configure GTM listeners |
| Meta Conversion API | Google Cloud + server-side GTM + Meta Events Manager |
| Google Consent Mode v2 | GTM → Consent Initialization tag |
