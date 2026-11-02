"""專案常數集中於此：AEDT 版本、圖形模式、輸出 / log 路徑。"""

from pathlib import Path

from ansys.aedt.core import settings

AEDT_VERSION = "2025.2"   # AEDT 2025 R2
NG_MODE = False           # 開發期保持 False 看得到畫面；穩定後改 True

PROJECT_ROOT = Path(__file__).resolve().parents[2]
OUTPUT_DIR = PROJECT_ROOT / "output"
LOG_DIR = PROJECT_ROOT / "logs"
OUTPUT_DIR.mkdir(exist_ok=True)
LOG_DIR.mkdir(exist_ok=True)

TEST_PROJECT = OUTPUT_DIR / "connect_test.aedt"

# PyAEDT 自身的 log 導到專案 logs/
settings.logger_file_path = str(LOG_DIR / "pyaedt.log")
