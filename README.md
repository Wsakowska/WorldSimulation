# World Simulation

## Project Description
This project is a simulation of a flat world inhabited by various organisms such as sheep, grass, lynxes, and antelopes. Each organism has specific attributes like `power`, `initiative`, `liveLength`, and special behaviors. Additionally, there is a "plague mode" that cuts the lifespan of existing organisms in half for two turns.

## Features
- **Lynx** (`power = 6`, `initiative = 5`, `liveLength = 18`, `sign = 'R'`): a predator with standard animal behavior.
- **Antelope** (`power = 4`, `initiative = 3`, `liveLength = 11`, `sign = 'A'`): tries to run two fields away from a lynx if it detects one nearby; if escape is impossible, it will attack.
- **Plague Mode**: reduces the `liveLength` of all current organisms by half for two turns.
- **Add New Organisms** at any free position after each round.
- Comprehensive **unit tests** to validate the behavior of each organism and new features.