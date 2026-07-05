from datetime import datetime

from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Text

from app.database import Base


class Asset(Base):

    __tablename__ = "assets"

    id = Column(Integer, primary_key=True, index=True)

    # NEW
    company = Column(String(255), nullable=False, index=True)

    uuid = Column(String(36), unique=True, nullable=False, index=True)

    excel_file = Column(String(255), nullable=False)

    excel_slug = Column(String(255), nullable=False)

    sheet_name = Column(String(255), nullable=False)

    sheet_slug = Column(String(255), nullable=False)

    row_number = Column(Integer, nullable=False)

    data = Column(Text, nullable=False)

    created_at = Column(DateTime, default=datetime.utcnow)