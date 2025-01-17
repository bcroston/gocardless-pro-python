# WARNING: Do not edit by hand, this file was generated by Crank:
#
#   https://github.com/gocardless/crank
#

from . import base_service
from .. import resources
from ..paginator import Paginator
from .. import errors

class PayerAuthorisationsService(base_service.BaseService):
    """Service class that provides access to the payer_authorisations
    endpoints of the GoCardless Pro API.
    """

    RESOURCE_CLASS = resources.PayerAuthorisation
    RESOURCE_NAME = 'payer_authorisations'


    def get(self,identity,params=None, headers=None):
        """Get a single Payer Authorisation.

        Retrieves the details of a single existing Payer Authorisation. It can
        be used for polling the status of a Payer Authorisation.

        Args:
              identity (string): Unique identifier, beginning with "PA".
              params (dict, optional): Query string parameters.

        Returns:
              PayerAuthorisation
        """
        path = self._sub_url_params('/payer_authorisations/:identity', {
          
            'identity': identity,
          })
        

        response = self._perform_request('GET', path, params, headers,
                                         retry_failures=True)
        return self._resource_for(response)
  

    def create(self,params=None, headers=None):
        """Create a Payer Authorisation.

        Creates a Payer Authorisation. The resource is saved to the database
        even if incomplete. An empty array of incomplete_fields means that the
        resource is valid. The ID of the resource is used for the other
        actions. This endpoint has been designed this way so you do not need to
        save any payer data on your servers or the browser while still being
        able to implement a progressive solution, such as a multi-step form.

        Args:
              params (dict, optional): Request body.

        Returns:
              PayerAuthorisation
        """
        path = '/payer_authorisations'
        
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
  

    def update(self,identity,params=None, headers=None):
        """Update a Payer Authorisation.

        Updates a Payer Authorisation. Updates the Payer Authorisation with the
        request data. Can be invoked as many times as needed. Only fields
        present in the request will be modified. An empty array of
        incomplete_fields means that the resource is valid. This endpoint has
        been designed this way so you do not need to save any payer data on
        your servers or the browser while still being able to implement a
        progressive solution, such a multi-step form. <p class="notice"> Note
        that in order to update the `metadata` attribute values it must be sent
        completely as it overrides the previously existing values. </p>

        Args:
              identity (string): Unique identifier, beginning with "PA".
              params (dict, optional): Request body.

        Returns:
              PayerAuthorisation
        """
        path = self._sub_url_params('/payer_authorisations/:identity', {
          
            'identity': identity,
          })
        
        if params is not None:
            params = {self._envelope_key(): params}

        response = self._perform_request('PUT', path, params, headers,
                                         retry_failures=True)
        return self._resource_for(response)
  

    def submit(self,identity,params=None, headers=None):
        """Submit a Payer Authorisation.

        Submits all the data previously pushed to this PayerAuthorisation for
        verification. This time, a 200 HTTP status is returned if the resource
        is valid and a 422 error response in case of validation errors. After
        it is successfully submitted, the Payer Authorisation can no longer be
        edited.

        Args:
              identity (string): Unique identifier, beginning with "PA".
              params (dict, optional): Request body.

        Returns:
              PayerAuthorisation
        """
        path = self._sub_url_params('/payer_authorisations/:identity/actions/submit', {
          
            'identity': identity,
          })
        
        if params is not None:
            params = {'data': params}
        response = self._perform_request('POST', path, params, headers,
                                         retry_failures=False)
        return self._resource_for(response)
  

    def confirm(self,identity,params=None, headers=None):
        """Confirm a Payer Authorisation.

        Confirms the Payer Authorisation, indicating that the resources are
        ready to be created.
        A Payer Authorisation cannot be confirmed if it hasn't been submitted
        yet.
        
        <p class="notice">
          The main use of the confirm endpoint is to enable integrators to
        acknowledge the end of the setup process. 
          They might want to make the payers go through some other steps after
        they go through our flow or make them go through the necessary
        verification mechanism (upcoming feature).
        </p>

        Args:
              identity (string): Unique identifier, beginning with "PA".
              params (dict, optional): Request body.

        Returns:
              PayerAuthorisation
        """
        path = self._sub_url_params('/payer_authorisations/:identity/actions/confirm', {
          
            'identity': identity,
          })
        
        if params is not None:
            params = {'data': params}
        response = self._perform_request('POST', path, params, headers,
                                         retry_failures=False)
        return self._resource_for(response)
  
