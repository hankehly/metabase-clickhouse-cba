try:
    from pathlib import Path
    from urllib.request import urlopen
except ImportError:
    print("python version 3+ required")
    exit(1)


try:
    import pandas as pd
except ImportError:
    print("sorry, please install pandas too")
    exit(1)

BASE_DIR = Path(__file__).parent.parent.absolute()

# 15.45 MB as of 2021/06/05
DATASET_URI = "https://data.london.gov.uk/download/coronavirus--covid-19--cases/ae4d5fc9-5448-49a6-810f-910f7cbc9fd2/phe_vaccines_age_london_boroughs.csv"

DATASET_OUT_PATH = (
    BASE_DIR / "clickhouse_user_files" / "phe_vaccines_age_london_boroughs.csv"
)

if __name__ == "__main__":
    DATASET_OUT_PATH.parent.mkdir(exist_ok=True)
    print(f"Downloading resource: {DATASET_URI}")
    # clickhouse fails to load csv as-is (perhaps this could be fixed with some
    # configuration tweaking) so parsing with pandas first..
    pd.read_csv(DATASET_URI).to_csv(DATASET_OUT_PATH, index=False, header=False)
    print(f"Download complete. Saved to path: {DATASET_OUT_PATH}")
