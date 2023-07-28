#Install the custom library         
# 1. Create a virtual environment

sudo apt install python3.10-venv

python3 -m venv temp_venv

source temp_venv/bin/activate


pip --version

# 2. Install numpy package in the virtual environment (version 1.22.4 or higher, but lower than 2.0.0)

pip install numpy

# 3. Generate a requirements.txt file

python3 -m pip freeze > requirements.txt
       
# 4. Write a script that imports numpy. Execute code from their site (https://numpy.org/) and run it on a local computer\

python -m pip install -r requirements.txt

# 5. As a result, you should send a screenshot of the executed code on your machine, requirements.txt and a .py file

