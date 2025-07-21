$Env:CONDA_EXE = "E:/interviews/HSC chatbot/Basic-Rag-Chatbot-HSC/conda\Scripts\conda.exe"
$Env:_CE_M = ""
$Env:_CE_CONDA = ""
$Env:_CONDA_ROOT = "E:/interviews/HSC chatbot/Basic-Rag-Chatbot-HSC/conda"
$Env:_CONDA_EXE = "E:/interviews/HSC chatbot/Basic-Rag-Chatbot-HSC/conda\Scripts\conda.exe"
$CondaModuleArgs = @{ChangePs1 = $True}

Import-Module "$Env:_CONDA_ROOT\shell\condabin\Conda.psm1" -ArgumentList $CondaModuleArgs

Remove-Variable CondaModuleArgs