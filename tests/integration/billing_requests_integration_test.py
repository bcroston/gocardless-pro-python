# WARNING: Do not edit by hand, this file was generated by Crank:
#
#   https://github.com/gocardless/crank
#

import json

import requests
import responses
from nose.tools import (
  assert_equal,
  assert_is_instance,
  assert_is_none,
  assert_is_not_none,
  assert_not_equal,
  assert_raises
)

from gocardless_pro.errors import MalformedResponseError
from gocardless_pro import resources
from gocardless_pro import list_response

from .. import helpers
  

@responses.activate
def test_billing_requests_list():
    fixture = helpers.load_fixture('billing_requests')['list']
    helpers.stub_response(fixture)
    response = helpers.client.billing_requests.list(*fixture['url_params'])
    body = fixture['body']['billing_requests']

    assert_is_instance(response, list_response.ListResponse)
    assert_is_instance(response.records[0], resources.BillingRequest)

    assert_equal(response.before, fixture['body']['meta']['cursors']['before'])
    assert_equal(response.after, fixture['body']['meta']['cursors']['after'])
    assert_is_none(responses.calls[-1].request.headers.get('Idempotency-Key'))
    assert_equal([r.actions for r in response.records],
                 [b.get('actions') for b in body])
    assert_equal([r.created_at for r in response.records],
                 [b.get('created_at') for b in body])
    assert_equal([r.id for r in response.records],
                 [b.get('id') for b in body])
    assert_equal([r.metadata for r in response.records],
                 [b.get('metadata') for b in body])
    assert_equal([r.status for r in response.records],
                 [b.get('status') for b in body])

@responses.activate
def test_timeout_billing_requests_list_retries():
    fixture = helpers.load_fixture('billing_requests')['list']
    with helpers.stub_timeout_then_response(fixture) as rsps:
      response = helpers.client.billing_requests.list(*fixture['url_params'])
      assert_equal(2, len(rsps.calls))
      assert_equal(rsps.calls[0].request.headers.get('Idempotency-Key'),
                   rsps.calls[1].request.headers.get('Idempotency-Key'))
    body = fixture['body']['billing_requests']

    assert_is_instance(response, list_response.ListResponse)
    assert_is_instance(response.records[0], resources.BillingRequest)

    assert_equal(response.before, fixture['body']['meta']['cursors']['before'])
    assert_equal(response.after, fixture['body']['meta']['cursors']['after'])

def test_502_billing_requests_list_retries():
    fixture = helpers.load_fixture('billing_requests')['list']
    with helpers.stub_502_then_response(fixture) as rsps:
      response = helpers.client.billing_requests.list(*fixture['url_params'])
      assert_equal(2, len(rsps.calls))
      assert_equal(rsps.calls[0].request.headers.get('Idempotency-Key'),
                   rsps.calls[1].request.headers.get('Idempotency-Key'))
    body = fixture['body']['billing_requests']

    assert_is_instance(response, list_response.ListResponse)
    assert_is_instance(response.records[0], resources.BillingRequest)

    assert_equal(response.before, fixture['body']['meta']['cursors']['before'])
    assert_equal(response.after, fixture['body']['meta']['cursors']['after'])

@responses.activate
def test_billing_requests_all():
    fixture = helpers.load_fixture('billing_requests')['list']

    def callback(request):
        if 'after=123' in request.url:
          fixture['body']['meta']['cursors']['after'] = None
        else:
          fixture['body']['meta']['cursors']['after'] = '123'
        return [200, {}, json.dumps(fixture['body'])]

    url = 'http://example.com' + fixture['path_template']
    responses.add_callback(fixture['method'], url, callback)

    all_records = list(helpers.client.billing_requests.all())
    assert_equal(len(all_records), len(fixture['body']['billing_requests']) * 2)
    for record in all_records:
      assert_is_instance(record, resources.BillingRequest)
    
  

@responses.activate
def test_billing_requests_create():
    fixture = helpers.load_fixture('billing_requests')['create']
    helpers.stub_response(fixture)
    response = helpers.client.billing_requests.create(*fixture['url_params'])
    body = fixture['body']['billing_requests']

    assert_is_instance(response, resources.BillingRequest)
    assert_is_not_none(responses.calls[-1].request.headers.get('Idempotency-Key'))
    assert_equal(response.actions, body.get('actions'))
    assert_equal(response.created_at, body.get('created_at'))
    assert_equal(response.id, body.get('id'))
    assert_equal(response.metadata, body.get('metadata'))
    assert_equal(response.status, body.get('status'))
    assert_equal(response.links.bank_authorisation,
                 body.get('links')['bank_authorisation'])
    assert_equal(response.links.creditor,
                 body.get('links')['creditor'])
    assert_equal(response.links.customer,
                 body.get('links')['customer'])
    assert_equal(response.links.customer_bank_account,
                 body.get('links')['customer_bank_account'])
    assert_equal(response.links.customer_billing_detail,
                 body.get('links')['customer_billing_detail'])
    assert_equal(response.links.mandate_request,
                 body.get('links')['mandate_request'])
    assert_equal(response.links.mandate_request_mandate,
                 body.get('links')['mandate_request_mandate'])
    assert_equal(response.links.payment_request,
                 body.get('links')['payment_request'])
    assert_equal(response.links.payment_request_payment,
                 body.get('links')['payment_request_payment'])
    assert_equal(response.mandate_request.currency,
                 body.get('mandate_request')['currency'])
    assert_equal(response.mandate_request.links,
                 body.get('mandate_request')['links'])
    assert_equal(response.mandate_request.metadata,
                 body.get('mandate_request')['metadata'])
    assert_equal(response.mandate_request.scheme,
                 body.get('mandate_request')['scheme'])
    assert_equal(response.mandate_request.verify,
                 body.get('mandate_request')['verify'])
    assert_equal(response.payment_request.amount,
                 body.get('payment_request')['amount'])
    assert_equal(response.payment_request.app_fee,
                 body.get('payment_request')['app_fee'])
    assert_equal(response.payment_request.currency,
                 body.get('payment_request')['currency'])
    assert_equal(response.payment_request.description,
                 body.get('payment_request')['description'])
    assert_equal(response.payment_request.links,
                 body.get('payment_request')['links'])
    assert_equal(response.payment_request.metadata,
                 body.get('payment_request')['metadata'])
    assert_equal(response.payment_request.scheme,
                 body.get('payment_request')['scheme'])
    assert_equal(response.resources.customer,
                 body.get('resources')['customer'])
    assert_equal(response.resources.customer_bank_account,
                 body.get('resources')['customer_bank_account'])
    assert_equal(response.resources.customer_billing_detail,
                 body.get('resources')['customer_billing_detail'])

@responses.activate
def test_billing_requests_create_new_idempotency_key_for_each_call():
    fixture = helpers.load_fixture('billing_requests')['create']
    helpers.stub_response(fixture)
    helpers.client.billing_requests.create(*fixture['url_params'])
    helpers.client.billing_requests.create(*fixture['url_params'])
    assert_not_equal(responses.calls[0].request.headers.get('Idempotency-Key'),
                     responses.calls[1].request.headers.get('Idempotency-Key'))

def test_timeout_billing_requests_create_idempotency_conflict():
    create_fixture = helpers.load_fixture('billing_requests')['create']
    get_fixture = helpers.load_fixture('billing_requests')['get']
    with helpers.stub_timeout_then_idempotency_conflict(create_fixture, get_fixture) as rsps:
      response = helpers.client.billing_requests.create(*create_fixture['url_params'])
      assert_equal(2, len(rsps.calls))

    assert_is_instance(response, resources.BillingRequest)

@responses.activate
def test_timeout_billing_requests_create_retries():
    fixture = helpers.load_fixture('billing_requests')['create']
    with helpers.stub_timeout_then_response(fixture) as rsps:
      response = helpers.client.billing_requests.create(*fixture['url_params'])
      assert_equal(2, len(rsps.calls))
      assert_equal(rsps.calls[0].request.headers.get('Idempotency-Key'),
                   rsps.calls[1].request.headers.get('Idempotency-Key'))
    body = fixture['body']['billing_requests']

    assert_is_instance(response, resources.BillingRequest)

def test_502_billing_requests_create_retries():
    fixture = helpers.load_fixture('billing_requests')['create']
    with helpers.stub_502_then_response(fixture) as rsps:
      response = helpers.client.billing_requests.create(*fixture['url_params'])
      assert_equal(2, len(rsps.calls))
      assert_equal(rsps.calls[0].request.headers.get('Idempotency-Key'),
                   rsps.calls[1].request.headers.get('Idempotency-Key'))
    body = fixture['body']['billing_requests']

    assert_is_instance(response, resources.BillingRequest)
  

@responses.activate
def test_billing_requests_get():
    fixture = helpers.load_fixture('billing_requests')['get']
    helpers.stub_response(fixture)
    response = helpers.client.billing_requests.get(*fixture['url_params'])
    body = fixture['body']['billing_requests']

    assert_is_instance(response, resources.BillingRequest)
    assert_is_none(responses.calls[-1].request.headers.get('Idempotency-Key'))
    assert_equal(response.actions, body.get('actions'))
    assert_equal(response.created_at, body.get('created_at'))
    assert_equal(response.id, body.get('id'))
    assert_equal(response.metadata, body.get('metadata'))
    assert_equal(response.status, body.get('status'))
    assert_equal(response.links.bank_authorisation,
                 body.get('links')['bank_authorisation'])
    assert_equal(response.links.creditor,
                 body.get('links')['creditor'])
    assert_equal(response.links.customer,
                 body.get('links')['customer'])
    assert_equal(response.links.customer_bank_account,
                 body.get('links')['customer_bank_account'])
    assert_equal(response.links.customer_billing_detail,
                 body.get('links')['customer_billing_detail'])
    assert_equal(response.links.mandate_request,
                 body.get('links')['mandate_request'])
    assert_equal(response.links.mandate_request_mandate,
                 body.get('links')['mandate_request_mandate'])
    assert_equal(response.links.payment_request,
                 body.get('links')['payment_request'])
    assert_equal(response.links.payment_request_payment,
                 body.get('links')['payment_request_payment'])
    assert_equal(response.mandate_request.currency,
                 body.get('mandate_request')['currency'])
    assert_equal(response.mandate_request.links,
                 body.get('mandate_request')['links'])
    assert_equal(response.mandate_request.metadata,
                 body.get('mandate_request')['metadata'])
    assert_equal(response.mandate_request.scheme,
                 body.get('mandate_request')['scheme'])
    assert_equal(response.mandate_request.verify,
                 body.get('mandate_request')['verify'])
    assert_equal(response.payment_request.amount,
                 body.get('payment_request')['amount'])
    assert_equal(response.payment_request.app_fee,
                 body.get('payment_request')['app_fee'])
    assert_equal(response.payment_request.currency,
                 body.get('payment_request')['currency'])
    assert_equal(response.payment_request.description,
                 body.get('payment_request')['description'])
    assert_equal(response.payment_request.links,
                 body.get('payment_request')['links'])
    assert_equal(response.payment_request.metadata,
                 body.get('payment_request')['metadata'])
    assert_equal(response.payment_request.scheme,
                 body.get('payment_request')['scheme'])
    assert_equal(response.resources.customer,
                 body.get('resources')['customer'])
    assert_equal(response.resources.customer_bank_account,
                 body.get('resources')['customer_bank_account'])
    assert_equal(response.resources.customer_billing_detail,
                 body.get('resources')['customer_billing_detail'])

@responses.activate
def test_timeout_billing_requests_get_retries():
    fixture = helpers.load_fixture('billing_requests')['get']
    with helpers.stub_timeout_then_response(fixture) as rsps:
      response = helpers.client.billing_requests.get(*fixture['url_params'])
      assert_equal(2, len(rsps.calls))
      assert_equal(rsps.calls[0].request.headers.get('Idempotency-Key'),
                   rsps.calls[1].request.headers.get('Idempotency-Key'))
    body = fixture['body']['billing_requests']

    assert_is_instance(response, resources.BillingRequest)

def test_502_billing_requests_get_retries():
    fixture = helpers.load_fixture('billing_requests')['get']
    with helpers.stub_502_then_response(fixture) as rsps:
      response = helpers.client.billing_requests.get(*fixture['url_params'])
      assert_equal(2, len(rsps.calls))
      assert_equal(rsps.calls[0].request.headers.get('Idempotency-Key'),
                   rsps.calls[1].request.headers.get('Idempotency-Key'))
    body = fixture['body']['billing_requests']

    assert_is_instance(response, resources.BillingRequest)
  

@responses.activate
def test_billing_requests_collect_customer_details():
    fixture = helpers.load_fixture('billing_requests')['collect_customer_details']
    helpers.stub_response(fixture)
    response = helpers.client.billing_requests.collect_customer_details(*fixture['url_params'])
    body = fixture['body']['billing_requests']

    assert_is_instance(response, resources.BillingRequest)
    assert_is_not_none(responses.calls[-1].request.headers.get('Idempotency-Key'))
    assert_equal(response.actions, body.get('actions'))
    assert_equal(response.created_at, body.get('created_at'))
    assert_equal(response.id, body.get('id'))
    assert_equal(response.metadata, body.get('metadata'))
    assert_equal(response.status, body.get('status'))
    assert_equal(response.links.bank_authorisation,
                 body.get('links')['bank_authorisation'])
    assert_equal(response.links.creditor,
                 body.get('links')['creditor'])
    assert_equal(response.links.customer,
                 body.get('links')['customer'])
    assert_equal(response.links.customer_bank_account,
                 body.get('links')['customer_bank_account'])
    assert_equal(response.links.customer_billing_detail,
                 body.get('links')['customer_billing_detail'])
    assert_equal(response.links.mandate_request,
                 body.get('links')['mandate_request'])
    assert_equal(response.links.mandate_request_mandate,
                 body.get('links')['mandate_request_mandate'])
    assert_equal(response.links.payment_request,
                 body.get('links')['payment_request'])
    assert_equal(response.links.payment_request_payment,
                 body.get('links')['payment_request_payment'])
    assert_equal(response.mandate_request.currency,
                 body.get('mandate_request')['currency'])
    assert_equal(response.mandate_request.links,
                 body.get('mandate_request')['links'])
    assert_equal(response.mandate_request.metadata,
                 body.get('mandate_request')['metadata'])
    assert_equal(response.mandate_request.scheme,
                 body.get('mandate_request')['scheme'])
    assert_equal(response.mandate_request.verify,
                 body.get('mandate_request')['verify'])
    assert_equal(response.payment_request.amount,
                 body.get('payment_request')['amount'])
    assert_equal(response.payment_request.app_fee,
                 body.get('payment_request')['app_fee'])
    assert_equal(response.payment_request.currency,
                 body.get('payment_request')['currency'])
    assert_equal(response.payment_request.description,
                 body.get('payment_request')['description'])
    assert_equal(response.payment_request.links,
                 body.get('payment_request')['links'])
    assert_equal(response.payment_request.metadata,
                 body.get('payment_request')['metadata'])
    assert_equal(response.payment_request.scheme,
                 body.get('payment_request')['scheme'])
    assert_equal(response.resources.customer,
                 body.get('resources')['customer'])
    assert_equal(response.resources.customer_bank_account,
                 body.get('resources')['customer_bank_account'])
    assert_equal(response.resources.customer_billing_detail,
                 body.get('resources')['customer_billing_detail'])

def test_timeout_billing_requests_collect_customer_details_doesnt_retry():
    fixture = helpers.load_fixture('billing_requests')['collect_customer_details']
    with helpers.stub_timeout(fixture) as rsps:
      with assert_raises(requests.ConnectTimeout):
        response = helpers.client.billing_requests.collect_customer_details(*fixture['url_params'])
      assert_equal(1, len(rsps.calls))

def test_502_billing_requests_collect_customer_details_doesnt_retry():
    fixture = helpers.load_fixture('billing_requests')['collect_customer_details']
    with helpers.stub_502(fixture) as rsps:
      with assert_raises(MalformedResponseError):
        response = helpers.client.billing_requests.collect_customer_details(*fixture['url_params'])
      assert_equal(1, len(rsps.calls))
  

@responses.activate
def test_billing_requests_collect_bank_account():
    fixture = helpers.load_fixture('billing_requests')['collect_bank_account']
    helpers.stub_response(fixture)
    response = helpers.client.billing_requests.collect_bank_account(*fixture['url_params'])
    body = fixture['body']['billing_requests']

    assert_is_instance(response, resources.BillingRequest)
    assert_is_not_none(responses.calls[-1].request.headers.get('Idempotency-Key'))
    assert_equal(response.actions, body.get('actions'))
    assert_equal(response.created_at, body.get('created_at'))
    assert_equal(response.id, body.get('id'))
    assert_equal(response.metadata, body.get('metadata'))
    assert_equal(response.status, body.get('status'))
    assert_equal(response.links.bank_authorisation,
                 body.get('links')['bank_authorisation'])
    assert_equal(response.links.creditor,
                 body.get('links')['creditor'])
    assert_equal(response.links.customer,
                 body.get('links')['customer'])
    assert_equal(response.links.customer_bank_account,
                 body.get('links')['customer_bank_account'])
    assert_equal(response.links.customer_billing_detail,
                 body.get('links')['customer_billing_detail'])
    assert_equal(response.links.mandate_request,
                 body.get('links')['mandate_request'])
    assert_equal(response.links.mandate_request_mandate,
                 body.get('links')['mandate_request_mandate'])
    assert_equal(response.links.payment_request,
                 body.get('links')['payment_request'])
    assert_equal(response.links.payment_request_payment,
                 body.get('links')['payment_request_payment'])
    assert_equal(response.mandate_request.currency,
                 body.get('mandate_request')['currency'])
    assert_equal(response.mandate_request.links,
                 body.get('mandate_request')['links'])
    assert_equal(response.mandate_request.metadata,
                 body.get('mandate_request')['metadata'])
    assert_equal(response.mandate_request.scheme,
                 body.get('mandate_request')['scheme'])
    assert_equal(response.mandate_request.verify,
                 body.get('mandate_request')['verify'])
    assert_equal(response.payment_request.amount,
                 body.get('payment_request')['amount'])
    assert_equal(response.payment_request.app_fee,
                 body.get('payment_request')['app_fee'])
    assert_equal(response.payment_request.currency,
                 body.get('payment_request')['currency'])
    assert_equal(response.payment_request.description,
                 body.get('payment_request')['description'])
    assert_equal(response.payment_request.links,
                 body.get('payment_request')['links'])
    assert_equal(response.payment_request.metadata,
                 body.get('payment_request')['metadata'])
    assert_equal(response.payment_request.scheme,
                 body.get('payment_request')['scheme'])
    assert_equal(response.resources.customer,
                 body.get('resources')['customer'])
    assert_equal(response.resources.customer_bank_account,
                 body.get('resources')['customer_bank_account'])
    assert_equal(response.resources.customer_billing_detail,
                 body.get('resources')['customer_billing_detail'])

def test_timeout_billing_requests_collect_bank_account_doesnt_retry():
    fixture = helpers.load_fixture('billing_requests')['collect_bank_account']
    with helpers.stub_timeout(fixture) as rsps:
      with assert_raises(requests.ConnectTimeout):
        response = helpers.client.billing_requests.collect_bank_account(*fixture['url_params'])
      assert_equal(1, len(rsps.calls))

def test_502_billing_requests_collect_bank_account_doesnt_retry():
    fixture = helpers.load_fixture('billing_requests')['collect_bank_account']
    with helpers.stub_502(fixture) as rsps:
      with assert_raises(MalformedResponseError):
        response = helpers.client.billing_requests.collect_bank_account(*fixture['url_params'])
      assert_equal(1, len(rsps.calls))
  

@responses.activate
def test_billing_requests_fulfil():
    fixture = helpers.load_fixture('billing_requests')['fulfil']
    helpers.stub_response(fixture)
    response = helpers.client.billing_requests.fulfil(*fixture['url_params'])
    body = fixture['body']['billing_requests']

    assert_is_instance(response, resources.BillingRequest)
    assert_is_not_none(responses.calls[-1].request.headers.get('Idempotency-Key'))
    assert_equal(response.actions, body.get('actions'))
    assert_equal(response.created_at, body.get('created_at'))
    assert_equal(response.id, body.get('id'))
    assert_equal(response.metadata, body.get('metadata'))
    assert_equal(response.status, body.get('status'))
    assert_equal(response.links.bank_authorisation,
                 body.get('links')['bank_authorisation'])
    assert_equal(response.links.creditor,
                 body.get('links')['creditor'])
    assert_equal(response.links.customer,
                 body.get('links')['customer'])
    assert_equal(response.links.customer_bank_account,
                 body.get('links')['customer_bank_account'])
    assert_equal(response.links.customer_billing_detail,
                 body.get('links')['customer_billing_detail'])
    assert_equal(response.links.mandate_request,
                 body.get('links')['mandate_request'])
    assert_equal(response.links.mandate_request_mandate,
                 body.get('links')['mandate_request_mandate'])
    assert_equal(response.links.payment_request,
                 body.get('links')['payment_request'])
    assert_equal(response.links.payment_request_payment,
                 body.get('links')['payment_request_payment'])
    assert_equal(response.mandate_request.currency,
                 body.get('mandate_request')['currency'])
    assert_equal(response.mandate_request.links,
                 body.get('mandate_request')['links'])
    assert_equal(response.mandate_request.metadata,
                 body.get('mandate_request')['metadata'])
    assert_equal(response.mandate_request.scheme,
                 body.get('mandate_request')['scheme'])
    assert_equal(response.mandate_request.verify,
                 body.get('mandate_request')['verify'])
    assert_equal(response.payment_request.amount,
                 body.get('payment_request')['amount'])
    assert_equal(response.payment_request.app_fee,
                 body.get('payment_request')['app_fee'])
    assert_equal(response.payment_request.currency,
                 body.get('payment_request')['currency'])
    assert_equal(response.payment_request.description,
                 body.get('payment_request')['description'])
    assert_equal(response.payment_request.links,
                 body.get('payment_request')['links'])
    assert_equal(response.payment_request.metadata,
                 body.get('payment_request')['metadata'])
    assert_equal(response.payment_request.scheme,
                 body.get('payment_request')['scheme'])
    assert_equal(response.resources.customer,
                 body.get('resources')['customer'])
    assert_equal(response.resources.customer_bank_account,
                 body.get('resources')['customer_bank_account'])
    assert_equal(response.resources.customer_billing_detail,
                 body.get('resources')['customer_billing_detail'])

def test_timeout_billing_requests_fulfil_doesnt_retry():
    fixture = helpers.load_fixture('billing_requests')['fulfil']
    with helpers.stub_timeout(fixture) as rsps:
      with assert_raises(requests.ConnectTimeout):
        response = helpers.client.billing_requests.fulfil(*fixture['url_params'])
      assert_equal(1, len(rsps.calls))

def test_502_billing_requests_fulfil_doesnt_retry():
    fixture = helpers.load_fixture('billing_requests')['fulfil']
    with helpers.stub_502(fixture) as rsps:
      with assert_raises(MalformedResponseError):
        response = helpers.client.billing_requests.fulfil(*fixture['url_params'])
      assert_equal(1, len(rsps.calls))
  

@responses.activate
def test_billing_requests_confirm_payer_details():
    fixture = helpers.load_fixture('billing_requests')['confirm_payer_details']
    helpers.stub_response(fixture)
    response = helpers.client.billing_requests.confirm_payer_details(*fixture['url_params'])
    body = fixture['body']['billing_requests']

    assert_is_instance(response, resources.BillingRequest)
    assert_is_not_none(responses.calls[-1].request.headers.get('Idempotency-Key'))
    assert_equal(response.actions, body.get('actions'))
    assert_equal(response.created_at, body.get('created_at'))
    assert_equal(response.id, body.get('id'))
    assert_equal(response.metadata, body.get('metadata'))
    assert_equal(response.status, body.get('status'))
    assert_equal(response.links.bank_authorisation,
                 body.get('links')['bank_authorisation'])
    assert_equal(response.links.creditor,
                 body.get('links')['creditor'])
    assert_equal(response.links.customer,
                 body.get('links')['customer'])
    assert_equal(response.links.customer_bank_account,
                 body.get('links')['customer_bank_account'])
    assert_equal(response.links.customer_billing_detail,
                 body.get('links')['customer_billing_detail'])
    assert_equal(response.links.mandate_request,
                 body.get('links')['mandate_request'])
    assert_equal(response.links.mandate_request_mandate,
                 body.get('links')['mandate_request_mandate'])
    assert_equal(response.links.payment_request,
                 body.get('links')['payment_request'])
    assert_equal(response.links.payment_request_payment,
                 body.get('links')['payment_request_payment'])
    assert_equal(response.mandate_request.currency,
                 body.get('mandate_request')['currency'])
    assert_equal(response.mandate_request.links,
                 body.get('mandate_request')['links'])
    assert_equal(response.mandate_request.metadata,
                 body.get('mandate_request')['metadata'])
    assert_equal(response.mandate_request.scheme,
                 body.get('mandate_request')['scheme'])
    assert_equal(response.mandate_request.verify,
                 body.get('mandate_request')['verify'])
    assert_equal(response.payment_request.amount,
                 body.get('payment_request')['amount'])
    assert_equal(response.payment_request.app_fee,
                 body.get('payment_request')['app_fee'])
    assert_equal(response.payment_request.currency,
                 body.get('payment_request')['currency'])
    assert_equal(response.payment_request.description,
                 body.get('payment_request')['description'])
    assert_equal(response.payment_request.links,
                 body.get('payment_request')['links'])
    assert_equal(response.payment_request.metadata,
                 body.get('payment_request')['metadata'])
    assert_equal(response.payment_request.scheme,
                 body.get('payment_request')['scheme'])
    assert_equal(response.resources.customer,
                 body.get('resources')['customer'])
    assert_equal(response.resources.customer_bank_account,
                 body.get('resources')['customer_bank_account'])
    assert_equal(response.resources.customer_billing_detail,
                 body.get('resources')['customer_billing_detail'])

def test_timeout_billing_requests_confirm_payer_details_doesnt_retry():
    fixture = helpers.load_fixture('billing_requests')['confirm_payer_details']
    with helpers.stub_timeout(fixture) as rsps:
      with assert_raises(requests.ConnectTimeout):
        response = helpers.client.billing_requests.confirm_payer_details(*fixture['url_params'])
      assert_equal(1, len(rsps.calls))

def test_502_billing_requests_confirm_payer_details_doesnt_retry():
    fixture = helpers.load_fixture('billing_requests')['confirm_payer_details']
    with helpers.stub_502(fixture) as rsps:
      with assert_raises(MalformedResponseError):
        response = helpers.client.billing_requests.confirm_payer_details(*fixture['url_params'])
      assert_equal(1, len(rsps.calls))
  

@responses.activate
def test_billing_requests_cancel():
    fixture = helpers.load_fixture('billing_requests')['cancel']
    helpers.stub_response(fixture)
    response = helpers.client.billing_requests.cancel(*fixture['url_params'])
    body = fixture['body']['billing_requests']

    assert_is_instance(response, resources.BillingRequest)
    assert_is_not_none(responses.calls[-1].request.headers.get('Idempotency-Key'))
    assert_equal(response.actions, body.get('actions'))
    assert_equal(response.created_at, body.get('created_at'))
    assert_equal(response.id, body.get('id'))
    assert_equal(response.metadata, body.get('metadata'))
    assert_equal(response.status, body.get('status'))
    assert_equal(response.links.bank_authorisation,
                 body.get('links')['bank_authorisation'])
    assert_equal(response.links.creditor,
                 body.get('links')['creditor'])
    assert_equal(response.links.customer,
                 body.get('links')['customer'])
    assert_equal(response.links.customer_bank_account,
                 body.get('links')['customer_bank_account'])
    assert_equal(response.links.customer_billing_detail,
                 body.get('links')['customer_billing_detail'])
    assert_equal(response.links.mandate_request,
                 body.get('links')['mandate_request'])
    assert_equal(response.links.mandate_request_mandate,
                 body.get('links')['mandate_request_mandate'])
    assert_equal(response.links.payment_request,
                 body.get('links')['payment_request'])
    assert_equal(response.links.payment_request_payment,
                 body.get('links')['payment_request_payment'])
    assert_equal(response.mandate_request.currency,
                 body.get('mandate_request')['currency'])
    assert_equal(response.mandate_request.links,
                 body.get('mandate_request')['links'])
    assert_equal(response.mandate_request.metadata,
                 body.get('mandate_request')['metadata'])
    assert_equal(response.mandate_request.scheme,
                 body.get('mandate_request')['scheme'])
    assert_equal(response.mandate_request.verify,
                 body.get('mandate_request')['verify'])
    assert_equal(response.payment_request.amount,
                 body.get('payment_request')['amount'])
    assert_equal(response.payment_request.app_fee,
                 body.get('payment_request')['app_fee'])
    assert_equal(response.payment_request.currency,
                 body.get('payment_request')['currency'])
    assert_equal(response.payment_request.description,
                 body.get('payment_request')['description'])
    assert_equal(response.payment_request.links,
                 body.get('payment_request')['links'])
    assert_equal(response.payment_request.metadata,
                 body.get('payment_request')['metadata'])
    assert_equal(response.payment_request.scheme,
                 body.get('payment_request')['scheme'])
    assert_equal(response.resources.customer,
                 body.get('resources')['customer'])
    assert_equal(response.resources.customer_bank_account,
                 body.get('resources')['customer_bank_account'])
    assert_equal(response.resources.customer_billing_detail,
                 body.get('resources')['customer_billing_detail'])

def test_timeout_billing_requests_cancel_doesnt_retry():
    fixture = helpers.load_fixture('billing_requests')['cancel']
    with helpers.stub_timeout(fixture) as rsps:
      with assert_raises(requests.ConnectTimeout):
        response = helpers.client.billing_requests.cancel(*fixture['url_params'])
      assert_equal(1, len(rsps.calls))

def test_502_billing_requests_cancel_doesnt_retry():
    fixture = helpers.load_fixture('billing_requests')['cancel']
    with helpers.stub_502(fixture) as rsps:
      with assert_raises(MalformedResponseError):
        response = helpers.client.billing_requests.cancel(*fixture['url_params'])
      assert_equal(1, len(rsps.calls))
  

@responses.activate
def test_billing_requests_notify():
    fixture = helpers.load_fixture('billing_requests')['notify']
    helpers.stub_response(fixture)
    response = helpers.client.billing_requests.notify(*fixture['url_params'])
    body = fixture['body']['billing_requests']

    assert_is_instance(response, resources.BillingRequest)
    assert_is_not_none(responses.calls[-1].request.headers.get('Idempotency-Key'))
    assert_equal(response.actions, body.get('actions'))
    assert_equal(response.created_at, body.get('created_at'))
    assert_equal(response.id, body.get('id'))
    assert_equal(response.metadata, body.get('metadata'))
    assert_equal(response.status, body.get('status'))
    assert_equal(response.links.bank_authorisation,
                 body.get('links')['bank_authorisation'])
    assert_equal(response.links.creditor,
                 body.get('links')['creditor'])
    assert_equal(response.links.customer,
                 body.get('links')['customer'])
    assert_equal(response.links.customer_bank_account,
                 body.get('links')['customer_bank_account'])
    assert_equal(response.links.customer_billing_detail,
                 body.get('links')['customer_billing_detail'])
    assert_equal(response.links.mandate_request,
                 body.get('links')['mandate_request'])
    assert_equal(response.links.mandate_request_mandate,
                 body.get('links')['mandate_request_mandate'])
    assert_equal(response.links.payment_request,
                 body.get('links')['payment_request'])
    assert_equal(response.links.payment_request_payment,
                 body.get('links')['payment_request_payment'])
    assert_equal(response.mandate_request.currency,
                 body.get('mandate_request')['currency'])
    assert_equal(response.mandate_request.links,
                 body.get('mandate_request')['links'])
    assert_equal(response.mandate_request.metadata,
                 body.get('mandate_request')['metadata'])
    assert_equal(response.mandate_request.scheme,
                 body.get('mandate_request')['scheme'])
    assert_equal(response.mandate_request.verify,
                 body.get('mandate_request')['verify'])
    assert_equal(response.payment_request.amount,
                 body.get('payment_request')['amount'])
    assert_equal(response.payment_request.app_fee,
                 body.get('payment_request')['app_fee'])
    assert_equal(response.payment_request.currency,
                 body.get('payment_request')['currency'])
    assert_equal(response.payment_request.description,
                 body.get('payment_request')['description'])
    assert_equal(response.payment_request.links,
                 body.get('payment_request')['links'])
    assert_equal(response.payment_request.metadata,
                 body.get('payment_request')['metadata'])
    assert_equal(response.payment_request.scheme,
                 body.get('payment_request')['scheme'])
    assert_equal(response.resources.customer,
                 body.get('resources')['customer'])
    assert_equal(response.resources.customer_bank_account,
                 body.get('resources')['customer_bank_account'])
    assert_equal(response.resources.customer_billing_detail,
                 body.get('resources')['customer_billing_detail'])

def test_timeout_billing_requests_notify_doesnt_retry():
    fixture = helpers.load_fixture('billing_requests')['notify']
    with helpers.stub_timeout(fixture) as rsps:
      with assert_raises(requests.ConnectTimeout):
        response = helpers.client.billing_requests.notify(*fixture['url_params'])
      assert_equal(1, len(rsps.calls))

def test_502_billing_requests_notify_doesnt_retry():
    fixture = helpers.load_fixture('billing_requests')['notify']
    with helpers.stub_502(fixture) as rsps:
      with assert_raises(MalformedResponseError):
        response = helpers.client.billing_requests.notify(*fixture['url_params'])
      assert_equal(1, len(rsps.calls))
  
