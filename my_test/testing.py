import json
class Item:

    all=[]
    def __init__(self,itemall,name1):
        self.gg = "ddfdfdfdf"
        self.itemall = itemall
        self.__name1 = name1
        self.__all =['Cmartphon',"dffdfdf"]
        print(self.__all)

    @property
    def name(self):
        return self.__all

    @name.setter
    def name(self, value):
        self.__all = ["value"]

    @property
    def name1(self):
        return self.__name

    @name1.setter
    def name1(self, value):
        if len(value) >= 10:
            # print("Длина наименования товара превышает 10 символов")
            print(value[:10])
        else:
            self.__name = value

    @classmethod
    def instantiate_from_csv(cls):
        cls.all.append("str")

        return cls.all




it = Item("111","Cmartphon")
it.name1 = 'СуперСмартфон'
Item.instantiate_from_csv()

Item.all.append("hgf123")
print(Item.all)
item1 = Item.all[0]
print(item1[0].name)






