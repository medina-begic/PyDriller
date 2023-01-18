from pydriller import Repository
from datetime import datetime, timezone, timedelta
from pydriller.metrics.process.commits_count import CommitsCount

remote_repositories = [

    # repositories for analyse
    'https://github.com/jgraber/PythonFriday'
    # 'https://github.com/vuejs/core',  # project1
    # 'https://github.com/facebook/react',  # project2
    # 'https://github.com/nuxt/nuxt.js',  # project3
    # 'https://github.com/facebook/react-native',  # project4
    # 'https://github.com/remix-run/remix',  # project5
    # 'https://github.com/axios/axios',  # project6
    # 'https://github.com/tailwindlabs/tailwindcss',  # project7
    # 'https://github.com/twbs/bootstrap',  # project8
    # 'https://github.com/sveltejs/svelte',  # project9
    # 'https://github.com/expressjs/express'  # project10


]

commit_list = []

for repository in remote_repositories:
    for commit in Repository(path_to_repo=repository, since=datetime(2022, 1, 1, 0, 0, 0)).traverse_commits():
        commit_format = f"{commit.committer_date} - {commit.hash[0:8]} - {commit.author.name}"
        commit_list.append(commit_format)

        for file in commit.modified_files:
            commit_format = f" {file.filename} has changed {file.change_type.name}"
            commit_list.append(commit_format)

            metric = CommitsCount(path_to_repo=repository,     from_commit='42722d558b3175a0c60ba7e513b7786ae6dbb591',
                                  to_commit='36425461ed2e42883ee7935af79cb620218f88b2')
            files = metric.count()
            commit_format = f"{files}"
            commit_list.append(files)


with open('result.txt', 'w') as f:
    for commit in commit_list:
        f.write(commit)
        f.write('\n')
