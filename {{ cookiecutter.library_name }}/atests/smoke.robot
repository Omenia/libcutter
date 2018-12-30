*** Settings ***
Library         {{ cookiecutter.library_name }}


*** Test Cases ***
Use the library keyword
    Hello       {{ cookiecutter.author_name }}
