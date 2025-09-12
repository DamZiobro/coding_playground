# GitHub API Public Gists Fetcher

The simple script which lists publicaly available Gist of user in GitHub.

The script lists all the public Gists of the selected user on the 1st run.
On the 2nd run it prints only newly created gists since the previous run. 

In order to reset this functionality you need to remove file `recent_run_file.txt`
which will be created after first run.

## Single-command run

To run the script inside the virtualenv with pre-installed dependencies you
need just one command:

```
make run GITHUB_USER=<GITHUB_USER_TO_FETCH_GISTS>
```

This command will automatically perform all the actions desribed in `Step by
step run`

## Run with authentication

If you exceeded your GitHub API limits, you can run the script with authentication.
In order to do that you need to:
1. [Generate GitHub personal access token](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token)
2. Pass the access token to the below command
```
make run GITHUB_USER=<YOUR_GITHUB_USER> GITHUB_ACCESS_TOKEN=<YOUR_GITHUB_ACCESS_TOKEN>
```

## Run tests scripts

To run unit tests into the virtualenv run:
```
make test
```

## Step-by-step run

1. Create virtualenv for the get_public_gists.py script (idempotent): `python -m venv .venv`
2. Activate virtualenv (idempotent): `source .venv/bin/activate`
3. Pre-install dependencies for the script (idempotent): `pip install -r requirements.txt` 
4. Run the get_public_gists.py inside the virtualenv: `python get_public_gists.py <YOUR_GITHUB_USER>`
5. Run unit tests inside virtualenv: `pytest tests_get_public_gists.py`


## Helpful commands

The script is accompanied with Makefile which defines number of useful dev commands:

* **make run**: run the **get_public_gists.py** script inside the virtualenv (venv will be created and deps installed automatically)
* **make clean** clean the virtualenv and temporary files to start development / usage from scratch
* **make test** run unit tests in the virtualenv
* **make .deps**: install dependencies into the virtualenv (idempotent)
* **make .venv**: create virtualenv (idempotent)
