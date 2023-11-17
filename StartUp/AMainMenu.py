from selenium import webdriver
driver = webdriver.Chrome(r"C:\Simulation\Simulation\Setting\chromedriver.exe")
driver.get("http://localhost:12345/")

from flask import Flask
app = Flask(__name__, static_folder='.', static_url_path='')
@app.route('/')
def index():
    return app.send_static_file('AMainMenu.html')

app.run(port=8080, debug=False)