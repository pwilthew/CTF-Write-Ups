# Captured Mail
## Challenge: We intercepted this mail message. Can you open the attachment?

With Wireshark:

![WIRESHARK](https://github.com/pwilthew/CTF-Write-Ups/blob/master/SHA2017CTF-Junior/Captured%20Mail/Wireshark1.png)

![WIRESHARK](https://github.com/pwilthew/CTF-Write-Ups/blob/master/SHA2017CTF-Junior/Captured%20Mail/Wireshark2.png)

That looks like Base 64 encoded text. Using an online base64 decoder:

![BASE64DECODER](https://github.com/pwilthew/CTF-Write-Ups/blob/master/SHA2017CTF-Junior/Captured%20Mail/Base64Decoder.png)

We get a zip file that contains flag.txt
```
$- unzip decoded.zip
Archive:  decoded.zip
  inflating: flag.txt 
$- cat flag.txt
Congratulations, the flag for this challenge is flag{1b5978777658baca99ce653af6fa596e}.
```
