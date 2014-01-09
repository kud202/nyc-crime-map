People have been complaining a lot about how you can't get the raw data out of this
[NYC Crime Map](http://maps.nyc.gov/crime/). I don't know what they're talking about.

## API for the data
Go to the crime map, and look at the network requests that are being made.
You'll see a bunch of calls to the Google Maps Engine API.

![A network request in the console in Firefox](firefox.png)

Look at one of them, and you'll see the exact query that is being made.

![A window with more information about the request](request-window.png)

## Two tables
The data are stored in two tables.

* 02378420399528461352-11853667273131550346
* 02378420399528461352-17772055697785505571

The latter of these tables contains a "CR" field for the crime type;
the former does not.

I don't know why they do this.

## Getting the data as GeoJSON
I downloaded the full tables from the Google Maps Engine API,
so now you can download them as ordinary GeoJSON files, one per table.
Read more [here](https://github.com/tlevine/nyc-crime-map).
