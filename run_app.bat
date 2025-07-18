@echo OFF
:: This batch file will correctly initialize Conda, activate your environment,
:: change to the correct directory, and launch your Streamlit application.

:: Set the full path to your main miniconda3 or Anaconda3 installation folder.
set CONDA_BASE_PATH=C:\Users\nisha\miniconda3

:: Set the path to your project folder.
set PROJECT_PATH=C:\Users\nisha\OneDrive\Documents\websites\Algebra

:: Set the name of your conda environment.
set ENV_NAME=mission

:: --- Do not change the lines below ---

:: First, initialize the Conda shell for this script.
:: This is the crucial step that makes 'conda' commands available.
call %CONDA_BASE_PATH%\Scripts\activate.bat %CONDA_BASE_PATH%

:: Now that the shell is prepared, execute your sequence of commands.
:: The 'call' before 'conda activate' is important for script flow.
echo Activating Conda environment '%ENV_NAME%'...
call conda activate %ENV_NAME%

echo Changing directory to %PROJECT_PATH%...
cd /d %PROJECT_PATH%

echo Starting Streamlit application...
streamlit run app.py

:: The 'pause' command is optional. It will keep the command window open
:: after your Streamlit app server is stopped (e.g., by pressing Ctrl+C).
:: This is useful for seeing any final error messages.
pause