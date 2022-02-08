###

# py_fedex_tracking

## Description

py_fedex_tracking is a python3 library which will fetch the tracking details
for a fedex tracking number

## Installation

```
python3 -m pip install  git+https://github.com/rhhayward/py_fedex_tracking.git@master
```

## Usage

```
from fedex_tracking import FedexTracker

tracker = FedexTracker()
result = tracker.get_tracking('123456789098')
print("estimated delivery date/time={}".format(result['estDeliveryDateTime']))
print("status={}".format(result['status']))
print("lastScanStatus={}".format(result['lastScanStatus']))
print("lastScanDateTime={}".format(result['lastScanDateTime']))
```
