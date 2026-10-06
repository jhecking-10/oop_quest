class Character:
    def __init__(
        self,
        name: str,
        race: str = "Human",
    ) -> None:
        self.name = name
        self.race = race

    def attack(self) -> None:
        print(f"{self.name} attacks")

class Swordsman(Character):
    def attack(self):
        print(f"{self.name} swings his sword")

class Archer(Character):
    def __init__(
        self,
        name: str,
        race: str = "Elf",
        num_arrows: int = 10,
    ) -> None:
        super().__init__(name, race)
        self.num_arrows = num_arrows

    def attack(self) -> None:
        self.num_arrows -= 1
        print(f"{self.name} fires an arrow")

    def display_num_arrows(self) -> None:
        print(f"{self.name} currently holds {self.num_arrows} arrows")

class Mage(Character):
    def __init__(
        self,
        name: str,
        race: str = "Human",
        mana: int = 100,
    ) -> None:
        super().__init__(name, race)
        self.mana = mana
    
    def attack(self) -> None:
        self.mana -= 10
        print(f"{self.name} casts a spell")

    def meditate(self) -> None:
        self.mana += 10
        print(f"{self.name} is meditating...")

    def display_current_mana(self) -> None:
        print(f"{self.name} currently has {self.mana} mana")
