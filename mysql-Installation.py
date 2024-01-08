# ******--    My-SQL Installation Procedure For Ubuntu
# 
# ----------- https://www.youtube.com/watch?v=zRfI79BHf3k

# sudo apt update
# sudo apt upgrade
# sudo apt install mysql-server           # install mysql software from ubuntu
# sudo systemctl status mysql.service     # to check the status of installation
# sudo mysql                              # to enter in mysql shell
# ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'your password';
# *** paste the above query to create root user/password for localhost
# sudo mysql_secure_installation          # start installation process and follow the instruction
# sudo mysql -u root -p                   # login to the mysql root user

# To install msql workbench community version follow the link below
# https://snapcraft.io/mysql-workbench-community 
# or search "snap mysql-workbench-community" in google
# select stable version copy the commandline link

# sudo snap install mysql-workbench-community