# megabus_cli
Basic CLI for [Megabus](https://megabus.com/) prices

## Usage 
Clone the repo to your host and run as follows:

```
usage: megabus.py [-h] [-o ORIGIN] [-d DEST] [-t TIME] [-p PASSENGERS] command

positional arguments:
  command               'origin_cities', 'dest_cities', 'dates', or 'prices'

optional arguments:
  -h, --help            show this help message and exit
  -o ORIGIN, --origin ORIGIN
                        origin city ID
  -d DEST, --dest DEST  destination city ID
  -t TIME, --time TIME  date of departure in format: 'YYYY-MM-DD'
  -p PASSENGERS, --passengers PASSENGERS
                        number of passengers
```

- `origin_cities`: Return all origin cities & their applicable information.
- `dest_cities`: Given an origin city, returns all possible destination cities. 
- `dates`: Given an origin and destination, returns available dates.
- `prices`: Given an origin, destination, time (date), and passenger count, returns a list of prices & their applicable information. 

**All outputs are in JSON.**

## Requirements
The script requires Python 3.  Libraries used are: `argparse`, `json`, `requests`. All of these are likely already companionated with your Python 3 installation. 

## Contribute
Please open an issue if you find a bug. Also, you're more than welcome to fork & open a PR if you want to suggest changes! 
