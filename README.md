## Setup guide
<ol>
    <li> Create virtual environment
        <code>python -m venv venv</code>
    </li>
    <li> Activate venv
        <code>source venv/bin/activate</code>
    </li>
    <li> Install requirements
        <code>pip install -r requirements.txt</code>
    </li>
    <li> Export flask settings
        <code>export FLASK_APP=app</code>
    </li>
    <li> Run flask
        <code>flask run</code>
    </li>
</ol>


## For test run:
python -m pytest tests/
