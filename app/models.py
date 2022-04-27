from app import db


class Image(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    image_location = db.Column(db.String(), index=True, unique=True)

    def __repr__(self) -> str:
        return super().__repr__()
