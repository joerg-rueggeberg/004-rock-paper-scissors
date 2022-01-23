import random

stein = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

papier = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

schere = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

waffen = ["stein", "papier", "schere"]
waffe_cpu = waffen[random.randint(0, 2)]

print("##################################"
      "\nSTEIN PAPIER SCHERE - Best of One"
      "\nBesiege den Computer!"
      "\n##################################\n")

waffe = input("Triff deine Auswahl (Stein/ Papier/ Schere): ").lower()

print(f"\nDER KAMPF BEGINNT:\n\nSpieler wählt: {waffe}")

# SPIELER WÄHLT STEIN
if waffe == "stein":
    print(stein)
    if waffe_cpu == waffen[0]:
        print(f"\nCPU wählt stein {stein}")
        print(f"SPANNEND! Beide haben {waffe_cpu} gewählt. Ein unentschieden!")
    elif waffe_cpu == waffen[1]:
        print(f"\nCPU wählt papier {papier}")
        print(f"SCHADE SPIELER! {waffe_cpu} schlägt {waffe}. Du hast verloren!")
    else:
        print(f"\nCPU wählt schere {schere}")
        print(f"GLÜCKWUNSCH SPIELER! {waffe} schlägt {waffe_cpu}. Du hast gewonnen!")

# SPIELER WÄHLT PAPIER
elif waffe == "papier":
    print(papier)
    if waffe_cpu == waffen[0]:
        print(f"\nCPU wählt stein {stein}")
        print(f"GLÜCKWUNSCH SPIELER! {waffe} schlägt {waffe_cpu}. Du hast gewonnen!")
    elif waffe_cpu == waffen[1]:
        print(f"\nCPU wählt papier {papier}")
        print(f"SPANNEND! Beide haben {waffe_cpu} gewählt. Ein unentschieden!")
    else:
        print(f"\nCPU wählt schere {schere}")
        print(f"SCHADE SPIELER! {waffe_cpu} schlägt {waffe}. Du hast verloren!")

# SPIELER WÄHLT SCHERE
elif waffe == "schere":
    print(schere)
    if waffe_cpu == waffen[0]:
        print(f"\nCPU wählt stein {stein}")
        print(f"SCHADE SPIELER! {waffe_cpu} schlägt {waffe}. Du hast verloren!")
    elif waffe_cpu == waffen[1]:
        print(f"\nCPU wählt papier {papier}")
        print(f"GLÜCKWUNSCH SPIELER! {waffe} schlägt {waffe_cpu}. Du hast gewonnen!")
    else:
        print(f"\nCPU wählt schere {schere}")
        print(f"SPANNEND! Beide haben {waffe_cpu} gewählt. Ein unentschieden!")
else:
    print("Falsche Eingabe!")
