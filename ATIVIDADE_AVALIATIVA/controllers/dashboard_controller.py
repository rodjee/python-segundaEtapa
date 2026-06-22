from flask import Blueprint, render_template
from models import ClienteLocadora, Locacao, veiculo
dashboard_bp = Blueprint("dashboard", __name__)