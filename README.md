# aedt-connect — Phase 0/1 快速開始

計畫全文見 `plan.html`。

## 一次性安裝（在本資料夾）

```powershell
uv sync
git init ; git add . ; git commit -m "init: uv + pyaedt skeleton"
uv run python -c "import ansys.aedt.core as a; print(a.__version__)"
```

## 執行測試（依序）

```powershell
uv run python -m aedt_connect.test_desktop   # Phase 1
uv run python -m aedt_connect.test_icepak    # Phase 2
uv run python -m aedt_connect.test_circuit   # Phase 3
```

每支跑完把終端機輸出（含錯誤）貼回 Claude 對話。
