class Usuario():
    def __init__(self, id, login, senha, dtexpiracao):
        self.id = id
        self.login = login
        self.senha = senha
        self.dtexpiracao = dtexpiracao

class Coordenador():
    def __init__(self, id, usuario, nome, email, celular):
        self.id = id
        self.usuario = usuario
        self.nome = nome
        self.email = email
        self.celular = celular
        self.lista_disciplinas_administradas = []
        self.lista_disciplinas_abertas = []
        self.lista_solicitacao_matricula_aprovadas = []

class Aluno():
    def __init__(self, id, usuario, nome, email, celular, ra, foto = None):
        self.id = id
        self.usuario = usuario
        self.nome = nome
        self.email = email
        self.celular = celular
        self.ra = ra
        self.foto = foto
        self.lista_solicitacao_matricula = []
        self.lista_atividades_entregues = []
        self.lista_mensagens = []
    
    def atribuir_foto(self, foto):
        self.foto = foto

class Professor():
    def __init__(self, id, usuario, email, celular, apelido):
        self.id = id
        self.usuario = usuario
        self.email = email
        self.celular = celular
        self.apelido = apelido
        self.lista_disciplinas_ministradas = []
        self.lista_atividades_criadas = []
        self.lista_entregas_avaliadas = []
        self.lista_mensagens = []

class Disciplina():
    def __init__(self, id, nome, data, status, planoensino, cargahoraria, competencias, habilidades, ementa, conteudoprogramatico, bibliografias, percentuais, coordenador):
        self.id = id
        self.nome = nome
        self.data = data
        self.status = status
        self.planoensino = planoensino
        self.cargahoraria = cargahoraria
        self.competencias = competencias
        self.habilidades = habilidades
        self.ementa = ementa
        self.conteudoprogramatico = conteudoprogramatico
        self.bibliografiabasica = bibliografias['bibliografiabasica']
        self.bibliografiacomplementar = bibliografias['bibliografiacomplementar']
        self.percentualpratico = percentuais['percentualpratico']
        self.percentualteorico = percentuais['percentualteorico']
        self.coordenador = coordenador
        self.lista_disciplinas_ofertas = []
        self.coordenador.lista_disciplinas_administradas.append(self)

class Curso():
    def __init__(self, id, nome):
        self.id = id
        self.nome = nome

class DisciplinaOfertada():
    def __init__(self, id, coordenador, disciplina, curso, ano, semestre, turma, dtiniciomatricula = None, dtfimmatricula = None, professor = None, metodologia = None, recursos = None, criterioavaliacao = None, planoaulas = None):
        self.id = id
        self.coordenador = coordenador
        self.disciplina = disciplina
        self.curso = curso
        self.ano = ano
        self.semestre = semestre
        self.turma = turma
        self.dtiniciomatricula = dtiniciomatricula
        self.dtfimmatricula = dtfimmatricula
        self.professor = professor
        self.metodologia = metodologia
        self.recursos = recursos
        self.criterioavaliacao = criterioavaliacao
        self.planoaulas = planoaulas
        self.lista_atividades_vinculadas = []
        self.lista_solicitacoes_matricula = []
        self.coordenador.lista_disciplinas_abertas.append(self)
        self.disciplina.lista_disciplinas_ofertas.append(self)        
        if professor != None:
            self.professor.lista_disciplinas_ministradas.append(self)

    def atribuir_professor(self, professor, metodologia, recursos, criterioavaliacao, planoaulas):
        self.professor = professor
        self.metodologia = metodologia
        self.recursos = recursos
        self.criterioavaliacao = criterioavaliacao
        self.planoaulas = planoaulas
        self.professor.lista_disciplinas_ministradas.append(self)

    def inicio_fim_matricula(self, dtiniciomatricula, dtfimmatricula):
        self.dtiniciomatricula = dtiniciomatricula
        self.dtfimmatricula = dtfimmatricula

class SolicitacaoMatricula():
    def __init__(self, id, aluno, disciplinaofertada, dtsolicitacao, status, coordenador = None):
        self.id = id
        self.aluno = aluno
        self.disciplinaofertada = disciplinaofertada
        self.dtsolicitacao = dtsolicitacao
        self.status = status
        self.coordenador = coordenador
        self.aluno.lista_solicitacao_matricula.append(self)
        self.disciplinaofertada.lista_solicitacoes_matricula.append(self)
        if coordenador != None:
            self.coordenador.lista_solicitacao_matricula_aprovadas.append(self)

    def aprovar_solicitacao_matricula(self, coordenador):
        self.coordenador = coordenador
        self.coordenador.lista_solicitacao_matricula_aprovadas.append(self)

class Atividade():
    def __init__(self, id, titulo, conteudo, tipo, professor, descricao = None, extras = None):
        self.id = id
        self.titulo = titulo
        self.conteudo = conteudo
        self.tipo = tipo
        self.professor = professor
        self.descricao = descricao
        self.extras = extras
        self.professor.lista_atividades_criadas.append(self)

    def descrever_atividade(self, descricao):
        self.descricao = descricao

class AtividadeVinculada():
    def __init__(self, id, atividade, professor, disciplinaofertada, rotulo, status, dtiniciorespostas, dtfimrespostas):
        self.id = id
        self.atividade = atividade
        self.professor = professor
        self.disciplinaofertada = disciplinaofertada
        self.rotulo = rotulo
        self.status = status
        self.dtiniciorespostas = dtiniciorespostas
        self.dtfimrespostas = dtfimrespostas
        self.disciplinaofertada.lista_atividades_vinculadas.append(self)

class Entrega():
    def __init__(self, id, aluno, atividadevinculada, titulo, resposta, dtentrega, status, professor = None, nota = None, dtavaliacao = None, obs = None):
        self.id = id
        self.aluno = aluno
        self.atividadevinculada = atividadevinculada
        self.titulo = titulo
        self.resposta = resposta
        self.dtentrega = dtentrega
        self.status = status
        self.professor = professor
        self.nota = nota
        self.dtavaliacao = dtavaliacao
        self.obs = obs
        self.aluno.lista_atividades_entregues.append(self)
        if professor != None:
            self.professor.lista_entregas_avaliadas.append(self)

    def avaliar_entrega(self, professor, nota, dtavaliacao, obs):
        self.professor = professor
        self.nota = nota
        self.dtavaliacao = dtavaliacao
        self.obs = obs
        self.professor.lista_entregas_avaliadas.append(self)

class Mensagem():
    def __init__(self, id, aluno, professor, assunto, referencia, conteudo, status, dtenvio, dtresposta = None, resposta = None):
        self.id = id
        self.aluno = aluno
        self.professor = professor
        self.assunto = assunto
        self.referencia = referencia
        self.conteudo = conteudo
        self.status = status
        self.dtenvio = dtenvio
        self.dtresposta = dtresposta
        self.resposta = resposta
        self.aluno.lista_mensagens.append(self)
        self.professor.lista_mensagens.append(self)

    def responder(self, dtresposta, resposta):
         self.dtresposta = dtresposta
         self.resposta = resposta