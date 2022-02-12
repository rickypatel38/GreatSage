#Pre-requisite script
# do sudo apt-get update --fix-missing first

echo "Pre-requisites are being installed onto this Operating System."

if sudo apt-get install python3.7; then
    echo "Python3.7 Installed Successfully.."
    echo "Installing other dependencies"
else    
    echo "Python3.7 Installation failed..."
    echo "Exiting..."
    exit 1
fi 

if sudo apt-get remove python2.7; then
    echo "Python 2.7 REMOVED"
    echo "Installing other dependencies"
else
    echo "Python 2.7 not removed"
    echo  "Exiting..."
    exit 1
fi

if sudo apt-get install libpq-dev; then
    echo "libpq-dev Installed Successfully..."
else
    echo "libpq Installation failed..."
    echo "Exiting..."

if sudo apt-get install python3-pip; then 
    echo "Python-PIP Installed Successfully..."
    echo "Installing other dependencies"
else
    echo "Python-PIP Installation failed..."
    echo "Exiting..."
    exit 1
fi

if sudo apt-get install build-essential python-dev; then 
    echo "build-essential python-dev Installed Successfully..."
    echo "Installing other dependencies"
else
    echo "build-essential python-dev Installation failed..."
    echo "Exiting..."
    exit 1
fi

echo "Installing pipenv...."
if pip3 install pipenv; then
    echo "pipenv installed successfully"
else
    echo "pipenv installation failed..."
    echo "Exiting..."
    exit 1
fi 

echo "Installing dlipower...."
if pip3 install dlipower; then
    echo "dlipower installed successfully"
else
    echo "dlipower installation failed..."
    echo "Exiting..."
    exit 1
fi 
