#!/usr/bin/env bash

if [ $# -lt 2 ]; then
    echo "usage: apt.sh virtualenv_name python_version"
    exit
fi

sudo apt-get install gcc nginx-full runit rabbitmq-server redis-server python-pip make build-essential libssl-dev zlib1g-dev libbz2-dev libreadline-dev wget curl llvm git
sudo apt-get install python-psycopg2 postgresql-9.5 postgresql-server-dev-9.5 postgresql-client-9.5 postgresql-9.5-postgis-2.2 libmemcached-dev memcached

pip install --upgrade pip
sudo pip install virtualenvwrapper

echo "" >> ~/.bashrc
echo "# virtualenvwrapper" >> ~/.bashrc
echo "export WORKON_HOME=$HOME/.virtualenvs" >> ~/.bashrc
echo "export PROJECT_HOME=$HOME/$1" >> ~/.bashrc
echo "source /usr/local/bin/virtualenvwrapper.sh" >> ~/.bashrc
echo "" >> ~/.bashrc

mkdir web
source ~/.bashrc

# Settings pyenv
git clone git://github.com/yyuu/pyenv.git .pyenv

echo "" >> ~/.bashrc
echo "# pyenv" >> ~/.bashrc
echo "export PYENV_ROOT="$HOME/.pyenv"" >> ~/.bashrc
echo "export PATH="$PYENV_ROOT/bin:$PATH"" >> ~/.bashrc
echo "eval "$(pyenv init -)"" >> ~/.bashrc
echo "" >> ~/.bashrc

exec $SHELL

pyenv install $2 -v
pyenv rehash

mkvirtualenv -p ~/.pyenv/versions/$2/bin/python production
deactivate

mkvirtualenv -p ~/.pyenv/versions/$2/bin/python sandbox
deactivate
