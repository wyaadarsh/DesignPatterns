import xml.etree.ElementTree as etree
import json


# Non Factory Approach
class A(object):
    def __init__(self):
        print("Created Object of A")


# factory Approach
class JSONConnector:
    def __init__(self, filepath):
        self.data = dict()
        with open(filepath, mode='r') as f:
            self.data = json.load(f)

    @property
    def parsed_data(self):
        return self.data


class XMLConnector:
    def __init__(self, filepath):
        self.tree = etree.parse(filepath)

    @property
    def parsed_data(self):
        return self.tree


def connection_factory(filepath):
    if filepath.endswith('json'):
        connector = JSONConnector
    elif filepath.endswith('xml'):
        connector = XMLConnector
    else:
        raise ValueError('Cannot connect to {}'.format(filepath))
    return connector(filepath)


def connect_to(filepath):
    factory = None
    try:
        factory = connection_factory(filepath)
    except ValueError as ve:
        print(ve)
    return factory


if __name__ == "__main__":
    # a = A()
    # b = A()
    # print(id(a))
    # print(id(b))

    def main():
        sqlite_factory = connect_to('text.json')
        print(sqlite_factory.parsed_data)
        xml_factory = connect_to("text.xml")
        xml_data = xml_factory.parsed_data
    main()
