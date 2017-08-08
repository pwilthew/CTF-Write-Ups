#Wanna Buy A Flag?
##Challenge: Analyse this Network capure to get the flag.

To get the flag, we can open the .pcap with Wireshark and follow the TCP stream.

![WIRESHARK](https://github.com/pwilthew/CTF-Write-Ups/blob/master/SHA2017CTF-Junior/WannaBuyAFlag/Wireshark1.png)

![WIRESHARK](https://github.com/pwilthew/CTF-Write-Ups/blob/master/SHA2017CTF-Junior/WannaBuyAFlag/Wireshark2.png)

Then actually save you some time by `echo`ing the copied text into a file; like `echo "Copied text" > pastebin.txt`.

And finally, use `tr` with `-d` to delete newline characters:

```
 -$ cat pastebin.txt | tr -d '\n'
 Hello! Wanna buy a flag?Yes pleaseOk, but it will cost you some timeflag{f08574923ec9c9ffb47188e6edc1a20f}%
 ```

