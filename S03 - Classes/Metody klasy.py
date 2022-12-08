class Cake:

    def __init__(self, name, kind, taste, additives, filling):
        self.name = name
        self.kind = kind
        self.taste = taste
        self.additives = additives
        self.filling = filling

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
        print('-'*20)


    def set_filling(self, filling):
        self.filling = filling


    def add_additives(self, additives):
        self.additives.extend(additives)




cake_01 = Cake('Torcik wiedeński', 'tort', 'czekoladowy', ['bakalie', 'pomarańcza'], 'marmolada')
cake_02 = Cake('Chocolade Muffin','muffin', 'chocolade', ['chocolade'], '')
cake_03 = Cake('Super Sweet Maringue','meringue', 'very sweet', [], '')

cake_02.set_filling('nadzienie kremowe')
cake_03.add_additives(['kokos', 'posypka kakaowa'])
cake_01.set_filling('Dzem truskawkowy')


bakery_offer = []
bakery_offer.append(cake_01)
bakery_offer.append(cake_02)
bakery_offer.append(cake_03)

print('Today in our offer:')
for cake in bakery_offer:
    cake.show_info()
