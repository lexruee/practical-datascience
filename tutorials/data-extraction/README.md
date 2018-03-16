# Data Exctration
Examplae data extraction from eth-based blockchains.

## Dependencies

 * a local [ellaism node](https://ellaism.org/install/)
 * python3 
 * [matplotlib](https://github.com/matplotlib/matplotlib)
 * [web3.py](https://github.com/ethereum/web3.py)

You can install the Python deps via `pip`:

```
pip install matplotlib web3
```

## Usage

```
./data_extractor.py -h
usage: data_extractor.py [-h] [-V] [-a JSONRPC] [-s START_BLOCK]
                         [-e END_BLOCK] [-r SAMPLING_RATE] [-o OUTPUT]

ethdx - Simple tool to extract data from eth blockchains

optional arguments:
  -h, --help            show this help message and exit
  -V, --version         Print version number.
  -a JSONRPC, --jsonrpc JSONRPC
                        Set JSONRPC URL address.
  -s START_BLOCK, --start-block START_BLOCK
                        Set start block.
  -e END_BLOCK, --end-block END_BLOCK
                        Set end block.
  -r SAMPLING_RATE, --sampling-rate SAMPLING_RATE
                        Set sampling rate (value r e [0,1]).
  -o OUTPUT, --output OUTPUT
                        JSON output file.
```

## Example Usage

Extracting data from the genesis block to the latest block:

```
./data_extractor.py -a http://localhost:8545 -o ella.json --end-block -1 -r 0.1 
```



```
./diff_plotter.py -i ella.json --show  
```



![](https://raw.githubusercontent.com/lexruee/practical-datasience/master/tutorials/data-extraction/ella-diff.png)
