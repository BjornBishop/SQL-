from sqlalchemy import (
    create_engine, Table, Column, Float, ForeignKey, Integer, String, MetaData
)

# Execute instructions from localhost, "chinook" db
db = create_engine("postgresql:///chinook")

meta = MetaData(db)

# "artist" variable
artist_table = Table(
    "Artist", meta,
    Column("ArtistId", Integer, primary_key=True),
    Column("Name", String)
)

# Create an "Album" table
album_table = Table(
    "Album", meta,
    Column("AlbumId", Integer, primary_key=True),
    Column("Title", String),
    Column("ArtistId", Integer, ForeignKey("Artist.ArtistId"))
)

# "Track" Variable
track_table = Table(
    "Track", meta,
    Column("TrackId", Integer, primary_key=True),
    Column("Name", String),
    Column("AlbumId", Integer, ForeignKey("Album.AlbumId")),
    Column("MediaTypeId", Integer),
    Column("GenreId", Integer),
    Column("Composer", String),
    Column("Milliseconds", Integer),
    Column("Bytes", Integer),
    Column("UnitPrice", Float)
)

# Connecting to the database
with db.connect() as connection:
    #select_query = artist_table.select()
    #select_query = artist_table.select().with_only_columns([artist_table.c.Name])
    #select_query = artist_table.select().where(artist_table.c.Name == "Queen")
    #select_query = artist_table.select().where(artist_table.c.ArtistId == 51)
    #select_query = album_table.select().where(album_table.c.ArtistId == 51)
    select_query = track_table.select().where(track_table.c.Composer == 'Queen')
    results = connection.execute(select_query)

    for result in results:
        print(result)
