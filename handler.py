# serverless unzip step to reduce package size
try:
  import unzip_requirements
except ImportError:
  pass

import os
import logging
from datetime import datetime, date, timedelta

import requests
import pandas as pd
from dotenv import load_dotenv

load_dotenv()

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# START BUILD CSV
def fetch_pdf():
    if os.path.exists("./data/EOS-Report.pdf"):
        return
    logger.info("Downloading data file...")
    url = 'https://www.cisecurity.org/wp-content/uploads/2020/07/EOS-Report-July-2020.pdf'
    response = requests.get(url, stream=True)
    with open('./data/EOS-Report.pdf', 'wb') as f:
        f.write(response.content)

def parse_pdf():
    import camelot
    df_list = []
    tables = camelot.read_pdf('./data/EOS-Report.pdf', pages='1-end')
    for i in range(0, tables.n):
        df_list.append(tables[i].df)
    df = pd.concat(df_list)
    df = df.drop(columns=[4]) # empty column
    df = df.rename(columns={0:'Provider', 1:'Product', 2:'Version', 3:'EOS Date', 5:'Reference'})
    df['EOS Date'] = pd.to_datetime(df['EOS Date'], format="%m/%d/%Y")
    df.to_csv('./data/eos-report.csv', index=False)
# END BUILD CSV


def slack_alert(title, df_payload, icon=""):
    payload={
        "blocks": [
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    'text': icon + ' ' + title
                }
            }
        ]
    }
    print(df_payload)
    for index, row in df_payload.iterrows():
        payload['blocks'].append(
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": 'EOS ' + row['EOS Date'].strftime('%Y-%m-%d') + ': <' + row['Reference'] + '|' + row['Provider'] + ' ' + row['Product'] + ' ' + row['Version'] + '>'
                }
            }
        )
    import json
    print(json.dumps(payload))
    url = os.getenv("SLACK_WEBHOOK_URL")
    r = requests.post(url, json=payload)
    print(r.text)

def main(event, context):
    df = pd.read_csv('./data/eos-report.csv')
    #df['EOS Date'] = pd.to_datetime(df['EOS Date'])
    df = df.astype({'Provider':'str', 'Product':'str', 'Version':'str', 'EOS Date':'datetime64[ns]', 'Reference':'str'})
    today = datetime.now()
    todays_date = pd.Timestamp(today.date())
    if today.strftime("%d") == '01':
        print('ok')
        next_month = pd.Timestamp(today.date() + timedelta(days=31))
        eos_monthly = df[(df['EOS Date'] > todays_date) & (df['EOS Date'] < next_month)]
        if len(eos_monthly) > 0:
            logger.info("Sending monthly alert...")
            title = 'EOS Within 31 Days:'
            slack_alert(title, eos_monthly)
    eos_today = df[df['EOS Date'] == todays_date]
    if len(eos_today) > 0:
        logger.info("Sending daily alert...")
        title = 'EOS Today:'
        slack_alert(title, eos_today, icon=":exclamation:")

# for running locally (not on AWS lambda)
if __name__ == "__main__":
    main('','')
