def main():
    jar = Jar()
    jar.deposit(2)
    jar.withdraw(1)
    print(jar.capacity)
    print(jar.size)

class Jar:
    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError
        else:
            self._capacity = capacity
            self._size = 0

    def __str__(self):
        return("*" * self._size)

    def deposit(self, n):
        if (n + self.size) > self._capacity:
            raise ValueError
        else:
            self._size += n


    def withdraw(self, n):
        if (self._size - n) < 0:
            raise ValueError
        else:
            self._size -= n



    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size

main()