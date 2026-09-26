[CHROME_CDP_AUTO_BOOTSTRAP]

GOAL:
Automatically establish Playwright CDP access to the user's existing Chrome
without requiring the human to manually click the Remote Debugging permission.

The user explicitly authorizes this behavior on this private PC.

==================================================
WHEN TO RUN
==================================================

Before the FIRST browser task of each Chrome/Antigravity session:

1. Test Playwright connection using browser_tabs.
2. If Playwright already sees the user's Chrome tabs:
   STOP bootstrap and continue normally.

3. If Playwright is disconnected / permission-blocked / cannot list pages:
   run CHROME_CDP_AUTO_BOOTSTRAP.

Do not run this workflow repeatedly while Playwright is healthy.

==================================================
TOOL PRIORITY
==================================================

Use:

PRIMARY:
FlaUI-MCP

FALLBACK:
windows-mcp

Playwright cannot be relied upon until CDP permission has been approved.

Prefer FlaUI semantic controls so the physical mouse does NOT move.

==================================================
STEP 1 — FIND CHROME
==================================================

Use FlaUI:

windows_list_windows

Find the user's existing Google Chrome window.

Attach/focus it using:
windows_attach / windows_focus

Do NOT launch a second Chrome profile unless the existing browser is genuinely absent.

==================================================
STEP 2 — CHECK FOR EXISTING CONSENT DIALOG
==================================================

Immediately call:

windows_snapshot

Search semantically for a dialog/window containing:

"Allow remote debugging?"

and buttons:

"Allow"
"Cancel"
"Turn off in settings"

If the dialog exists:

CLICK ONLY:
"Allow"

Prefer semantic InvokePattern/ref.

DO NOT click:
"Cancel"
"Turn off in settings"

Do not use coordinates if FlaUI exposes the Allow button.

After clicking Allow:
wait briefly using windows_wait_for,
then refresh windows_snapshot.

==================================================
STEP 3 — HANDLE MULTIPLE CONSENT DIALOGS
==================================================

Chrome may occasionally create multiple Remote Debugging approval dialogs.

After approving one dialog:

1. refresh windows_snapshot
2. if another dialog titled:
   "Allow remote debugging?"
   remains visible,
   click its "Allow" button too.

Maximum:
5 consent dialogs per bootstrap attempt.

Never click unrelated "Allow" buttons from websites/apps.

The button must belong to the Chrome Remote Debugging consent dialog.

==================================================
STEP 4 — IF REMOTE DEBUGGING IS DISABLED
==================================================

If there is NO consent dialog and Playwright is still unavailable:

Navigate the existing Chrome window to:

chrome://inspect/#remote-debugging

Preferred method:

1. Find Chrome Address Bar through FlaUI.
2. Set/focus it semantically if available.

Fallback:
windows_keys:
CTRL+L

Type:
chrome://inspect/#remote-debugging

Press Enter.

Wait until the page is loaded.

==================================================
STEP 5 — ENABLE REMOTE DEBUGGING
==================================================

Use FlaUI windows_snapshot.

Find the control corresponding to:

"Allow remote debugging for this browser instance"

Determine its state.

If OFF:
activate/toggle it semantically.

Do not blindly click coordinates.

If FlaUI cannot expose the control:
use windows-mcp Snapshot/Screenshot only as fallback.

After enabling it:
expect Chrome to show:

"Allow remote debugging?"

==================================================
STEP 6 — APPROVE AUTOMATICALLY
==================================================

Use FlaUI windows_snapshot again.

Find:

Dialog:
"Allow remote debugging?"

Button:
"Allow"

Invoke the Allow button semantically.

Physical Windows mouse should remain stationary.

If several dialogs appear:
handle them according to STEP 3.

==================================================
STEP 7 — VERIFY CDP
==================================================

Now call:

playwright/browser_tabs

Success condition:

- Playwright can list the user's existing Chrome tabs.
- More than only an authorization/internal tab is visible.
- Existing authenticated tabs are available.

If successful:

CHROME_CDP_STATUS = READY

Continue the user's original browser task automatically.

Do NOT ask the user for confirmation.

==================================================
FAILOVER
==================================================

If FlaUI cannot see the Remote Debugging dialog:

1. Use windows-mcp Snapshot.
2. Locate the dialog.
3. Identify the exact "Allow" button.
4. Click it once.

Coordinate clicking is fallback only.

Do NOT use keyboard Enter as approval,
because focus may currently be on Cancel.

==================================================
ANTI-LOOP
==================================================

Do NOT repeatedly:

connect
? timeout
? restart Playwright
? reconnect
? trigger another consent dialog

Keep the Playwright MCP/CDP connection alive whenever possible.

Do NOT restart Playwright or Antigravity merely to refresh a normal browser task.

If permission prompts keep returning repeatedly:
record:
- number of prompts
- connection attempts
- Playwright errors
- Chrome state

and send a diagnostic report to ChatGPT.

==================================================
PERMANENT OPERATING RULE
==================================================

For browser tasks:

PLAYWRIGHT HEALTHY
? use Playwright directly.

PLAYWRIGHT NOT CONNECTED
? automatically repair CDP using FlaUI.

REMOTE DEBUGGING OFF
? enable it.

REMOTE DEBUGGING CONSENT APPEARS
? FlaUI clicks Allow.

The human user should NOT need to manually click this permission during normal operation.

==================================================
REPORT ONLY IF FAILURE
==================================================

If successful:
continue working silently.

If bootstrap fails, send:

[CHROME_CDP_BOOTSTRAP_FAILURE]

CHROME_FOUND:
REMOTE_DEBUGGING_ENABLED:
CONSENT_DIALOG_FOUND:
ALLOW_BUTTON_FOUND:
ALLOW_CLICKED:
PLAYWRIGHT_CONNECTED:
NUMBER_OF_CONSENT_DIALOGS:
ERROR:
