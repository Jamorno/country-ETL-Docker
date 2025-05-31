import logging, psycopg2, os

class DataLoad:
    def __init__(self):
        self.conn = psycopg2.connect(
            host=os.getenv("DB_HOST"),
            port=os.getenv("DB_PORT"),
            dbname=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD")
        )

    def load_data(self, df):
        try:
            cursor = self.conn.cursor()

            cursor.execute("DROP TABlE IF EXISTS country_etl")

            cursor.execute(
                """CREATE TABLE IF NOT EXISTS country_etl 
                (name TEXT, region TEXT, languages TEXT, area INTEGER, population INTEGER, continents TEXT)"""
            )

            for _, row in df.iterrows():
                cursor.execute(
                    """INSERT INTO country_etl (name, region, languages, area, population, continents) 
                    VALUES (%s, %s, %s, %s, %s, %s)""", (
                        row["name"],
                        row["region"],
                        row["languages"],
                        row["area"],
                        row["population"],
                        row["continents"]
                    )
                )
            logging.info("Load data to PostgresSQL.")
            self.conn.commit()

        except Exception as e:
            logging.error("DEBUG: Failed to load data to PostgresSQL.")

        finally:
            cursor.close()
            self.conn.close()