stuff = {'rope': 1, 'torth': 6, 'gold coin': 42, 'dagger':1, 'arrow':12}

import pprint

def displayInventory(inventory):
    print("inventory: ")
    item_total = 0
    for k, v in inventory.items():
        item_total = item_total + v
        print(str(v) + '  ' + str(k))
    print("Total number of items: " +  str(item_total))

displayInventory(stuff)

