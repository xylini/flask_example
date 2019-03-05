from .. import db
import datetime


tags = db.Table('post_tags',
                db.Column('post_id', db.Integer(), db.ForeignKey('post.id')),
                db.Column('tag_id', db.Integer(), db.ForeignKey('tag.id')))



class Post(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    text = db.Column(db.Text())
    publish_date = db.Column(db.DateTime(), default=datetime.datetime.now())

    # Many-one
    user_id = db.Column(db.Integer(), db.ForeignKey('user.id'))

    # One-many
    comments = db.relationship(
        'Comment',
        backref='post',
        lazy='dynamic'
    )

    # many - many
    tags = db.relationship(
        'Tag',
        secondary=tags,
        backref=db.backref('posts', lazy='dynamic')
    )

    def __init__(self, title=""):
        self.title = title

    def __repr__(self):
        return "<Post '{}'>".format(self.title)


class Comment(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    text = db.Column(db.Text())
    date = db.Column(db.DateTime(), default=datetime.datetime.now())

    # Many - One
    post_id = db.Column(db.Integer(), db.ForeignKey('post.id'))

    # def __init__(self, title):
    #     self.title = title

    def __repr__(self):
        return "<Comment '{}'>".format(self.text[:15])


# a lower-level access to the database than the abstraction of
# db.Model


class Tag(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String(255), unique=True, nullable=False)

    def __init__(self, title="flask"):
        self.title = title

    def __repr__(self):
        return "<Tag '{}'>".format(self.title)