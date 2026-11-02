"""AEDT Desktop 啟動 / 釋放的 context manager。

無論成功或丟出例外，離開 with 區塊時都會 release_desktop，
避免殘留 ansysedt.exe、專案 .lock 與授權鎖。
"""

from contextlib import contextmanager

from ansys.aedt.core import Desktop

from .config import AEDT_VERSION, NG_MODE


@contextmanager
def aedt_session(non_graphical: bool = NG_MODE, new_desktop: bool = True):
    desktop = Desktop(
        version=AEDT_VERSION,
        non_graphical=non_graphical,
        new_desktop=new_desktop,
        close_on_exit=True,
    )
    try:
        yield desktop
    finally:
        desktop.release_desktop(close_projects=True, close_desktop=True)
