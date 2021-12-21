import sqlalchemy as sq
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

from settings.settings import db_settings

Base = declarative_base()

engine = sq.create_engine(db_settings.create_db())
Session = sessionmaker(bind=engine)

class User(Base):
    __tablename__ = 'user'

    id = sq.Column(sq.Integer, primary_key=True)
    user_id = sq.Column(sq.String, nullable=True, unique=True)
    results = relationship('Result', secondary='user_result', back_populates='users',
                          cascade="all, delete", cascade_backrefs=True)


class Result(Base):
    __tablename__ = 'result'
    id = sq.Column(sq.Integer, primary_key=True)
    profile_link = sq.Column(sq.String, nullable=False, unique=True)
    users = relationship(User, secondary='user_result', back_populates='results', cascade="all, "
                                                                                          "delete")
    photos = relationship('Photo', secondary='result_photo', back_populates='res',
                          cascade="all, delete", cascade_backrefs=True)

user_result = sq.Table(
    'user_result', Base.metadata,
    sq.Column('user_id', sq.Integer, sq.ForeignKey('user.id')),
    sq.Column('result_id', sq.Integer, sq.ForeignKey('result.id'))
)


class Photo(Base):
    __tablename__ = 'photo'
    id = sq.Column(sq.Integer, primary_key=True)
    photo_link = sq.Column(sq.String, nullable=False, unique=True)
    res = relationship(Result, secondary='result_photo', back_populates='photos', cascade="all, "
                                                                                          "delete")

result_photo = sq.Table(
    'result_photo', Base.metadata,
    sq.Column('result_id', sq.Integer, sq.ForeignKey('result.id')),
    sq.Column('photo_id', sq.Integer, sq.ForeignKey('photo.id'))
)


def get_user_id(us_id):
    session = Session()
    _user = User(user_id=us_id)
    session.add(_user)
    session.commit()

def get_result(link):
    session = Session()
    _result = Result(
        profile_link=link,
    )

    session.add(_result)
    session.commit()

def get_photo(photo_link):
    session = Session()
    _photo = Photo(photo_link=photo_link)
    session.add(_photo)
    session.commit()

def get_result_photo(domain, photo_link):
    session = Session()
    query_result = session.query(Result).filter(Result.profile_link == domain).one()
    query_photo = session.query(Photo).filter(Photo.photo_link == photo_link).one()
    query_photo.res.append(query_result)
    session.commit()

def get_user_result(user, domain):
    session = Session()
    query_user = session.query(User).filter(User.user_id == user).one()
    query_result = session.query(Result).filter(Result.profile_link == domain).one()
    query_user.results.append(query_result)
    session.commit()

def get_all_users():
    session = Session()
    all_users = session.query(User.user_id).all()
    return all_users

def get_all_domains():
    session = Session()
    all_photos = session.query(Result.profile_link).all()
    return all_photos

def get_exist_pairs():
    session = Session()
    all_pairs = session.query(User.user_id, Result.profile_link).join(User.results).all()
    return all_pairs


if __name__ == '__main__':
    session = Session()
    # init scheme
    # Base.metadata.create_all(engine)
    # get_user_id()
    # get_result('', '')
    # get_photo('')
    # get_result_photo('', '')
    # print(get_all_users())
    # print(show_all_results(''))
    # print(get_photos(''))
    # print(get_user_result('', ''))
    # print(get_all_domains())
    # domain = '
    # if (domain,) in get_all_domains():
    #     (get_user_result('', domain))
    # print(len(get_exist_pairs()))
    # if ('', '') in get_exist_pairs():
    #     print("Совпадение")
