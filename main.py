from contextlib import asynccontextmanager
from fastapi import FastAPI, HTTPException, Depends
from sqlmodel import SQLModel, Field, Session, create_engine, select
from pydantic import BaseModel

# Configuración de base de datos SQLite guardamos en un archivo
sqlite_url = "sqlite:///./database.db" 
engine = create_engine(sqlite_url, connect_args={"check_same_thread": False})

# Modelo de Base de Datos SQLModel
class User(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    username: str = Field(index=True)
    password: str 

# Modelo para recibir la petición Pydantic
class LoginRequest(BaseModel):
    username: str
    password: str

# Evento de inicio (Lifespan): crea tablas y un usuario por defecto
@asynccontextmanager
async def lifespan(app: FastAPI):
    SQLModel.metadata.create_all(engine)
    with Session(engine) as session:
        usuario_prueba = User(username="admin", password="pupo")
        session.add(usuario_prueba)
        session.commit()
    yield 

app = FastAPI(title="API de Login Sencilla", lifespan=lifespan)

# Dependencia para obtener la sesion
def get_session():
    with Session(engine) as session:
        yield session

# Endpoint de login
@app.post("/login")
def login(request: LoginRequest, session: Session = Depends(get_session)):
    statement = select(User).where(User.username == request.username)
    user = session.exec(statement).first()

    if not user or user.password != request.password:
        raise HTTPException(status_code=401, detail="Usuario o contraseña incorrectos")

    return {"mensaje": "Login exitoso", "usuario": user.username}