from app.application.settings.extensions import db
import os
from dotenv import load_dotenv


load_dotenv()
schema = os.getenv('SQLALCHEMY_DATABASE_SCHEMA')


class OperadorEntity(db.Model):
    __tablename__ = 'operador'
    __table_args__ = {'schema': schema}

    id = db.Column(db.Integer, primary_key=True)
    id_usuario = db.Column(db.Integer, db.ForeignKey(f'{schema}.usuario.id'))
    area_operacao = db.Column(db.String(50), nullable=False)
    supervisor_direto = db.Column(db.String(50), nullable=True)

    def __init__(self,
                 area_operacao,
                 supervisor_direto
                 ) -> None:
        self.area_operacao = area_operacao,
        self.supervisor_direto = supervisor_direto
        super().__init__()
        pass

    def __repr__(self):
        return "<Operador %r>" % self.id