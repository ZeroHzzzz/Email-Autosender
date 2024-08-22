# 邮件群发程序

## 简介

本项目旨在创建一个邮件生成和发送的系统，主要用于自动化邮件生成和发送流程。项目中包含 Python 脚本和 HTML 模板，能够动态生成个性化邮件内容并通过指定的发送功能发送邮件。

## 功能

-   邮件生成：通过 HTML 模板生成个性化邮件内容。
-   邮件发送：使用 send.py 脚本发送生成的邮件。

## 文件说明

项目的文件结构为：

```tree
│- backend.py
│- data.xlsx
│- sender.py
│- requirements.txt
|- config.yaml
│- README.md
│
└─templates\
    templates.html
```

-   backend.py：后端处理逻辑，包含邮件内容的生成和数据处理。
-   sender.py：负责发送邮件的功能模块。
-   templates.html：邮件的 HTML 模板，用于定义邮件的样式和内容。
-   config.yaml：配置文件，包含邮件发送的所有配置信息。

## 使用

1. 克隆项目

```bash
git clone https://github.com/your-repo/email-sender.git
cd email-sender
```

2. 安装依赖

```bash
pip install -r requirements.txt
```

3. 配置文件
   在运行程序前，请确保在项目根目录下创建并正确配置 config.yaml 文件。配置文件的示例如下：

```yaml
backend:
    port: 5000
send:
    sender: "your-email@example.com"
    sendernickname: "Your Name"
    auth_code: "your-smtp-auth-code"
    subject: "邮件主题"
    backend_url: "http://127.0.0.1:5000/email"
    data_path: "data.xlsx"
```

**配置文件说明**

-   backend.port：Flask 服务器运行的端口号。
-   send.sender：发送邮件的邮箱地址。
-   send.sendernickname：发件人昵称。须符合对应邮箱的 From 合法性检查
-   send.auth_code：发送邮箱的 SMTP 授权码。
-   send.subject：邮件主题。
-   send.backend_url：邮件内容生成的后端 URL。
-   send.data_path：Excel 数据文件的路径。

1. 数据
   将包含收件人信息的 Excel 文件放置在项目目录中，并确保该文件的路径与配置文件中的 data_path 一致。Excel 文件需确保包含以下列：

-   姓名
-   邮箱
-   Username
-   Password

5. 运行项目
   首先运行`backend.py`文件，然后再运行 `sender.py`
