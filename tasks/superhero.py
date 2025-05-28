#task 1 2 3
class Superhero:
    def __init__(self, name, alias, superpower, sidekick=None):
        self.name = name
        self.alias = alias
        self.superpower = superpower
        self.sidekick = sidekick

    def introduce(self):
        print(f"I am {self.alias}, also known as {self.name}!")
        print(f"My superpower is: {self.superpower}")
        if self.sidekick:
            print(f"My sidekick is {self.sidekick}.")

scooby_doo = Superhero(
    name="Scooby Doo",
    alias="Scooby-Doo",
    superpower="Super sniffing & mystery solving",
    sidekick="Shaggy"
)

# Introducing Scooby-Doo
scooby_doo.introduce()

# task 4 
class Superhero:
    def __init__(self, name, alias, sidekick=None):
        self.name = name
        self.alias = alias
        self.sidekick = sidekick

    def introduce(self):
        print(f"I am {self.alias}, also known as {self.name}!")
        if self.sidekick:
            print(f"My sidekick is {self.sidekick}.")

    # Superpower methods
    def super_sniff(self):
        print(f"{self.alias} uses super sniffing to find clues!")

    def mystery_solver(self):
        print(f"{self.alias} is solving a mystery with amazing logic!")

    def snack_detect(self):
        print(f"{self.alias} detects snacks from miles away!")

    def speed_escape(self):
        print(f"{self.alias} runs away really fast when scared!")

    def disguise_mode(self):
        print(f"{self.alias} puts on a funny disguise to trick the villain!")

    # Method to choose an action
    def use_power(self, power_name):
        if power_name == "super_sniff":
            self.super_sniff()
        elif power_name == "mystery_solver":
            self.mystery_solver()
        elif power_name == "snack_detect":
            self.snack_detect()
        elif power_name == "speed_escape":
            self.speed_escape()
        elif power_name == "disguise_mode":
            self.disguise_mode()
        else:
            print(f"{self.alias} doesn't have the power '{power_name}'.")

# Create the superhero
scooby_doo = Superhero(name="Scooby Doo", alias="Scooby-Doo", sidekick="Shaggy")

# Introduce
scooby_doo.introduce()

# Choose powers to use
scooby_doo.use_power("super_sniff")
scooby_doo.use_power("snack_detect")
scooby_doo.use_power("dance_party")  # to test a mistake

