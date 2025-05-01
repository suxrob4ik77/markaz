
# ssh root@64.226.105.129
# ssh-keygen
#  cat .ssh/id_rsa.pub
    # cd /var/
# mkdir www/
# cd www/
# git clone
# cd project/
# python3 -m venv venv
# source venv/bin/activate
# pip install -r requirements.txt
# python3 manage.py migrate
# python3 manage.py collectstatic
# sudo ufw 8000
# python3 manage.py runserver 0.0.0.0:8000
#

"""
1.
ssh-keygen
2.
cat .ssh/id_rsa.pub

3.

[Unit]
Description=gunicorn socket

[Socket]
ListenStream=/run/gunicorn.sock

[Install]
WantedBy=sockets.target

4.

[Unit]
Description=gunicorn daemon
Requires=gunicorn.socket
After=network.target

[Service]
User=root
Group=www-data
WorkingDirectory=/var/www/markaz
ExecStart=/var/www/markaz/venv/bin/gunicorn \
          --access-logfile - \
          --workers 3 \
          --bind unix:/run/gunicorn.sock \
          config.wsgi:application

[Install]
WantedBy=multi-user.target



5.


server {
    listen 80;
    server_name 207.154.245.36;

    location = /favicon.ico { access_log off; log_not_found off; }
    location /static/ {
       root /var/www/markaz;
    }

    location / {
        include proxy_params;
        proxy_pass http://unix:/run/gunicorn.sock;
    }
}
"""
