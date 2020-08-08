# Types :

# A remote proxy, which acts as the local representation of an object that really
# exists in a different address space (for example, a network server). Ex: Bank Cheque

# A virtual proxy, which uses lazy initialization to defer the creation of a
# computationally expensive object until the moment it is actually needed.

# A protection/protective proxy, which controls access to a sensitive object. Ex: ATM Pin

# A smart (reference) proxy, which performs extra actions when an
# object is accessed. Examples of such actions are reference counting
# and thread-safety checks


# Virtual Proxy

# LazyProperty is a descriptor
class LazyProperty:
    # Descriptors are
    # the recommended mechanism to use in Python to override the default behavior
    # of its attribute access methods: __get__(), __set__(), and __delete__()
    def __init__(self, method):
        self.method = method
        self.method_name = method.__name__
        print('function overriden: {}'.format(self.method))
        print("function's name: {}".format(self.method_name))

    def __get__(self, obj, cls):
        # only initializes once
        if not obj:
            return None
        value = self.method(obj)
        print('value {}'.format(value))
        setattr(obj, self.method_name, value)
        return value


class Test:
    def __init__(self):
        self.x = 'foo'
        self.y = 'bar'
        self._resource = None  # lAZY lOAD

    @LazyProperty
    def resource(self):
        # Only initialized once
        print('initializing self._resource which is:{}'.format(self._resource))
        self._resource = tuple(range(5))  # expensive
        return self._resource


def main():
    t = Test()
    print(t.x)
    print(t.y)
    # do more work...
    print(t.resource)
    print(t.resource)


if __name__ == "__main__":
    main()
