class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        print("汪汪汪")

class Cat(Animal):
    def speak(self):
        print("喵喵喵")

def make_noise(animal:Animal):
    # 制造点噪音，需要传入Animal对象
    animal.speak()

dog = Dog()
cat = Cat()

make_noise(dog)
make_noise(cat)

class AC:
    def cood_wind(self):
        """制冷"""
        pass

    def hot_loss(self):
        """制热"""
        pass

    def swing_l_r(self):
        """左右摆风"""
        pass

class Mieda_AC(AC):
    def cood_wind(self):
        print("美的空调制冷")

    def hot_loss(self):
        print("美的空调制热")

    def swing_l_r(self):
        print("美的空调左右摆风")


class GREE_AC(AC):
    def cood_wind(self):
        print("格力空调制冷")

    def hot_loss(self):
        print("格力空调制热")

    def swing_l_r(self):
        print("格力空调左右摆风")

def make_cool(ac:AC):
    ac.cood_wind()

midea_ac = Mieda_AC()
gree_ac = GREE_AC()

make_cool(midea_ac)
make_cool(gree_ac)

