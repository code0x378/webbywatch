WebbyWatcher is a simple web page change notifier.  It just watches web pages then sends an email (and logs) 
when keywords are no longer included in the page content.  I use it to be notified when products are available again.

# Requirements

* python

# Installation

Rename .env.example to .env and edit the contents as needed

```
python -m venv venv
. venv/bin/activate
pip install -r requirements.txt
python webbywatch.py
```


