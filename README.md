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

## Usage

Run the script:

```sh
python app/unemp.py

# equivalent:
python -m app.unemp
```