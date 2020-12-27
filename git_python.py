from github import Github
from git import Repo
from getpass import getpass
import schedule
import time
from phue import Bridge
from playsound import playsound


# # adress IP du Bridge Philips
# b = Bridge("192.168.1.51")
# # connect le script au pont en cliquant une fois sur le bouton du pont
# b.connect()
# # retourne les infos du Bridge
# b.get_api()
# # Récupère toutes les lights du pont
# lights = b.lights

# Joue un son dans le dossier parent
playsound('/Users/noe/Desktop/GIT_API/xp.mp3')

# set toutes les lumieres sur ON et la lumière / éclairage et saturation voulu
# for l in lights:
#     l.on = True
#     l.brightness = 254
#     l.saturation = 254
#     l.hue = 44000

# Permet de récuperer les différents input

while True:
    _user = input("YOUR GITHUB USERNAME ")
    
    if(_user == "juliennoe"):
        print("VALIDATION AUTHENTIFICATION")
        playsound('/Users/noe/Desktop/GIT_API/gamecube.mp3')
        # for l in lights:
        #     l.on = True                                          
        #     l.brightness = 254
        #     l.saturation = 254
        #     playsound('/Users/noe/Desktop/GIT_API/gamecube.mp3')
        #     l.hue = 50000
        break
    else:
        print("VALIDATION FAIL")
        playsound('/Users/noe/Desktop/GIT_API/sardoche.mp3')
        # for l in lights:
        #     l.on = True                                          
        #     l.brightness = 254
        #     l.saturation = 254
        #     playsound('/Users/noe/Desktop/GIT_API/sardoche.mp3')
        #     l.hue = 500



# _token = "e56cbbbf5570f90b25a5f1bca88b9d914fccef40"
_token = getpass("YOUR GITHUB TOKEN ")
_repoTarget = input("YOUR GITHUB REPOSITORY NAME ")

# récupère les infos de l'api GITHUB par rapport au token
g = Github(_token)
userGit = g.get_user()

        
# set dans des variables les infos de l'API GITHUB
repo = g.get_repo(_user + "/" + _repoTarget)
repos = userGit.get_repos()
labels = repo.get_labels()
contents = repo.get_contents("")
branch = g.get_repo(_user + "/" +_repoTarget).get_branch("master")
commit = repo.get_commit(sha="master")
commitSaveValue = 0
repoSaveValue = 0

#print(commitSaveValue)
#print(repoSaveValue)

print("WAITING UPDATE")

# for l in lights:
#     l.on = True
#     l.brightness = 254
#     l.saturation = 120
#     l.hue = 15000

# Sauvegarde le nombre de commit initial
def SaveInitialCommitCount():
    return repo.get_commits().totalCount
    
commitSaveValue = SaveInitialCommitCount()
# print(commitSaveValue)
# print("SAVE COMMITS COUNT")

# Sauvegarde le nombre de repo initial
def SaveInitialRepoCount():
    return userGit.get_repos().totalCount

repoSaveValue = SaveInitialRepoCount()
# print(repoSaveValue)
# print("SAVE REPO COUNT")

# Check avec l'update le nombre de commit
def SaveUpdateCommitCount():
    return repo.get_commits().totalCount

# Check avec l'update le nombre de repo 
def SaveUpdateRepoCount():
    return userGit.get_repos().totalCount

# Boucle pour checker en temps réel le nombre de commit et repo
while True:

    #print(commitSaveValue)
    SaveUpdateCommitCount()
    #print(SaveUpdateCommitCount())

    #print(repoSaveValue)
    SaveUpdateRepoCount()
    #print(SaveUpdateRepoCount())

    if SaveUpdateCommitCount() > commitSaveValue:
        print("UPGRADE COMMIT ...")
        playsound('/Users/noe/Desktop/GIT_API/pavard.mp3')
        # for l in lights:
        #     l.on = True
        #     l.brightness = 254
        #     l.saturation = 255
        #     l.hue = 25000
        #     playsound('/Users/noe/Desktop/GIT_API/sardoche.mp3')
        #     time.sleep(10)
        pass
        
        print("UPGRADE COMMIT DONE")
        print("WAITING UPDATE")
        commitSaveValue = SaveUpdateCommitCount()
        
        # for l in lights:
        #     l.on = True
        #     l.brightness = 254
        #     l.saturation = 120
        #     l.hue = 15000
        pass
    
    if SaveUpdateRepoCount() > repoSaveValue:
        print("UPGRADE REPO ...")
        playsound('/Users/noe/Desktop/GIT_API/lepers.mp3')
        # for l in lights:
        #     l.on = True
        #     l.brightness = 254
        #     l.saturation = 255
        #     l.hue = 500
        #     playsound('/Users/noe/Desktop/GIT_API/lepers.mp3')
        #     time.sleep(10)
        pass
        
        print("UPGRADE REPO DONE")
        print("WAITING UPDATE")
        
        repoSaveValue = SaveUpdateRepoCount()

        # for l in lights:
        #     l.on = True
        #     l.brightness = 254
        #     l.saturation = 120
        #     l.hue = 15000
        pass

    time.sleep(1)

# print(repo)
# print(userGit.name)
# print(userGit.login)
# print(repo.get_topics())
# print(labels)
# print(list(repo.get_branches()))
# print(branch.commit)
# print(commit.commit.author.date)
# print(commit.commit.message)
# print(commit.commit.sha)





