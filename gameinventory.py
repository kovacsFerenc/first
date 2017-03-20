

inv = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12} 



def display_inventory(inventory):
        print("Inventory: ")
        totalItems = 0
        for value, key in inventory.items():
            print (str(value) + ' ' + str(key))
            totalItems += key
        print ("Total number of your items: " + str(totalItems))

display_inventory(inv)



dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

def addToInventory(inventory, addedItems):
    new_inventory = dict(inventory)
    for item in addedItems:
        if item  in inventory:
            new_inventory[item] += 1
        else:
            new_inventory[item] = 1 
            
    return new_inventory


inv = addToInventory(inv, dragon_loot)

display_inventory(inv)


def print_table(inventory, order):
    listforvalues = list()
    listforkeys = list()
    for keys in inventory:
        listforvalues.append(inventory[keys])
        listforkeys.append(keys)

    print(listforvalues.rjust(40))



print_table(inv, "count,desc")
