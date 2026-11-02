"""Phase 2：Icepak smoke test。

建立 Icepak 設計 -> 畫一個矽晶片 box -> 指定 1 W 熱源 -> 建立 Setup -> 存檔。
RUN_SOLVE=True 時額外呼叫 analyze()，用來確認求解器授權可取得。
驗收：output/connect_test.aedt 可用 AEDT GUI 開啟，看得到 chip、熱源邊界、Setup1。
"""

from ansys.aedt.core import Icepak

from aedt_connect.config import AEDT_VERSION, NG_MODE, TEST_PROJECT

RUN_SOLVE = False


def main() -> None:
    ipk = Icepak(
        project=str(TEST_PROJECT),
        design="ipk_smoke",
        version=AEDT_VERSION,
        non_graphical=NG_MODE,
        new_desktop=True,
    )
    try:
        ipk.modeler.model_units = "mm"

        ipk.modeler.create_box(
            origin=[0, 0, 0],
            sizes=[10, 10, 2],
            name="chip",
            material="silicon",
        )
        ipk.assign_solid_block(object_name="chip", power_assignment="1W")

        ipk.create_setup(name="Setup1")

        print("design  :", ipk.design_name)
        print("units   :", ipk.modeler.model_units)
        print("objects :", ipk.modeler.object_names)
        print("setups  :", [s.name for s in ipk.setups])

        if RUN_SOLVE:
            ok = ipk.analyze(setup="Setup1")
            print("analyze :", ok)

        ipk.save_project()
        print("saved   :", ipk.project_file)
    finally:
        ipk.release_desktop(close_projects=True, close_desktop=True)
        print("released OK")


if __name__ == "__main__":
    main()
