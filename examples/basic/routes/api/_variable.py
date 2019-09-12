"""
This is a variable file.  This route will get converted into
a route parameter, in this case producing the route:

/api/<variable>/ which will be passed to all RESTfull methods
that this function supports.  You are *not* required to pass
it in for all methods, it will be ignored if you leave it out
"""


def get(variable):
    return {"variable": variable}
