"""Import and instanced main core"""
from app import main_core

app = main_core()


if __name__ == '__main__':
    app.run(port=5000)