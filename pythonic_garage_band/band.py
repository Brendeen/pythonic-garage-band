# REMEMBER: Write classes with a capital, singular
class Band:
    def __init__(self, name, members):
        self.name = name
        self.members = members

    def play_solos(self):
        play_solo = [musician.play_solo() for musician in self.members]
        return play_solo
    # done with Anthony

    def __str__(self):
        return f"{self.name}"

    def __repr__(self):
        return f"Band instance. Name = {self.name}"


class Musician:
    # Base class
    def __init__(self, name):
        self.name = name


class Guitarist(Musician):
    def get_instrument(self):
        return "guitar"

    def play_solo(self):
        return "face melting guitar solo"

    def __str__(self):
        return f"My name is {self.name} and I play {self.get_instrument()}"

    def __repr__(self):
        return f"Guitarist instance. Name = {self.name}"


class Bassist(Musician):
    def get_instrument(self):
        return "bass"

    def play_solo(self):
        return "bom bom buh bom"

    def __str__(self):
        return f"My name is {self.name} and I play {self.get_instrument()}"

    def __repr__(self):
        return f"Bassist instance. Name = {self.name}"


class Drummer(Musician):
    def get_instrument(self):
        return "drums"

    def play_solo(self):
        return "rattle boom crash"

    def __str__(self):
        return f"My name is {self.name} and I play {self.get_instrument()}"

    def __repr__(self):
        return f"Drummer instance. Name = {self.name}"


if __name__ == "__main__":
    joan = Guitarist("Joan Jett")
    sheila = Drummer("Sheila E.")
    meshell = Bassist("Meshell Ndegeocello")
    jimi = Guitarist("Jimi Hendrix")
    print(joan.name, sheila.name, meshell.name, jimi.get_instrument(), joan.get_instrument(), str(joan))
