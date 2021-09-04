echo "***Install sshpass to get rid of enter password***"
sudo apt-get install sshpass

echo "***Copy image, compose and env file***"
sshpass -p 'password' scp ~/path/to/tar_name.tar user_name@ip_address:/path/to/tar
sshpass -p 'password' scp ~/path/to/docker-compose-prod.yml user_name@ip_address:/path/to/compose-file

echo "***Load image***"
sshpass -p 'password' ssh user_name@ip_address docker load -i /path/to/tar

echo "***Run project***"
sshpass -p 'password' ssh user_name@ip_address docker-compose -f /path/to/compose-file/docker-compose-prod.yml up -d