Get data from the [NYC Crime Map](http://maps.nyc.gov/crime/),
and save them as geojson files.

## Check out

    git clone git://github.com/tlevine/nyc-crime-map.git --recursive
    cat nyc-crime-map/data/02378420399528461352-17772055697785505571.geojson

## Run

    ./crime.py

(This won't do much if you've already downloaded the `./data` directory.)

## More about the data
The data are stored in two tables.

* 02378420399528461352-11853667273131550346
* 02378420399528461352-17772055697785505571

The latter of these tables contains a "CR" field for the crime type;
the former does not.
