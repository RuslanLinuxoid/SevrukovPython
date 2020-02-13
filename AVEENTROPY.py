description = [
    '1. Реверс числа: ',
    '2. Перевод из 10чной в любую другую (N, base): ',
    '3. Ход конём (x1, x2, y1, y2): ']

print(input(description[0])[::-1])

from string import printable as alphabet
def dec_to_base(N=0, base=100):
    x, y = divmod(N, base)
    return dec_to_base(x, base) + alphabet[y] if x else alphabet[y]
print(dec_to_base(*list(map(int, input(description[1]).split()))[:2]))

def horse(x1=0, x2=0, y1=0, y2=0):
    return "Y" if (x1 - x2) ** 2 + (x1 - x2) ** 2 == 5 else "N"
print(horse(*list(map(int, input(description[2]).split()))[:4]))