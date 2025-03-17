# World Simulation

## Project Description
This project is an object-oriented simulation of a flat world populated by organisms like lynxes, antelopes, sheep, and grass. It was originally developed as a university assignment in 2024 and uploaded to GitHub in March 2025 to showcase my programming skills in Python. The simulation includes unique organism behaviors and a "plague mode" mechanic.

## Features
- **Lynx** (`power = 6`, `initiative = 5`, `liveLength = 18`, `sign = 'R'`): A predator with standard animal behavior.
- **Antelope** (`power = 4`, `initiative = 3`, `liveLength = 11`, `sign = 'A'`): Escapes two fields away from a lynx if detected; attacks if escape is impossible.
- **Sheep** and **Grass**: Additional organisms with basic behaviors.
- **Plague Mode**: Reduces the `liveLength` of all organisms by half for two turns.
- **Dynamic World**: Add new organisms at free positions after each round.
- **Unit Tests**: Comprehensive tests to validate organism behaviors and plague mechanics.

## Technologies
- Python 3.x
- Object-Oriented Programming (OOP)
- Unit testing with Python's `unittest` module

## How to Run
1. Clone the repository: `git clone https://github.com/Wsakowska/WorldSimulation.git`
2. Navigate to the project directory: `cd WorldSimulation`
3. Run the simulation: `python Main.py`
4. (Optional) Run tests: `python Tests.py`

## Learning Outcomes
- Improved understanding of OOP principles like inheritance and polymorphism.
- Experience in designing and testing interactive simulations.
