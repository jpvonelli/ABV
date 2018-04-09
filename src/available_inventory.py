
def make_subset(item):
    return {key: item[key] for key in ['name', 'size', 'category', 'price', 'quantity', ]}


class InventoryQueries:

    def __init__(self, inventory):
        self.inventory = inventory

    def get_available_inventory(self):
        historic_inventory = self.inventory.get_historic_inventory()
        return [make_subset(item) for item in historic_inventory if item['quantity'] > 0]
