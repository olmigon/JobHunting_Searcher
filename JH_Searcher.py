import keyboard
import pyperclip
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import sys
def create_file():
    global selected_text
    selected_text = pyperclip.paste()

    set_url ='https://www.openwork.jp/company_list?field=&pref=&src_str='+selected_text+'&sort=1&ct=comlist'
    search_in_firefox(set_url)#urlを開く関数へ

def search_in_firefox(url):
    # FirefoxのWebDriverを初期化
    global driver
    driver = webdriver.Firefox()

    try:
        # 指定されたURLを開く
        driver.get(url)

        # ここで必要な処理を追加
        global a
        a=1
    finally:        
        print("This program is currently showing results for "+selected_text +" on openwork. ")

# CTRL+Q を押したときに create_file() 関数を呼び出す
keyboard.add_hotkey('ctrl+q', create_file)

  # 仮のURL、実際のURLに置き換えてください
# プログラムを実行し続ける
keyboard.wait()
