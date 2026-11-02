"""Phase 3：Circuit smoke test。

建立 Circuit 設計 -> 放 R、C、GND 並接線 -> 建立 Nexxim LNA 掃頻 Setup -> 存檔。
RUN_SOLVE=True 時額外 analyze，並匯出一張 S11 報表圖到 output/。
驗收：schematic 中元件已連線、Setup 參數正確。
"""

from ansys.aedt.core import Circuit

from aedt_connect.config import AEDT_VERSION, NG_MODE, OUTPUT_DIR, TEST_PROJECT

RUN_SOLVE = False


def main() -> None:
    cir = Circuit(
        project=str(TEST_PROJECT),
        design="cir_smoke",
        version=AEDT_VERSION,
        non_graphical=NG_MODE,
        new_desktop=True,
    )
    try:
        sch = cir.modeler.schematic

        # 1-port R-C 對地：P1 -> R1 -> C1 -> GND
        p1 = sch.create_interface_port(name="P1", location=[-0.02, 0.0])
        r1 = sch.create_resistor(name="R1", value=50, location=[0.0, 0.0])
        c1 = sch.create_capacitor(name="C1", value=1e-12, location=[0.02, 0.0])
        gnd = sch.create_gnd(location=[0.04, 0.0])

        p1.pins[0].connect_to_component(r1.pins[0])
        r1.pins[1].connect_to_component(c1.pins[0])
        c1.pins[1].connect_to_component(gnd.pins[0])

        setup = cir.create_setup(name="LNA", setup_type="NexximLNA")
        setup.props["SweepDefinition"]["Data"] = "LINC 1GHz 10GHz 101"

        print("design     :", cir.design_name)
        print("components :", [c.name for c in sch.components.values()])
        print("setups     :", [s.name for s in cir.setups])

        if RUN_SOLVE:
            ok = cir.analyze_setup("LNA")
            print("analyze    :", ok)
            rpt = cir.post.create_report(expressions="dB(S(P1,P1))", setup_sweep_name="LNA")
            cir.post.export_report_to_jpg(str(OUTPUT_DIR), rpt.plot_name)
            print("report     :", OUTPUT_DIR / f"{rpt.plot_name}.jpg")

        cir.save_project()
        print("saved      :", cir.project_file)
    finally:
        cir.release_desktop(close_projects=True, close_desktop=True)
        print("released OK")


if __name__ == "__main__":
    main()
