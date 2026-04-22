from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

DATABASE_URL = "sqlite:///./local.db"

engine = create_engine(DATABASE_URL, echo=True)


SessionFactory = sessionmaker(
    bind=engine,
    autocommit=False,
    autoflush=False,
    expire_on_commit=False,
)


