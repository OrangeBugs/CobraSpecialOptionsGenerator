class Label:
    def __init__(
        self,
        optionName: str,
        x,
        y: int,
        w: int = 800,
        h: int = 18,
        text: str = "",
        tooltip: str = "",
        skin=None,
        depends_on: str = None,
    ):
        self.name = f"{optionName}Label"
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.text = text
        self.tooltip = tooltip
        self.skin = skin
        self.depends_on = depends_on

    def __str__(self):

        skin_name = self.skin.name if self.skin else "HelpSkin"

        return f"""\t\t\t\t["{self.name}"] = {{
\t\t\t\t\t["params"] = {{
\t\t\t\t\t\t["bounds"] = {{
\t\t\t\t\t\t\t["h"] = {self.h},
\t\t\t\t\t\t\t["w"] = {self.w},
\t\t\t\t\t\t\t["x"] = {self.x},
\t\t\t\t\t\t\t["y"] = {self.y},
\t\t\t\t\t\t}},
\t\t\t\t\t\t["enabled"] = true,
\t\t\t\t\t\t["text"] = "{self.text}",
\t\t\t\t\t\t["tooltip"] = "{self.tooltip}",
\t\t\t\t\t\t["visible"] = true,
\t\t\t\t\t\t["zindex"] = 0,
\t\t\t\t\t}},
\t\t\t\t\t["skin"] = {skin_name},
\t\t\t\t\t["type"] = "Static",
\t\t\t\t}},
"""
