import requests
import ujson


# Verify endpoint GET {base_url}/users can be reached with a successful status code  of 200 and the elements in
# the response dictionary have the expected keys.
def test_get_all_users(context):
    uri = context.base_url + "/users"
    resp = requests.get(uri)
    assert resp.status_code is 200

    expected_keys = ["login", "id", "node_id", "avatar_url", "gravatar_id", "url", "html_url",
                     "followers_url", "following_url", "gists_url","starred_url","subscriptions_url","organizations_url",
                     "repos_url", "events_url", "received_events_url", "type", "site_admin"]
    verify_keys(resp, expected_keys)


# Verify endpoints GET {base_url}/repos/:owner/:repo/commits can be reached with a successful status code of 200 and
# the elements in the response dictionary have the expected keys.
def test_commits_on_repo(context):
    owner = "marcela-reyna"
    repo = "s-factor"
    uri = context.base_url + "/repos/" + owner + "/" + repo + "/commits"
    resp = requests.get(uri)
    assert resp.status_code is 200

    expected_keys = ["sha", "node_id", "commit", "url", "html_url", "comments_url", "author", "committer", "parents"]
    verify_keys(resp, expected_keys)


def verify_keys(resp, expected_keys):
    dict = ujson.loads(resp.content)
    for element in dict:
        for key in element:
            assert key in expected_keys


