# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

A FreeCell solitaire game implemented with Ren'Py (v8.5.2). Uses Ren'Py's `draggroup`/`drag` system for card interactions.

## Common Commands

```bash
renpy /path/to/renpy_freecell_v2
```

## Architecture

### File Structure — `game/free_cell/`

```
free_cell/
  card.rpy                  # Card class definition
  config.rpy                # Layout constants (CARD_WIDTH, GAP, PADDING, etc.)
  game.rpy                  # FreeCellGame class, game state, xpos_of/ypos_of helpers
  screen.rpy                # Main screen free_cell_game_screen, defines `default game = FreeCellGame()`
  screen_*.rpy              # Individual screen components
```

### Key Classes

**`Card`** (`card.rpy`):
- `Card(suit, number)` — suit 0-3, number 1-13
- `card.is_red()` — hearts/diamonds return True
- `card.name` — property returning "♥️A", "♠️10" etc.
- `card.num_diff(other)` — returns `other.number - self.number`; diff == -1 means stackable

**`FreeCellGame`** (`game.rpy`):
- `game.piles` — 16 lists indexed 0-15:
  - 0-7: tableau (8 columns), cards stack with `MINI_CARD_HEIGHT` offset
  - 8-11: foundation (4 piles), cards stack fully overlapped at `PADDING`
  - 12-15: freecell (4 cells), single card at `PADDING`
- `game.xpos_of(col_index)`, `game.ypos_of(col_index, row_index=0)` — pixel positions
- `TABLEAU_RANGE`, `FOUNDATION_RANGE`, `FREECELL_RANGE` — range constants for iteration
- `find_click_move_target(card, col, row)` — returns `(target_col, reason)`; reason is `MOVE_NO_TARGET`, `MOVE_INVALID_SEQUENCE`, or `MOVE_NO_SPACE`

### Layout Constants (`config.rpy`)

- Canvas: 1920x1080, with `PADDING` margin
- Card sizes: `CARD_WIDTH=150`, `CARD_HEIGHT=200`, `MINI_CARD_HEIGHT=50` (tableau stack offset)
- `GAP=32` between columns
- Freecell: top-left; Foundation: top-right; Tableau: centered below

### Card Interaction

- `Drag.dragged(drags, drop)` — handle drag events (drags first arg, drop second); use `Drag.snap()` to snap back if invalid
- `Drag.dropped(drop, drags)` — handle drop onto a drag (drop first arg, drags second); used on empty cells
- `Drag.drag_joined(drag) -> [(drag, x, y)]` — drag multiple stacked cards together
- `Drag.snapped(drag, x, y, completed)` — update game data after move completes
- `Drag.clicked(drag)` — click-to-move: finds target via `find_click_move_target`, animates with `snap`, updates with `snapped`

Click-to-move priority: foundation → tableau stack → tableau empty → freecell (single card only)

Foundation rules: only the top card is draggable; all cards render fully overlapped.

### Standard Ren'Py Files

- `game/script.rpy` — entry point with `start` label
- `game/screens.rpy` — all screens (main menu, save/load, preferences, etc.)
- `game/gui.rpy` — GUI config (1920x1080 base, SourceHanSansLite font, phone variant)
- `game/options.rpy` — game settings