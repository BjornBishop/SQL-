from sqlalchemy import create_engine, Column, Float, ForeignKey, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

# Create engine
db = create_engine("postgresql:///chinook")
Base = declarative_base()

# Define the Artist table
class ArtistTable(Base):
    __tablename__ = "Artist"
    ArtistId = Column(Integer, primary_key=True)
    Name = Column(String)

# Define the Album table
class AlbumTable(Base):
    __tablename__ = "Album"
    AlbumId = Column(Integer, primary_key=True)
    Title = Column(String)
    ArtistId = Column(Integer, ForeignKey("Artist.ArtistId"))  # Corrected assignment

# Define the Track table
class TrackTable(Base):
    __tablename__ = "Track"
    TrackId = Column(Integer, primary_key=True)
    Name = Column(String)
    AlbumId = Column(Integer, ForeignKey("Album.AlbumId"))
    MediaTypeId = Column(Integer)
    GenreId = Column(Integer)
    Composer = Column(String)
    Milliseconds = Column(Integer)
    Bytes = Column(Integer)
    UnitPrice = Column(Float)

# Create session
Session = sessionmaker(bind=db)
session = Session()

# Create tables in the database if they don't exist
Base.metadata.create_all(db)

# Query the Artist table
artists = session.query(ArtistTable).all()
for artist in artists:
    print(artist.ArtistId, artist.Name, sep=" | ")
