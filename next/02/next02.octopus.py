class Octopus:
    count_animals = 0

    def __init__(self, age, name='Octavio'):
        self._name = name
        self._age = age
        Octopus.count_animals += 1

    def birthday(self):
        self._age += 1

    def get_age(self):
        return self._age

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name


def main():
    octopus = Octopus(5, 'Octapocta')
    octopus2 = Octopus(3)
    octopus.birthday()
    print(octopus.get_age(), octopus2.get_age())
    print(octopus.get_name(), octopus2.get_name())
    octopus2.set_name('Octain')
    print(octopus.get_name(), octopus2.get_name())
    print(Octopus.count_animals)


if __name__ == '__main__':
    main()
