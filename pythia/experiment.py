import requests
import urlparse

from api_base import ApiBase
from model import Model


class Experiment(ApiBase):
    _attributes = ['_name', '_description', 'date_added']

    @property
    def name(self):
        return self._name

    @property
    def description(self):
        return self._description

    @name.setter
    def name(self, value):
        if value:
            self._name = value
            self._update_self({
                'name': value
            })

    @description.setter
    def description(self, value):
        if value:
            self._description = value
            self._update_self({
                'description': value
            })

    def _resource_path(self):
        return self._join_url(self.api_base, 'experiment', self._id or '')

    def create_model(self, _id=None):
        return Model(self.api_base, self._id, _id=_id)

    def __str__(self):
        return self._name
