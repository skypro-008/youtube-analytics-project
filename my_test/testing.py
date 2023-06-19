import json
class Item:
    def __init__(self,itemall):
        self.gg = "ddfdfdfdf"
        self.itemall = itemall

    def to_json(self):
        dict = {
            "gg": self.gg
        }
        with open("moscowpython.json", "w") as file_json:
            json.dump(dict, file_json)

it = Item("111")
it.to_json()


