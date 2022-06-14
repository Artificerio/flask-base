from . import db

class Img(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(1000))
    data = db.Column(db.LargeBinary)
    mimetype = db.Column(db.Text, nullable=False)
    def __repr__(self) -> str:
        d = {'id' : self.id, 'filename' : self.filename, 'filetype' : self.mimetype}
        return f'id {d["id"]} filename {d["filename"]} filetype {d["filetype"]}'