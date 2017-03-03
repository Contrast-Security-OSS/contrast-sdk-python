## Contrast Python Sdk

## Usage
The endpoints available through this module are available through a ContrastSdk object.
contrast_sdk = ContrastSdk('username', 'api_key', 'service_key', 'teamserver_url')

contrast_sdk.applications_api.get_applications()
### Developing
Use pip to install the projects dependencies
```commandline
    pip install -r requirements.txt
```

To run the tests
```commandline
    nosetests
```