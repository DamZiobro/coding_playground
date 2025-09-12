import atexit
import unittest

from pact import Consumer, Provider


pact = Consumer('Consumer').has_pact_with(Provider('Provider'))
pact.start_service()
atexit.register(pact.stop_service)


class GetUserInfoContract(unittest.TestCase):
  def test_get_user(self):
    expected = {
      'username': 'UserA',
      'id': 123,
      'groups': ['Editors']
    }

    (pact
     .given('UserA exists and is not an administrator')
     .upon_receiving('a request for UserA')
     .with_request('get', '/users/UserA')
     .will_respond_with(200, body=expected))

    with pact:
      result = user('UserA')

    self.assertEqual(result, expected)
