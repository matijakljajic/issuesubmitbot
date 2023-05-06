import sys
import os
try:
    from configparser import ConfigParser
except ImportError:
    from ConfigParser import ConfigParser  # ver. < 3.0
try:
    import github
except ImportError:
    sys.exit("ImportError: PyGithub not installed. Install it with \'pip install PyGithub\'")

config = ConfigParser()
config.read('config.ini')

g = github.Github(config['config'].get('accesskey'))
# g = Github(os.environ['GITHUB_API_KEY'])

try:
    repo = g.get_repo(config['config'].get('repo'))
except:
    sys.exit("ConfigError: An attribute is invalid.")

# Issue creating process

title = input("Enter the title of the issue: ")
body = input("Describe the issue: ")
if (body == ""):
    body = github.GithubObject.NotSet

repo.create_issue(
    title = title,
    body = body,
    assignee = github.GithubObject.NotSet,
    milestone = github.GithubObject.NotSet,
    labels = github.GithubObject.NotSet,
    assignees = github.GithubObject.NotSet,
)