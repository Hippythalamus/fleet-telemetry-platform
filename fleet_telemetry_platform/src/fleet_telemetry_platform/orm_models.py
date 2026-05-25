from sqlalchemy import (
    create_engine,
    Float,
    Integer,
    String,
)

from sqlalchemy.orm import (
    DeclarativeBase,
    Mapped,
    mapped_column,
)
from sqlalchemy.orm import sessionmaker

class Base(DeclarativeBase):
    pass

DATABASE_URL = "sqlite:///telemetry.db"

engine = create_engine(
    DATABASE_URL,
    echo=True,
)

SessionLocal = sessionmaker(bind=engine)

class TelemetryORM(Base):
    __tablename__ = "telemetry"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True,
    )

    robot_id: Mapped[str] = mapped_column(String)

    battery: Mapped[float] = mapped_column(Float)

    temperature: Mapped[float] = mapped_column(Float)

def create_tables():
    Base.metadata.create_all(engine)