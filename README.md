# Setup

Python 3.4.3 or later required. 

If you use virtualenv, create virtualenv and activate it.

    $ virtualenv --no-site-packages venv
    $ source venv/bin/activate

To install required package, run pip install as follows

    $ pip install -r requirements.txt

# Run scripts

    $ ipython --matplotlib
    In [1]: %run chapter/ch1_1.py

To clean namespace in IPython interactive session, run %reset magic command.

    In [2]: %reset -f
