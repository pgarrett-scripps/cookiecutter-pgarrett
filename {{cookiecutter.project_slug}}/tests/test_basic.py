from {{ cookiecutter.project_module }} import hello

def test_hello():
    assert hello() == "Hello from {{ cookiecutter.project_name }}!"
