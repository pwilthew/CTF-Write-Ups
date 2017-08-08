# Captured Mail
## Challenge: We intercepted this mail message. Can you open the attachment?

With Wireshark:

![WIRESHARK]()

![WIRESHARK]()

That looks like Base 64 encoded text. Using an online base64 decoder:

![BASE64DECODER]()

We get a zip file that contains flag.txt
```
$- unzip decoded.zip
Archive:  decoded.zip
  inflating: flag.txt 
$- cat flag.txt
Congratulations, the flag for this challenge is flag{1b5978777658baca99ce653af6fa596e}.
```
