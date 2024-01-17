import maps

class RenderMaps:
    def __init__(self):
        self.current_map = maps.current_map
        self.symbolMeanings = [("0", " "), ("1", "X"),("2", "\n"),("3", "-"),("@","@")]
        self.map = ""

    def render_current_map(self):
        for i in self.current_map:
            for v in self.symbolMeanings:
                if i == v[0]:
                    self.map += v[1]

        return self.map