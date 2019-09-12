"""
Basic usage example of registering routes
from a file structure to valid flask api routes.

The following file uses the directory structure defined
in routes to create a very simple endpoint with two routes:

/api/
/api/<variable>

It supports GET requests on both endpoints

GET /api/ will return "Welcome to the Base API path"

GET /api/<variable> will return "The variable is <variable>"
"""

import os

from fastapi import FastAPI
from fastapi_router import FastRouter

app = FastAPI()

route_dir = os.path.dirname(os.path.realpath(__file__)) + "/routes/"
router = FastRouter(route_dir)

router.register_routes(app)
