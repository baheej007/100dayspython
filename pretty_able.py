from prettytable import PrettyTable
table=PrettyTable()
table.add_column("Pokeman name",["pikachu","squirtle","charmander"])
table.add_column("Type",["electric","water","fire"])
table.add_column("colour",["yellow","violet","red"])


print(table[1])