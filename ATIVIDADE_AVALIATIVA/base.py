from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase

# Define a classe base do SQLAlchemy moderno (versão 3.x+)
class ModeloBase(DeclarativeBase):
    pass

# Cria a instância do banco de dados utilizando a sua base customizada
db = SQLAlchemy(model_class=ModeloBase)
