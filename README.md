# WhoCan
## Installation
WhoCan requires Google Cloud Application Default Credentials (ADC) with access to the Google Cloud Platform project. Install the gCloud CLI by following the instructions [here](https://cloud.google.com/sdk/docs/install).
Once the gCloud CLI has been installed, follow [these](https://cloud.google.com/docs/authentication/provide-credentials-adc#local-user-cred) instructions to configure your ADC.

Lastly, create a constants.py file with the line
```python
PROJECT = "my_project_name"
```
Where *my_project_name* is replaced with your gCloud Project ID