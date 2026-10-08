from models import Autor, Livro
from database import SessionLocal


def popular_banco(session):
    """Cadastre autores e livros iniciais para testar a aplicação."""
    # TODO: crie pelo menos 3 autores.
    # TODO: crie pelo menos 6 livros.
    # TODO: inclua livros disponíveis e indisponíveis.
    # TODO: use session.add ou session.add_all e finalize com session.commit().
    pass


    autor1 = Autor(nome="Autor 1", pais="País 1")
    autor2 = Autor(nome="Autor 2", pais="País 2")
    autor3 = Autor(nome="Autor 3", pais="País 3")

    session.add_all([autor1, autor2, autor3])

    livro1 = Livro(titulo="Livro 1", autor=autor1)
    livro2 = Livro(titulo="Livro 2", autor=autor2)
    livro3 = Livro(titulo="Livro 3", autor=autor3)
    livro4 = Livro(titulo="Livro 4", autor=autor1)
    livro5 = Livro(titulo="Livro 5", autor=autor2)
    livro6 = Livro(titulo="Livro 6", autor=autor3)

    lirvo2.disponivel = False
    lirvo6.disponivel = False


    session.add_all([livro1, livro2, livro3, livro4, livro5, livro6])
    session.commit()