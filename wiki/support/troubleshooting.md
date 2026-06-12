# Troubleshooting Guide

General approach for diagnosing and resolving issues, plus escalation guidelines.

---

## Troubleshooting Steps

### 1. Identify the Problem
- Gather details: error messages, screenshots, timestamps
- Ask: *What happened? When? Was anything changed before it started?*
- Define scope: one user affected, multiple users, or the entire system?

### 2. Reproduce the Issue
- Try to replicate step by step
- Is the error consistent or intermittent?
- Note conditions: device, browser, network, user role

### 3. Check the Basics
- Verify connectivity, login credentials, system access
- Check for recent changes (software update, configuration, integration change)
- Clear cache, restart the app, or try another browser/device

### 4. Isolate the Cause
- Is the issue user-side (device, settings) or system-side (server, backend, integration)?
- Use Global Logs (admin panel → Settings → Global Logs) to trace what changed and when
- Test related components individually

### 5. Implement a Fix
- Start with the simplest solution: restart service, re-sync data, correct configuration
- If fix requires developer access, escalate with full context

### 6. Verify the Solution
- Re-test the full workflow
- Ask the user to confirm on their side
- Monitor briefly for stability

### 7. Document
- Record root cause, actions taken, solution

---

## Escalation Guidelines

Escalate to the development team **only when**:
- You've checked all available documentation and support resources
- You've checked relevant Slack channels for similar cases
- All suggested solutions were tested and didn't help
- The issue requires internal system access only developers have

### What to include when escalating

| Issue type | What to provide |
|-----------|----------------|
| **Website bug (hard to reproduce)** | Video recording from the client |
| **Marketplace issue** | Link to the marketplace listing |
| **B2B notification issue** | Logs from the relevant time period + example order ID |
| **Order not arriving from marketplace** | Marketplace order ID (needed to trace it) |
| **B2B loading/crash issue** (not reproducible on your device) | Full device specs from the client |
| **Dishes showing as "sold out" when enabled** | Plugin logs + plugin version |

### How to read logs from Choice Business

Logs guide: available in Notion — "How to read logs from Choice Business" page.

When attaching logs: make sure the log time range covers when the problematic order or event occurred.
