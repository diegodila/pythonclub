import urllib3, base64, os, json

#connect with github api 
USER='diegodila'
API_TOKEN='ATOKEN'
GIT_API_URL= f'https://api.github.com/users/{USER}/repos'
print(GIT_API_URL)

http = urllib3.PoolManager()

resp = http.request("GET", GIT_API_URL)

#headers and data of response
# print(resp.headers)
# print(resp.data)


json_data = json.loads(resp.data.decode('utf-8'))
repositories = [i['html_url'] for i in json_data]

os.chdir("./githubapi")
os.system('mkdir repositories')
os.chdir("./repositories")
os.system('pwd')

for i in repositories:
    os.system(f'git clone {i}')

    
os.system(''' GHUSER=diegodila; curl "https://api.github.com/users/$GHUSER/repos?per_page=100" | grep -o 'git@[^"]*' >> github_return''')



#commands return github repos
# The following curl command to list the repositories:
# GHUSER=CHANGEME; curl "https://api.github.com/users/$GHUSER/repos?per_page=100" | grep -o 'git@[^"]*'
# os.system(''' GHUSER=diegodila; curl "https://api.github.com/users/$GHUSER/repos?per_page=100" | grep -o 'git@[^"]*' >> github_return''')

#List cloned URLs, run:
# GHUSER=CHANGEME; curl -s "https://api.github.com/users/$GHUSER/repos?per_page=1000" | grep -w clone_url | grep -o '[^"]\+://.\+.git'

#If it's private, you need to add your API key (access_token=GITHUB_API_TOKEN), for example:
# curl "https://api.github.com/users/$GHUSER/repos?access_token=$GITHUB_API_TOKEN" | grep -w clone_url