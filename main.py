import os
import subprocess

def unsafe_exec(command):
    # Intentional unsafe subprocess usage
    os.system(command)


def eval_input(user_input):
    # Intentional unsafe use of eval
    eval(user_input)


class TestClass:
    def __init__(self, data):
        self.data = data

    def insecure_format(self):
        # Potential format string vulnerability
        print(self.data % ())


def write_to_file(filepath, data):
    # Writing data to file without proper checks
    with open(filepath, 'w') as f:
        f.write(data)


def main():
    unsafe_exec('echo "Testing unsafe exec"')
    eval_input('print("Testing eval")')

    obj = TestClass("Potentially unsafe %s")
    obj.insecure_format()

    write_to_file('/tmp/test.txt', 'Potentially sensitive information')


if __name__ == '__main__':
    main()
