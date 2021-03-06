from server import db


class Actor(db.Model):
    __tablename__ = 'actor'
    actor_username = db.Column(db.Text)
    actor_name = db.Column(db.Text)
    subscribers = db.Column(db.Integer)
    video_count = db.Column(db.Integer)
    title = db.Column(db.Text)
    channel_id = db.Column(db.String(30), primary_key=True)
    view_count = db.Column(db.Integer)
    created_date = db.Column(db.String(10))
    collected_date = db.Column(db.Date, primary_key=True)
    thumbnail_url = db.Column(db.Text)
    description = db.Column(db.Text)
    keywords = db.Column(db.Text)
    banner_url = db.Column(db.Text)
    above_one_hundred_thousand = db.Column(db.Boolean)
    channel_videos = db.relationship('Relationship_Actor_Videos',
                                     backref='actor', lazy=True)

    def __init__(self, actor_name, actor_username,
                 subscribers, video_count, title,
                 channel_id, view_count, created_date, collected_date,
                 thumbnail_url, description,
                 keywords, banner_url, above_one_hundred_thousand):
        self.actor_username = actor_username
        self.actor_name = actor_name
        self.subscribers = subscribers
        self.video_count = video_count
        self.title = title
        self.channel_id = channel_id
        self.view_count = view_count
        self.created_date = created_date
        self.collected_date = collected_date
        self.thumbnail_url = thumbnail_url
        self.description = description
        self.keywords = keywords
        self.banner_url = banner_url
        self.above_one_hundred_thousand = above_one_hundred_thousand

    def __repr__(self):
        return '{}'.format(self.title)


class Videos(db.Model):
    __tablename__ = 'videos'
    title = db.Column(db.Text)
    likes = db.Column(db.Text)
    views = db.Column(db.Text)
    dislikes = db.Column(db.Text)
    comments = db.Column(db.Text)
    favorites = db.Column(db.Text)
    url = db.Column(db.Text)
    publishedAt = db.Column(db.Text)
    description = db.Column(db.Text)
    tags = db.Column(db.Text)
    embeddable = db.Column(db.Text)
    duration = db.Column(db.Text)
    thumbnail = db.Column(db.Text)
    category = db.Column(db.Text)
    video_id = db.Column(db.Text, primary_key=True)
    collected_date = db.Column(db.Date, primary_key=True)
    channel_id = db.Column(db.String(30))

    def __init__(self, title, views, dislikes, likes,
                 comments, favorites, url, publishedAt,
                 description, tags, embeddable, duration, thumbnail,
                 category, collected_date, channel_id,
                 video_id):
            self.title = title
            self.likes = likes
            self.views = views
            self.dislikes = dislikes
            self.comments = comments
            self.favorites = favorites
            self.url = url
            self.publishedAt = publishedAt
            self.description = description
            self.tags = tags
            self.embeddable = embeddable
            self.duration = duration
            self.thumbnail = thumbnail
            self.category = category
            self.collected_date = collected_date
            self.channel_id = channel_id
            self.video_id = video_id

    def __repr__(self):
        return '{}'.format(self.title)


class Relationship_Videos(db.Model):
    __tablename__ = 'relationship_videos'
    video_id = db.Column(db.Text, primary_key=True)
    original_video_id = db.Column(db.Text, primary_key=True)
    collected_date = db.Column(db.Date, primary_key=True)
    __table_args__ = (db.ForeignKeyConstraint(
        [video_id, collected_date],
        [Videos.video_id, Videos.collected_date]), {})

    def __init__(self, video_id, original_video_id,
                 collected_date):
            self.video_id = video_id
            self.original_video_id = original_video_id
            self.collected_date = collected_date


class Relationship_Actor_Videos(db.Model):
    __tablename__ = 'relationship_actor_videos'
    video_id = db.Column(db.Text, primary_key=True)
    channel_id = db.Column(db.Text, primary_key=True)
    collected_date = db.Column(db.Date, primary_key=True)
    __table_args__ = (
        db.ForeignKeyConstraint(
            [video_id, collected_date],
            [Videos.video_id, Videos.collected_date]
            ),
        db.ForeignKeyConstraint(
            [channel_id, collected_date],
            [Actor.channel_id, Actor.collected_date]
            )
        )

    def __init__(self, video_id, channel_id,
                 collected_date):
            self.video_id = video_id
            self.channel_id = channel_id
            self.collected_date = collected_date
