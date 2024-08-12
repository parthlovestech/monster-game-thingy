# Turn-Based RPG Battle Game

## Overview

A simple RPG game thingy that I created for some reason even I don't know.

## How to Play

1. **Start the Game**: Run the Python script to begin the game.
2. **Player's Turn**: On your turn, you will be prompted to choose an action:
   - **Attack**: Type `1` to attack the monster.
   - **Do Nothing**: Type `2` to skip your turn.
3. **Monster's Turn**: After your turn, the monster will automatically take its turn and attack you.
4. **Winning the Game**: The battle continues until either you or the monster is defeated. If you defeat the monster, you win. If the monster defeats you, the game ends.

## Game Mechanics

- **Characters**: The game features two characters:
  - **Hero**: The player, with 100 health points and 20 attack power.
  - **Monster**: The opponent, with 80 health points and 15 attack power.
  
- **Attack System**: The damage dealt in each attack is randomly generated based on the attack power of the character.

## Code Structure

- **Character Class**: Handles the attributes and behaviors of the characters (Hero and Monster).
- **Game Class**: Manages the battle flow, including turns, actions, and victory conditions.

## Prerequisites

- **Python 3.x**: Make sure you have Python installed on your system. You can download it from [python.org](https://www.python.org/).

## How to Run the Game

1. **Clone the Repository**:
   ```bash
   https://github.com/parthlovestech/monster-game-thingy
   ```
2. **Navigate to the Project Directory**:
   ```bash
   cd monster-game-thingy/
   ```
3. **Run the Script**:
   ```bash
   python monster.py
   ```

## Contributing

Feel free to fork this repository, make improvements, and submit pull requests. Any contributions that enhance the gameplay or add new features are welcome!

## License

This project is open-source and available under the [MIT License](LICENSE).

---

