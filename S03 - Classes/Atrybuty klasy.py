class Cake:

    def __init__(self, name, kind, taste, additives, filling):
        self.name = name
        self.kind = kind
        self.taste = taste
        self.additives = additives
        self.filling = filling


cake_01 = Cake('Torcik wiedeński', 'tort', 'czekoladowy', ['bakalie', 'pomarańcza'], 'marmolada')
cake_02 = Cake('Chocolade Muffin','muffin', 'chocolade', ['chocolade'], '')
cake_03 = Cake('Super Sweet Maringue','meringue', 'very sweet', [], '')

print(cake_01.name, cake_01.kind, cake_01.taste, cake_01.additives, cake_01.filling)
print(cake_02.name, cake_02.kind, cake_02.taste, cake_02.additives, cake_02.filling)
print(cake_03.name, cake_03.kind, cake_03.taste, cake_03.additives, cake_03.filling)


bakery_offer = []
bakery_offer.append(cake_01)
bakery_offer.append(cake_02)
bakery_offer.append(cake_03)

for cake in bakery_offer:
    print('{} main taste: {} with additives of {}, filled with {}'.format(cake.name, cake.kind, cake.taste, cake.additives, cake.filling))