# Location
## Like in real estate, the web is all about location, location and _location_. 

The third "location" is just a link to `http://location.stillhackinganyway.nl/`

![SITE](https://github.com/pwilthew/CTF-Write-Ups/blob/master/SHA2017CTF-Junior/Location/Screen%20Shot%202017-08-07%20at%2021.23.35.png)

I noticed that it was taking approximately 2 seconds to reload after clicking on that 'here' link. 

In the Inspect interface, I was able to see what was actually happening during those seconds and took a screenshot. Putting those strings together and changing `%7b` and `%7d` for `{` and `}` will get the flag.
