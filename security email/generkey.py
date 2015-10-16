import os 
import gnupg

#os.system('rm -rf /home/yufangxian/program/gpghome1/')
gpg=gnupg.GPG(gnupghome=raw_input('key path(save):'))
input_data=gpg.gen_key_input(name_email=raw_input('name_email:'),passphrase=raw_input('passphrase:'))
key=gpg.gen_key(input_data)

print key

