def copyColours(colours, n):
    return colours[:n]

colours = ["red", "orange", "green", "violet", "blue", "yellow"]


for i in range(1, len(colours)+1):
    print(copyColours(colours, i))


tekst = '''Korporacja (z łac. corpo – ciało, ratus – szczur; pol. ciało szczura) – organizacja, 
        która pod przykrywką prowadzenia biznesu włada dzisiejszym światem. Wydawać się może 
        utopijnym miejscem realizacji pasji zawodowych. W rzeczywistości jednak nie jest wcale 
        tak kolorowo. Korporacja służy do wyzyskiwania człowieka w imię postępu. Rządzi w niej 
        prawo dżungli. '''

print(tekst[tekst.index('(')+1:tekst.index(')')])


