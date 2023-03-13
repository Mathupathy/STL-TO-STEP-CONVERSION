Stl to Step convert
#CONVERSION OF STL TO STEP FORMET

Objective: To convert the .stl file format to .step file format Procedures: Install the python-OCC package. Install anaconda command prompt. Open the anaconda command prompt and run the following codes.

conda -n pyoccenv python=3.8.

conda activate pyoccenv.

conda install -c conda-forge pythonocc-core.

python -c "import OCC; print(OCC.VERSION)"

conda install -c conda-forge pyside2.

now the environment to be created for python occ.

run the occ.py file on anaconda command prompt.

Now the .stl file converted to .step file
