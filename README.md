# unemp-report-07.30.24

## Setup

Create virtual environment:

```sh
conda create -n ump-env python=3.11
```

Activate the environment

```sh
conda activate unemp-env
```

Install packages:

```sh
# best practice to list the packages in the requirements.txt file
pip install -r requirements.txt
```

Access API Key from ALPHAVANTAGE
Also create a ".env" file in the root directory of the repo, and paste some contents in like this

## Usage

Run the script:

```sh
#python app/unemp.py

# equivalent (modular command) --> need to use this when importing files across each other
python -m app.unemp
```

stocks report:

```sh
python -m app.stocks