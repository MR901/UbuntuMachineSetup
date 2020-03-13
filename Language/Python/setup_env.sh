
echo
echo "----------------------------------------------------------------------"
echo Creating Virtual Environment for RASA has been created at $(pwd)/resources/virtual_env
echo "----------------------------------------------------------------------"
virtualenv -p python3 $(pwd)/resources/virtual_env
echo "| Complete"
echo

echo "----------------------------------------------------------------------"
echo Activating the Environment
echo "----------------------------------------------------------------------"
source $(pwd)/resources/virtual_env/bin/activate
echo "Current Python3 is used"
which python3
echo "| Complete"
echo

echo "----------------------------------------------------------------------"
echo Installing Required Packages in the Virtual Environment
echo "----------------------------------------------------------------------"
pip3 install -r $(pwd)/resources/requirements.txt
echo
echo "Following packages are present inside the Virtual Environment"
pip3 freeze
echo "| Complete"
echo

echo "----------------------------------------------------------------------"
echo Creating Jupyter ipykernel with the name RasaEnv
echo "----------------------------------------------------------------------"
python3 -m ipykernel install --name RasaEnv --display-name "RasaEnv"
echo
echo "Following kernels are present inside jupyter"
jupyter kernelspec list
echo
echo "Kernel Information"
cat /usr/local/share/jupyter/kernels/rasaenv/kernel.json
echo "| Complete"
echo

# jupyter kernelspec list
# jupyter kernelspec remove rasaenv


$(pwd)/resources/virtual_env/bin/python3 -m spacy download en_core_web_md
$(pwd)/resources/virtual_env/bin/python3 -m spacy link en_core_web_md en
$(pwd)/resources/virtual_env/bin/python3 -m spacy download en



echo "----------------------------------------------------------------------"
echo Deactivating the Environemt
echo "----------------------------------------------------------------------"
deactivate
echo "| Complete"
echo
