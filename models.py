from sqlalchemy import Column, String, Float, Boolean, DateTime, create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from datetime import datetime
# Define DuckDB database URL
DATABASE_URL = "duckdb:///data/sensex_data.duckdb"
# Initialize SQLAlchemy
engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()
# Define SensexCompany model
class SensexCompany(Base):
    __tablename__ = "sensex_company_list"
    stock = Column(String, primary_key=True)
    date_time = Column(DateTime, nullable=False, default=lambda: datetime.now().replace(hour=15, minute=15, second=0))
# Define EndingPrice model
class EndingPrice(Base):
    __tablename__ = "ending_price"
    stock = Column(String, primary_key=True)
    close_price = Column(Float)
    active = Column(Boolean, nullable=False)
# Create tables only if they don’t exist
if __name__ == "__main__":
    Base.metadata.create_all(engine)