# WARNING: Do not edit by hand, this file was generated by Crank:
#
#   https://github.com/gocardless/crank
#

from . import base_service
from .. import resources
from ..paginator import Paginator

class SubscriptionsService(base_service.BaseService):
    """Service class that provides access to the subscriptions
    endpoints of the GoCardless Pro API.
    """

    RESOURCE_CLASS = resources.Subscription
    RESOURCE_NAME = 'subscriptions'

    def create(self, params=None, headers=None):
        """Create a subscription.

        Creates a new subscription object

        Args:
          params (dict, optional): Request body.

        Returns:
          Subscription
        """
        path = '/subscriptions'
        if params is not None:
            params = {self._envelope_key(): params}
        response = self._perform_request('POST', path, params, headers)
        return self._resource_for(response)

    def list(self, params=None, headers=None):
        """List subscriptions.

        Returns a [cursor-paginated](#api-usage-cursor-pagination) list of your
        subscriptions.

        Args:
          params (dict, optional): Query string parameters.

        Returns:
          ListResponse of Subscription instances
        """
        path = '/subscriptions'
        response = self._perform_request('GET', path, params, headers)
        return self._resource_for(response)

    def all(self, params=None):
        if params is None:
            params = {}
        return Paginator(self, params)

    def get(self, identity, params=None, headers=None):
        """Get a single subscription.

        Retrieves the details of a single subscription.

        Args:
          identity (string): Unique identifier, beginning with "SB".
          params (dict, optional): Query string parameters.

        Returns:
          Subscription
        """
        path = self._sub_url_params('/subscriptions/:identity', {
            'identity': identity,
        })
        response = self._perform_request('GET', path, params, headers)
        return self._resource_for(response)

    def update(self, identity, params=None, headers=None):
        """Update a subscription.

        Updates a subscription object.

        Args:
          identity (string): Unique identifier, beginning with "SB".
          params (dict, optional): Request body.

        Returns:
          Subscription
        """
        path = self._sub_url_params('/subscriptions/:identity', {
            'identity': identity,
        })
        if params is not None:
            params = {self._envelope_key(): params}
        response = self._perform_request('PUT', path, params, headers)
        return self._resource_for(response)

    def cancel(self, identity, params=None, headers=None):
        """Cancel a subscription.

        Immediately cancels a subscription; no more payments will be created
        under it. Any metadata supplied to this endpoint will be stored on the
        payment cancellation event it causes.
        
        This will fail
        with a cancellation_failed error if the subscription is already
        cancelled or finished.

        Args:
          identity (string): Unique identifier, beginning with "SB".
          params (dict, optional): Request body.

        Returns:
          Subscription
        """
        path = self._sub_url_params('/subscriptions/:identity/actions/cancel', {
            'identity': identity,
        })
        if params is not None:
            params = {'data': params}
        response = self._perform_request('POST', path, params, headers)
        return self._resource_for(response)

