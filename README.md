# Simple Whatsapp Bots
To run, follow these steps on command line:
 - Install yowsup library :
```git clone git://github.com/tgalal/yowsup.git
cd yowsup
sudo python setup.py install```

 - Register on Whatsapp using OTP method : You can check the country-code, mcc and mnc from this https://en.wikipedia.org/wiki/Mobile_country_code.

 ``` yowsup-cli registration --requestcode sms --phone <country-code><phone-number> --cc <country-code> --mcc <mcc> --mnc <mnc>```

 - You will receive an OTP on the mobile number mentioned in step above. Please use that otp for the last step of registeration.
  ```yowsup-cli registration --register <otp> --phone <country-code><phone-number> --cc <country-code> --mcc <mcc> --mnc <mnc>```

 - After completing the registeration process you will get a password for your phone number.
  Add your phone number and password in```config.py``` file.

```python run.py```

Now you can chat with this echobot by sending it whatsapp messages from any other number.

Need to dicuss shoot me a tweet at @imuditsrn.