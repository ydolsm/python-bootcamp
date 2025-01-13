class Character:
    def __init__(self, name: str, health: int, stamina: int, attack: int, defense: int, skills: dict[dict]) -> None:
        """
        Initializes the character's attributes.

        Args:
            name (str): The character's name.
            health (int): The character's health points.
            stamina (int): The character's stamina points.
            attack (int): The character's attack power.
            defense (int): The character's defense value.
            skills (dict[dict]): A dictionary of dictionaries, each containing stamina cost, and damage
        """
        # TODO: Implement constructor to initialize attributes

    def basic_attack(self, enemy: 'Character') -> None:
        """
        Performs a basic attack on the enemy, reducing enemy health and self stamina.

        Args:
            enemy (Character): The enemy character to attack.

        Effects:
            - Reduces the enemy’s health.
            - Reduces the character’s stamina by 10 points.
        """
        # TODO: Implement basic attack logic
        pass

    def use_skill(self, skill_name: str, enemy: 'Character') -> None:
        """
        Uses a skill from the character's available skills.

        Args:
            skill_name (str): The name of the skill to use.
            enemy (Character): The enemy character to attack.

        Effects:
            - Reduces the enemy’s health by the skill's damage.
            - Reduces stamina by the skill's stamina cost.
        """
        # TODO: Implement skill usage logic
        pass

    def is_defeated(self) -> bool:
        """
        Checks if the character's health has dropped to zero or below.

        Returns:
            bool: True if the character is defeated, False otherwise.
        """
        # TODO: Implement defeat check
        pass

    def restore_stamina(self, amount: int) -> None:
        """
        Restores stamina for the character.

        Args:
            amount (int): The amount of stamina to restore.

        Effects:
            - Restores stamina, ensuring it doesn’t exceed 100 points.
        """
        # TODO: Implement stamina restoration logic
        pass


def select_enemy() -> 'Character':
    """
    Allows the player to choose an enemy from a list of available characters.
    Note: You'll make the enemies in advanced (usually)

    Returns:
        Character: The selected enemy character.
    """
    # TODO: Implement enemy selection logic
    pass


def game_loop(player: 'Character', enemy: 'Character') -> None:
    """
    Runs the main game loop where the player and enemy take turns.

    Args:
        player (Character): The player's character.
        enemy (Character): The enemy character.

    Effects:
        - Alternates turns between player and enemy until one is defeated.
        - Prints the result of each action and the current status.
    """
    # TODO: Implement game loop logic, where each character alternates actions
    pass


def main() -> None:
    """
    Initializes the game and starts the player character selection and game loop.
    """
    # TODO: Implement main game flow (e.g., selecting player, starting game loop)
    pass


main()