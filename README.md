# Langchain


### Cloning the repository
Choose the current working directory to the location where you want the cloned directory.\
To clone the remote repository to your locale, use the following command in your terminal:
```bash
$ git clone https://github.com/pan4a4os/Langchain/tree/a1e1e8bf3367459bbe8c7840e4fb0c9da35e3406
```

--------------------------------------------------------

### Set virtual environment
Creating virtual environments `venv`:
```bash
$ python -m venv venv
```

After creating the `venv`, your directory should look like this:
```bash
TestTask   <- Your project name
   ├── files/..
   ├── requirements/..
   ├── src/..
   ├── venv/..
   └── ...
```

If everything matches, then run the next command:
```bash
$ pip install -r requirements/base.txt
```

--------------------------------------------------------

### Starting localhost
To start localhost, you need to run this command:
```bash
$ uvicorn api:app --reload
```
from the `src` directory.

Press `Ctrl + C` to stop this process.

--------------------------------------------------------
## Postconditions
- pre-commit ([pre-commit installation document](https://pre-commit.com/#install)).

### Install pre-commit hooks
Install `pre-commit` into your git hooks:
```bash
$ pre-commit install
```


Check all files with `pre-commit`:
```bash
$ pre-commit run --all-files
```