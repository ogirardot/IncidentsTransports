from fabric.api import local

def deploy():
        # reset hard env
        local('git reset --hard', capture=False)
        # update with git
        local('git pull origin master', capture=False)
        # reset application
        # re-set setting properly
        local('cp -f settings.py.alwaysdata settings.py', capture=False)
        # re-syncdb


def deploy_preprod():
        # reset hard env
        local('git reset --hard', capture=False)
        # update with git
        local('git pull origin master', capture=False)
        # reset application
        # re-set setting properly
        local('cp -f settings.py.pre-prod settings.py', capture=False)
        # re-syncdb
