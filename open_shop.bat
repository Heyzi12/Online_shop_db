@echo off
setlocal enabledelayedexpansion

:: Ім'я файлу, який шукаємо
set "filename=shop.py"

:: Шукаємо файл у всіх підпапках (від поточної директорії)
for /r %%f in (*%filename%) do (
    echo Знайдено: %%f

    :: Якщо хочеш відкрити/запустити його з Python:
    python "%%f"
    goto :eof
)

echo Файл %filename% не знайдено.
pause

