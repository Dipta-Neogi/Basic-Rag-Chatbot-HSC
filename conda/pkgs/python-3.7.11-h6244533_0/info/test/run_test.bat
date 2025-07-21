



python -V
IF %ERRORLEVEL% NEQ 0 exit /B 1
2to3 -h
IF %ERRORLEVEL% NEQ 0 exit /B 1
pydoc -h
IF %ERRORLEVEL% NEQ 0 exit /B 1
python -m venv %%TEMP%%\venv
IF %ERRORLEVEL% NEQ 0 exit /B 1
pushd tests
IF %ERRORLEVEL% NEQ 0 exit /B 1
pushd distutils
IF %ERRORLEVEL% NEQ 0 exit /B 1
python setup.py install -v -v
IF %ERRORLEVEL% NEQ 0 exit /B 1
python -c "import foobar"
IF %ERRORLEVEL% NEQ 0 exit /B 1
popd
IF %ERRORLEVEL% NEQ 0 exit /B 1
pushd distutils.cext
IF %ERRORLEVEL% NEQ 0 exit /B 1
python setup.py install --single-version-externally-managed --record=record.txt -v -v
IF %ERRORLEVEL% NEQ 0 exit /B 1
python -v -v -v -c "import greet"
IF %ERRORLEVEL% NEQ 0 exit /B 1
python -v -v -v -c "import greet; greet.greet('Python user')" | rg "Hello Python"
IF %ERRORLEVEL% NEQ 0 exit /B 1
popd
IF %ERRORLEVEL% NEQ 0 exit /B 1
pushd processpoolexecutor-max_workers-61
IF %ERRORLEVEL% NEQ 0 exit /B 1
python ppe.py
IF %ERRORLEVEL% NEQ 0 exit /B 1
popd
IF %ERRORLEVEL% NEQ 0 exit /B 1
pushd cmake
IF %ERRORLEVEL% NEQ 0 exit /B 1
cmake -GNinja -DPY_VER=3.7.11 -DPython_ROOT_DIR=%PREFIX% --trace --debug-output --debug-trycompile .
IF %ERRORLEVEL% NEQ 0 exit /B 1
popd
IF %ERRORLEVEL% NEQ 0 exit /B 1
popd
IF %ERRORLEVEL% NEQ 0 exit /B 1
exit /B 0
