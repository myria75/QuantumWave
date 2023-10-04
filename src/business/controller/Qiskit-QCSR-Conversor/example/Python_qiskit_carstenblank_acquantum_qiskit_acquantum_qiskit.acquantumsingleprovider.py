#  Copyright (c) 2019.  Carsten Blank
# 
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
# 
#       http://www.apache.org/licenses/LICENSE-2.0
# 
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.

from collections import OrderedDict, _OrderedDictItemsView

from acquantumconnector.connector.acquantumconnector import AcQuantumConnector
from acquantumconnector.credentials.credentials import AcQuantumCredentials
from jsonschema import ValidationError
from qiskit.providers import BaseProvider

from .acquantumbackend import AcQuantumBackend
from .backendconfiguration import AcQuantumBackendConfiguration


class AcQuantumSingleProvider(BaseProvider):

    def __init__(self, credentials, provider):
        # type: (AcQuantumCredentials, 'AcQuantumProvider') -> None
        super().__init__()

        self._ac_provider = provider
        self.credentials = credentials  # type: AcQuantumCredentials
        self._api = self._authenticate(self.credentials)  # type: AcQuantumConnector

        self._backends = self._discover_remote_backends()

    def backends(self, name=None, **kwargs):
        # type: (str, dict) -> _OrderedDictItemsView
        """
        :param name:  name of backends
        :param kwargs:
        :return:
        """
        backends = self._backends.items()
        if name:
            backends = [b for n, b in backends if n == name]

        return backends

    def _discover_remote_backends(self):
        # type: () -> OrderedDict[str, AcQuantumBackend]

        ret = OrderedDict()
        configs_list = self._api.available_backends()

        for raw_config in configs_list:
            try:
                config = AcQuantumBackendConfiguration.from_dict(raw_config)
                ret[config.backend_name] = AcQuantumBackend(
                    configuration=config,
                    provider=self._ac_provider,
                    credentials=self.credentials,
                    api=self._api)
            except ValidationError as ex:
                print(
                    'Remote backend {} could not be instantiated due to an invalid config: {}'.format(
                        raw_config.get('backend_name', raw_config.get('name', 'unknown')), ex)
                )

        return ret

    @classmethod
    def _authenticate(cls, credentials):
        # type: (AcQuantumCredentials) -> AcQuantumConnector
        connector = AcQuantumConnector()
        connector.create_session(credentials)
        return connector
