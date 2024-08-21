from app import db
from app.domain.repositories.base_repository import BaseRepository

class SQlAlchemyBaseRepository(BaseRepository):
    def __init__(self, model):
        self.model = model

    def get_all(self):
        return self.model.query.all()

    def get_by_id(self, id):
        return self.model.query.get(id)

    def create(self, obj):
        db.session.add(obj)
        db.session.commit()

    def update(self, obj):
        db.session.merge(obj)
        db.session.commit()

    def delete(self, obj):
        db.session.delete(obj)
        db.session.commit()