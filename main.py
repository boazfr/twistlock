import subprocess
import os


def run_tests():
    start_server_command = './twtask'

    try:
        os.popen(start_server_command)
    except os.error as e:
        print(f"Error running twtask: {e}")
        return

    tests_folder = os.path.abspath("tests")
    os.chdir(tests_folder)

    for folder in os.listdir(tests_folder):
        if os.path.isdir(folder):
            pytest_command = f"pytest {folder}"
            try:
                subprocess.run(pytest_command, check=True, shell=True)
            except subprocess.CalledProcessError as e:
                print(f"Error running pytest for folder {folder}: {e}")


if __name__ == "__main__":
    run_tests()
