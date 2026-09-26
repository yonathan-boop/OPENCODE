[CHROME_STARTUP_NORMALIZATION_POLICY]

CRITICAL UPDATE:

Chrome is now launching correctly.

The recurring problem is NOT Chrome startup anymore.
The problem is recurring startup dialogs/overlays.

Treat these as NORMAL Chrome startup state and resolve them automatically.

==================================================
RULE 1 — NEVER FORCE-KILL HEALTHY CHROME
==================================================

Do NOT use:

Stop-Process -Name chrome -Force

during normal recovery.

Do NOT kill all Chrome processes just because Playwright/CDP is disconnected.

A forced Chrome termination causes abnormal-shutdown state and may trigger:

"Restore pages?"

on the next launch.

Preferred shutdown if truly necessary:

1. close Chrome semantically through FlaUI
2. wait for Chrome processes to exit normally
3. only force-kill if Chrome is genuinely frozen and normal close fails

==================================================
CHROME STARTUP GATE
==================================================

Every time Chrome is opened or restored:

BEFORE attempting Playwright/CDP:

1. inspect Chrome + desktop using FlaUI
2. resolve all KNOWN startup dialogs
3. verify Chrome is in a clean usable state
4. only then test Playwright

Use FlaUI semantic controls.
Do NOT use coordinate mouse unless semantic controls fail.

==================================================
KNOWN DIALOG A
==================================================

TITLE/TEXT:

"Allow remote debugging?"

ACTION:

Invoke:

"Allow"

AUTOMATICALLY.

The human has already authorized remote debugging for this private PC workflow.

Do NOT ask again.

Do NOT click:

Cancel
Turn off in settings

After Allow:
verify the dialog disappears.

==================================================
KNOWN DIALOG B
==================================================

TEXT:

"Restore pages?"
"Chrome didn't shut down correctly."

DEFAULT ACTION:

Dismiss/close this popup.

Do NOT restore old pages automatically unless restoring the previous browsing session
is necessary for the current user task.

This popup should become uncommon once Chrome is no longer force-killed.

==================================================
KNOWN DIALOG C
==================================================

BrowserLock extension popup:

"Activate BrowserLock"
"Your browser is currently unprotected..."

For this automation setup:

Invoke:

"Don't remind me again"

unless the human explicitly asks to configure BrowserLock.

Do NOT activate/configure unrelated browser-security extensions while executing another task.

==================================================
GENERIC STARTUP OVERLAY RULE
==================================================

After Chrome launches:

perform ONE FlaUI snapshot.

Classify visible overlays.

Resolve only:

- known Chrome startup dialogs
- known extension notifications that block workflow
- known CDP permission dialogs

Do NOT start browsing while blocking modal dialogs remain open.

Do NOT keep clicking random visible buttons.

==================================================
ORDER OF OPERATIONS
==================================================

Every Chrome startup must follow:

OPEN CHROME
?
FLAUI SNAPSHOT
?
HANDLE "ALLOW REMOTE DEBUGGING"
?
HANDLE "RESTORE PAGES"
?
HANDLE KNOWN EXTENSION POPUPS
?
VERIFY CLEAN CHROME WINDOW
?
PLAYWRIGHT browser_tabs
?
CONTINUE TASK

==================================================
PLAYWRIGHT RULE
==================================================

Playwright is NOT responsible for fixing Chrome-level native startup dialogs.

Use:

FlaUI
? clean native Chrome UI

then:

Playwright
? control web content

==================================================
SELF-HEALING
==================================================

If Playwright is unavailable:

DO NOT restart Chrome immediately.

First inspect whether:

- Remote Debugging consent is waiting
- a Chrome modal is blocking it
- CDP was disconnected
- remote debugging toggle is off

Repair those states with FlaUI.

Only restart Chrome when there is evidence the browser itself needs restarting.

==================================================
CURRENT SCREEN RECOVERY
==================================================

For the CURRENT Chrome state:

1. Use FlaUI snapshot.
2. Invoke "Allow" on:
   "Allow remote debugging?"

3. Dismiss:
   "Restore pages?"

4. Invoke:
   "Don't remind me again"
   on the BrowserLock popup.

5. Verify all three overlays are gone.

6. Do NOT close Chrome.

7. Call:
   playwright/browser_tabs

8. If tabs are visible:
   continue BRIDGE-TEST-001.

9. Do NOT restart or kill Chrome again.
