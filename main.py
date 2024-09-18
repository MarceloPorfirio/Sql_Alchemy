from sqlalchemy import create_engine, Column, String, Integer, Boolean, ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base

db = create_engine("sqlite:///meubanco.db")
Session = sessionmaker(bind=db)
session = Session()


Base = declarative_base()

# tabelas

class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    nome = Column("nome", String)
    email = Column("email", String)
    senha = Column("senha", String)
    ativo = Column("ativo", Boolean)

    def __init__(self, nome, email, senha, ativo=True):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.ativo = ativo



class Livro(Base):
    __tablename__ = "livros"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    titulo = Column("titulo", String)
    qtd_pag = Column("qtd_pag", String)
    dono = Column("dono", ForeignKey("usuarios.id"))
    
    def __init__(self, titulo, qtd_pag, dono):
        self.titulo = titulo
        self.qtd_pag = qtd_pag
        self.dono = dono
        


Base.metadata.create_all(bind=db)

# CRUD

# CREATE
usuario = Usuario(nome="Marcelo", email="marcelo@gmail.com", senha="123456")
session.add(usuario)
session.commit()


# READ
# lista_usuarios = session.query(Usuario).all()
usuario_marcelo = session.query(Usuario).filter_by(email='marcelo@gmail.com').first()
print(usuario_marcelo)
print(usuario_marcelo.nome)
print(usuario_marcelo.email)

# CREATE
livro = Livro(titulo="Nome do livro",qtd_pag=100, dono=usuario_marcelo.id)
session.add(livro)
session.commit()

# UPDATE
usuario_marcelo.nome = "Marcelo Porfirio"
session.add(usuario_marcelo)
session.commit()

session.delete(usuario_marcelo)
session.commit()