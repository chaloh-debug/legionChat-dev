web: daphne -e ssl:443:privateKey=key.pem:certKey=crt.pem legionChat.asgi:application -v2
worker: python manage.py runworker --settings=legionChat.settings -v2

