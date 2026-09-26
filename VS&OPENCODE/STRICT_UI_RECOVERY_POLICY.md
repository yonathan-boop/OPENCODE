[STRICT_UI_RECOVERY_POLICY]

CRITICAL:
Never attempt multiple UI fallback methods at the same time.

ONE ACTION PATH ONLY.

Before every fallback:
1. Observe current desktop state.
2. Identify all open dialogs/overlays.
3. Close/cancel unrelated temporary UI created by previous attempts.
4. Confirm the desktop is in a clean known state.
5. Choose ONE recovery method.
6. Execute it.
7. Verify result.
8. Only if it fails, clean up that attempt before trying another method.

NEVER do combinations such as:
- Run dialog + Start Menu + taskbar click simultaneously
- Win+P / projection controls during application launch
- multiple keyboard shortcuts while another dialog is active
- repeated launch methods without verifying the previous one
- opening new overlays while an old modal/dialog remains active

[APP_LAUNCH]

To open Chrome:

METHOD 1:
FlaUI -> detect existing Chrome window -> focus/restore.

If FAILED:
clean state.

METHOD 2:
FlaUI -> taskbar Chrome icon -> Invoke.

If FAILED:
clean state.

METHOD 3:
Start Menu -> search Google Chrome -> Invoke.

If FAILED:
clean state.

METHOD 4:
Desktop shortcut -> Invoke/double-click.

Only if ALL GUI methods fail:
use shell/process launch.

Never execute more than ONE launch method before verification.

[KEYBOARD SAFETY]

Do not send global Windows shortcuts unless you are certain what they do.

Forbidden during ordinary application launch:
Win+P
Win+K
Win+L
Win+U
display/project shortcuts
system accessibility shortcuts

Before sending any Windows shortcut:
verify the intended shortcut and active window.

[STATE LOCK]

Maintain:

ACTIVE_WINDOW:
OPEN_MODAL:
OPEN_OVERLAY:
CURRENT_METHOD:
EXPECTED_RESULT:

If OPEN_MODAL != none:
do not start another unrelated UI action.

If CURRENT_METHOD is still unresolved:
do not start a second recovery path.

[RECOVERY]

If desktop intermittent UI or overlays block operation:

STOP actions.

Use FlaUI/windows_snapshot to inspect:
- active window
- modal dialogs
- overlays

Close ONLY temporary UI created by the agent (via Escape or Cancel buttons).

Return to a clean desktop state.

Then resume from the last confirmed state.

[ANTI-CHAOS]

Maximum:
1 GUI action at a time.
1 fallback strategy at a time.
1 verification after each meaningful state transition.

Speed is secondary to maintaining a coherent desktop state.

If two recovery methods fail:
STOP local experimentation and consult ChatGPT before doing anything else.
