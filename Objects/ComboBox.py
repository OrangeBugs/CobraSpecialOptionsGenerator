class ComboBox:
    def __init__(
        self,
        optionName: str,
        x,
        y: int,
        items,
        w: int = 140,
        h: int = 24,
        default=0,
        text: str = "Item1",
        tooltip: str = "",
        skin=None,
        depends_on: str = None,
        callback: bool = False,
        _cockpit_livery_folder: str = None,
    ):
        self.base_name = optionName
        self.name = f"{optionName}ComboList"
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.items = list(items) if items is not None else []

        if not self.items and _cockpit_livery_folder is None:
            raise ValueError("ComboBox items cannot be empty")
        if any(not isinstance(item, (tuple, list)) or len(item) != 2 for item in self.items):
            raise ValueError("ComboBox items must be (label, value) pairs")

        self.default = default
        self.text = text
        self.tooltip = tooltip
        self.skin = skin
        self.depends_on = depends_on
        self.callback = callback
        self.cockpit_livery_folder = _cockpit_livery_folder

    @classmethod
    def cockpit_livery(
        cls,
        cockpit_folder: str,
        x,
        y: int,
        w: int = 140,
        h: int = 24,
        text: str = "Item1",
        tooltip: str = "",
        skin=None,
        depends_on: str = None,
    ):
        """Create DCS's standard local cockpit-livery selector."""
        if not isinstance(cockpit_folder, str) or not cockpit_folder:
            raise ValueError("cockpit_folder must be a non-empty string")

        return cls(
            optionName="CPLocalList",
            x=x,
            y=y,
            items=None,
            w=w,
            h=h,
            text=text,
            tooltip=tooltip,
            skin=skin,
            depends_on=depends_on,
            _cockpit_livery_folder=cockpit_folder,
        )

    @staticmethod
    def _escape_lua_string(value):
        return value.replace("\\", "\\\\").replace("'", "\\'").replace('"', '\\"')

    def _format_value(self, value):
        if isinstance(value, str):
            return f'"{self._escape_lua_string(value)}"'
        if isinstance(value, bool):
            return str(value).lower()
        return value

    def __str__(self):
        skin_block = self.skin.name if self.skin else """{
\t\t\t\t\t["params"] = {
\t\t\t\t\t\t["name"] = "comboListSkin_options",
\t\t\t\t\t},
\t\t\t\t}"""

        return f"""
\t\t\t\t["{self.name}"] = {{
\t\t\t\t\t["params"] = {{
\t\t\t\t\t\t["bounds"] = {{
\t\t\t\t\t\t\t["h"] = {self.h},
\t\t\t\t\t\t\t["w"] = {self.w},
\t\t\t\t\t\t\t["x"] = {self.x},
\t\t\t\t\t\t\t["y"] = {self.y - 4},
\t\t\t\t\t\t}},
\t\t\t\t\t\t["enabled"] = true,
\t\t\t\t\t\t["tabOrder"] = 0,
\t\t\t\t\t\t["text"] = "{self._escape_lua_string(self.text)}",
\t\t\t\t\t\t["tooltip"] = "{self._escape_lua_string(self.tooltip)}",
\t\t\t\t\t\t["visible"] = true,
\t\t\t\t\t\t["zindex"] = 3,
\t\t\t\t\t}},
\t\t\t\t\t["skin"] = {skin_block},
\t\t\t\t\t["type"] = "ComboList",
\t\t\t\t}},
"""

    def to_db(self):
        if self.cockpit_livery_folder is not None:
            return None

        item_lines = []
        for label, value in self.items:
            escaped_label = self._escape_lua_string(str(label))
            item_lines.append(
                f"\t\tDbOption.Item(_('{escaped_label}')):Value({self._format_value(value)})"
            )

        base = (
            f"{self.base_name}\t= DbOption.new():setValue({self._format_value(self.default)}):combo({{\n"
            + ",\n".join(item_lines)
            + ",})"
        )
        if self.callback:
            base += ":callback(function(v) Update() end)"
        return "\t" + base + ","

    def to_post_db(self):
        if self.cockpit_livery_folder is None:
            return None

        folder = self._escape_lua_string(self.cockpit_livery_folder)
        return f'result.CPLocalList = oms.getCPLocalList("{folder}")'
