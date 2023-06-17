acme.sh --issue --server letsencrypt -d lyaman-askerova.kz -w /var/www/local_static --config-home
/acme.sh

acme.sh --install-cert -d lyaman-askerova.kz --config-home /acme.sh --key-file
/etc/nginx/certs/key.pem --fullchain-file /etc/nginx/certs/cert.pem --reloadcmd "nginx -s reload"
