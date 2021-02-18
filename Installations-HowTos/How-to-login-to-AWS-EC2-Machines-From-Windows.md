# Login to EC2 Machines

Windows.

In Windows, we’ll assume that you are using the PuTTY suite of tools.

https://www.putty.org/

# You need to download
putty.exe and puttygen.exe from here
https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html

1. First fre up PuTTYgen. Click "Load" and then in the fle type drop-down menu, choose "all fles".

2. Then select "MyFirstKeyPair.pem" (your .pem fle will have a diferent name, depending upon what you called your key pair).

3. Then choose "save" and save your fle as "MyFirstKeyPair" in an appropriate directory, where 
you can find it (again, use the name that you chose above; PuTTYgen will add a .ppk 
extension to the fle you are saving) and "yes" to choose to save the fle without paraphrase.

4. Next, fre up PuTTY. This will allow you to connect to your Amazon machine via SSH. In the
left-hand side of the dialog that comes up, click "Connection" then "ssh" then "auth" and then
click on "Browse" to select the private key fle that you created above using PuTTYgen.
Then Connect. 

Important: Never share your .pem fle.  
