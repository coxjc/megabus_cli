# megabus_cli
Basic CLI for [Megabus](https://megabus.com/) prices

## Usage 
Clone the repo to your host and run as follows:

```
megabus.py [COMMAND]
```

Available commands:
- `origin-cities`: Return all origin cities & their applicable information.
- `destination-cities`: Given an origin city, returns all possible destination cities. 
- `dates`: Given an origin and destination, returns available dates.
- `prices`: Given an origin, destination, time (date), and passenger count, returns a list of prices & their applicable information. 

Outputs are pretty printed by default but the `--raw` argument specifies JSON output.

## Requirements
The script requires Python 3.  Libraries used are: `click`, `json`, `requests`.
You may need to install `click` from [Pypi](https://pypi.python.org/pypi/click).

## Contribute
Please open an issue if you find a bug. Also, you're more than welcome to fork &
open a PR if you want to suggest changes! 
