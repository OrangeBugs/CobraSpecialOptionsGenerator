class HelpSkin:
    name = "HelpSkin"

    def __str__(self):
        return """local HelpSkin = {
\t["params"] = {
\t\t["name"] = "staticSkin2",
\t},
\t["states"] = {
\t\t["disabled"] = {
\t\t\t[1] = {
\t\t\t\t["text"] = {
\t\t\t\t\t["color"] = "0x808080ff",
\t\t\t\t\t["font"] = "DejaVuLGCSansCondensed.ttf",
\t\t\t\t\t["fontSize"] = 11,
\t\t\t\t\t["horzAlign"] = {
\t\t\t\t\t\t["type"] = "min"
\t\t\t\t\t},
\t\t\t\t\t["vertAlign"] = {
\t\t\t\t\t\t["offset"] = 0,
\t\t\t\t\t\t["type"] = "middle"
\t\t\t\t\t}
\t\t\t\t}
\t\t\t}
\t\t},
\t\t["released"] = {
\t\t\t[1] = {
\t\t\t\t["text"] = {
\t\t\t\t\t["fontSize"] = 11,
\t\t\t\t\t["horzAlign"] = {
\t\t\t\t\t\t["type"] = "min"
\t\t\t\t\t}
\t\t\t\t}
\t\t\t}
\t\t}
\t}
}
"""
