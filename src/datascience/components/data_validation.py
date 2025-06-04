import os
from src.datascience import logger
import pandas as pd 
from src.datascience.entity.config_entity import DataValidationConfig

class DataValidation:
    def __init__(self, config: DataValidationConfig):
        self.config = config
    
    def validate_all_columns(self) -> bool:
        try:
            validation_status = True

            # Load data
            data = pd.read_csv(self.config.unzip_data_dir)
            actual_columns = list(data.columns)
            expected_schema = self.config.all_schema  # this should be config.schema['COLUMNS']

            # 1. Validate all columns are present
            for col in expected_schema:
                if col not in actual_columns:
                    validation_status = False
                    break

            # 2. Validate data types
            for col, expected_dtype in expected_schema.items():
                if col in data.columns:
                    actual_dtype = str(data[col].dtype)
                    if actual_dtype != expected_dtype:
                        print(f"Type mismatch for '{col}': expected {expected_dtype}, got {actual_dtype}")
                        validation_status = False
                        break

            # Write validation result to file
            with open(self.config.STATUS_FILE, 'w') as f: 
                f.write(f"Validation status: {validation_status}")

            return validation_status

        except Exception as e: 
            raise e