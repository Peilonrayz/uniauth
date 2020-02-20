import urllib.parse

from flask import redirect, request

null = object()


# https://developers.google.com/identity/protocols/OAuth2#webserver
class Unify:
    def __init__(self):
        self._handlers = {}

    def auth(self, endpoint, **kwargs):
        if endpoint not in self._handlers:
            return '{"error": "endpoint not found"}', 404
        return self._handlers[endpoint].auth(**kwargs)

    def add_handler(self, handler):
        if handler.id is None:
            raise ValueError('Handler not properly configured')
        self._handlers[handler.id] = handler


class Handler:
    id = None

    @staticmethod
    def redirect(url, **query):
        url_parts = list(urllib.parse.urlparse(url))
        url_parts[4] = urllib.parse.urlencode({
            key: value
            for key, value in query.items()
            if value is not null
        })
        url = urllib.parse.urlunparse(url_parts)
        response = redirect(url)
        for attr in ('headers',):
            setattr(response, attr, getattr(request, attr))
        return response

    def auth(self, **_):
        raise NotImplemented('Function auth needs to be implemented in child object')
