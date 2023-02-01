from tkinter import Tk     # from tkinter import Tk for Python 3.x
from tkinter.filedialog import askopenfilename
from tkinter import filedialog, Tk
import platform
from pathlib import Path

# This function work on any OS.

def select_file():
    # ダイアログ用のルートウィンドウの作成
    root = Tk()
    # ウィンドウサイズを0にする（Windows用の設定）
    root.geometry("0x0")
    # ウィンドウのタイトルバーを消す（Windows用の設定）
    root.overrideredirect(1)
    # ウィンドウを非表示に
    root.withdraw()
    system = platform.system()

    # Windowsの場合withdrawの状態だとダイアログも
    # 非表示になるため、rootウィンドウを表示する
    if system == "Windows":
        root.deiconify()
    # macOS用にダイアログ作成前後でupdate()を呼ぶ
    root.update()
    # ダイアログを前面に
    root.lift()
    root.focus_force()
    path_str = filedialog.askopenfilename()
    root.update()
    if system == "Windows":
        # 再度非表示化（Windowsのみ）
        root.withdraw()
    path = Path(path_str)
    return path.absolute()

if __name__ == "__main__":

    f = select_file()
    print(f)


    # If LINUX ONLY, this is all you need.---------------------------------------------------------
    """
    import tkinter.filedialog

    target_file = tkinter.filedialog.askopenfilename(filetypes=[("select amazon report", "*.txt")])
    
    print(target_file)
    """
        