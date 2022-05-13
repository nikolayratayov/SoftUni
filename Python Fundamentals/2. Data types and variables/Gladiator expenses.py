losts = int(input())
helmet_cena = float(input())
sword_cena = float(input())
shield_cena = float(input())
armor_cena = float(input())
helmet = 0
sword = 0
shield = 0
armor = 0
for i in range(1, losts + 1):
    if i % 2 == 0:
        helmet += 1
    if i % 3 == 0:
        sword += 1
        if i % 2 == 0:
            shield += 1
            if shield % 2 == 0:
                armor += 1

cena = helmet * helmet_cena + sword_cena * sword + shield_cena * shield + armor_cena * armor
print(f'Gladiator expenses: {cena:.2f} aureus')