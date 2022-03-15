# Python IP scanner
Python file made to scan for websites.



## Download
```
git clone https://github.com/pipe05/ip-scanner
```



## Usage
### Domains
To add the desired domain(s), you can edit the variable ***domains*** to include any domain you may like (etc., .com, .net)
Example
```
domains = (".com", ".net", ".org")
```
### Domain name limit
The domain name limit randomly selects a number between the set range
To limit the length of the domain name you can change variable ***length*** on line *26*
```
length = random.randint(x, y)
```
### Dump File
Upon finding a valid address the program will dump the IP and the time found to the file *ipadresses.txt* by default. To change it edit:
```
f = open("filename.txt", "a")
```
On some linux systems you must run the program as *sudo* to write the file.
