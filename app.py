from flask import Flask, render_template
from subprocess import Popen, PIPE

app = Flask(__name__)

@app.route('/')
def index():
   return render_template('index.html')

@app.route('/status')
def status():
    pass


def run(command):
    process = Popen(command, stdout=PIPE, shell=True)
    while True:
        line = process.stdout.readline().rstrip()
        if not line:
            break
        yield line

if __name__ == "__main__":
    for path in run("./minergate-cli/minergate-cli -u vinay@programmer.net --xmr 2 -g"):
        print(path)
    app.run()