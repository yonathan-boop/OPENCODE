[KNOWN_PERMISSION_AUTO_APPROVAL_POLICY]

The human explicitly authorizes automatic approval of KNOWN TRUSTED permission dialogs
required by this PC automation setup.

==================================================
CHROME REMOTE DEBUGGING
==================================================

KNOWN TRUSTED DIALOG:

Title/text contains:

"Allow remote debugging?"

AND contains buttons:

"Allow"
"Cancel"
"Turn off in settings"

ACTION:

ALWAYS invoke:

"Allow"

Do this automatically.

Do NOT:
- press Escape
- choose Cancel
- choose Turn off in settings
- close the dialog
- ignore it
- continue Playwright connection attempts while this dialog is unresolved

==================================================
REPEATED POPUPS
==================================================

If the SAME trusted dialog appears repeatedly:

Allow it EVERY TIME.

Loop:

FlaUI snapshot
? find exact "Allow remote debugging?" dialog
? invoke its "Allow" button
? wait for dialog to disappear
? snapshot again

If another identical dialog appears:
repeat.

Maximum automatic approvals per recovery cycle:
10

Do NOT assume approving one dialog means all pending dialogs are gone.

==================================================
VERY IMPORTANT
==================================================

Do NOT click arbitrary buttons named "Allow".

Only auto-approve when the button belongs to the verified Chrome native dialog:

"Allow remote debugging?"

Match:
- dialog text/title
- parent window/application = Google Chrome
- surrounding known remote-debugging text

Never auto-approve:
- website notification permissions
- camera/microphone permissions
- location permissions
- downloads
- extension permissions
- unrelated security dialogs

unless a separate explicit policy exists for them.

==================================================
AFTER EVERY APPROVAL
==================================================

After clicking Allow:

1. Verify the dialog disappeared.
2. Check for another identical dialog.
3. Clear all pending remote-debugging approval dialogs.
4. Only when none remain:
   call playwright/browser_tabs.

SUCCESS:

Playwright can see the user's normal Chrome tabs.

Then stop permission handling and continue the original task.

==================================================
FAILURE DETECTION
==================================================

If the same remote-debugging popup appears more than 3 times:

do NOT change strategy.

Continue approving it,
BUT also record:

POPUP_COUNT
TIME
PLAYWRIGHT_CONNECTION_STATE

If it reaches 10 approvals and still returns:

STOP reconnect attempts.

Report:

[REMOTE_DEBUGGING_APPROVAL_LOOP]

POPUP_COUNT:
PLAYWRIGHT_STATUS:
CHROME_STATE:
LAST_ERROR:

Do not kill Chrome.
Do not restart Chrome.
Do not press random shortcuts.
