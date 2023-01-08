class Cake:

    known_types = ['cake', 'muffin', 'meringue', 'biscuit', 'eclair', 'christmas', 'pretzel','other']
    bakery_offer = []

    def __init__(self, name, kind, taste, additives, filling, gluten_free):
        self.name = name
        if kind is self.known_types:
            self.kind = kind
        else:
            self.kind = 'other'
        self.taste = taste
        self.additives = additives
        self.filling = filling
        self.__gluten_free = gluten_free
        self.bakery_offer.append(self)

    def show_info(self):
        print('{}'.format(self.name.upper()))
        print('Kind: {}'.format(self.kind))
        print('Taste: {}'.format(self.taste))
        if len(self.additives) > 0:
            print('Additives:')
            for a in self.additives:
                print('       {}'.format(a))
        if len(self.filling) > 0:
            print('Filling: {}'.format(self.filling))
        print('Gluten: {}'.format(self.__gluten_free))
        print('-'*20)


    def set_filling(self, filling):
        self.filling = filling


    def add_additives(self, additives):
        self.additives.extend(additives)




cake_01 = Cake('Torcik wiedeński', 'tort', 'czekoladowy', ['bakalie', 'pomarańcza'], 'marmolada', True)
cake_02 = Cake('Chocolade Muffin','muffin', 'chocolade', ['chocolade'], '', True)
cake_03 = Cake('Super Sweet Maringue','meringue', 'very sweet', [], '', False)
cake_04 = Cake('Cocoa waffle','waffle','cocoa',[],'cocoa', False)

cake_01.set_filling('Dzem truskawkowy')
cake_02.set_filling('nadzienie kremowe')
cake_03.add_additives(['kokos', 'posypka kakaowa'])

# print('Today in our offer:')
# for cake in Cake.bakery_offer:
#     cake.show_info()

cake_01.__gluten_free = False

print(dir(cake_01))
print(vars(cake_01))

cake_01._Cake__gluten_free = False
cake_01.show_info()

cake_01.__setattr__('_Cake__gluten_free', True)
cake_01.show_info()
print(vars(cake_01))

# print(isinstance(cake_01, Cake))
# print(isinstance(cake_02, Cake))
# print(isinstance(cake_03, Cake))
# print(isinstance(cake_04, Cake))

# print('Instancja {}'.format(vars(cake_01)))
# print('Klasa {}'.format(vars(Cake)))