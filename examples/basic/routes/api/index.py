"""
This is an index file, here you define the base methods for a route,
the index, unlike other files, does not get added to the route, so
the proper route for this file would be /api/, not /api/index.

In this file, like all other files, you can define all RESTful methods
that flask supports
"""


def get():
    return "Welcome to the Base API path"
