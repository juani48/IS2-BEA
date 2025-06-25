from data.config import Base
from sqlalchemy import Column, Integer, String, Float

class CommentaryModel(Base):
    __tablename__ = "commentary_table"

    id = Column(Integer, primary_key=True)
    machine_number = Column(Integer,nullable=False)
    commentary = Column(String, nullable=False)
    name = Column(String(50), nullable= False)
    #answer = Column(String, nullable=False)

