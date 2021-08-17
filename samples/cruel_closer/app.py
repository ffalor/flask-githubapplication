import os

from flask import Flask
from flask_githubapplication import GitHubApp

app = Flask(__name__)

app.config['GITHUBAPP_ID'] = int(os.environ['GITHUBAPP_ID'])

with open(os.environ['GITHUBAPP_KEY_PATH'], 'rb') as key_file:
    app.config['GITHUBAPP_KEY'] = key_file.read()

app.config['GITHUBAPP_SECRET'] = os.environ['GITHUBAPP_SECRET']

github_app = GitHubApp(app)
@app.route('/')
def index():
    return 'Hello World!'

@github_app.on('issues.opened')
def cruel_closer():
    owner = github_app.payload['repository']['owner']['login']
    repo = github_app.payload['repository']['name']
    num = github_app.payload['issue']['number']
    client = github_app.client
    client.issues.create_comment(owner=owner, repo=repo, issue_number=num, body="Could not replicate.")
    client.issues.update(owner=owner, repo=repo, issue_number=num, state="closed")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=True)
