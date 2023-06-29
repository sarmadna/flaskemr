@ECHO OFF
start http://127.0.0.1:5000/
wsl.exe bash -c "python3 $HOME/flaskemr/app.py"
