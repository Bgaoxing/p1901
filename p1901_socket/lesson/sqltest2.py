from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
                                        #用户名 密码    地址       库名
engine = create_engine('mysql+pymysql://root:12345678@127.0.0.1/p1901', echo=True)
Base = declarative_base()

from sqlalchemy import Column, Integer, String
class User(Base):
    __tablename__= 'al_users'
    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    fullname = Column(String(255))
    nickname = Column(String(200))

# Base.metadata.create_all(engine)

from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=engine)
session = Session()

ed_user = User(name='山上优亚', fullname='山上优亚', nickname='edsnickname')

session.add(ed_user)
session.commit()