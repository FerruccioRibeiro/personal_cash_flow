from database.config import engine, SessionLocal, Base
from database.models import Nature, Person, Bank, Entity, Moviment, FutureMoviment

# Cria as tabelas se não existirem
Base.metadata.create_all(bind=engine)

# Inicia uma sessão para trabalhar
db = SessionLocal()

# Seu código aqui...