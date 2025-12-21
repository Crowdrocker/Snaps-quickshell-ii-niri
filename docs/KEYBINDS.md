# Default Keybinds

These are the default keybinds shipped with ii. They live in `~/.config/niri/config.kdl` after install.

Change them. Break them. Make them yours. We won't judge.

---

## Workspace switching
| Key | Action |
|-----|--------|
| `Mod+1` | focus-workspace 1 + sound-system workspace 1 |
| `Mod+2` | focus-workspace 2 + sound-system workspace 2 |
| `Mod+3` | focus-workspace 3 + sound-system workspace 3 |
| `Mod+4` | focus-workspace 4 + sound-system workspace 4 |
| `Mod+5` | focus-workspace 5 + sound-system workspace 5 |
| `Mod+6` | focus-workspace 6 + sound-system workspace 6 |
| `Mod+7` | focus-workspace 7 + sound-system workspace 7 |
| `Mod+8` | focus-workspace 8 + sound-system workspace 8 |
| `Mod+9` | focus-workspace 9 + sound-system workspace 9 |
| `Mod+0` | focus-workspace 10 + sound-system workspace 10 |
| `Mod+Shift+1` ... `Mod+Shift+0` | move-column-to-workspace 1..10 (shifted numbers move current column) |

## System / Overview / Locks
| Key | Action / Notes |
|-----|----------------|
| `Mod+Tab` (repeat=false) | toggle-overview |
| `Mod+Shift+E` | quit |
| `Mod+Escape` (allow-inhibiting=false) | toggle-keyboard-shortcuts-inhibit |
| `Alt+Tab` | ii altSwitcher next (window switcher) |
| `Alt+Shift+Tab` | ii altSwitcher previous |
| `Super+G` | ii overlay toggle |
| `Mod+Space` (repeat=false) | ii overview toggle |
| `Mod+V` | ii clipboard toggle |
| `Mod+Alt+L` (allow-when-locked=true) | ii lock activate |
| `Ctrl+Alt+T` | ii wallpaperSelector toggle |
| `Mod+Comma` | ii settings open |
| `Mod+Slash` | ii cheatsheet toggle |
| `Mod+Shift+W` | ii panelFamily cycle |

## Window management
| Key | Action |
|-----|--------|
| `Mod+Q` (repeat=false) | run close-window script (~/.config/quickshell/ii/scripts/close-window.sh) |
| `Mod+D` | maximize-column |
| `Mod+F` | fullscreen-window |
| `Mod+A` | toggle-window-floating |

### Focus navigation
| Key | Action |
|-----|--------|
| `Mod+Left` / `Mod+H` | focus-column-left |
| `Mod+Right` / `Mod+L` | focus-column-right |
| `Mod+Up` / `Mod+K` | focus-window-up |
| `Mod+Down` / `Mod+J` | focus-window-down |

### Move windows/columns
| Key | Action |
|-----|--------|
| `Mod+Shift+Left` / `Mod+Shift+H` | move-column-left |
| `Mod+Shift+Right` / `Mod+Shift+L` | move-column-right |
| `Mod+Shift+Up` / `Mod+Shift+K` | move-window-up |
| `Mod+Shift+Down` / `Mod+Shift+J` | move-window-down |

## Gaming & toggles
| Key | Action |
|-----|--------|
| `Mod+G` | sound-system gaming-toggle (hotkey-overlay-title="sound-system gaming-toggle") |
| `Mod+Shift+g` | run jarvis-manager.sh (toggle gaming mode) |
| `Mod+Alt+r` | run ~/bin/niri-validate.sh |

## Applications
| Key | Action |
|-----|--------|
| `Mod+T` or `Mod+Return` | spawn terminal (`ghostty`) |
| `Mod+B` | open Vivaldi (`vivaldi-stable`) |
| `Super+E` | open Thunar |
| `Mod+Alt+D` | open Rofi (`-show drun`) |
| `Mod+Shift+B` | open Brave (`brave`) |
| `Mod+Shift+T` | open Kate |
| `Mod+O` | open OBS (flatpak run com.obsproject.Studio) |
| `Mod+P` | open spotify-launcher |

## Webapps (custom launcher)
| Key | Action |
|-----|--------|
| `Mod+Ctrl+t` | launch Twitch webapp script |
| `Mod+Ctrl+y` | launch YouTube webapp script |
| `Mod+Ctrl+s` | launch Spotify webapp script |
| `Mod+Ctrl+d` | launch Discord webapp script |

## Gaming & launchers (cont.)
| Key | Action |
|-----|--------|
| `Mod+Shift+S` | sound-system steam-launch && steam |
| `Mod+Alt+P` | open protonup-qt |

## Screenshots
| Key | Action |
|-----|--------|
| `Mod+Print` | grim to ~/Pictures/Screenshots/<timestamp>.png && sound-system screenshot (hotkey-overlay-title="Take screenshot") |
| `Ctrl+Print` | screenshot-screen |
| `Alt+Print` | screenshot-window |

## Media controls
| Key | Action (allow-when-locked=true) |
|-----|---------------------------------|
| `XF86AudioPlay` | playerctl play-pause |
| `XF86AudioNext` | playerctl next |
| `XF86AudioPrev` | playerctl previous |
| `XF86AudioStop` | playerctl stop |

## Audio controls (adaptive / sound-system)
| Key | Action (allow-when-locked=true) |
|-----|---------------------------------|
| `XF86AudioMute` | sound-system mute |
| `XF86AudioRaiseVolume` | sound-system volume-up |
| `XF86AudioLowerVolume` | sound-system volume-down |
| `XF86AudioMicMute` | sound-system mic-mute |

---

## Customizing

Edit `~/.config/niri/config.kdl` to change keybinds. See [IPC.md](IPC.md) for all available ii targets you can bind.

Example (because you're definitely going to ask):

```kdl
binds {
    // Your custom binds
    Super+P { spawn "qs" "-c" "ii" "ipc" "call" "session" "toggle"; }
}
```

Then reload Niri so it actually notices:

```bash
niri msg action load-config-file
```

If your keybind doesn't work, you probably forgot to reload. Don't worry, we've all been there.
