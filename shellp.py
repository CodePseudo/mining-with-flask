from subprocess import Popen, PIPE

def run(command):
    process = Popen(command, stdout=PIPE, shell=True)
    while True:
        line = process.stdout.readline().rstrip()
        if not line:
            break
        yield line


if __name__ == "__main__":
    for path in run("minergate-cli -u vinay@programmer.net --xmr 2 -g"):
        print(path)
