# FreeBitcoin.in-claimer
Freebitcoin.io free claimer with and without captcha

create .env file and add email and password of your account

#1st edit

I forgot to add loop to rerun code every 60 min.
to rerun code every 60min you can add fuction after importing and user agent as 
 def perform_actions():
( entire code here even driver quit )
then call the entire function at last as 
while True:
    perform_actions()
    time.sleep(3600) 
this will rerun the code every 60min but you cant close the ide/prompt running

also you can copy the script and env file into startup folder in your C drive so it runs code everytime you turn on your pc
you can also write a bash script that checks if the file is running and runs the file if its not running
