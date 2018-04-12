class AvailabilityFilter:
    def __init__(self, subfilter, quantity_requested):
        self.subfilter = subfilter
        self.quantity_requested = quantity_requested

    def is_match(self, beer):
        available = beer.quantity
        if available <= 0 or available < self.quantity_requested:
            return False
        return self.subfilter.is_match(beer)
