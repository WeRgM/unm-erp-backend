from panel import Column

from .base import Base

class Product(Base):
    __tablename__ = 'products'

    name = Column(db.String(255), primary_key=True)
    price = Column(db.Float, nullable=false)

    def __repr__(self):
        return '<Product %r>' % self.name