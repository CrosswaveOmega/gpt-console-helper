# gpt_console_helper


A simple command line tool that asks gpt-3.5-turbo how to do shell commands. 


## Install it from Github

```bash
pip install git+https://github.com/CrosswaveOmega/gpt-console-helper.git
```

Ensure that you've set the OPENAI_API_KEY enviornment variable to your API key before use.


## Usage

```py
from gpt_console_helper import run_sync

BaseClass().base_method()
base_function()
```

```bash
$ python -m howto "How do I tarball this directory."
#or
$ howto "How do I tarball this directory."
```
