#!/usr/bin/env python3
""" Index views
"""
from flask import jsonify, abort
from api.v1.views import app_views


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status() -> str:
    """ GET /api/v1/status
    Return:
      - the API statue
    """
    return jsonify({"status": "OK"})


@app_views.route('/stats/', strict_slashes=False)
def stats() -> str:
    """ GET /api/v1/stats
    Return:
      - the numb of each objects
    """
    from models.user import User
    stats = {}
    stats['users'] = User.count()
    return jsonify(stats)


@app_views.route('/unauthorized', strict_slashes=False)
def unauthorized() -> str:
    """ GET /api/v1/unauthorized[/]
    Returns:
      -  error message
    """
    abort(401)


@app_views.route('/forbidden', strict_slashes=False)
def forbidden() -> str:
    """ GET /api/v1/forbidden[/]
    Returns:
      -  error message
    """
    abort(403)