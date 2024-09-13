from datetime import datetime
from app.application.settings.extensions_setting import db
from app.domain.entities.common.base_entity import BaseEntity, schema


class FuncionarioEntity(BaseEntity):
    __tablename__ = 'funcionarios'

    id_usuario = db.Column(db.Integer, db.ForeignKey(f'{schema}.usuarios.id'))
    id_cargo = db.Column(db.Integer, db.ForeignKey(f'{schema}.cargos.id'))
    data_admissao = db.Column(db.Date, nullable=False)

    usuario = db.relationship('UsuarioEntity', uselist=False, back_populates='funcionario')
    cargo = db.relationship('CargoEntity', uselist=False, back_populates='funcionario')
    administrador = db.relationship('AdministradorEntity', uselist=False, back_populates='funcionario')
    operador= db.relationship('OperadorEntity', uselist=False, back_populates='funcionario')

    def __init__(self, 
        id_cargo: int = None,
        id_pessoa: int = None,
        data_admissao: datetime = None
        ) -> None:
        self.id_cargo = id_cargo
        self.id_pessoa = id_pessoa
        self.data_admissao = data_admissao

    def __repr__(self):
        return "<Funcionario %r>" % self.id
