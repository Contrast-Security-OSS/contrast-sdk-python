from distutils.core import setup

setup(
  name='contrast_security',
  packages=['contrast_security', 'contrast_security/filters', 'contrast_security/types', 'contrast_security/user_api'],
  version='0.12',
  description='Module to easily interact with the Contrast api',
  author='Donnie Propst',
  author_email='donald.propst@contrastsecurity.com',
  url='https://github.com/Contrast-Security-OSS/contrast-sdk-python',
  download_url='https://github.com/Contrast-Security-OSS/contrast-sdk-python/archive/0.1.tar.gz',
  keywords=['contrast', 'security'],
  classifiers=[],
  install_requires=[
    'requests',
    'validators'
  ],
)
