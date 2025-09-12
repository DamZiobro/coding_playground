import re
import datetime
import os
import sys
from typing import Any, Dict, List, Optional

from apiclient import APIClient, paginated
from apiclient.authentication_methods import (HeaderAuthentication,
                                              NoAuthentication)
from apiclient.response_handlers import RequestsResponseHandler
from apiclient_pydantic import response_serializer, serialize_all_methods
from pydantic import BaseModel, HttpUrl


class GistFile(BaseModel):
    filename: str
    type: str
    language: Optional[str]
    raw_url: HttpUrl
    size: int


class Gist(BaseModel):
    url: HttpUrl
    forks_url: HttpUrl
    commits_url: HttpUrl
    id: str
    node_id: str
    git_pull_url: HttpUrl
    git_push_url: HttpUrl
    html_url: HttpUrl
    files: Dict[str, GistFile]
    public: bool
    created_at: datetime.datetime
    updated_at: datetime.datetime
    description: str
    comments: int
    comments_url: HttpUrl


class ListGistQueryParams(BaseModel):
    since: Optional[datetime.datetime]


#def next_page_by_url(response, previous_page_params):
    ## pagination helper function
    ## Function reads the response data and returns the query param
    ## that tells the next request to go to.
    #link_header = response.headers["link"]
    #urls = []
    #if "rel=\"last\"" in link_header: ## if the link_header contains 'last' then still pages left
        #urls = link_header.split(", ")
        #next_url_chunk = [url for url in urls if "next" in url][0]
        #HTTP_URL_PATTERN=r"(?:https?://|www\.)[^\s/$.?].[^\s>]*"
        #next_url = re.findall(HTTP_URL_PATTERN, next_url_chunk)[0]
        #return next_url
    #return None

class GitHubAPIClient(APIClient):
    def __init__(
        self,
        base_url: HttpUrl = None,
        token: str = None,
        *args: Optional[List[Any]],
        **kwargs: Optional[Dict[Any, Any]],
    ):
        super().__init__(*args, **kwargs)
        self._base_url = base_url or "https://api.github.com"

        self.set_response_handler(RequestsResponseHandler)
        self.set_authentication_method(
            HeaderAuthentication(token=token) if token else NoAuthentication()
        )

    def list_user_gists(
        self, username: str, query_params: ListGistQueryParams
    ) -> List[Gist]:
        resp = self.get(self._base_url + f"/users/{username}/gists", query_params.dict())
        return resp


class LastScriptRunState:
    def __init__(self):
        self._recent_run_file = "recent_run_file.txt"

    def get_last_run_timestamp(self) -> Optional[datetime.datetime]:
        last_run = None
        if os.path.exists(self._recent_run_file):
            with open(self._recent_run_file, "r") as f:
                last_run = datetime.datetime.fromisoformat(f.read().strip())
        return last_run

    def set_last_run_timestamp(self, time_to_set: datetime.datetime):
        with open(self._recent_run_file, "w") as f:
            f.write(time_to_set.isoformat())


def get_users_gists(username: str, since: datetime.datetime = None) -> List[Gist]:

    api_token = os.getenv("GITHUB_ACCESS_TOKEN")
    api_client = GitHubAPIClient(token=api_token)

    list_gist_query_params = ListGistQueryParams(since=since)
    return api_client.list_user_gists(username, query_params=list_gist_query_params)


def main():
    try:
        github_user = sys.argv[1]
    except IndexError:
        print("ERROR: please provide github_user as param to the script")
        print(f"       Usage: {sys.argv[0]} GITHUB_USER")
        sys.exit(-1)

    state = LastScriptRunState()
    since = state.get_last_run_timestamp()

    since_text = f"since {since}" if since else ""

    print(f"Retrieving gists of user: {github_user}")
    gists: List[Gist] = get_users_gists(github_user, since)

    print(f"Number of all gist retrieved {since_text}: {len(gists)}")

    public_gists: list[Gist] = [gist for gist in gists if gist.public]
    print(f"Number of publicly available gists {since_text}: {len(gists)}")

    for i, gist in enumerate(public_gists):
        print(f"==== Gist number: {i+1}")
        print(f"     Description: {gist.description}")
        print(f"     Gist Url: {gist.url}")

    state.set_last_run_timestamp(datetime.datetime.now())


if __name__ == "__main__":
    main()
