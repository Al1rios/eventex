# Eventex

Sistema de Eventos encomendado pela Morena

[![Build Status](https://travis-ci.org/Al1rios/eventex.svg?branch=master)](https://travis-ci.org/Al1rios/eventex)

[![Code Health](https://landscape.io/github/Al1rios/eventex/master/landscape.svg?style=flat)](https://landscape.io/github/Al1rios/eventex/master)

## Como Desenvolver?

1. Clone o repositorio.
2. Crie um virtualenv com python 3.5
3. Ative o virtualenv
4. Instale as dependencias.
5. Configure a instância com o .env
6. Execute os testes.

'''console
git clone git@github.com:alirios/eventex.git wttd
cd wttd
python -m venv .wttd
source .wttd/bin/active
pip install -r requirements-dev.txt
cp contrib/env-sample .env
python manage.py test
'''

## Como fazer o deploy

1. Crie um instãncia no heroku
2. Envie as configurações para o heroku
3. Define uma SECRET_KEY segura para instância.
4. Defina DEBUG=False
5. Configure o serviço de email.
6. Envie o código para o heroku


'''console
heroku create minhainstancia
heroku config:push
heroku config:set SECRET_KEY='python contrib/secret_gen.py'
heroku config:set DEBUG=False
#configuro o email
git push keroku master --force

'''