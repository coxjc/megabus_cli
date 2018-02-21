# megabus_cli
Basic CLI for [Megabus](https://megabus.com/) prices

## Usage 
Clone the repository to your host and run as follows:

```
megabus.py [COMMAND]
```

Available commands:
- `origin-cities`: Return all origin cities and their applicable information.
- `destination-cities`: Given an origin city, returns all possible destination
  cities. 
- `dates`: Given an origin and destination (in that order), returns available
  dates.
- `prices`: Given an origin, destination, departure date, and passenger count
  (in that order), returns a list of prices & their applicable information. 

Outputs are pretty printed by default but the `--raw` argument specifies JSON output.

For detailed command documentation, run `megabus.py --help` and `megabus.py
[COMMAND] --help`.

## Requirements
The script requires Python 3.  External dependencies are listed in
`requirements.txt` and can be installed with:

```
python3 -m pip install -r requirements.txt
```

## Contribute
Please open an issue if you find a bug. Also, you're more than welcome to fork
and open a PR if you want to suggest changes! 
