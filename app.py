from flask import Flask, render_template
from subprocess import Popen, PIPE

app = Flask(__name__)

@app.route('/')
def index():
    g = len(open("./logs.txt",'r').read().split('\n'))
    return render_template('index.html', source=g)

@app.route('/status')
def status():
    with open('./logs.txt','a+') as f:
        runA(f)
    return render_template('index.html',)

@app.route('/stop')
def stop():
    for path in run("kill `pidof -x minergate-cli`"):
        print(path)
    return render_template('stop.html')

def run(command):
    process = Popen(command, stdout=PIPE, shell=True)
    while True:
        line = process.stdout.readline().rstrip()
        if not line:
            break
        yield line

def runA(f):
    for path in run("./minergate-cli/minergate-cli -u vinay@programmer.net --xmr 4"):
        print(path)
        f.write(str(path))
        f.write('\n')


if __name__ == "__main__":
    app.run()
