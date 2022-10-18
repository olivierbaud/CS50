class Jar:
    def __init__(self, capacity=12):
        if int(capacity)<0:
            raise ValueError("Must be a positive integer")
        self.capacity = capacity
        self.size = 0

    def __str__(self):
        cookies = ""
        for _ in range(self.size):
            cookies += "🍪"
        return cookies

    def deposit(self, n):
        if self.size + n > self.capacity:
            raise ValueError("not enough capacity")
        self.size += n

    def withdraw(self, n):
        if self.size - n < 0:
            raise ValueError("there is not enough cookies")
        self.size -= n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size

    @capacity.setter
    def capacity(self, capacity):
        self._capacity = capacity

    @size.setter
    def size(self, size):
        self._size = size

def main():
    test = Jar(15)
    test.deposit(15)
    test.withdraw(10)
    print(test)
    print(test.capacity)


if __name__ == "__main__":
    main()