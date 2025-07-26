



lzmadec --help
IF %ERRORLEVEL% NEQ 0 exit /B 1
lzmainfo --help
IF %ERRORLEVEL% NEQ 0 exit /B 1
xz --help
IF %ERRORLEVEL% NEQ 0 exit /B 1
xzdec --help
IF %ERRORLEVEL% NEQ 0 exit /B 1
exit /B 0
