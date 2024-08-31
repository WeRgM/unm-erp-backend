from app.domain.entities.user import User
from app.infrastructure.repository.sql_alchemy_repository import SQlAlchemyBaseRepository

class SQLAlchemyUserRepository(SQlAlchemyBaseRepository):
    def __init__(self):
        super().__init__(User)

    def get_by_username(self, username):
        return self.model.query.filter_by(username=username).first()

    def get_by_email(self, email):
        return self.model.query.filter_by(email=email).first()