name = "Nils"
if name == "Nils":
    print("woh")


class Toolbox:
    """an example of a class, something a lot of people do not take advantage of in Python"""

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"Toolbox(name={self.name!r})"

