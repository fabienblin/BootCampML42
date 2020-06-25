class GotCharacter:
    def __init__(self, first_name=None, is_alive=True):
        self.first_name = ""
        self.is_alive = True

        if first_name is not None:
            self.first_name = first_name
        if is_alive is not None:
            self.is_alive = is_alive


class Stark(GotCharacter):
    """A class representing the Stark family.
       Or when bad things happen to good people."""
    pass

    def __init__(self, first_name=None, is_alive=True):
        self.last_name = ""
        self.house_words = ""

        super().__init__(first_name=first_name, is_alive=is_alive)
        self.family_name = "Stark"
        self.house_words = "Winter is Coming"

    def print_house_words():
        print(self.house_words)

    def die():
        self.is_alive = False
