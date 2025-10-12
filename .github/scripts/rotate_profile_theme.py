#!/usr/bin/env python3
"""
Profile Theme Rotator
Rotates through available 3D contribution graph themes weekly
"""

import re
import os
from pathlib import Path

# Available themes in rotation order (you can customize this order)
THEMES = [
    "profile-night-view.svg",
    "profile-night-green.svg",
    "profile-night-rainbow.svg",
    "profile-season-animate.svg",
    "profile-green-animate.svg",
    "profile-gitblock.svg",
    "profile-south-season-animate.svg",
    "profile-south-season.svg",
    "profile-season.svg",
    "profile-green.svg"
]

README_PATH = "README.md"
THEME_DIR = "./profile-3d-contrib"


def get_current_theme():
    """Extract the current theme from README.md"""
    try:
        with open(README_PATH, "r", encoding="utf-8") as f:
            content = f.read()
        
        # Find the profile image line
        pattern = r'<img src="\.\/profile-3d-contrib\/([^"]+)"'
        match = re.search(pattern, content)
        
        if match:
            return match.group(1)
        else:
            print("Warning: Could not find profile theme in README.md")
            return THEMES[0]  # Default to first theme
    except Exception as e:
        print(f"Error reading README.md: {e}")
        return THEMES[0]


def get_next_theme(current_theme):
    """Get the next theme in rotation"""
    try:
        current_index = THEMES.index(current_theme)
        next_index = (current_index + 1) % len(THEMES)
        return THEMES[next_index]
    except ValueError:
        # Current theme not in list, start from beginning
        print(f"Current theme '{current_theme}' not in rotation list, starting from beginning")
        return THEMES[0]


def verify_theme_exists(theme):
    """Verify that the theme file actually exists"""
    theme_path = Path(THEME_DIR) / theme
    if not theme_path.exists():
        print(f"Warning: Theme file {theme_path} does not exist!")
        return False
    return True


def update_readme(new_theme):
    """Update README.md with the new theme"""
    try:
        with open(README_PATH, "r", encoding="utf-8") as f:
            content = f.read()
        
        # Replace the profile image line
        pattern = r'(<img src="\.\/profile-3d-contrib\/)([^"]+)(")'
        replacement = rf'\g<1>{new_theme}\g<3>'
        
        new_content = re.sub(pattern, replacement, content)
        
        if new_content == content:
            print("Warning: No changes made to README.md")
            return False
        
        with open(README_PATH, "w", encoding="utf-8") as f:
            f.write(new_content)
        
        print(f"✓ Successfully updated README.md with theme: {new_theme}")
        return True
        
    except Exception as e:
        print(f"Error updating README.md: {e}")
        return False


def main():
    """Main execution function"""
    print("Starting profile theme rotation...")
    
    # Get current theme
    current_theme = get_current_theme()
    print(f"Current theme: {current_theme}")
    
    # Get next theme
    next_theme = get_next_theme(current_theme)
    print(f"Next theme: {next_theme}")
    
    # Verify theme exists
    if not verify_theme_exists(next_theme):
        print(f"Skipping rotation - theme file not found")
        return
    
    # Update README
    if update_readme(next_theme):
        print("✓ Theme rotation complete!")
    else:
        print("✗ Theme rotation failed")


if __name__ == "__main__":
    main()
