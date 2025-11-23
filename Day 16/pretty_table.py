from prettytable import PrettyTable

table = PrettyTable()

table.add_column('Pokemon Name', ['Pikachu','Charizard','Squirtle','Charmander'],)
table.add_column('Type', ['Electric','Fire-Flying','Water','Fire'])
# table.add_divider()
table.align='l'
print(table)














