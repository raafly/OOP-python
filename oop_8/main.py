class Hero:

    def __init__(self, nama, health, armor):
        self.__nama = nama
        self.__health = health
        self.__armor = armor
        self.info = "nama {} : \n\thealth: {}".format(self.__nama, self.__health)


nia = Hero('nia', 100, 10)

print(nia.info)