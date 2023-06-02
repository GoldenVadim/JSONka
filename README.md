# JSONka
The JSON parser written in Python. You can use it as module.
### Documentation
#### Installation guide
To install this package via terminal use this command:
```shell
pip install jsonka
```
#### Functions
`add_key(key,value)` - Adds key to JSON object.<br>
`change_key(key,new_value)` - Changes the value in key.<br>
`clear()` - Clears the non-parsed JSON.<br>
`parse()` - Parses and returns a real JSON object. *JSON()*`.parsed` is a value of parsed JSON.<br>
`to_bytes()` - Converts and returns the parsed JSON to bytes.
#### Examples
To parse and print this JSON `{"Name":"Vadim"}` you need to use this code below:
```python
from JSONka import JSON

with JSON() as JSONObject:
    JSONObject.add_key('Name','Vadim')
    print(JSONObject.parse())
```
