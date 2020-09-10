# nethserver-meshcentral

nethserver-meshcentral integrates MeshCentral remote monitoring and management server

## Installation

Letsencrypt and a virtualhost name are needed for MeshCentral to work.

  config setprop meshcentral VirtualHost somehost.tld

  yum -y install nethserver-meshcentral

## Enable Mail Validation
 
  config setprop meshcentral MailValidation enabled

If you do not use the local mail server or like to edit "From" address

  config setprop meshcentral MailHost mail.somehost.tld
  config setprop meshcentral MailPort 993
  config setprop meshcentral MailFrom user@somehost.tld
  config setprop meshcentral MailTLS enabled

## Customize MeshCentral

  config setprop meshcentral Title 'My NethCentral'
  config setprop meshcentral Title2 'This is my NethCentral Server'
  config setprop meshcentral TitlePicture 'title.png'
  config setprop meshcentral LoginPicture 'login.png'

## Apply configuration change

  signal-event nethserver-meshcentral-update

## Upgrade MeshCentral

To upgrade meshcentral to the latest version:

  signal-event nethserver-meshcentral-upgrade

## NethServer install howto

https://community.nethserver.org/t/howto-install-meshcentral-on-nethserver/15331

## ToDo

Test, test, test
