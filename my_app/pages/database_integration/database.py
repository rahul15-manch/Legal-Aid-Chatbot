from sqlalchemy import create_engine, Column, Integer, String

from sqlalchemy.orm import declarative_base
Base = declarative_base()


DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class Lawyer(Base):
    __tablename__ = "lawyers"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    specialization = Column(String, index=True)
    contact = Column(String, index=True)

# 👇 yeh line add karo, ye sab tables banayega agar exist nahi karte
Base.metadata.create_all(bind=engine)
