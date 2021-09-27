# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplays"
user_table_drop = "DROP TABLE IF EXISTS users"
song_table_drop = "DROP TABLE IF EXISTS songs"
artist_table_drop = "DROP TABLE IF EXISTS artists"
time_table_drop = "DROP TABLE IF EXISTS time"

# CREATE TABLES

songplay_table_create = ("""CREATE TABLE IF NOT EXISTS songplays
                            (
                                songplay_id serial PRIMARY KEY NOT NULL, 
                                start_time timestamp NOT NULL, 
                                user_id int NOT NULL, level varchar, 
                                song_id varchar, artist_id varchar,
                                session_id int NOT NULL, 
                                location varchar NOT NULL, 
                                user_agent varchar NOT NULL
                            );
                        """)

user_table_create = ("""CREATE TABLE IF NOT EXISTS users 
                        (
                            userId int PRIMARY KEY NOT NULL, 
                            firstName varchar NOT NULL, 
                            lastName varchar NOT NULL, 
                            gender varchar NOT NULL, 
                            level varchar NOT NULL
                        );
                        """)

song_table_create = ("""CREATE TABLE IF NOT EXISTS songs 
                        (
                            song_id varchar PRIMARY KEY NOT NULL, 
                            title varchar NOT NULL, 
                            artist_id varchar NOT NULL, 
                            year int, 
                            duration numeric NOT NULL
                        );
                        """)

artist_table_create = ("""CREATE TABLE IF NOT EXISTS artists 
                          (
                              artist_id varchar PRIMARY KEY NOT NULL, 
                              artist_name varchar, 
                              artist_location varchar, 
                              artist_latitude numeric,
                              artist_longitude numeric
                          );
                            """)

time_table_create = ("""CREATE TABLE IF NOT EXISTS time 
                        (
                            start_time timestamp PRIMARY KEY NOT NULL, 
                            hour int NOT NULL,
                            day int NOT NULL, 
                            week_of_year int NOT NULL, 
                            month int NOT NULL, 
                            year int NOT NULL, 
                            weekday int NOT NULL
                        );
                        """)

# INSERT RECORDS

songplay_table_insert = ("""INSERT INTO songplays 
                            (
                                start_time, 
                                user_id, 
                                level, 
                                song_id, 
                                artist_id, 
                                session_id, 
                                location, 
                                user_agent
                            ) 
                            VALUES 
                            (%s,%s,%s,%s,%s,%s,%s,%s)
                            """)

user_table_insert = ("""INSERT INTO users 
                        (
                            userId, 
                            firstName, 
                            lastName, 
                            gender, 
                            level
                        )
                        VALUES 
                        (%s,%s,%s,%s,%s) 
                        ON CONFLICT(userId) DO UPDATE SET level=EXCLUDED.level
                        """)

song_table_insert = ("""INSERT INTO songs 
                        (
                            song_id, 
                            title, 
                            artist_id, 
                            year, 
                            duration
                        )
                        VALUES 
                        (%s,%s,%s,%s,%s) 
                        ON CONFLICT(song_id) DO NOTHING
                        """)

artist_table_insert = ("""INSERT INTO artists 
                         (
                             artist_id, 
                             artist_name, 
                             artist_location, 
                             artist_latitude, 
                             artist_longitude
                         )
                        VALUES (%s,%s,%s,%s,%s) 
                        ON CONFLICT(artist_id) DO NOTHING""")

time_table_insert = (""" INSERT INTO time 
                        (
                            start_time, 
                            hour, 
                            day, 
                            week_of_year, 
                            month, 
                            year, 
                            weekday
                        )
                         VALUES
                         (%s,%s,%s,%s,%s,%s,%s) 
                         ON CONFLICT(start_time) DO NOTHING""")


# FIND SONGS

# Implement the song_select query in sql_queries.py to find the song ID and artist ID based on the title, artist name, and duration of a son
song_select = (""" SELECT songs.song_id, artists.artist_id
                    FROM songs 
                    INNER JOIN artists 
                    ON songs.artist_id = artists.artist_id
                    WHERE songs.title = %s
                    AND artists.artist_name = %s
                    AND songs.duration = %s""")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]