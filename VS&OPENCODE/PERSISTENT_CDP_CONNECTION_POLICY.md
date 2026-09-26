[PERSISTENT_CDP_CONNECTION_POLICY]

ROOT CAUSE:
Repeated "Allow remote debugging?" prompts are most likely caused by repeated
CDP reconnect attempts to Chrome / localhost / 127.0.0.1:9222.

Chrome may require approval again for EACH NEW CDP connection.

GOAL:
Maintain ONE persistent Playwright/CDP connection for the lifetime of the Chrome session.

==================================================
RULE 1 — DO NOT RECONNECT IF HEALTHY
==================================================

Once:

playwright/browser_tabs

succeeds and the expected Chrome tabs are visible:

set:

CDP_STATE = CONNECTED

Do NOT:
- restart Playwright MCP
- reconnect to Chrome
- recreate the CDP client
- relaunch Playwright
- toggle remote debugging off/on
- repeatedly perform "connection tests"

while CDP_STATE = CONNECTED.

Reuse the existing connection.

==================================================
RULE 2 — HEALTH CHECK MUST REUSE SESSION
==================================================

A health check must NOT intentionally create a new CDP connection.

If an existing Playwright tool call succeeds:
connection is healthy.

Do not perform a separate reconnect just to verify health.

==================================================
RULE 3 — SINGLE CONNECTION ATTEMPT
==================================================

When disconnected:

allow ONLY ONE Playwright connection attempt at a time.

Never allow:
- parallel reconnect attempts
- multiple Playwright MCP subprocesses
- repeated connection polling from separate recovery routines

Maintain:

CDP_CONNECT_IN_PROGRESS = true/false

If true:
do not start another connection attempt.

==================================================
RULE 4 — CONSENT LOOP
==================================================

During ONE connection attempt:

if Chrome shows:
"Allow remote debugging?"

use FlaUI to click:
Allow

If another identical consent dialog appears:
Allow it too.

Continue until:
- consent dialogs are gone
AND
- Playwright connection succeeds

Once successful:
STOP all connection/recovery attempts immediately.

==================================================
RULE 5 — RECONNECT DEBOUNCE
==================================================

If Playwright genuinely disconnects:

do not reconnect instantly from multiple code paths.

Wait approximately 3-5 seconds.

Check whether the existing MCP process/session recovered.

Only then initiate ONE reconnect attempt.

==================================================
RULE 6 — DO NOT RESTART CHROME
==================================================

A Playwright/CDP failure is NOT automatically a Chrome failure.

Do not:
- kill Chrome
- restart Chrome
- reopen Chrome
- toggle remote debugging

unless evidence shows Chrome itself is unhealthy.

Try restoring only the Playwright/CDP layer first.

==================================================
RULE 7 — MCP PROCESS LIFETIME
==================================================

Keep the Playwright MCP server process alive for the entire Antigravity session.

Do not create a new:

npx @playwright/mcp

process for every browser task.

One Antigravity session
? one Playwright MCP process
? one persistent Chrome CDP connection

==================================================
RULE 8 — LOG CONNECTION GENERATION
==================================================

Track:

CDP_CONNECTION_ID
CDP_CONNECT_TIME
CDP_DISCONNECT_TIME
CDP_RECONNECT_COUNT
REMOTE_DEBUGGING_APPROVAL_COUNT

If APPROVAL_COUNT increases while DISCONNECT_COUNT is zero:
investigate duplicate/parallel connection attempts.

==================================================
SUCCESS STATE
==================================================

When Chrome shows remote debugging active
AND Playwright can list the normal tabs:

CDP_STATE = CONNECTED
REMOTE_DEBUGGING = ACTIVE

Leave everything alone.

Continue normal browser tasks through the existing connection.
