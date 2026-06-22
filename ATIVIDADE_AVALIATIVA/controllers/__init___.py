from flask_sqlalchemy import SQLAlchemy

# Cria a instância do banco de dados que todos os modelos vão usar
db = SQLAlchemy()

# Importa as classes para que fiquem visíveis ao pacote models
from .cliente_locadora import Cliente
from .locacao import Locacao
from .veiculo import Veiculo
