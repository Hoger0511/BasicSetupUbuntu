# BasicSetupUbuntu
Join me to create a Linux server with Ubuntu

## Step 1 
>1. Download [Rasberry Imager](https://www.raspberrypi.com/software/).
>2. Download Ubuntu on your SD
>3. Put you SD in your Laptop
<img src="https://i.imgur.com/YhBR0cL.png">
>4. Go to operating system 
>5. Find "Other general-purpose OS"
<img src="https://i.imgur.com/CkIYHjG.png">
>6. Choose Ubuntu and download it
>7. Go to storage choose your SD card.

## Step 2 
set up Ubuntu

>1. choose your language  
>2. choose your keyboard
>3. choose your time zone
>4. continue and let ubuntu download
>5. Ubuntu is ready for use

## Step 4
Setup SSH and MariaDB

> 1. Open your Ubuntu 
> 2. go to cmd
> 3. Type
> ```  sudo apt-get install openssh-server ``` 
> 4. then your SSH is ready you can start SSH
> 5. Open PowerShell as administrator.
> 6. if you want to connect it to your laptop type
 ```ssh username@ip-address```

Now you have connected your laptop to your Ubuntu server with SSH.

## MariaDB 

> 1. Download [MariaDB](https://mariadb.org/download/?t=mariadb&p=mariadb&r=11.5.2&os=windows&cpu=x86_64&pkg=msi&mirror=dotsrc) 
> 2. Go to CMD and type ```Sudo MariaDB```
when this is done you can test it by typing
> 1. Create Database "Name of your database";
> 2. Use "Name of your Database";
Then your done your ready to test the Files connected to this repository.
