from contrast.user_api.contrast_sdk import ContrastSdk

contrast_sdk = ContrastSdk('contrast_admin', 'demo', 'demo', 'http://127.0.0.1:19080/Contrast')
orgUuid = 'de7dd2a9-7643-46fb-b9d8-9c38aeffed7e'

print contrast_sdk.get_applications(orgUuid, params={'expand': 'skip_links'})
