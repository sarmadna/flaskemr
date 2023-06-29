@ECHO OFF
start http://127.0.0.1:5000/
call %HOMEPATH%\flaskemr\venv\Scripts\activate.bat
python.exe %HOMEPATH%\flaskemr\app.py

