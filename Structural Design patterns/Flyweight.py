# Object-oriented systems can face performance issues due to the overhead of object
# creation. Performance issues usually appear in embedded systems

# Graphics software, including computer games, should be able to render 3D information (for example,
# a forest with thousands of trees or a village full of soldiers) extremely fast. If each
# object of a 3D terrain is created individually and no data sharing is used, the
# performance will be prohibitive

# A Flyweight is a shared object that contains state-independent, immutable
# (also known as intrinsic) data. The state-dependent, mutable (also known as
# extrinsic) data should not be part of Flyweight because this is information that
# cannot be shared since it differs per object

# In general we use Flyweight when an application needs to create a large number of
# computationally expensive objects that share many properties

# The application needs to use a large number of objects.

# There are so many objects that it's too expensive to store/render them. Once
# the mutable state is removed (because if it is required, it should be passed
# explicitly to Flyweight by the client code), many groups of distinct objects
# can be replaced by relatively few shared objects.

# Object identity is not important for the application. We cannot rely on object
# identity because object sharing causes identity comparisons to fail (objects
# that appear different to the client code, end up having the same identity).

# Before diving into the code, let's spend a moment to note the difference between
# memoization and the Flyweight pattern. Memoization is an optimization technique
# that uses a cache to avoid recomputing results that were already computed in an
# earlier execution step. Memoization does not focus on a specific programming
# paradigm such as object-oriented programming (OOP). In Python, memoization
# can be applied on both methods and simple functions. Flyweight is an OOP-specific
# optimization design pattern that focuses on sharing object data.


import random
from enum import Enum

TreeType = Enum('TreeType', 'apple_tree cherry_tree peach_tree')


class Tree:
    pool = dict()

    # called before init
    def __new__(cls, tree_type):
        obj = cls.pool.get(tree_type, None)
        if not obj:
            obj = object.__new__(cls)
            cls.pool[tree_type] = obj
            obj.tree_type = tree_type
        return obj

    def render(self, age, x, y):
        print('render a tree of type {} and age {} at ({},{})'.format(self.tree_type, age, x, y))


def main():
    rnd = random.Random()
    age_min, age_max = 1, 30  # in years
    min_point, max_point = 0, 100
    tree_counter = 0
    for _ in range(10):
        t1 = Tree(TreeType.apple_tree)
        t1.render(rnd.randint(age_min, age_max),
                  rnd.randint(min_point, max_point),
                  rnd.randint(min_point, max_point))
        tree_counter += 1
    for _ in range(3):
        t2 = Tree(TreeType.cherry_tree)
        t2.render(rnd.randint(age_min, age_max),
                  rnd.randint(min_point, max_point),
                  rnd.randint(min_point, max_point))
        tree_counter += 1
    for _ in range(5):
        t3 = Tree(TreeType.peach_tree)
        t3.render(rnd.randint(age_min, age_max),
                  rnd.randint(min_point, max_point),
                  rnd.randint(min_point, max_point))
        tree_counter += 1
    print('trees rendered: {}'.format(tree_counter))
    print('trees actually created: {}'.format(len(Tree.pool)))
    t4 = Tree(TreeType.cherry_tree)
    t5 = Tree(TreeType.cherry_tree)
    t6 = Tree(TreeType.apple_tree)
    print('{} == {}? {}'.format(id(t4), id(t5), id(t4) == id(t5)))
    print('{} == {}? {}'.format(id(t5), id(t6), id(t5) == id(t6)))


if __name__ == '__main__':
    main()
