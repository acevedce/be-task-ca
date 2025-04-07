import subprocess
import uvicorn

def start():
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)

def auto_format():
    subprocess.call(["black", "."])

def run_linter():
    subprocess.call(["flake8", "."])

def run_tests():
    subprocess.call(["pytest", "tests"])

def check_types():
    subprocess.call(["mypy", "."])