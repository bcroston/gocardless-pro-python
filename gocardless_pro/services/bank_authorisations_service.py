# WARNING: Do not edit by hand, this file was generated by Crank:
#
#   https://github.com/gocardless/crank
#

from . import base_service
from .. import resources
from ..paginator import Paginator
from .. import errors

class BankAuthorisationsService(base_service.BaseService):
    """Service class that provides access to the bank_authorisations
    endpoints of the GoCardless Pro API.
    """

    RESOURCE_CLASS = resources.BankAuthorisation
    RESOURCE_NAME = 'bank_authorisations'


    def get(self,identity,params=None, headers=None):
        """Get a Bank Authorisation..

        Fetches a bank authorisation

        Args:
              identity (string): Unique identifier, beginning with "BAU".
              params (dict, optional): Query string parameters.

        Returns:
              BankAuthorisation
        """
        path = self._sub_url_params('/bank_authorisations/:identity', {
          
            'identity': identity,
          })
        

        response = self._perform_request('GET', path, params, headers,
                                         retry_failures=True)
        return self._resource_for(response)
  

    def create(self,params=None, headers=None):
        """Create a Bank Authorisation.

        Create a Bank Authorisation.

        Args:
              params (dict, optional): Request body.

        Returns:
              BankAuthorisation
        """
        path = '/bank_authorisations'
        
        if params is not None:
            params = {self._envelope_key(): params}

        try:
          response = self._perform_request('POST', path, params, headers,
                                            retry_failures=True)
        except errors.IdempotentCreationConflictError as err:
          if self.raise_on_idempotency_conflict:
            raise err
          return self.get(identity=err.conflicting_resource_id,
                          params=params,
                          headers=headers)
        return self._resource_for(response)
  
