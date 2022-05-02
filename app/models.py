from app import db


class Image(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    image_location = db.Column(db.String(), index=True, unique=True)

    def __repr__(self) -> str:
        fmt = "{}.{}({})"
        package = self.__class__.__module__
        class_ = self.__class__.__name__
        attrs = sorted((k, getattr(self, k)) for k in self.__mapper__.columns.keys())
        sattrs = ", ".join("{}={!r}".format(*x) for x in attrs)
        return fmt.format(package, class_, sattrs)
