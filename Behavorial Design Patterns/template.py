# The Strategy pattern promotes using multiple algorithms to solve a problem. Its
# killer feature is that it makes it possible to switch algorithms at runtime transparently
# (the client code is unaware of the change)

# The code duplication elimination happens using action/hook methods/
# functions, which are first-class citizens in Python. We saw an actual example of code
# refactoring using the Template pattern with the BFS and DFS algorithms.

# The Template design pattern focuses on eliminating code repetition. If we notice that
# there is repeatable code in algorithms that have structural similarities, we can keep
# the invariant (common) parts of the algorithms in a template method/function and
# move the variant (different) parts in action/hook methods/functions

# Pagination is a good use case to use Template. A pagination algorithm can be split
# into an abstract (invariant) part and a concrete (variant) part. The invariant part takes
# care of things such as the maximum number of lines/page. The variant part contains
# functionality to show the header and footer of a specific page that is paginated
