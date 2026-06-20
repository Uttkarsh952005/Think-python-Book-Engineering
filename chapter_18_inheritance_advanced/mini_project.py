"""
Chapter 18: Mini Project - RPG Character System
Demonstrates how Mixins compose behavior horizontally across different class hierarchies.
"""

# --- Base Class ---
class Character:
    def __init__(self, name: str, hp: int):
        self.name = name
        self.hp = hp

    def __str__(self):
        return f"{self.name} [HP: {self.hp}]"

# --- Mixins (Horizontal Behavior) ---
class HealerMixin:
    """Can be attached to any Character class to grant healing abilities."""
    def heal(self, target: Character, amount: int) -> None:
        target.hp += amount
        print(f"✨ {self.name} heals {target.name} for {amount} HP!")

class AttackerMixin:
    """Can be attached to any Character class to grant attack abilities."""
    def attack(self, target: Character, damage: int) -> None:
        target.hp -= damage
        print(f"⚔️ {self.name} strikes {target.name} for {damage} damage!")

# --- Concrete Classes (Multiple Inheritance) ---
class Paladin(Character, HealerMixin, AttackerMixin):
    """A hybrid class that can both attack and heal."""
    pass

class Priest(Character, HealerMixin):
    """A dedicated healer class."""
    pass

def main():
    print("--- RPG Mixin System ---")
    
    arthas = Paladin("Arthas", 100)
    anduin = Priest("Anduin", 60)
    enemy = Character("Orc", 50)
    
    print(arthas)
    print(anduin)
    print(enemy)
    print("-" * 30)
    
    # Paladin has access to AttackerMixin
    arthas.attack(enemy, 25)
    
    # Paladin has access to HealerMixin
    arthas.heal(arthas, 10)
    
    # Priest has access to HealerMixin
    anduin.heal(enemy, 50) # Oops, healed the enemy!
    
    print("-" * 30)
    print(arthas)
    print(anduin)
    print(enemy)

if __name__ == "__main__":
    main()
