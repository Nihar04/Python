class Address:
    def __init__(self, street, city, state, zipcode, street2=''):
        self.street = street
        self.city = city
        self.state = state
        self.zipcode = zipcode
        self.street2 = street2

    def __str__(self):
        lines = [self.street]
        if self.street2:
            lines.append(self.street2)
        lines.append(f'{self.city}, {self.street}, {self.zipcode}')
        return '\n'.join(lines)
