import logging
import pandas as pd

class DataTransform:
    def transform_data(self, raw_data):
        try:
            records = []
            for data in raw_data:
                name = data.get("name", {}).get("common", "Unknown")
                region = data.get("region", "Unknown")
                languages = ", ".join(data.get("languages", {}).values())
                area = data.get("area", 0)
                population = data.get("population", 0)
                continents = ", ".join(data.get("continents", []))

                records.append({
                    "name": name,
                    "region": region,
                    "languages": languages,
                    "area": area,
                    "population": population,
                    "continents": continents
                })

            df = pd.DataFrame(records)
            logging.info(f"Transformed {len(df)} records.")
            return df

        except Exception as e:
            logging.error(f"DEBUG: Failed to transform data: {e}")
            return pd.DataFrame()