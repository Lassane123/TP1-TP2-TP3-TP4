from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column
from sqlalchemy.orm import relationship
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import ForeignKey

engine = create_engine('sqlite:////tmp/tdlog.db', echo=True, future=True)
Base = declarative_base(bind=engine)
Session = sessionmaker(bind=engine)

class GameEntity(Base):
 __tablename__ = 'game'
 id = Column(Integer, primary_key=True)
 players = relationship("PlayerEntity", back_populates="game",
 cascade="all, delete-orphan")

 class PlayerEntity(Base):
     __tablename__ = 'player'
     id = Column(Integer, primary_key=True)
     name = Column(String, nullable=False)
     game_id = Column(Integer, ForeignKey("game.id"), nullable=False)
     game = relationship("GameEntity", back_populates="players")
     battle_field = relationship("BattlefieldEntity",
                                 back_populates="player",
                                 uselist=False, cascade="all, delete-orphan")


class BattlefieldEntity (Base):
    __tablename__ = 'Battle'
    id = Column(Integer, primary_key=True)


class VesselEntity(Base):
    __tablename__ = 'Vessel'
    id = Column(Integer, primary_key=True)


class WeaponEntity(Base):
    __tablename__ = 'Weapon'
    id = Column(Integer, primary_key=True)


class GameDao:
 def __init__(self):
     Base.metadata.create_all()
     self.db_session = Session()

 def map_to_game_entity( self,game) :
     pass
     # ici on va coder afin de convertir un objet de type Game en un objet
 # de type GameEntity

 def  map_to_game(self,game_entity):
     pass
     # ici on va coder afin de convertir un objet de type Game entity en  game

 def create_game(self, game: Game) -> int:
     game_entity = self.map_to_game_entity(game)
     self.db_session.add(game_entity)
     self.db_session.commit()
     return game_entity.id
 def find_game(self, game_id: int) -> Game:
     stmt = select(GameEntity).where(GameEntity.id == game_id)
     game_entity = self.db_session.scalars(stmt).one()
     return self.map_to_game(game_entity)

