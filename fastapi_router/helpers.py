# -*- coding: utf-8 -*-
"""
    helpers
    ~~~~~
    Tests helper functions
    :copyright: 2019 Chris Zimmerman
    :license: BSD-3-Clause
"""
import os
import re


def _convert_path_to_route(clipped_path, index_name="index.py"):
    """
    Parameters
    ----------
    clipped_path : str
        api route with absolute path clipped
    index_name : str
        name of index files to remove.  This is not currently
        able to be altered through Router, but might be worth
        exposing to users eventually if they want to conform
        to a different name than index.py for their index files
    Returns
    -------
    r : str -- route url
    """
    swapped_slashes = clipped_path.replace(os.sep, "/")
    escaped_index = re.escape(index_name)
    rgx = "({})$".format(escaped_index)

    # steps to do stuff, probably can be optimized
    removed_index = re.sub(rgx, "", swapped_slashes)
    inner_links_formatted = re.sub(r"/_([^/]+)/", r"/{\1}/", removed_index)
    final_link_formatted = re.sub(r"/_(.*?).py$", r"/{\1}/", inner_links_formatted)

    remove_trailing_py = re.sub(r".py$", "/", final_link_formatted)

    return remove_trailing_py