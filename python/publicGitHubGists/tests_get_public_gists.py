import pytest
from typing import List

from apiclient.authentication_methods import (HeaderAuthentication,
                                              NoAuthentication)

from get_public_gists import GitHubAPIClient, Gist

@pytest.fixture
def api_client():
    # TODO!!!! IMPORTANT
    # not best practice used here- just for demonstration purposes of this home-based tasks 
    # tests are runned on REAL GitHub API URL - in real world it SHOULDN'T happen
    # instead it would be worth to spin some docker-based API simulator
    # which could autogenerate API endpoints based on it's OpenAPI specs
    # sample docker image to use for it could be: 'stoplight/prism'
    # TODO!!! IMPORTANT READ ABOVE
    return GitHubAPIClient(base_url="https://api.github.com")

def test_no_auth_when_token_not_provided(api_client):
    auth = api_client.get_authentication_method()
    assert isinstance(auth, NoAuthentication)

def test_header_auth_returned_for_api_token_provided():
    client = GitHubAPIClient(token="whatever")
    auth = client.get_authentication_method()
    assert isinstance(auth, HeaderAuthentication)

def test_list_user_gists_returns_list_of_gists(api_client):
    gists: List[Gist] = (
        api_client.list_user_gists(username="whatever")
    )
    assert isinstance(gists, list)

def test_list_user_gists_throws_exception_for_unknown_user(api_client):
    with pytest.raises(Exception) as exc:
        api_client.list_user_gists(username="SOME_KIND_OF_UNKNOWN=XXX")
        assert "404 Error: Not found" in str(exc.value)
