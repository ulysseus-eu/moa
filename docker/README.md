# Docker install
We provide a tutorial for an easy docker installation based on Phusion Passenger image but feel free to do your own based on other ligher images if you wish so.
Please share with us all the work you're doing in that direction.
## Copy template files into real ones
```bash
cp defaults-template.py defaults.py
cp moa-template.conf moa.conf
cp docker-compose-template.yml docker-compose.yml
```
## Build image
Traditional production deployment would encourage you to version the base image you use and the image you generate.  
For simplicity purpose, you can just go for:
```bash
docker build -t moa-passenger .
```
## Setup your certificates
### For Local DEV
#### Install mkcert
Certificates can be generated with [`mkcert`](https://github.com/FiloSottile/mkcert), this software allows you to register your own CA so there is no security warning. It is a better solution than the self signed certificates from [ssl.](https://stackoverflow.com/questions/10175812/how-to-generate-a-self-signed-ssl-certificate-using-openssl)

Install for macOs : `brew install mkcert`  
or if you use Linux, build from source :
```console
sudo apt install libnss3-tools
git clone https://github.com/FiloSottile/mkcert && cd mkcert
go build -ldflags "-X main.Version=$(git describe --tags)"
```
or from prebuilt packages : https://github.com/FiloSottile/mkcert/releases
#### Generation of certificates
Generate the certificates.  
```bash
echo What will be the domain for your end users?;read your_domain
mkcert &your_domain
mkdir certificates
mv ${your_domain}.pem certificates/
mv ${your_domain}-key.pem certificates/${your_domain}.key
chmod 600 certificates/${your_domain}.key
```
#### Redirection of server URL
If you're on Linux and for the time of your tests, update your /etc/hosts file
```bash
echo '127.0.0.1 '${your_domain} | sudo tee -a /etc/hosts
```
Don't forget to remove it as soon as you have your own domain and server
### For production - not tested
Not tested suggestion as I cannot issue certificate from certbot on my domain  
USE WITH CAUTION  
After having a domain name pointing to your instance, install and setup certbot  
```bash
echo What will be the domain for your end users?;read your_domain
cat 'apt install certbot python3-certbot-nginx' >> create_db.sh
cat 'certbot --nginx -d '$your_domain >> create_db.sh
```
-----------------
## Update your settings
You shall update your nginx configuration and put your server domain
```bash
echo What will be the domain for your end users?;read your_domain
sed -i -e "s/<your_domain>/${your_domain}/g" moa.conf docker-compose.yml
```
You shall update your defaults.py configuration
```bash
cp defaults-template.py defaults.py
echo What is your twitter consumer key?;read twitter_consumer_key
sed -i -e "s/<your_consumer_key>/${twitter_consumer_key}/g" defaults.py
```
You can do the same with your_instagram_client_id and your_email_user_name  

You shall add your secrets in the secrets directory
```bash
mkdir secrets
touch secrets/SECRET_KEY_PASS secrets/TWITTER_PASS secrets/SMTP_PASS secrets/INSTAGRAM_PASS
chmod 600 secrets/SECRET_KEY_PASS secrets/TWITTER_PASS secrets/SMTP_PASS secrets/INSTAGRAM_PASS
echo What is your MOA secret key?;read secret_key
echo $secret_key > ./secrets/SECRET_KEY_PASS
echo What is your twitter secret?;read twitter_secret
echo $twitter_secret > ./secrets/TWITTER_PASS
```
You can do the same with instagram secret => INSTAGRAM_PASS and SMTP password => SMTP_PASS

## Launch your moa server
We're done
```bash
docker-compose up -d
```

