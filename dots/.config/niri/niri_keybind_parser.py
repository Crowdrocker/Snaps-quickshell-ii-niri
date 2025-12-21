#!/usr/bin/env python3
"""
Niri Keybind Cheatsheet Generator
Parses KDL keybind configuration and generates a formatted cheatsheet
"""

import re
import sys
from pathlib import Path
from collections import defaultdict

def parse_keybind_line(line):
    """Extract keybind and action from a line"""
    # Match patterns like: Mod+Q repeat=false { spawn "bash" ... }
    # or: Mod+1 { spawn "sh" "-c" "niri msg action focus-workspace 1 && sound-system workspace 1"; }
    
    # First, try to extract hotkey-overlay-title if present
    title_match = re.search(r'hotkey-overlay-title="([^"]+)"', line)
    overlay_title = title_match.group(1) if title_match else None
    
    # Extract the keybind (before the first {)
    keybind_match = re.match(r'^\s*([^\s{]+(?:\s+[^\s{]+)*?)\s*(?:repeat=[^\s{]+\s*)?(?:allow-when-locked=[^\s{]+\s*)?(?:allow-inhibiting=[^\s{]+\s*)?(?:hotkey-overlay-title=[^\s{]+\s*)?\{', line)
    if not keybind_match:
        return None
    
    keybind = keybind_match.group(1).strip()
    
    # Extract the action (inside the braces)
    action_match = re.search(r'\{\s*([^}]+)\s*\}', line)
    if not action_match:
        return None
    
    action = action_match.group(1).strip()
    
    # Clean up the action for better readability
    action = clean_action(action, overlay_title)
    
    return {
        'keybind': keybind,
        'action': action,
        'raw_line': line.strip()
    }

def clean_action(action, overlay_title=None):
    """Make action more readable"""
    # If there's an overlay title, use that
    if overlay_title:
        return overlay_title
    
    # Remove quotes and simplify common patterns
    action = action.replace('"', '')
    
    # Simplify spawn commands
    if action.startswith('spawn'):
        # Extract the main command
        parts = action.split()
        if len(parts) >= 2:
            cmd = parts[1]
            
            # Handle special cases
            if 'workspace' in action:
                workspace_match = re.search(r'focus-workspace (\d+)', action)
                if workspace_match:
                    return f"Switch to workspace {workspace_match.group(1)}"
            
            if 'move-column-to-workspace' in action:
                return action.replace('spawn', '').strip()
            
            if cmd == 'sh' or cmd == 'bash':
                # Try to extract the actual command being run
                script_match = re.search(r'(?:sh|bash)\s+-c\s+(.+)', action)
                if script_match:
                    script = script_match.group(1)
                    # Extract main program name
                    if 'sound-system' in script:
                        if 'gaming-toggle' in script:
                            return "Toggle gaming mode"
                        elif 'workspace' in script:
                            return "Switch workspace (with sound)"
                        elif 'screenshot' in script:
                            return "Screenshot (with sound)"
                        elif 'volume' in script:
                            return "Volume control (with sound)"
                        elif 'mute' in script:
                            return "Mute/unmute (with sound)"
                        elif 'steam-launch' in script:
                            return "Launch Steam"
                    
                    if 'webapp-launcher' in script:
                        app_match = re.search(r'webapp-launcher\.sh\s+(\w+)', script)
                        if app_match:
                            return f"Open {app_match.group(1).title()} webapp"
                    
                    if 'jarvis-manager' in script:
                        return "Toggle Jarvis (gaming mode)"
                    
                    if 'close-window' in script:
                        return "Close window"
                    
                    if 'grim' in script:
                        return "Take screenshot"
            
            # Handle qs/ii commands
            if cmd == 'qs':
                if 'altSwitcher' in action:
                    if 'next' in action:
                        return "Switch to next window"
                    elif 'previous' in action:
                        return "Switch to previous window"
                elif 'overlay' in action:
                    return "Toggle ii overlay"
                elif 'overview' in action:
                    return "Toggle ii overview"
                elif 'clipboard' in action:
                    return "Toggle ii clipboard"
                elif 'lock' in action:
                    return "Lock screen"
                elif 'region' in action:
                    if 'ocr' in action:
                        return "OCR region"
                    elif 'search' in action:
                        return "Search region"
                    elif 'screenshot' in action:
                        return "Screenshot region"
                elif 'wallpaperSelector' in action:
                    return "Toggle wallpaper selector"
                elif 'settings' in action:
                    return "Open ii settings"
                elif 'cheatsheet' in action:
                    return "Toggle cheatsheet"
                elif 'panelFamily' in action:
                    return "Cycle panel style"
            
            # Direct application launches
            return f"Launch {cmd}"
    
    # Handle direct actions (not spawn)
    action_map = {
        'toggle-overview': 'Toggle overview',
        'quit': 'Quit Niri',
        'toggle-keyboard-shortcuts-inhibit': 'Toggle keyboard shortcuts inhibit',
        'maximize-column': 'Maximize column',
        'fullscreen-window': 'Fullscreen window',
        'toggle-window-floating': 'Toggle floating window',
        'focus-column-left': 'Focus left column',
        'focus-column-right': 'Focus right column',
        'focus-window-up': 'Focus window above',
        'focus-window-down': 'Focus window below',
        'move-column-left': 'Move column left',
        'move-column-right': 'Move column right',
        'move-window-up': 'Move window up',
        'move-window-down': 'Move window down',
        'screenshot-screen': 'Screenshot screen',
        'screenshot-window': 'Screenshot window',
    }
    
    for key, value in action_map.items():
        if key in action:
            return value
    
    # Handle move-column-to-workspace
    if 'move-column-to-workspace' in action:
        workspace_match = re.search(r'move-column-to-workspace (\d+)', action)
        if workspace_match:
            return f"Move to workspace {workspace_match.group(1)}"
    
    return action

def categorize_keybind(keybind_data):
    """Categorize keybind based on its action"""
    action = keybind_data['action'].lower()
    keybind = keybind_data['keybind']
    
    if 'workspace' in action:
        return 'Workspaces'
    elif any(x in action for x in ['focus', 'move column', 'move window']):
        return 'Window Management'
    elif any(x in action for x in ['launch', 'open', 'webapp']):
        return 'Applications'
    elif any(x in action for x in ['volume', 'mute', 'play', 'next', 'previous', 'stop']):
        return 'Media & Audio'
    elif any(x in action for x in ['screenshot', 'ocr', 'region']):
        return 'Screenshots & Capture'
    elif any(x in action for x in ['gaming', 'steam', 'obs']):
        return 'Gaming & Streaming'
    elif any(x in action for x in ['overview', 'clipboard', 'overlay', 'lock', 'settings', 'cheatsheet']):
        return 'System & UI'
    elif 'quit' in action or 'inhibit' in action:
        return 'System Control'
    else:
        return 'Other'

def format_keybind(keybind):
    """Format keybind for display"""
    # Replace common modifiers with symbols or prettier names
    replacements = {
        'Mod+': '⊞ ',
        'Super+': '❖ ',
        'Alt+': '⎇ ',
        'Ctrl+': '⌃ ',
        'Shift+': '⇧ ',
    }
    
    result = keybind
    for old, new in replacements.items():
        result = result.replace(old, new)
    
    return result

def generate_markdown(keybinds_by_category, output_file):
    """Generate markdown cheatsheet"""
    with open(output_file, 'w') as f:
        f.write("# Niri Keybind Cheatsheet\n\n")
        f.write("*Auto-generated from configuration file*\n\n")
        f.write("---\n\n")
        
        # Sort categories
        category_order = [
            'Workspaces',
            'Window Management',
            'Applications',
            'Gaming & Streaming',
            'Media & Audio',
            'Screenshots & Capture',
            'System & UI',
            'System Control',
            'Other'
        ]
        
        for category in category_order:
            if category not in keybinds_by_category:
                continue
            
            f.write(f"## {category}\n\n")
            f.write("| Keybind | Action |\n")
            f.write("|---------|--------|\n")
            
            # Sort keybinds within category
            for kb in sorted(keybinds_by_category[category], key=lambda x: x['keybind']):
                keybind_formatted = format_keybind(kb['keybind'])
                f.write(f"| `{keybind_formatted}` | {kb['action']} |\n")
            
            f.write("\n")
        
        f.write("---\n\n")
        f.write("*Legend: ⊞ = Super/Mod | ❖ = Super | ⎇ = Alt | ⌃ = Ctrl | ⇧ = Shift*\n")

def generate_html(keybinds_by_category, output_file):
    """Generate HTML cheatsheet"""
    with open(output_file, 'w') as f:
        f.write("""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Niri Keybind Cheatsheet</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            padding: 20px;
            color: #333;
        }
        .container {
            max-width: 1200px;
            margin: 0 auto;
            background: white;
            border-radius: 12px;
            box-shadow: 0 20px 60px rgba(0,0,0,0.3);
            overflow: hidden;
        }
        header {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 30px;
            text-align: center;
        }
        header h1 { font-size: 2.5em; margin-bottom: 10px; }
        header p { opacity: 0.9; }
        .content { padding: 30px; }
        .category {
            margin-bottom: 40px;
            border-left: 4px solid #667eea;
            padding-left: 20px;
        }
        .category h2 {
            color: #667eea;
            margin-bottom: 15px;
            font-size: 1.8em;
        }
        .keybind-grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
            gap: 15px;
        }
        .keybind-item {
            background: #f8f9fa;
            padding: 15px;
            border-radius: 8px;
            border: 1px solid #e9ecef;
            transition: all 0.2s;
        }
        .keybind-item:hover {
            transform: translateY(-2px);
            box-shadow: 0 4px 12px rgba(0,0,0,0.1);
            border-color: #667eea;
        }
        .keybind {
            font-family: 'Courier New', monospace;
            background: #667eea;
            color: white;
            padding: 6px 12px;
            border-radius: 6px;
            display: inline-block;
            margin-bottom: 8px;
            font-weight: bold;
            font-size: 0.9em;
        }
        .action {
            color: #555;
            font-size: 0.95em;
        }
        footer {
            text-align: center;
            padding: 20px;
            background: #f8f9fa;
            color: #666;
            font-size: 0.9em;
        }
        .legend {
            background: #fff3cd;
            border: 1px solid #ffc107;
            padding: 15px;
            border-radius: 8px;
            margin-bottom: 30px;
        }
        .legend strong { color: #856404; }
    </style>
</head>
<body>
    <div class="container">
        <header>
            <h1>🎮 Niri Keybind Cheatsheet</h1>
            <p>Auto-generated from configuration file</p>
        </header>
        <div class="content">
            <div class="legend">
                <strong>Legend:</strong> ⊞ = Super/Mod | ❖ = Super | ⎇ = Alt | ⌃ = Ctrl | ⇧ = Shift
            </div>
""")
        
        category_order = [
            'Workspaces',
            'Window Management',
            'Applications',
            'Gaming & Streaming',
            'Media & Audio',
            'Screenshots & Capture',
            'System & UI',
            'System Control',
            'Other'
        ]
        
        for category in category_order:
            if category not in keybinds_by_category:
                continue
            
            f.write(f'            <div class="category">\n')
            f.write(f'                <h2>{category}</h2>\n')
            f.write(f'                <div class="keybind-grid">\n')
            
            for kb in sorted(keybinds_by_category[category], key=lambda x: x['keybind']):
                keybind_formatted = format_keybind(kb['keybind'])
                f.write(f'                    <div class="keybind-item">\n')
                f.write(f'                        <div class="keybind">{keybind_formatted}</div>\n')
                f.write(f'                        <div class="action">{kb["action"]}</div>\n')
                f.write(f'                    </div>\n')
            
            f.write(f'                </div>\n')
            f.write(f'            </div>\n')
        
        f.write("""        </div>
        <footer>
            Generated for WehttamSnaps Niri Configuration
        </footer>
    </div>
</body>
</html>
""")

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 niri_keybind_parser.py <config_file> [output_format]")
        print("Output formats: markdown (default), html, both")
        sys.exit(1)
    
    config_file = Path(sys.argv[1])
    output_format = sys.argv[2] if len(sys.argv) > 2 else "markdown"
    
    if not config_file.exists():
        print(f"Error: Config file '{config_file}' not found!")
        sys.exit(1)
    
    print(f"📖 Parsing {config_file}...")
    
    keybinds_by_category = defaultdict(list)
    
    with open(config_file, 'r') as f:
        for line in f:
            # Skip comments and empty lines
            if line.strip().startswith('//') or not line.strip():
                continue
            
            # Parse keybind
            keybind_data = parse_keybind_line(line)
            if keybind_data:
                category = categorize_keybind(keybind_data)
                keybinds_by_category[category].append(keybind_data)
    
    total_keybinds = sum(len(v) for v in keybinds_by_category.values())
    print(f"✅ Found {total_keybinds} keybinds in {len(keybinds_by_category)} categories")
    
    # Generate output
    output_dir = config_file.parent
    
    if output_format in ["markdown", "both"]:
        md_file = output_dir / "keybind_cheatsheet.md"
        generate_markdown(keybinds_by_category, md_file)
        print(f"📝 Generated markdown: {md_file}")
    
    if output_format in ["html", "both"]:
        html_file = output_dir / "keybind_cheatsheet.html"
        generate_html(keybinds_by_category, html_file)
        print(f"🌐 Generated HTML: {html_file}")
    
    print("\n✨ Cheatsheet generation complete!")

if __name__ == "__main__":
    main()
