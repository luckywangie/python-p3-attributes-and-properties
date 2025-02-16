import sys

class Dog:
    approved_breeds = ["Mastiff", "Chihuahua", "Corgi", "Shar Pei", "Beagle", "French Bulldog", "Pug", "Pointer"]

    def __init__(self, name="Unknown", breed=None):
        self._name = "Unknown"
        self._breed = "Unknown"

        self.name = name  # Calls the setter
        if breed is not None:
            self.breed = breed  # Calls the setter only if breed is provided

    def get_name(self):
        return self._name

    def set_name(self, name):
        if isinstance(name, str) and 1 <= len(name) <= 25:
            self._name = name
        else:
            print("Name must be string between 1 and 25 characters.", file=sys.stdout)
            self._name = "Unknown"  # Ensures the attribute has a valid default value

    def get_breed(self):
        return self._breed

    def set_breed(self, breed):
        if breed in Dog.approved_breeds:
            self._breed = breed
        else:
            print("Breed must be in list of approved breeds.", file=sys.stdout)
            self._breed = "Unknown"  # Ensures the attribute has a valid default value

    name = property(get_name, set_name)
    breed = property(get_breed, set_breed)


# ✅ Test the class
if __name__ == "__main__":
    dog1 = Dog(name="Buddy", breed="Beagle")
    print(dog1.name)  # Output: Buddy
    print(dog1.breed)  # Output: Beagle

    dog1.name = "Max"
    print(dog1.name)  # Output: Max

    dog1.name = ""  # Output: Name must be string between 1 and 25 characters.
    print(dog1.name)  # Output: Unknown (Default Value)

    dog1.breed = "Corgi"
    print(dog1.breed)  # Output: Corgi

    dog1.breed = "Golden Retriever"  # Output: Breed must be in list of approved breeds.
    print(dog1.breed)  # Output: Unknown (Default Value)