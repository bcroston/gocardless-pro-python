# WARNING: Do not edit by hand, this file was generated by Crank:
#
#   https://github.com/gocardless/crank
#

import sys
import platform
try:
    import urllib.parse as urlparse
except ImportError:
    import urlparse
import json

import requests

from . import errors

class ApiClient(object):
    """Client for interacting with a JSON HTTP API, using OAuth2-style auth.

    Args:
      base_url (string): The prefix that's prepended to all request paths.
      access_token (string): Token used in the Authorization header.
    """

    def __init__(self, base_url, access_token):
        self.base_url = base_url
        self.access_token = access_token

    def get(self, path, params=None, headers=None):
        """Perform a GET request, optionally providing query-string params.

        Args:
          path (str): A path that gets appended to ``base_url``.
          params (dict, optional): Dictionary of param names to values.

        Example:
          api_client.get('/users', params={'active': True})

        Returns:
          A requests ``Response`` object.
        """
        response = requests.get(
            self._url_for(path),
            params=params,
            headers=self._headers(headers)
        )
        self._handle_errors(response)
        return response

    def post(self, path, body, headers=None):
        """Perform a POST request, providing a body, which will be JSON-encoded.

        Args:
          path (str): A path that gets appended to ``base_url``.
          body (dict): Dictionary that will be JSON-encoded and sent as the body.

        Example:
          api_client.post('/users', body={'name': 'Billy Jean'})

        Returns:
          A requests ``Response`` object.
        """

        response = requests.post(
            self._url_for(path),
            data=json.dumps(body),
            headers=self._headers(headers)
        )
        self._handle_errors(response)
        return response

    def put(self, path, body, headers=None):
        """Perform a PUT request, providing a body, which will be JSON-encoded.

        Args:
          path (str): A path that gets appended to ``base_url``.
          body (dict): Dictionary that will be JSON-encoded and sent as the body.

        Example:
          api_client.put('/users', body={'name': 'Billy Jean'})

        Returns:
          A requests ``Response`` object.
        """
        response = requests.put(
            self._url_for(path),
            data=json.dumps(body),
            headers=self._headers(headers)
        )
        self._handle_errors(response)
        return response

    def delete(self, path, body, headers=None):
        """Perform a DELETE request, providing a body, which will be JSON-encoded.

        Args:
          path (str): A path that gets appended to ``base_url``.
          body (dict): Dictionary that will be JSON-encoded and sent as the body.

        Example:
          api_client.delete('/users', body={'name': 'Billy Jean'})

        Returns:
          A requests ``Response`` object.
        """
        response = requests.delete(
            self._url_for(path),
            data=json.dumps(body),
            headers=self._headers(headers)
        )
        self._handle_errors(response)
        return response

    def _handle_errors(self, response):
        try:
            response_body = response.json()
        except ValueError:
            msg = 'Malformed response received from server'
            raise errors.MalformedResponseError(msg, response.text)

        if response.status_code < 400:
            return

        error = response.json()['error']
        exception_class = errors.ApiError.exception_for(response.status_code, error['type'], error.get('errors'))
        raise exception_class(error)

    def _url_for(self, path):
        return urlparse.urljoin(self.base_url, path)

    def _headers(self, custom_headers):
        headers = self._default_headers()
        if custom_headers:
          headers.update(custom_headers)
        return headers

    def _default_headers(self):
        return {
            'Accept': 'application/json',
            'Authorization': 'Bearer {0}'.format(self.access_token),
            'Content-Type': 'application/json',
            'GoCardless-Client-Library': 'gocardless-pro-python',
            'GoCardless-Client-Version': '1.26.0',
            'User-Agent': self._user_agent(),
            'GoCardless-Version': '2015-07-06',
        }

    def _user_agent(self):
        python_version = '.'.join(platform.python_version_tuple()[0:2])
        vm_version = '{}.{}.{}-{}{}'.format(*sys.version_info)
        return ' '.join([
            'gocardless-pro-python/1.26.0',
            'python/{0}'.format(python_version),
            '{0}/{1}'.format(platform.python_implementation(), vm_version),
            '{0}/{1}'.format(platform.system(), platform.release()),
            'requests/{0}'.format(requests.__version__),
        ])
