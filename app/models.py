from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Text
from sqlalchemy import DateTime

from datetime import datetime

from app.database import Base


class Asset(Base):

    __tablename__ = "assets"

    id = Column(Integer, primary_key=True)

    uuid = Column(String(64), unique=True, nullable=False)

    excel_file = Column(String(255), nullable=False)

    sheet_name = Column(String(255), nullable=False)

    row_number = Column(Integer)

    data = Column(Text)

    created_at = Column(DateTime, default=datetime.utcnow)