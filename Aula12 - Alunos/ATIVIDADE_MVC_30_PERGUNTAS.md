# Atividade Aula 12 — Model, Controller e View (StreamFlix)

**Disciplina:** Python / Flask  
**Profª:** Janaína Duarte  
**Projeto:** `flask/Aula12/`  
**Objetivo:** Explorar o código, localizar arquivos e explicar o que cada camada faz.

---

## Como responder

1. Abra a pasta `flask/Aula12/` no editor ou GitHub.
2. Navegue pelas pastas `models/`, `controllers/` e `views/`.
3. Rode o site (`python app.py`) quando a pergunta pedir para testar no navegador.
4. Responda com **caminho do arquivo** + **explicação em suas palavras**.

**Identificação**

- Nome: _______________________________
- Turma: _______________________________

---

## Bloco A — Model (perguntas 1 a 10)

**1.** Em qual pasta ficam as classes que representam tabelas do banco SQLite? Cite o caminho.

         H:\python\Aula12 - Alunos\models

**2.** Qual é o nome do arquivo de banco criado quando o app roda? Em qual arquivo Python essa configuração está?

streamflix.db  Ele é criado no app.py (eu acho)

**3.** Quais classes Model existem no projeto (nome das classes)? Em quais arquivos `.py` cada uma está?


base.py : ModeloBase
filme_favorito.py : FilmeFavorito 
historico_busca.py : HistoricoBusca


**4.** De qual superclasse `FilmeFavorito` e `HistoricoBusca` herdam? O que elas ganham automaticamente por herança (cite 3 campos)?

Eles herdam a superclasse ModeloBase. eles ganham id, data_criacao e data_atualizacao

**5.** Qual é o `__tablename__` da tabela de favoritos? Por que usamos `__tablename__` em vez de só o nome da classe?

__tablename__ = "filmes_favoritos". não sei


**6.** No model `FilmeFavorito`, qual coluna guarda o id do filme vindo da API TMDB? Ela tem alguma restrição especial (`unique`, `nullable`)?

tmdb_id = db.Column(db.Integer, nullable=False, unique=True)

**7.** Abra `models/filme_favorito.py`. O que o método `@classmethod adicionar` faz passo a passo? O que acontece se o filme já existir nos favoritos?

se o id do filme adicionado for identico ao id de um filme ja existente, ele não retorna nada, mas se não existir ele adiciona todos os dados exigidos para adicionar um filme novo, salva as auterações e atuializa elas

**8.** Onde está o método que lista as últimas 8 buscas? Qual é o nome da classe e do método?

o metodo "ultimas" fica em historico_busca.py. o nome da classe é HistoricoBusca, e o metodo se chama ultimas.

**9.** O model grava dados da API TMDB inteira ou só alguns campos espelhados? Cite 4 campos salvos em `FilmeFavorito`.

O model grava somente alguns campos espelhados

    tmdb_id = db.Column(db.Integer, nullable=False, unique=True)
    titulo = db.Column(db.String(200), nullable=False)
    poster_path = db.Column(db.String(255), nullable=True)
    nota = db.Column(db.Float, nullable=True)

**10.** Em `models/__init__.py`, o que é exportado além de `db`? Por que o controller importa `from models import FilmeFavorito` em vez de importar o arquivo inteiro da pasta?

as classes modelobase, filmefavorito e historicobusca. importar o arquivo inteiro é mais lento e menos eficiente

---

## Bloco B — Controller (perguntas 11 a 20)

**11.** Quantos Blueprints existem no projeto? Cite o **nome** de cada um e o **url_prefix** (se tiver).

existem 3 blueprint no projeto. dashboard_bp = Blueprint("dashboard", __name__)   favoritos_bp = Blueprint("favoritos", __name__, url_prefix="/favoritos")   filmes_bp = Blueprint("filmes", __name__, url_prefix="/filmes")

**12.** Em qual arquivo está a rota `/filmes/populares`? Qual é o nome da função Python que responde essa URL?

H:\python\Aula12 - Alunos\controllers\filmes_controller.py. o nome da função é o populares

**13.** O que a função `populares()` faz antes de chamar `render_template`? Cite duas chamadas (Model, Service ou API).

api = TmdbApi()
    filmes, demo = api.filmes_populares()
    ids_fav = {f.tmdb_id for f in FilmeFavorito.listar()}

**14.** Quando o usuário busca um filme em `/filmes/buscar`, qual controller registra o termo no banco? Qual model é usado e em qual linha aproximada?

o controller é o filmes_controller.py 
    @classmethod
    def buscar_por_tmdb(cls, tmdb_id):
        return cls.query.filter_by(tmdb_id=tmdb_id).first()

**15.** Abra `controllers/favoritos_controller.py`. Qual método HTTP é exigido para adicionar favorito (`GET` ou `POST`)? Qual a URL completa de exemplo para adicionar o filme id 550?

o metodo exigido é o post. a url é /adicionar/<int:tmdb_id>

**16.** No `filmes_controller.py`, rota `detalhe(filme_id)`: o que acontece se `api.detalhe(filme_id)` retornar `None`?

ele não retorna nada

**17.** Onde os Blueprints são **registrados** no Flask? Cite o arquivo e o comando usado (3 registros).

no app.py 
    app.register_blueprint(dashboard_bp)
    app.register_blueprint(filmes_bp)
    app.register_blueprint(favoritos_bp)

**18.** Qual controller cuida da página inicial `/`? Quais variáveis ele envia para o template `index.html`?

a controller que cuida da páginda inicial é a dashboard_controller. ele envia as seguintes variaveis:  api = TmdbApi()
    populares, demo = api.filmes_populares()
    melhores, _ = api.filmes_melhores()
    favoritos = FilmeFavorito.listar()
    historico = HistoricoBusca.ultimas(5)

**19.** A pasta `services/tmdb_api.py` é Model, Controller ou View? Justifique: quem chama essa classe e para quê?

ela não é nenhuma dessas opções, é uma pasta a parte, mas quem chama essa classe é o controller, para poder simplificar e diminuir o trabalho da pasta controllers

**20.** No controller de busca, de onde vem o termo digitado quando o usuário usa o formulário da home (`index.html`)? É `request.form` ou `request.args`? Explique a diferença nesse projeto.

não entendi

---

## Bloco C — View (perguntas 21 a 30)

**21.** Onde ficam os templates HTML? Qual caminho completo da pasta?

ficam na pasta de views
H:\python\Aula12 - Alunos\views\templates, H:\python\Aula12 - Alunos\views\templates\favoritos, H:\python\Aula12 - Alunos\views\templates\filmes

**22.** Qual template é a “base” de todas as páginas (layout com menu)? Como os outros templates usam esse layout (qual comando Jinja)?

a template que é a "base" de todas as outras é a layout.html. Eles usam esse layout com o comando {% extends "layout.html" %}

**23.** Abra `views/templates/layout.html`. Liste os 5 links do menu e o `url_for` de cada um.

<nav class="nav">
        <a class="nav-brand" href="{{ url_for('dashboard.index') }}">StreamFlix</a>
        <a href="{{ url_for('filmes.populares') }}">Populares</a>
        <a href="{{ url_for('filmes.melhores') }}">Melhores</a>
        <a href="{{ url_for('filmes.buscar') }}">Buscar</a>
        <a href="{{ url_for('favoritos.listar') }}">Favoritos</a>
    </nav>

**24.** Qual arquivo HTML exibe a seção **“Onde assistir (Brasil)”**? De onde vem a variável `streaming` usada nessa tela?

o arquivo que exibe essa seção é o detalhe.html. não sei

**25.** O arquivo `filmes/_card.html` é uma página inteira ou um pedaço reutilizado? Quem inclui esse arquivo e com qual tag Jinja?

não sei

**26.** Em `filmes/detalhe.html`, como a View sabe se o filme já está nos favoritos? Qual variável booleana/objeto controla o botão “Salvar” vs “Remover”?

ela descobre com essa parte do codigo : <div class="acoes-inline">
            {% if favorito %}
            <form method="POST" action="{{ url_for('favoritos.remover', tmdb_id=filme.id) }}">
                <input type="hidden" name="voltar" value="{{ url_for('filmes.detalhe', filme_id=filme.id) }}">
                <button type="submit" class="btn btn-outline">★ Remover dos favoritos</button>
            </form>
            {% else %}
            <form method="POST" action="{{ url_for('favoritos.adicionar', tmdb_id=filme.id) }}">
                <input type="hidden" name="titulo" value="{{ filme.titulo }}">
                <input type="hidden" name="poster_path" value="{{ filme.poster_path or '' }}">
                <input type="hidden" name="nota" value="{{ filme.nota }}">
                <input type="hidden" name="ano" value="{{ filme.ano }}">
                <input type="hidden" name="voltar" value="{{ url_for('filmes.detalhe', filme_id=filme.id) }}">
                <button type="submit" class="btn">★ Salvar favorito</button>
            </form>
            {% endif %}
            <a class="btn btn-outline" href="{{ url_for('filmes.populares') }}">← Voltar</a>
        </div>



**27.** Onde está o CSS do site? Como o `layout.html` carrega esse arquivo (função Flask/Jinja)?

o css fica na pasta static. o layout carrega esse arquivo com o link.css

**28.** Na listagem de favoritos (`favoritos/lista.html`), qual loop Jinja percorre os registros? Cite 3 campos exibidos na tabela.

{% for fav in favoritos %}
        <tr>
            <td>
                <a href="{{ url_for('filmes.detalhe', filme_id=fav.tmdb_id) }}" style="color:#e94560">
                    {{ fav.titulo }}
                </a>
            </td>
            <td><span class="nota">★ {{ fav.nota or '—' }}</span></td>
            <td>{{ fav.ano or '—' }}</td>
            <td>{{ fav.data_criacao.strftime('%d/%m/%Y') }}</td>
            <td>
                <form method="POST" action="{{ url_for('favoritos.remover', tmdb_id=fav.tmdb_id) }}" style="display:inline">
                    <button type="submit" class="btn btn-sm btn-outline">Remover</button>
                </form>
            </td>
        </tr>
        {% endfor %}

**29.** O que significa `{% if modo_demo %}` no layout? Quem disponibiliza essa variável para **todos** os templates?

isso significa uma outra versão do streamflix, que nesse caso só vai aparecer uma div com aquelas informações. quem disponibiliza essa variavel é o layout.html

**30.** Desenhe ou descreva o fluxo completo quando o aluno clica em **“Salvar favorito”** no detalhe do filme, indicando **View → Controller → Model** (e redirect de volta). Cite arquivos envolvidos.

após clicar em salvar no site, você vai para a parte de controllers, na parte de adicionar, @favoritos_bp.route("/adicionar/<int:tmdb_id>", methods=["POST"])
def adicionar(tmdb_id):
    titulo = request.form.get("titulo", "Filme")
    poster_path = request.form.get("poster_path") or None
    nota = request.form.get("nota")
    ano = request.form.get("ano") or None

    try:
        nota = float(nota) if nota else None
    except ValueError:
        nota = None

    FilmeFavorito.adicionar(tmdb_id, titulo, poster_path, nota, ano)

    voltar = request.form.get("voltar") or url_for("favoritos.listar")
    return redirect(voltar)
. e depois vai para a parte de models

---

## Entrega

- Arquivo `.txt` ou `.md` com as 30 respostas 

**Critério:** respostas que mostrem que você **abriu o código**, não chute.

Boa exploração!
