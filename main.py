import logging
from etl.extracter import DataExtract
from etl.transformer import DataTransform
from etl.loader import DataLoad

logging.basicConfig(
    filename="country.log",
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)

def run():
    extract = DataExtract("https://restcountries.com/v3.1/all")
    raw_data = extract.extract_data()
    if raw_data:
        transform = DataTransform()
        df = transform.transform_data(raw_data)

        if not df.empty:
            load = DataLoad()
            load.load_data(df)
            logging.info("ETL Process completed.")
        else:
            logging.warning("Dataframe is empty. Skipping load step.")

    else:
        logging.warning("No data extracted. Skipping transform and load step.")

    logging.info("....................................................................................................")


if __name__ == "__main__":
    run()