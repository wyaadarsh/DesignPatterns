# Example: Creating Exact Copy of Resources - Google docs sharing
# Basically: more than one independent copy of the same rewsource

# the Prototype pattern is just a clone() function that accepts an object as
# an input parameter and returns a clone of it

# Example: Copying Music / VFX tools
# Exmaple: Different Editions of book with many similarities but differences only at some points. - clone and work


# Prototype comes in handy is when we want to duplicate a
# complex object. By duplicating a complex object, we can think of an object that is
# populated from a database and has references to other objects that are also populated
# from a database. It is a lot of effort to create an object clone by querying the
# database(s) multiple times again. Using Prototype for such cases is more convenient.


# Using shallow copies might be worthwhile if
# the available resources are limited (such as embedded systems) or performance is
# critical (such as high-performance computing)

