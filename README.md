## Contrast Python Sdk

## Usage
The endpoints available through this module are available through a ContrastSdk object.
contrast_sdk = ContrastSdk('username', 'api_key', 'service_key', 'teamserver_url')

### Developing
Use pip to install the projects dependencies
```commandline
    pip install -r requirements.txt
```

To run the tests edit tests/test-config.json with local teamserver information.
An example file can be seen in tests/test-config.json.example

**Note:** The url validation does not accept localhost as a TeamServer url. 
 If you are running TeamServer locally please use: http://127.0.0.1:19080/Contrast as your teamserver_url

```commandline
    nosetests
```