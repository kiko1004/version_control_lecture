class Human:
    def __init__(
            self,
            first_name,
            last_name
    ):
        self.first_name = first_name
        self.last_name = last_name

    def greet(self):
        print(f"Hi! I am {self.first_name}!")

if __name__ == "__main__":
    h1 = Human("Ivan", "Petrov")
    h1.greet()
