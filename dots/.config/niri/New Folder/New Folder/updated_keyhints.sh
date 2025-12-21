#!/usr/bin/env bash
# === WEHTTAMSNAPS KEYBINDINGS CHEAT SHEET ===
# Author: Matthew (WehttamSnaps)
# Updated for Niri + Noctalia Shell + JARVIS Integration

set -euo pipefail

# Kill existing instances
pkill -9 yad 2>/dev/null || true

# Launch yad with updated keybindings
GDK_BACKEND=wayland yad \
    --center \
    --title="WehttamSnaps Niri Keybindings" \
    --no-buttons \
    --list \
    --column=Key: \
    --column=Description: \
    --column=Notes: \
    --timeout-indicator=bottom \
    --width=1100 \
    --height=750 \
    --search-column=2 \
"" "â•­â"€â"€â"€â"€â"€â"€â"€â"€â"€â"€â"€â"€â"€â"€â"€â"€â"€â"€â"€â"€â"€â"€â"€â"€â"€â"€â"€â"€â"€â"€â"€â"€â"€â"€â"€â"€â"€â"€â"€â"€â"€â"€â"€â"€â"€â"€â"€â"€â"€â"€â"€â"€â"€â"€â"€â"€â"€â"€â"€â"€â"€â"€â"€â"€â•®" "" \
"" "â"‚  WEHTTAMSNAPS NIRI CONFIGURATION - KEYBINDINGS REFERENCE  â"‚" "" \
"" "â•°â"€â"€â"€â"€â"€â"€â"€â"€â"€â"€â"€â"€â"€â"€â"€â"€â"€â"€â"€â"€â"€â"€â"€â"€â"€â"€â"€â"€â"€â"€â"€â"€â"€â"€â"€â"€â"€â"€â"€â"€â"€â"€â"€â"€â"€â"€â"€â"€â"€â"€â"€â"€â"€â"€â"€â"€â"€â"€â"€â"€â"€â"€â"€â"€â•¯" "" \
"Mod" "= SUPER KEY (Windows Key)" "" \
"" "" "" \
"â•­â"€â"€â"€â"€ NOCTALIA SHELL â"€â"€â"€â"€â•®" "" "" \
"Mod + Space" "Application Launcher" "Noctalia app launcher" \
"Mod + S" "Control Center" "Quick settings panel" \
"Mod + Comma" "Settings" "Noctalia settings" \
"Mod + V" "Clipboard History" "Clipboard manager" \
"Mod + C" "Calculator" "Quick calculator" \
"Mod + L" "Lock Screen" "Lock with Noctalia" \
"" "" "" \
"â•­â"€â"€â"€â"€ CORE APPLICATIONS â"€â"€â"€â"€â•®" "" "" \
"Mod + Enter" "Terminal" "Ghostty terminal" \
"Mod + B" "Browser" "Firefox" \
"Mod + Shift + B" "Alt Browser" "Brave browser" \
"Mod + E" "File Manager" "Thunar" \
"Mod + D" "Rofi Launcher" "Rofi drun menu" \
"Mod + H" "KeyHints" "This cheat sheet!" \
"Mod + Shift + T" "Text Editor" "Kate editor" \
"Mod + O" "OBS Studio" "Screen recording" \
"Mod + P" "Spotify" "Music player" \
"" "" "" \
"â•­â"€â"€â"€â"€ WEBAPPS (Mod + Ctrl) â"€â"€â"€â"€â•®" "" "" \
"Mod + Ctrl + Y" "YouTube" "YouTube webapp" \
"Mod + Ctrl + T" "Twitch" "Twitch webapp" \
"Mod + Ctrl + S" "Spotify" "Spotify webapp" \
"Mod + Ctrl + D" "Discord" "Discord webapp" \
"" "" "" \
"â•­â"€â"€â"€â"€ GAMING & PERFORMANCE â"€â"€â"€â"€â•®" "" "" \
"Mod + G" "Gaming Mode Toggle" "iDroid sounds, max performance" \
"Mod + Shift + S" "Steam" "Launch Steam with sound" \
"Mod + Alt + P" "ProtonUp-Qt" "Manage Proton versions" \
"" "" "" \
"â•­â"€â"€â"€â"€ WORKSPACES â"€â"€â"€â"€â•®" "" "" \
"Mod + 1" "Workspace 1" "ðŸŒ Browser" \
"Mod + 2" "Workspace 2" "ðŸ'» Terminal/Dev" \
"Mod + 3" "Workspace 3" "ðŸŽ® Gaming" \
"Mod + 4" "Workspace 4" "ðŸ"º Streaming/OBS" \
"Mod + 5" "Workspace 5" "ðŸ"¸ Photography" \
"Mod + 6" "Workspace 6" "ðŸŽ¬ Media/Video" \
"Mod + 7" "Workspace 7" "ðŸ'¬ Communication" \
"Mod + 8" "Workspace 8" "ðŸŽµ Music/Audio" \
"Mod + 9" "Workspace 9" "ðŸ"‚ Files" \
"Mod + 0" "Workspace 10" "âš™ï¸ Misc" \
"Mod + Shift + 1-0" "Move Window" "Move to workspace" \
"" "" "" \
"â•­â"€â"€â"€â"€ WINDOW MANAGEMENT â"€â"€â"€â"€â•®" "" "" \
"Mod + Q" "Close Window" "With sound effect" \
"Mod + F" "Maximize Column" "Fill workspace" \
"Mod + Shift + F" "Fullscreen" "True fullscreen" \
"Mod + Ctrl + V" "Toggle Floating" "Float/tile window" \
"Mod + Shift + V" "Switch Focus" "Float ↔ Tile" \
"Mod + W" "Toggle Tabbed" "Tab window display" \
"Mod + R" "Preset Width" "Cycle window width" \
"Mod + Shift + R" "Preset Height" "Cycle window height" \
"Mod + Alt + C" "Center Column" "Center in workspace" \
"Mod + Minus" "Decrease Width" "-10%" \
"Mod + Equal" "Increase Width" "+10%" \
"Mod + Shift + Minus" "Decrease Height" "-10%" \
"Mod + Shift + Equal" "Increase Height" "+10%" \
"" "" "" \
"â•­â"€â"€â"€â"€ FOCUS MOVEMENT â"€â"€â"€â"€â•®" "" "" \
"Mod + Left/H" "Focus Left" "Move focus left" \
"Mod + Right/;" "Focus Right" "Move focus right" \
"Mod + Up/K" "Focus Up" "Move focus up" \
"Mod + Down/J" "Focus Down" "Move focus down" \
"" "" "" \
"â•­â"€â"€â"€â"€ WINDOW MOVEMENT â"€â"€â"€â"€â•®" "" "" \
"Mod + Ctrl + H" "Move Left" "Move window left" \
"Mod + Ctrl + ;" "Move Right" "Move window right" \
"Mod + Ctrl + K" "Move Up" "Move window up" \
"Mod + Ctrl + J" "Move Down" "Move window down" \
"Mod + BracketLeft" "Consume Left" "Merge window left" \
"Mod + BracketRight" "Expel Right" "Split window right" \
"" "" "" \
"â•­â"€â"€â"€â"€ SCREENSHOTS â"€â"€â"€â"€â•®" "" "" \
"Mod + Print" "Screenshot" "Full screen + sound" \
"Ctrl + Print" "Screen Capture" "Niri screenshot screen" \
"Alt + Print" "Window Capture" "Niri screenshot window" \
"Mod + Shift + E" "Photo Export" "Export with sound" \
"" "" "" \
"â•­â"€â"€â"€â"€ AUDIO CONTROLS â"€â"€â"€â"€â•®" "" "" \
"XF86AudioMute" "Mute/Unmute" "With adaptive sound" \
"XF86AudioRaiseVolume" "Volume Up" "Sound feedback" \
"XF86AudioLowerVolume" "Volume Down" "Sound feedback" \
"XF86AudioMicMute" "Mic Mute" "Toggle microphone" \
"" "" "" \
"â•­â"€â"€â"€â"€ MEDIA CONTROLS â"€â"€â"€â"€â•®" "" "" \
"XF86AudioPlay" "Play/Pause" "Media playback" \
"XF86AudioNext" "Next Track" "Skip forward" \
"XF86AudioPrev" "Previous Track" "Skip backward" \
"XF86AudioStop" "Stop" "Stop playback" \
"" "" "" \
"â•­â"€â"€â"€â"€ BRIGHTNESS â"€â"€â"€â"€â•®" "" "" \
"XF86MonBrightnessUp" "Brightness +" "Increase brightness" \
"XF86MonBrightnessDown" "Brightness -" "Decrease brightness" \
"" "" "" \
"â•­â"€â"€â"€â"€ WALLPAPER & THEME â"€â"€â"€â"€â•®" "" "" \
"Mod + Shift + W" "Wallpaper Toggle" "Noctalia wallpaper" \
"" "" "" \
"â•­â"€â"€â"€â"€ SYSTEM â"€â"€â"€â"€â•®" "" "" \
"Mod + Shift + P" "Power Off Monitors" "Turn off displays" \
"Mod + Shift + /" "Hotkey Overlay" "Niri hotkey help" \
"Mod + Alt + L" "Lock Screen" "Swaylock" \
"Ctrl + Alt + Delete" "Quit Niri" "Exit compositor" \
"" "" "" \
"â•­â"€â"€â"€â"€ J.A.R.V.I.S. INTEGRATION â"€â"€â"€â"€â•®" "" "" \
"System Startup" "Greeting" "J.A.R.V.I.S. online" \
"Workspace Switch" "Confirmation" "With sound effect" \
"Gaming Mode On" "iDroid Mode" "Performance sounds" \
"Gaming Mode Off" "J.A.R.V.I.S. Mode" "Normal operation" \
"Window Close" "Closure Sound" "Feedback on close" \
"Screenshot" "Capture Sound" "Photo taken effect" \
"Steam Launch" "Launch Sound" "iDroid activation" \
"" "" "" \
"â•­â"€â"€â"€â"€ PHOTOGRAPHY WORKFLOW â"€â"€â"€â"€â•®" "" "" \
"" "1. Import → DigiKam" "Photo management" \
"" "2. Process → Darktable" "RAW editing" \
"" "3. Edit → GIMP" "Advanced editing" \
"" "4. Touch-up → Krita" "Digital painting" \
"" "5. Export → Ready!" "For social media" \
"" "" "" \
"â•­â"€â"€â"€â"€ GAMING OPTIMIZATIONS â"€â"€â"€â"€â•®" "" "" \
"" "Gaming Mode" "Disables animations" \
"" "Pre-configured Games" "Division 2, Cyberpunk, etc." \
"" "RX 580 Optimized" "Mesa tweaks applied" \
"" "GameMode Active" "CPU performance mode" \
"" "" "" \
"â•­â"€â"€â"€â"€ QUICK TIPS â"€â"€â"€â"€â•®" "" "" \
"" "Mod + H anytime" "Show this cheat sheet" \
"" "Gaming mode" "Max FPS, no animations" \
"" "Webapps" "Separate profiles/cookies" \
"" "J.A.R.V.I.S." "Contextual sound system" \
"" "iDroid" "Gaming/combat sounds" \
"" "" "" \
"â•­â"€â"€â"€â"€ RESOURCES â"€â"€â"€â"€â•®" "" "" \
"" "Documentation" "~/.config/wehttamsnaps/docs/" \
"" "GitHub" "github.com/Crowdrocker" \
"" "Twitch" "twitch.tv/WehttamSnaps" \
"" "YouTube" "@WehttamSnaps" \
"" "" "" \
"" "â•°â"€â"€â"€ Made with â¤ï¸ by WehttamSnaps â"€â"€â"€â•¯" "Photography â€¢ Gaming â€¢ Content"