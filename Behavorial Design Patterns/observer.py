# Assume that we are using the data of the same model in two views, for
# instance in a pie chart and in a spreadsheet. Whenever the model is modified,
# both the views need to be updated

# update a group of objects when the state of another
# object changes

# Social Network, RSS feed, Event driven systems

#  implement a data formatter - ActiveState Python Observer code

# There
# is a default formatter that shows a value in the decimal format. However, we
# can add/register more formatters. In this example, we will add a hex and binary
# formatter.

# Observer is actually one of the patterns where inheritance makes sense.

class Publisher:
    def __init__(self):
        self.observers = []

    def add(self, observer):
        if observer not in self.observers:
            self.observers.append(observer)
        else:
            print('Failed to add: {}'.format(observer))

    def remove(self, observer):
        try:
            self.observers.remove(observer)
        except ValueError:
            print('Failed to remove: {}'.format(observer))

    def notify(self):
        [o.notify(self) for o in self.observers]


class DefaultFormatter(Publisher):
    def __init__(self, name):
        Publisher.__init__(self)
        self.name = name
        self._data = 0

    def __str__(self):
        return "{}: '{}' has data = {}".format(
            type(self).__name__,
            self.name,
            self._data
        )

    @property
    def data(self):
        return self._data

    # Important to set in this way.

    @data.setter
    def data(self, new_value):
        try:
            self._data = int(new_value)
        except ValueError as e:
            print('Error: {}'.format(e))
        else:
            self.notify()


class HexFormatter:
    def notify(self, publisher):
        print("{}: '{}' has now hex data = {}".format(type(self).__name__, publisher.name, hex(publisher.data)))


class BinaryFormatter:
    def notify(self, publisher):
        print("{}: '{}' has now bin data = {}".format(type(self).__name__, publisher.name, bin(publisher.data)))


def main():
    df = DefaultFormatter('test1')
    print(df)
    print()
    hf = HexFormatter()
    df.add(hf)
    df.data = 3
    print(df)
    print()
    bf = BinaryFormatter()
    df.add(bf)
    df.data = 21
    print(df)
    print()
    df.remove(hf)
    df.data = 40
    print(df)
    print()
    df.remove(hf)
    df.add(bf)
    df.data = 'hello'
    print(df)
    print()
    df.data = 15.8
    print(df)

if __name__ == "__main__":
    main()