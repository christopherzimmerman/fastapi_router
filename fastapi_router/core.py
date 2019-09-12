# -*- coding: utf-8 -*-
"""
    core
    ~~~~~
    Tests helper functions
    :copyright: 2019 Chris Zimmerman
    :license: BSD-3-Clause
"""
import os

from trimport import FunctionPath
from trimport import FunctionPathFactory
from trimport.helpers import _find_files_from_path

from .helpers import _convert_path_to_route


class FastRoute(FunctionPath):
    """
    Turns functions into valid calls
    to a FastAPI
    """
    def __init___(self, filename, base_path, allowed_methods=None):
        super().__init__(filename, base_path, allowed_methods)

    @property
    def route_url(self):
        return _convert_path_to_route(self.clipped_path)


class FastRouter(FunctionPathFactory):
    """
    Takes a directory structure and converts
    it into valid routes for a FastAPI instance
    """
    def __init__(self, path, route_params=None):
        super().__init__(path, route_params)

    @property
    def norm_path(self):
        """standardized path to make switching
        between OS's easier.  Used for computing
        route names and removing the path from
        files
        Returns
        -------
        n : normalized path string
        """
        return os.path.normpath(self._path)

    def _compute_structure(self, allowed_methods=None):
        """uses a helper function to find files
        from a given path.  Currently uses glob
        in virtually a one line function, but in
        case that implementation changes it's easier
        to wrap it here
        Returns
        -------
        m : [BaseRoute] -- List of base routes for each found file
        """
        return [
            FastRoute(file, self.norm_path, allowed_methods)
            for file in _find_files_from_path(self.norm_path)
        ]

    def register_routes(self, app):
        for path in self.function_paths:
            for method, endpoint in path.methods.items():
                app.add_api_route(path.route_url, endpoint, methods=[method])