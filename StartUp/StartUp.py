import threading,webbrowser
from flask import Flask
app = Flask(__name__, static_folder='/View/static', static_url_path='/View/templates')

# 初期画面表示
@app.route('/')
def mainMenu():
    return app.send_static_file('AMainMenu.html')

# 等速・等加速度直線画面表示
@app.route('/LinearMotion')
def linearMotion():
    return app.send_static_file('Simulator\LinearMotion\LinearMotion.html')

# 鉛直投げ上げ画面表示
@app.route('/VerticalThrow')
def verticalThrow():
    return app.send_static_file('Simulator\VerticalThrow\VerticalThrow.html')

# 斜方投射画面表示
@app.route('/ObliqueProjection')
def obliqueProjection():
    return app.send_static_file('Simulator\ObliqueProjection\ObliqueProjection.html')

# 自由落下画面表示
@app.route('/FreeFall')
def freeFall():
    return app.send_static_file('Simulator\FreeFall\FreeFall.html')

if __name__ == "__main__":
    # ウィンドウオープン
    threading.Timer(1.0, lambda: webbrowser.open('http://localhost:8080') ).start()
    # サーバ起動
    app.run(port=8080, debug=False)