# CRM ( Customer Relationship Management) Application for SMBs
A quick CRM application I developed for Deca.

# Product Live Demo
<img width="231" alt="IMG_2982" src="https://github.com/user-attachments/assets/9187274f-aced-4ff6-99c6-1f445965b843" />

OR 

Click on the following URL:
https://deca-crm-from-gaurang.streamlit.app/

# Achievements

Won district level DECA award for Solo.
![75850069084__1DBF50B1-0E83-4D91-9AB9-E83A2749E1C9](https://github.com/user-attachments/assets/f54a42b2-7aed-44fc-a095-3daff2401bdc)


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
