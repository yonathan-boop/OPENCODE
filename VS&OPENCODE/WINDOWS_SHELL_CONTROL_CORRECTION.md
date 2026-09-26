[WINDOWS_SHELL_CONTROL_CORRECTION]

CRITICAL FINDING:

The current Windows global-shortcut strategy is unreliable on this machine.

Observed failures include:
- Run dialog appearing unexpectedly
- Voice Typing appearing unexpectedly
- Project/display panel appearing previously
- unrelated Windows overlays being triggered

Therefore:

WINDOWS-MCP SHORTCUT MUST NO LONGER BE USED FOR WINDOWS-KEY COMBINATIONS.
ALSO DO NOT USE WINDOWS_BATCH KEYS FOR WINDOWS-KEY COMBINATIONS.

==================================================
PERMANENT BAN
==================================================

Do NOT use windows-mcp/Shortcut or windows_batch keys for:

Win
Win+D
Win+R
Win+H
Win+P
Win+K
Win+S
Win+X
Win+Tab
or ANY Windows-key combination.

Do not attempt to "fix" this by changing timing.

The problem is considered operationally unreliable.

For Windows shell interaction:
USE FLAUI SEMANTIC CONTROL INSTEAD.

==================================================
NEW WINDOWS APP LAUNCH METHOD
==================================================

To open Google Chrome:

STEP 1:
Use FlaUI:
windows_list_windows

If an existing Google Chrome window exists:
? windows_focus
? restore if minimized
? SUCCESS

STEP 2:
If Chrome does not exist:

Inspect the Windows taskbar using FlaUI.

Find:
Google Chrome

If a Chrome taskbar button/icon exists:
invoke it semantically.

Verify a Chrome window appears.

STEP 3:
If Chrome is not available through taskbar:

Use FlaUI to invoke the Windows Start button semantically.

Do NOT press the physical Windows key.

After Start menu opens:
refresh windows_snapshot.

Find the Search textbox.

Set/type:
Google Chrome

using FlaUI semantic typing/value control.

Wait for search result.

Find:
Google Chrome

Invoke the result semantically.

STEP 4:
Verify Chrome window with:
windows_list_windows

Do NOT start another launch method until this method is confirmed failed.
