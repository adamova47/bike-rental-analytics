from pathlib import Path
import pandas as pd

# refers to the current file and moves us from src/data_loading to the projects root
PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATA_PATH = PROJECT_ROOT / "data" / "hour.csv"

def load_data() -> pd.DataFrame:
    return pd.read_csv(DATA_PATH)

data = load_data()
print(data.head()) # displays first five rows
print(f"\nData shape: {data.shape}") # returns number of rows and columns
print(f"Columns: {data.columns.to_list()}") # lists the names of the columns
print(f"\nData types:\n{data.dtypes}")
print(f"\nData information: {data.info()}")
print(f"\nMissing values per column:\n{data.isna().sum()}")
print(f"\nDuplicate rows: {data.duplicated().sum()}")
print(f"\nNumerical info:\n{data.describe()}")