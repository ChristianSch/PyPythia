import requests
import os


class ApiBase(object):
    """
    This class provides the basis for every remote entity. The resource simply
    specifies its ``attributes`` and path, as well as provides setters for the
    attributes.

    It might also provide custom methods as well as a custom initiator. It is
    mandatory that the inheriting entity calls this class's init method as
    well::

        ApiBase.__init__(self, api_base, _id=_id)
    """
    _id = None
    api_base = None

    def __init__(self, api_base, _id=None):
        """
        Creates a new entitiy. If ``_id`` is provided, an already existing
        remote entity is fetched, otherwise a new one is created.

        :param api_base: URI to the Pythia API instance
        :param _id: if given, attempts to fetch an already existing model.
        """
        self.api_base = api_base

        # init attributes to prevent "no such attribute" errors.
        for a in self._attributes:
            setattr(self, a, None)

        self.check_api_compatibility()

        if not _id:
            self._create_resource()
        else:
            self._id = _id
            self._fetch_self()

    def _fetch_self(self):
        """
        Fetches the resource from the remote and sets all fields which are
        returned to synch the object with the remote.
        """
        res = requests.get(self._resource_path())
        res.raise_for_status
        data = res.json()

        assert '_id' in data, 'Invalid _id'

        for attribute in self._attributes:
            if attribute.startswith('_'):
                _attribute = attribute[1:]
            else:
                _attribute = attribute

            if _attribute in data:
                setattr(self, attribute, data[_attribute])

    def _update_self(self, payload):
        """
        Sends all current attribute values to the remote.
        """
        res = requests.put(self._resource_path(), data=payload)

    def _create_resource(self):
        """
        Creates the resource on the remote. The remote returns a dict with
        the initial/sent fields, which, if in ``_attributes`` listed, are set
        for the current object, thus synched with the remote.
        """
        res = requests.post(self._resource_path())
        res.raise_for_status
        data = res.json()

        assert '_id' in data, 'Remote entity could not be registered'
        self._id = data['_id']

        for attribute in self._attributes:
            if attribute.startswith('_'):
                _attribute = attribute[1:]
            else:
                _attribute = attribute

            if _attribute in data:
                setattr(self, attribute, data[_attribute])

    def _join_url(self, *args):
        """
        Joins an arbritary number of URI fragments

        :param: One or more URI fragments that ought to be joined with a single
        slash in between

        :return: Joined URI
        """
        return os.path.join(*args)

    def check_api_compatibility(self):
        """
        Checks the API version to guarantee compatibility.
        """
        res = requests.get(self.api_base)
        assert "v1" in res.text, "incompatible or missing API version"

    def _resource_path(self):
        """
        Returns the full path where the resource can be accessed via the API.
        """
        raise NotImplementedError()
