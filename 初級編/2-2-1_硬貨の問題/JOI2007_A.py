N = int(input())

yen = 1000 - N

five_hund = yen // 500
yen -= five_hund * 500

one_hund = yen // 100
yen -= one_hund * 100

five_ten = yen // 50
yen -= five_ten * 50

ten = yen // 10
yen -= ten * 10

five = yen // 5
yen -= five * 5

result = five_hund + one_hund + five_ten + ten + five + yen
print(result)
