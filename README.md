# 🐍 Python Snake Game (OOP with Turtle)

This is a classic **Snake Game** built using **Python** and the **Turtle graphics module**, following **Object-Oriented Programming (OOP)** principles. The game consists of separate classes for the snake, food, and scoreboard, with all components tied together in `main.py`.

---

## 📁 Project Structure

All files are located in the `snake game/` directory:

<pre> <br>├── main.py <br>├── snake.py <br>├── food.py <br>└── scoreboard.py </pre>
---

## 🚀 Features

- 🎮 Real-time snake movement with keyboard input
- 🍎 Food detection and random repositioning
- 🐍 Snake grows with each food item eaten
- 💥 Collision detection with:
  - Walls (screen boundaries)
  - Self (snake's own tail)
- 🧠 Score tracking and game over message
- 🐢 Smooth animation using `screen.tracer(0)` and `time.sleep()`
- 🧱 Structured using OOP for readability and modularity

---

## 🧠 Class Overview

- **`Snake` (in `snake.py`)**
  - Manages the snake body, movement, direction changes
  - Detects collision with itself
  - Handles growth when food is eaten

- **`Food` (in `food.py`)**
  - Inherits from `turtle.Turtle`
  - Places food at random positions on the screen

- **`Scoreboard` (in `scoreboard.py`)**
  - Displays and updates the score
  - Shows a "Game Over" message on collision

- **`main.py`**
  - Sets up the screen and initializes game objects
  - Controls the game loop and input (arrow keys)
  - Checks for collisions and updates the screen

---

## 🎮 Controls

Use the following keys to control the snake:

- Arrow Keys: `↑ ↓ ← →`

---

## 🛠 Requirements

- Python 3.x
- `turtle` module (included with standard Python installations)

---

## ▶️ How to Run

1. Ensure all files (`main.py`, `snake.py`, `food.py`, `scoreboard.py`) are inside a folder named `snake game/`.
2. Open a terminal or IDE in that directory.
3. Run the game using:

```bash
python main.py
