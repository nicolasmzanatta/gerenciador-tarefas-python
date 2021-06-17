import random
import string

API_HOST = '127.0.0.1'
API_PORT = 5000
API_BASE_URL = '/api'

# Gera uma chave aleatória para geração do JWT
gen = string.ascii_letters + string.digits + string.ascii_uppercase
SECRET_KEY = ''.join(random.choice(gen) for i in range(32))


#Configuração MySQL
MYSQL_HOST = 'mysqlgerenciadortarefasnicolas.cy835xdf6k8l.sa-east-1.rds.amazonaws.com'
MYSQL_PORT = 3306
MYSQL_USER = 'devariauser'
MYSQL_PASSWORD = 'devaria2020'
MYSQL_DATABASE = 'gerenciador_tarefas'

DEBUG = True