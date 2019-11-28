from fabric.api import task, run, sudo, env, get, hide, prompt, put, get
from fabric.context_managers import cd
from fabric.contrib.files import upload_template, exists
from fabric.utils import abort, puts
from fabric.contrib.console import confirm
import yaml

import warnings
warnings.filterwarnings(action='ignore',module='.*paramiko.*')

with open("/etc/config.yml", 'r') as f:
    data = f.read()
    env.config = yaml.load(data)

env.hosts = ['curso0']
#env.port = 2232
env.user = "ubuntu"
env.key_filename = "../../cursopy.pem"


@task()
def uname():
    #run("uname -r")
    out = run('ls /tt')
    puts(out)

# podemos silenciar salida
@task()
def hostname():
    with hide('running', 'stdout', 'stderr'):
        hostname = run('hostname')
        puts(hostname)

# ejecutamos como sudo
@task()
def id():
    sudo('id')


@task()
def prod():
    env.entorno = "prod"
    puts("usando entorno prod")

@task()
def pre():
    env.entorno = "pre"
    puts("usando entorno prod")

# Cambiamos hostname al nodo, con parametro
# ej: fab sethostname:curso3
@task()
def deploy():
    sudo("echo 127.0.1.0 {}.localdomain >> /etc/hosts".format(env.config["hostname"]))
    sudo('hostnamectl set-hostname {}.localdomain'.format(env.config["hostname"]))


# cd contextmanager
@task()
def lstmp():
    with cd("/tmp"):
        run("ls -l")
    puts("Homedir:")
    run("ls -l")
