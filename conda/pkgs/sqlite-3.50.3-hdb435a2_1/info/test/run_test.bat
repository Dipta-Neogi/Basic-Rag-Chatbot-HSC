



sqlite3 --version
IF %ERRORLEVEL% NEQ 0 exit /B 1
echo PRAGMA compile_options; | sqlite3
IF %ERRORLEVEL% NEQ 0 exit /B 1
exit /B 0
