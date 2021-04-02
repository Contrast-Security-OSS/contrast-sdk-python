from setuptools import setup

setup(
  name='contrast-security',
  packages=['contrast_security', 'contrast_security/filters', 'contrast_security/types', 'contrast_security/user_api'],
  version='0.17',
  description='Module to easily interact with the Contrast api',
  author='Contrast Security',
  author_email='integrations@contrastsecurity.com',
  url='https://github.com/Contrast-Security-OSS/contrast-sdk-python',
  download_url='https://github.com/Contrast-Security-OSS/contrast-sdk-python/releases',
  keywords=['contrast', 'security', 'iast', 'sast', 'rasp'],
  classifiers=[],
  install_requires=[
    'requests',
    'validators'
  ],
)
