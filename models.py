from factory import db
from datetime import datetime


df_post_tag_transmission = db.Table('df_post_tag_transmission',
                                    db.Column('df_post_id', db.String(
                                        64), db.ForeignKey('DF_Post.df_post_id')),
                                    db.Column('df_tag_id', db.String(64), db.ForeignKey('df_tag.df_tag_id')))


class DF_User(db.Model):
    __tablename__ = 'DF_User'

    df_user_id = db.Column(db.String(128), primary_key=True)
    df_user_name = db.Column(db.String(256), nullable=False, unique=True, index=True)
    df_user_pass = db.Column(db.String(256), nullable=False)
    df_user_mail = db.Column(db.String(256), nullable=False, unique=True, index=True)
    df_user_phone = db.Column(db.String(256), nullable=False, index=True)
    df_user_country = db.Column(db.String(256), nullable=False)
    df_user_address = db.Column(db.String(256), nullable=False)
    df_user_gender = db.Column(db.String(256), nullable=False)
    df_user_register_date = db.Column(db.DateTime, default=datetime.now)
    df_user_update_date = db.Column(db.DateTime, default=datetime.now)
    df_user_logon_date = db.Column(db.DateTime, default=datetime.now)
    df_user_post = db.relationship(
        'DF_Post',
        backref='DF_User',
        lazy='dynamic'
    )

    def __init__(self, df_user_id, df_user_name, df_user_pass, df_user_mail, df_user_phone, df_user_country, df_user_address,
                 df_user_gender):
        self.df_user_id = df_user_id
        self.df_user_name = df_user_name
        self.df_user_pass = df_user_pass
        self.df_user_mail = df_user_mail
        self.df_user_phone = df_user_phone
        self.df_user_country = df_user_country
        self.df_user_address = df_user_address
        self.df_user_gender = df_user_gender

    def __repr__(self):
        return "<Model Type => `{}`>".format(self.df_user_name)


class DF_Post(db.Model):
    __tablename__ = 'DF_Post'

    df_post_id = db.Column(db.String(256), primary_key=True)
    df_post_title = db.Column(db.String(256), nullable=False, index=True)
    df_post_content = db.Column(db.Text(), nullable=True)
    df_post_publish_date = db.Column(db.DateTime, default=datetime.now)
    df_post_modify_date = db.Column(db.DateTime, default=datetime.now)
    # Set the foreign key for Post
    df_user_id = db.Column(db.String(256), db.ForeignKey('DF_User.df_user_id'))
    df_post_comment = db.relationship(
        'DF_Comment',
        backref='DF_Post',
        lazy='dynamic'
    )
    df_post_tag = db.relationship(
        'DF_Tag',
        secondary=df_post_tag_transmission,
        lazy='dynamic'
    )

    def __init__(self, df_post_title):
        self.df_post_title = df_post_title

    def __repr__(self):
        return "<Model DF_Post => `{}`>".format(self.df_post_title)


class DF_Comment(db.Model):
    __tablename__ = 'DF_Comment'

    df_comment_id = db.Column(db.String(64), primary_key=True)
    df_comment_text = db.Column(db.Text(), nullable=False)
    df_comment_publish_date = db.Column(db.DateTime, default=datetime.now)
    df_comment_post_id = db.Column(
        db.String(64), db.ForeignKey('DF_Post.df_post_id'))

    def __init__(self, df_comment_name):
        self.df_comment_name = df_comment_name

    def __repr__(self):
        return '<Model Comment `{}`>'.format(self.df_comment_name)


class DF_Tag(db.Model):
    __tablename__ = 'df_tag'

    df_tag_id = db.Column(db.String(64), primary_key=True)
    df_tag_name = db.Column(db.String(256), nullable=True, unique=True)

    def __init__(self, df_tag_name):
        self.name = df_tag_name

    def __repr__(self):
        return "<Model Tag `{}`>".format(self.df_tag_name)
