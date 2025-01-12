# CRM ( Customer Relationship Management) Application for SMBs
A quick CRM application I developed for Deca.

# How to setup and run?
## On AWS Cloud 

Run an Amazon Linux micro environment based container image.
Clone this repo. And change directory in to this folder.
```
git clone https://github.com/pendyalagaurang/deca-crm.git
cd deca-crm/
```
Enable Python Virtual Enviroment.

```
python3 -m venv deca-crm-app.venv
source deca-crm-ap.venv/bin/activate
```

Upgrade PIP
```
pip install --upgrade pip
```

Install python libraries from the provided requirements.txt
```
pip install -r requirements.txt
```

Now you are all set and ready to run the app.
```
streamlit run crm-app.py
```

The output may look like this. Simply open the External URL in a browser to start accessing the application.

```
$ streamlit run crm-app.py
Collecting usage statistics. To deactivate, set browser.gatherUsageStats to false.


  You can now view your Streamlit app in your browser.

  Local URL: http://localhost:8501
  Network URL: http://172.xx.yy.zz:8501
  External URL: http://44.XXX.YYY.ZZZ:8501

```
