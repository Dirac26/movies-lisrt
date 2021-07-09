from routes import db

class MovieTable(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(80))
    rating = db.Column(db.Integer)
    def __repr__(self):
        return '<Annotation {}-{}:{} >'.format(self.id, self.title, self.rating)