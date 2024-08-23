import smtplib
from email.mime.text import MIMEText
from email.header import Header
from tqdm import tqdm
import pandas as pd
import requests
import json
import yaml

def read_config(config_path='config.yaml'):
    with open(config_path, 'r', encoding='utf-8') as file:
        config = yaml.safe_load(file)
    return config

def read_xlsx(path):
    df = pd.read_excel(path)
    columns_of_interest = ['姓名', '邮箱', 'Username', 'Password']
    df_filtered = df[columns_of_interest]
    return df_filtered

def send_email(sender, auth_code, nickname, receiver, subject, text):
    message = MIMEText(text, 'html', 'utf-8')
    message['From'] = Header(f"{nickname}<{sender}>", 'utf-8')
    message['Subject'] = Header(subject, 'utf-8')
    message['To'] = Header(f"Receiver<{receiver}>", 'utf-8')
    
    try:
        server = smtplib.SMTP_SSL('smtp.qq.com')
        server.login(sender, auth_code)
        server.sendmail(sender, receiver, message.as_string())
        server.close()
    except smtplib.SMTPException as e:
        return False, str(e)
    return True, None

def main():
    config = read_config()
    data = read_xlsx(config['send']['data_path'])
    
    sender = config['send']['sender']
    auth_code = config['send']['auth_code']
    nickname = config['send']['sendernickname']
    subject = config['send']['subject']
    url = config['send']['backend_url']
    
    fails = []
    
    print('Begin to send message...')
    print(f'共 {len(data)} 名参赛者')

    for _, row in tqdm(data.iterrows()):
        name = row['姓名']
        receiver = row['邮箱']
        username = row['Username']
        password = row['Password']
        ret = {
            'name': name,
            'username': username,
            'pwd': password,
        }
        
        header = {'Content-Type': 'application/json'}
        response = requests.post(url, headers=header, data=json.dumps(ret))
        text = response.text
        
        success, error = send_email(sender, auth_code, nickname, receiver, subject, text)
        if not success:
            fails.append(receiver)
            print(f"Error: 无法发送邮件，失败邮箱为：{receiver} ，失败原因为： {error}")

    print('End to send message...')
    print(f'发送失败 {len(fails)} 封, 为 {fails}')

if __name__ == "__main__":
    main()
