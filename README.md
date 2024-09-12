## Prerequisites

- Python 3.x

## File Structure

- `main.py`: The main script to run the analysis
- `flow_logs.txt`: Input file containing VPC flow logs (without header)
- `look_up.txt`: Lookup file with headers (dstport, protocol, tag)
- `output/`: Directory where the output file will be saved

## Input File Formats

### flow_logs.txt

This file should contain VPC flow logs without a header. The format follows the AWS VPC Flow Logs structure:
https://docs.aws.amazon.com/vpc/latest/userguide/flow-log-records.html#flow-logs-fields

```
version account-id interface-id srcaddr dstaddr srcport dstport protocol packets bytes start end action log-status
```

Example:

```
2 123456789012 eni-0a1b2c3d 10.0.1.201 198.51.100.2 443 49153 6 25 20000 1620140761 1620140821 ACCEPT OK
```

### look_up.txt

This file should have a header and contain lookup information:

```
dstport,protocol,tag
```

## Protocol Numbers

The script uses protocol numbers as defined by IANA. You can find the full list here:
https://www.iana.org/assignments/protocol-numbers/protocol-numbers.xhtml#protocol-numbers-1

## Usage

To run the analysis:

```
python3 main.py
```

The output file will be generated in the `output/` directory.

## Notes

- Ensure that `flow_logs.txt` and `look_up.txt` are in the same directory as `main.py`
- The script assumes that `flow_logs.txt` does not have a header, while `look_up.txt` does have a header
- You can replace `flow_logs.txt` and `look_up.txt` with your own test files, but keep the same file names
