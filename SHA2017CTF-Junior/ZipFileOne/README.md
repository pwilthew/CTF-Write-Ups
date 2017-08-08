# Zipfile One
## Challenge: We received this zip file, but is asking for a password. All we know is that the password exists of 5 numbers, can you crack this password to get the hidden information?

The file is effectively a zip file that asks you for a password. I first wrote a script that creates a dictionary of possible passwords; all the numbers that contain only 5 digits.

```bash
#!/bin/bash

i="9999"

while [ $i -lt 99999 ]
do
i=$[$i+1]
echo $i >> dic.txt
done
```
I installed fcrackzip, `sudo apt-get install fcrackzip`.

And ran `fcrackzip -b -D -p dic.txt -u zipfileone.zip`

Which returns:
```bash
 PASSWORD FOUND!!!!: pw == 42831
 ```
Unzip it and you are done!
```bash
$- unzip zipfileone.zip
Archive:  zipfileone.zip
[zipfileone.zip] flag.txt password: 
$- cat flag.txt` 
flag{d6f56ae046bb241cc61f9d26f8e525d9}
```
