class Character:
    def __init__(
        self,
        name: str,
        race: str = "Human",
        health: int = 50,
        stamina: int = 40,
    ) -> None:
        self.name = name
        self.race = race
        self.health = health
        self.stamina = stamina

    def attack(self) -> None:
        print(f"{self.name} attacks")

class Swordsman(Character):
    def attack(self) -> None:
        print(f"{self.name} swings his sword")

class Archer(Character):
    def __init__(
        self,
        name: str,
        race: str = "Elf",
        health: int = 40,
        stamina: int = 60,
        num_arrows: int = 10,
    ) -> None:
        super().__init__(
            name,
            race,
            health,
            stamina,
        )
        self.num_arrows = num_arrows

    def attack(self) -> None:
        self.num_arrows -= 1
        print(f"{self.name} fires an arrow")

    def triple_shot(self) -> None:
        self.num_arrows -= 3
        print(f"{self.name} fires a triple shot")

    def display_num_arrows(self) -> None:
        print(f"{self.name} currently holds {self.num_arrows} arrows")

class Mage(Character):
    def __init__(
        self,
        name: str,
        race: str = "Human",
        health: int = 40,
        stamina: int = 50,
        mana: int = 100,
    ) -> None:
        super().__init__(
            name,
            race,
            health,
            stamina,
        )
        self.mana = mana
    
    def attack(self) -> None:
        self.mana -= 10
        print(f"{self.name} casts a spell")

    def meditate(self) -> None:
        self.mana += 10
        print(f"{self.name} is meditating...")

    def display_current_mana(self) -> None:
        print(f"{self.name} currently has {self.mana} mana")
