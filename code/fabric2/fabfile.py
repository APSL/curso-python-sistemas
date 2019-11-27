from fabric import task

HOSTS = ['kiwi7.apsl.net']

@task(hosts=HOSTS)
def uname(c):
    uname = c.run('uname -a')


