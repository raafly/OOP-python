class Hero: # template
    pass

hero1 = Hero() # object
hero2 = Hero() 
hero3 = Hero() 

hero1.nama = "sniper"
hero1.health = 100

hero2.name = "heale"
hero2.health = 50


hero3.health = 1000

print(hero1)
print(hero1.__dict__)
print(hero1.nama)