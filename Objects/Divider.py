class Divider:
    """A DXGUI horizontal divider rendered as a one-pixel Panel."""

    def __init__(
        self,
        optionName: str,
        x,
        y: int,
        w: int = 894,
        color: str = "0x00000041",
        zindex: int = 5,
    ):
        self.name = f"{optionName}Divider"
        self.x = x
        self.y = y
        self.w = w
        self.color = color
        self.zindex = zindex
        self.skin = None

    def __str__(self):
        return f'''\t\t\t\t["{self.name}"] = {{
\t\t\t\t\t["params"] = {{
\t\t\t\t\t\t["bounds"] = {{
\t\t\t\t\t\t\t["h"] = 1,
\t\t\t\t\t\t\t["w"] = {self.w},
\t\t\t\t\t\t\t["x"] = {self.x},
\t\t\t\t\t\t\t["y"] = {self.y + 10},
\t\t\t\t\t\t}},
\t\t\t\t\t\t["enabled"] = true,
\t\t\t\t\t\t["layout"] = {{}},
\t\t\t\t\t\t["text"] = "",
\t\t\t\t\t\t["tooltip"] = "",
\t\t\t\t\t\t["visible"] = true,
\t\t\t\t\t\t["zindex"] = {self.zindex},
\t\t\t\t\t}},
\t\t\t\t\t["skin"] = {{
\t\t\t\t\t\t["params"] = {{
\t\t\t\t\t\t\t["name"] = "panelSkin",
\t\t\t\t\t\t}},
\t\t\t\t\t\t["states"] = {{
\t\t\t\t\t\t\t["released"] = {{
\t\t\t\t\t\t\t\t[1] = {{
\t\t\t\t\t\t\t\t\t["bkg"] = {{
\t\t\t\t\t\t\t\t\t\t["center_bottom"] = "{self.color}",
\t\t\t\t\t\t\t\t\t\t["insets"] = {{
\t\t\t\t\t\t\t\t\t\t\t["bottom"] = 1,
\t\t\t\t\t\t\t\t\t\t}},
\t\t\t\t\t\t\t\t\t\t["left_bottom"] = "{self.color}",
\t\t\t\t\t\t\t\t\t\t["right_bottom"] = "{self.color}",
\t\t\t\t\t\t\t\t\t}},
\t\t\t\t\t\t\t\t}},
\t\t\t\t\t\t\t}},
\t\t\t\t\t\t}},
\t\t\t\t\t}},
\t\t\t\t\t["type"] = "Panel",
\t\t\t\t}},
'''
