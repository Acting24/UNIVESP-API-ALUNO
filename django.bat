@echo off
REM Script para executar comandos Django com o ambiente virtual
REM Uso: django.bat [comando]
REM Exemplo: django.bat runserver
REM          django.bat migrate
REM          django.bat shell

if "%1"=="" (
    echo Uso: django.bat [comando]
    echo Exemplos:
    echo   django.bat runserver
    echo   django.bat migrate  
    echo   django.bat shell
    echo   django.bat createsuperuser
    echo   django.bat collectstatic
    exit /b 1
)

venv\Scripts\python.exe manage.py %*
