'''
Find, install and publish Python packages with the Python Package Index:  https://pypi.org/

      Create a table
print("| Pokemon Name |")  # | Pokemon Name |
print("| Pokemon Name |")  # | Pokemon Name |           # etc.
print("___________________")  # ___________________'''


from prettytable import PrettyTable
table = PrettyTable()
table.add_column("pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])

print(table.align)  # {'pokemon Name': 'c', 'Type': 'c'}

print(table)# +--------------+----------+
            # | pokemon Name |   Type   |
            # +--------------+----------+
            # |   Pikachu    | Electric |
            # |   Squirtle   |  Water   |
            # |  Charmander  |   Fire   |
            # +--------------+----------+

table.align = "l"

print(table)#+--------------+----------+
            # | pokemon Name | Type     |
            # +--------------+----------+
            # | Pikachu      | Electric |
            # | Squirtle     | Water    |
            # | Charmander   | Fire     |
            # +--------------+----------+
