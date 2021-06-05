try:
    from pathlib import Path
    from urllib.request import urlopen
except ImportError:
    print("python version 3+ required")
    exit(1)

BASE_DIR = Path(__file__).parent.parent.absolute()

DRIVER_JAR_VER = "0.7.5"

DRIVER_JAR_URI = f"https://github.com/enqueue/metabase-clickhouse-driver/releases/download/{DRIVER_JAR_VER}/clickhouse.metabase-driver.jar"

DRIVER_JAR_OUT_PATH = BASE_DIR / "plugins" / "clickhouse.metabase-driver.jar"

if __name__ == "__main__":
    DRIVER_JAR_OUT_PATH.parent.mkdir(exist_ok=True)
    DRIVER_JAR_OUT_PATH.write_bytes(urlopen(DRIVER_JAR_URI).read())
