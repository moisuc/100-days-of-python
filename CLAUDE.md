# 100 Days of Python

## Overview
Educational repository containing exercises and projects from the 100 Days of Python tutorial

## Stack
- **Language**: Python 3.14
- **Package Manager**: uv
- **Dev Tools**: mypy (strict type checking)
- **Framework**: None (pure Python learning exercises)

## Commands
```bash
# Install dependencies
uv sync

# Run main entry point
uv run main.py

# Run specific exercises
python calculator.py
python blackjack/main.py

# Type checking (mypy configured in pyproject.toml)
mypy .
```

## Structure
```
.
├── main.py              # Main entry point (hello world)
├── calculator.py        # Calculator exercise with operations
├── blackjack/           # Blackjack game exercise
│   └── main.py
├── pyproject.toml       # Project config with strict mypy settings
└── README.md
```

## Patterns
Based on code analysis:

### Type Annotations
- **All functions have type hints** (enforced by strict mypy config)
- Return types explicitly declared (`-> None`, `-> float`, etc.)
- Function parameters typed (`n1: float`, `user_cards: list[int]`)

### Code Organization
- **Standalone exercises**: Each day/exercise is a separate file or directory
- **Function-based**: Pure functions for operations (calculator ops, card drawing)
- **Interactive CLI**: Uses `input()` for user interaction
- **Game loops**: While loops for repeated gameplay

### Error Handling
- **Exception raising**: Raises `Exception` for invalid operations (e.g., divide by zero)
- **Input validation**: Currently minimal, relies on valid user input

### Naming Conventions
- **Functions**: `snake_case` (e.g., `draw_card`, `check_sum`, `print_hands`)
- **Variables**: `snake_case` with descriptive names
- **Type dictionaries**: Used for operation mapping (`operations: dict[str, Callable]`)

## Conventions

### Naming
- Functions: `snake_case`
- Variables: `snake_case`
- Constants: Currently none, but would use `UPPER_CASE`

### Type Safety
- Strict mypy configuration enabled in `pyproject.toml`:
  - `disallow_untyped_defs = true`
  - `disallow_incomplete_defs = true`
  - All new code must have complete type annotations

### User Interaction
- Screen clearing: `print('\n'*20)` for console reset
- Input prompts: Descriptive with format guidance (e.g., "Type 'y' or 'n'")
- Game state: Boolean flags like `should_accumulate`, `should_play`

### Project Structure
- Root level: Simpler single-file exercises
- Subdirectories: More complex multi-day projects (e.g., `blackjack/`)

## Quick Reference

### Key Files
- `main.py`: Template entry point
- `calculator.py`: Example of operations dict pattern and recursion
- `blackjack/main.py`: Example of game loop and state management
- `pyproject.toml`: Mypy strict mode configuration

### Adding New Exercises
1. Create new `.py` file at root for simple exercises
2. Create subdirectory for complex multi-file projects
3. Ensure all functions have type hints (mypy will enforce)
4. Follow interactive CLI pattern with `input()` for user interaction
5. Update README.md with new exercise description

### Common Patterns to Follow
- **Operations dict**: Map symbols to functions (see calculator.py:22)
- **Input validation**: Check user choices in conditionals
- **Game loops**: Use `while` with boolean state variables
- **Type hints**: Always include for parameters and return types
