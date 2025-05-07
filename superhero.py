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
