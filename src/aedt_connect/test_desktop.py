"""Phase 1：Desktop 握手測試。

不開任何設計，只確認 Python 能啟動 AEDT、讀到版本 / PID / gRPC port，並乾淨釋放。
驗收：aedt_version_id 印出 2025.2；腳本結束後工作管理員沒有殘留 ansysedt.exe。
"""

import ansys.aedt.core

from aedt_connect.session import aedt_session


def main() -> None:
    print("PyAEDT version :", ansys.aedt.core.__version__)

    with aedt_session() as d:
        print("AEDT version   :", d.aedt_version_id)
        print("AEDT PID       :", d.aedt_process_id)
        print("gRPC port      :", d.port)
        print("Projects open  :", d.project_list)

    print("released OK")


if __name__ == "__main__":
    main()
