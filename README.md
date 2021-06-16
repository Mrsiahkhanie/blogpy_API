# blogpy_API
BlogpyApiSubmitArticleAndSerializers

virtualenv -p python3 .venv

source .venv/bin/activate

.venv:
      pip install -r requirements/requiremnent.txt
      
      ./manage.py createsuperuser
      
      ./manage.py runserver
