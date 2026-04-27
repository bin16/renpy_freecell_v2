# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a Ren'Py (v8.5.2) visual novel project that implements a FreeCell solitaire game. The project is written in Chinese and uses Ren'Py's drag-and-drop system for card interactions.

## Common Commands

### Running the Game
```bash
renpy /path/to/renpy_freecell_v2
```
Or open the Ren'Py launcher and select this project.

### Building Distributions
Use Ren'Py's built-in distribution building through the Ren'Py launcher (Build Distributions).

## Architecture

### Key Files
- `game/free_cell/game.rpy` - Core FreeCell game logic (FreeCellGame class)
- `game/script.rpy` - Entry point with `start` label
- `game/screens.rpy` - All screens (main menu, save/load, preferences, etc.)
- `game/gui.rpy` - GUI configuration and styling (1920x1080 base resolution)
- `game/options.rpy` - Game settings (name, version, transitions, etc.)

### Card Interaction System
The game uses Ren'Py's `draggroup` and `drag` system for cards:
- `handle_card_drop(drags, drop)` - Called when a card is dropped
- `handle_card_tap(drag)` - Called when a card is clicked
- `handle_card_joined(drag)` - Returns list of cards dragged together as a stack

Card placement priority (from README):
1. Foundation (回收区) - cards placed by clicking
2. Tableau (桌面区) - cards placed beneath other cards
3. Empty tableau slots
4. Foundation via dragging

### Data Model
- `FreeCellGame` class in `init python:` block manages all card state and position relationships
- Cards are displayed using Ren'Py's drag elements with `drag_name`, `xpos`, `ypos`, `draggable`, etc.

### GUI System
- Base resolution: 1920x1080
- Font: SourceHanSansLite.ttf (思源黑体)
- Phone variant GUI assets exist in `game/gui/phone/`
- Touch/small variant overrides styles for mobile devices

### Directory Structure
```
game/
  free_cell/        # FreeCell-specific code
    game.rpy         # Core game logic
  gui/              # GUI assets and styling
    phone/          # Mobile GUI variants
  tl/None/          # Translation files
  cache/            # Ren'Py bytecode cache
  saves/            # Save files
  script.rpy        # Entry point
  screens.rpy       # All screens
  gui.rpy           # GUI init and styling
  options.rpy       # Game options
```
