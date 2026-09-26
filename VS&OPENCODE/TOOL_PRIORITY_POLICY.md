# Tool Priority Policy (Three-Tier Architecture)

For every computer task, choose tools in this order:

## 1. PLAYWRIGHT MCP (Primary for Web)
Use for:
- websites
- Chrome tabs
- forms
- links
- web buttons
- browser DOM
- browser-based apps

## 2. FLAUI MCP (Primary for Native Windows)
Use for:
- File Explorer
- Settings
- Notepad
- Calculator
- native Windows dialogs
- Win32/WPF/UWP/WinForms apps
- semantic Windows controls

## 3. WINDOWS-MCP (Fallback)
Use ONLY when:
- Playwright cannot access the content
- FlaUI cannot expose the control
- canvas/pixel rendering is involved
- games/VNC/custom-rendered UI
- visual recognition is genuinely required

## GLOBAL RULE:
Never use physical mouse coordinates if Playwright or FlaUI can perform the same action semantically.
Prefer:
- DOM/ref
- UIA/ref
- InvokePattern
- ValuePattern
- SelectionPattern
- TogglePattern
- WindowPattern

Over:
- Screenshot
- Move
- coordinate Click

**Do not move the user's physical mouse unless there is no semantic/programmatic alternative.**
