# ライブラリ読み込み
from selenium import webdriver
from flask import Flask
from multiprocessing import Process
import time

# flask
app = Flask(__name__, static_folder='.', static_url_path='')

# ページ表示
@app.route('/')
def index():
    return app.send_static_file('AMainMenu.html')

# webブラウザ起動
def runChrome():
    driver = webdriver.Chrome()
    driver.get("http://localhost:8080/")

def run():
    app.run(port = 8080, debug = False)

if __name__ == '__main__':
    app.run(port = 8080, debug = False)