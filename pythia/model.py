import requests
import urlparse

from api_base import ApiBase

class Model(ApiBase):
    experiment_id = None
    _attributes = ['_hyperparameter', '_name', '_description', 'date_added']
    measurements = []

    @property
    def hyperparameters(self):
        return self._hyperparameters

    @property
    def name(self):
        return self._name

    @property
    def description(self):
        return self._description

    @hyperparameters.setter
    def description(self, value):
        if value:
            self._hyperparameters = value
            self.update

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

    def __init__(self, api_base, experiment_id, _id=None):
        self.experiment_id = experiment_id
        ApiBase.__init__(self, api_base, _id=_id)

    def _resource_path(self):
        assert(self.experiment_id)
        return self._join_url(self.api_base, 'experiment', self.experiment_id,
            'model', self._id or '')

    def add_metric(self, name, value, epoch=0, step=0):
        """
        Adds measurement point to the model.

        @param name name of metric
        @param value value of respective metric
        @param epoch respective epoch of the measurement point
        @param step respective step of the measurement point
        """
        url = self._join_url(self._resource_path(), 'measurements')
        res = requests.put(url, data={
            'name': name,
            'value': value,
            'epoch': epoch,
            'step': step
        })

        self.measurements.push(res.json())
