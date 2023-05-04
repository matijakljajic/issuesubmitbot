import sys
import os
try:
    from configparser import ConfigParser
except ImportError:
    from ConfigParser import ConfigParser  # ver. < 3.0
try:
    from github import Github
except ImportError:
    sys.exit("ImportError: PyGithub not installed. Install it with \'pip install PyGithub\'")

config = ConfigParser()
config.read('config.ini')

g = Github(config['config'].get('accesskey'))
# g = Github(os.environ['GITHUB_API_KEY'])

try:
    repo = g.get_repo(config['config'].get('repo'))
except:
    sys.exit("ConfigError: Invalid property must be changed.")

print(repo.stargazers_count)