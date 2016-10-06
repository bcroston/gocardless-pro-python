# WARNING: Do not edit by hand, this file was generated by Crank:
#
#   https://github.com/gocardless/crank
#

from . import base_service
from .. import resources
from ..paginator import Paginator

class RefundsService(base_service.BaseService):
    """Service class that provides access to the refunds
    endpoints of the GoCardless Pro API.
    """

    RESOURCE_CLASS = resources.Refund
    RESOURCE_NAME = 'refunds'

    def create(self, params=None, headers=None):
        """Create a refund.

        Creates a new refund object.
        
        This fails with:<a
        name="refund_payment_invalid_state"></a><a
        name="total_amount_confirmation_invalid"></a><a
        name="number_of_refunds_exceeded"></a>
        
        -
        `refund_payment_invalid_state` error if the linked
        [payment](#core-endpoints-payments) isn't either `confirmed` or
        `paid_out`.
        
        - `total_amount_confirmation_invalid` if
        the confirmation amount doesn't match the total amount refunded for the
        payment. This safeguard is there to prevent two processes from creating
        refunds without awareness of each other.
        
        -
        `number_of_refunds_exceeded` if five or more refunds have already been
        created against the payment.
        

        Args:
          params (dict, optional): Request body.

        Returns:
          Refund
        """
        path = '/refunds'
        if params is not None:
            params = {self._envelope_key(): params}
        response = self._perform_request('POST', path, params, headers)
        return self._resource_for(response)

    def list(self, params=None, headers=None):
        """List refunds.

        Returns a [cursor-paginated](#api-usage-cursor-pagination) list of your
        refunds.

        Args:
          params (dict, optional): Query string parameters.

        Returns:
          ListResponse of Refund instances
        """
        path = '/refunds'
        response = self._perform_request('GET', path, params, headers)
        return self._resource_for(response)

    def all(self, params=None):
        if params is None:
            params = {}
        return Paginator(self, params)

    def get(self, identity, params=None, headers=None):
        """Get a single refund.

        Retrieves all details for a single refund

        Args:
          identity (string): Unique identifier, beginning with "RF".
          params (dict, optional): Query string parameters.

        Returns:
          Refund
        """
        path = self._sub_url_params('/refunds/:identity', {
            'identity': identity,
        })
        response = self._perform_request('GET', path, params, headers)
        return self._resource_for(response)

    def update(self, identity, params=None, headers=None):
        """Update a refund.

        Updates a refund object.

        Args:
          identity (string): Unique identifier, beginning with "RF".
          params (dict, optional): Request body.

        Returns:
          Refund
        """
        path = self._sub_url_params('/refunds/:identity', {
            'identity': identity,
        })
        if params is not None:
            params = {self._envelope_key(): params}
        response = self._perform_request('PUT', path, params, headers)
        return self._resource_for(response)

