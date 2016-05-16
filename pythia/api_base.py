import requests
import os

class ApiBase(object):
    _id = None
    api_base = None

    def __init__(self, api_base, _id=None):
        self.api_base = api_base

        self.check_api_compatibility()

        if not _id:
            self._create_resource()
        else:
            self._id = _id
            self._fetch_self()

    def _fetch_self(self):
        res = requests.get(self._resource_path())
        d = res.json()

        for f in self._attributes:
            _f = f.replace('_', '')

            if _f in d:
                setattr(self, f, d[_f])

    def _update_self(self, payload):
        res = requests.put(self._resource_path(), data=payload)

    def _create_resource(self):
        res = requests.post(self._resource_path())
        d = res.json()

        self._id = d['_id']

        for f in self._attributes:
            _f = f.replace('_', '')

            if _f in d:
                setattr(self, f, d[_f])

    def _join_url(self, *args):
        """
        Joins an arbritary number of URI fragments

        @param one or more URI fragments that ought to be joined with a single slash in
        between

        @returns joined URI
        """
        return os.path.join(*args)

    def check_api_compatibility(self):
        res = requests.get(self.api_base)
        assert("v1" in res.text)

    def _resource_path(self):
        """
        Returns the full path where the resource can be accessed via the API.
        """
        raise NotImplementedError()
