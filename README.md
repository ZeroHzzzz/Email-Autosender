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

### 克隆项目

```bash
git clone https://github.com/your-repo/email-sender.git
cd email-sender
```

### 安装依赖

```bash
pip install -r requirements.txt
```

### 配置文件

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

### 数据

将包含收件人信息的 Excel 文件放置在项目目录中，并确保该文件的路径与配置文件中的 data_path 一致。Excel 文件需确保包含以下列：

-   姓名
-   邮箱
-   Username
-   Password

### 运行项目

首先运行`backend.py`文件，然后再运行 `sender.py`

## backend 接口说明

### Base URLs:

-   <a href="http://127.0.0.1:5000">开发环境: http://127.0.0.1:5000</a>

### Authentication

无

# Default

## GET 返回页面

> GET /email

### 请求参数

```json
{
    "name": "string",
    "username": "string",
    "pwd": "string"
}
```

| 名称       | 位置 | 类型   | 必选 | 说明 |
| ---------- | ---- | ------ | ---- | ---- |
| body       | body | object | 是   | none |
| » name     | body | string | 是   | none |
| » username | body | string | 是   | none |
| » pwd      | body | string | 是   | none |

### 返回结果

| 状态码 | 状态码含义                                              | 说明 | 数据模型 |
| ------ | ------------------------------------------------------- | ---- | -------- |
| 200    | [OK](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 成功 | Inline   |

#### 返回示例

将返回渲染完成的 html 页面

<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>邮件生成界面</title>
</head>

<body>
    <p>&nbsp;</p>
    <div>
        <div id="contentDiv" class="body" style="
                    position: relative;
                    font-size: 14px;
                    height: auto;
                    padding: 15px 15px 10px 15px;
                    z-index: 1;
                    zoom: 1;
                    line-height: 1.7;
                ">
            <div id="qm_con_body">
                <div id="mailContentContainer" class="qmbox qm_con_body_content qqmail_webmail_only" style="opacity: 1">
                    <table class="gwfw" style="
                                margin: 0;
                                padding: 0;
                                width: 100%;
                                height: 100%;
                            " border="0" width="100%" cellspacing="0" cellpadding="0" bgcolor="#ffffff">
                        <tbody>
                            <tr>
                                <td style="
                                            margin: 0;
                                            padding: 0;
                                            width: 100%;
                                            height: 100%;
                                        " align="center" valign="top">
                                    <table class="m-shell" border="0" width="775" cellspacing="0" cellpadding="0">
                                        <tbody>
                                            <tr>
                                                <td class="td" style="
                                                            width: 775px;
                                                            min-width: 775px;
                                                            font-size: 0pt;
                                                            line-height: 0pt;
                                                            padding: 0;
                                                            margin: 0;
                                                            font-weight: normal;
                                                        ">
                                                    <table border="0" width="100%" cellspacing="0" cellpadding="0">
                                                        <tbody>
                                                            <tr>
                                                                <td class="p-80 mpy-35 mpx-15" style="
                                                                            padding: 80px;
                                                                        " bgcolor="#212429">
                                                                    <table border="0" width="100%" cellspacing="0"
                                                                        cellpadding="0">
                                                                        <tbody>
                                                                            <tr>
                                                                                <td class="img pb-45" style="
                                                                                            font-size: 0pt;
                                                                                            line-height: 0pt;
                                                                                            text-align: left;
                                                                                            padding-bottom: 45px;
                                                                                        ">
                                                                                    <a href="http://www.myzjut.org"
                                                                                        target="_blank" rel="noopener">
                                                                                        <img
                                                                                                src="data:image/png;base64,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"
                                                                                                width="226"
                                                                                                height="91"
                                                                                                border="0"
                                                                                            />
                                                                                    </a>
                                                                                </td>
                                                                            </tr>
                                                                            <tr>
                                                                                <td>
                                                                                    <table border="0" width="100%"
                                                                                        cellspacing="0" cellpadding="0">
                                                                                        <tbody>
                                                                                            <tr>
                                                                                                <td class="title-36 pb-30 c-grey6 fw-b"
                                                                                                    style="
                                                                                                            font-size: 36px;
                                                                                                            line-height: 42px;
                                                                                                            font-family: Arial,
                                                                                                                sans-serif,
                                                                                                                'Motiva Sans';
                                                                                                            text-align: left;
                                                                                                            padding-bottom: 30px;
                                                                                                            color: #bfbfbf;
                                                                                                            font-weight: bold;
                                                                                                        ">
                                                                                                    托尼·斯塔克，您好！
                                                                                                </td>
                                                                                            </tr>
                                                                                        </tbody>
                                                                                    </table>
                                                                                    <table border="0" width="100%"
                                                                                        cellspacing="0" cellpadding="0">
                                                                                        <tbody>
                                                                                            <tr>
                                                                                                <td class="text-18 c-white pb-20"
                                                                                                    style="
                                                                                                            font-size: 18px;
                                                                                                            line-height: 25px;
                                                                                                            font-family: Arial,
                                                                                                                sans-serif,
                                                                                                                'Motiva Sans';
                                                                                                            text-align: left;
                                                                                                            color: #dbdbdb;
                                                                                                            padding-bottom: 20px;
                                                                                                        ">
                                                                                                    欢迎您报名2024精弘迎新赛！
                                                                                                </td>
                                                                                            </tr>
                                                                                        </tbody>
                                                                                    </table>
                                                                                    <table border="0" width="100%"
                                                                                        cellspacing="0" cellpadding="0">
                                                                                        <tbody>
                                                                                            <tr>
                                                                                                <td class="text-18 c-white pb-20"
                                                                                                    style="
                                                                                                            font-size: 18px;
                                                                                                            line-height: 25px;
                                                                                                            font-family: Arial,
                                                                                                                sans-serif,
                                                                                                                'Motiva Sans';
                                                                                                            text-align: left;
                                                                                                            color: #dbdbdb;
                                                                                                            padding-bottom: 20px;
                                                                                                        ">
                                                                                                    下面是您的账号与密码！
                                                                                                </td>
                                                                                            </tr>
                                                                                        </tbody>
                                                                                    </table>
                                                                                    <table border="0" width="100%"
                                                                                        cellspacing="0" cellpadding="0">
                                                                                        <tbody>
                                                                                            <tr>
                                                                                                <td class="text-18 c-white pb-20"
                                                                                                    style="
                                                                                                            font-size: 18px;
                                                                                                            line-height: 25px;
                                                                                                            font-family: Arial,
                                                                                                                sans-serif,
                                                                                                                'Motiva Sans';
                                                                                                            text-align: left;
                                                                                                            color: #dbdbdb;
                                                                                                            padding-bottom: 20px;
                                                                                                        ">
                                                                                                    祝您比赛愉快！
                                                                                                </td>
                                                                                            </tr>
                                                                                        </tbody>
                                                                                    </table>
                                                                                    <table border="0" width="100%"
                                                                                        cellspacing="0" cellpadding="0">
                                                                                        <tbody>
                                                                                            <tr>
                                                                                                <td class="pb-70 mpb-50"
                                                                                                    style="
                                                                                                            padding-bottom: 20px;
                                                                                                        ">
                                                                                                    <table border="0"
                                                                                                        width="100%"
                                                                                                        cellspacing="0"
                                                                                                        cellpadding="0"
                                                                                                        bgcolor="#17191c">
                                                                                                        <tbody>
                                                                                                            <tr>
                                                                                                                <td class="py-30 px-56"
                                                                                                                    style="
                                                                                                                            padding: 30px
                                                                                                                                56px
                                                                                                                                30px
                                                                                                                                56px;
                                                                                                                        ">
                                                                                                                    <table
                                                                                                                        border="0"
                                                                                                                        width="100%"
                                                                                                                        cellspacing="0"
                                                                                                                        cellpadding="0">
                                                                                                                        <tbody>
                                                                                                                            <tr>
                                                                                                                                <td
                                                                                                                                    style="
                                                                                                                                            font-size: 25px;
                                                                                                                                            line-height: 30px;
                                                                                                                                            font-family: Arial,
                                                                                                                                                sans-serif,
                                                                                                                                                'Motiva Sans';
                                                                                                                                            color: #f1f1f1;
                                                                                                                                            text-align: center;
                                                                                                                                            letter-spacing: 1px;
                                                                                                                                        ">
                                                                                                                                    账号
                                                                                                                                </td>
                                                                                                                            </tr>
                                                                                                                            <tr>
                                                                                                                                <td
                                                                                                                                    style="
                                                                                                                                            font-size: 25px;
                                                                                                                                            line-height: 30px;
                                                                                                                                            font-family: Arial,
                                                                                                                                                sans-serif,
                                                                                                                                                'Motiva Sans';
                                                                                                                                            color: #3a9aed;
                                                                                                                                            text-align: center;
                                                                                                                                            letter-spacing: 1px;
                                                                                                                                        ">
                                                                                                                                    ZeroHzzzz
                                                                                                                                </td>
                                                                                                                            </tr>
                                                                                                                            <tr>
                                                                                                                                <td
                                                                                                                                    style="
                                                                                                                                            padding-bottom: 16px;
                                                                                                                                        ">
                                                                                                                                    &nbsp;
                                                                                                                                </td>
                                                                                                                            </tr>
                                                                                                                            <tr>
                                                                                                                                <td
                                                                                                                                    style="
                                                                                                                                            font-size: 25px;
                                                                                                                                            line-height: 30px;
                                                                                                                                            font-family: Arial,
                                                                                                                                                sans-serif,
                                                                                                                                                'Motiva Sans';
                                                                                                                                            color: #f1f1f1;
                                                                                                                                            text-align: center;
                                                                                                                                            letter-spacing: 1px;
                                                                                                                                        ">
                                                                                                                                    密码
                                                                                                                                </td>
                                                                                                                            </tr>
                                                                                                                            <tr>
                                                                                                                                <td
                                                                                                                                    style="
                                                                                                                                            font-size: 25px;
                                                                                                                                            line-height: 30px;
                                                                                                                                            font-family: Arial,
                                                                                                                                                sans-serif,
                                                                                                                                                'Motiva Sans';
                                                                                                                                            color: #3a9aed;
                                                                                                                                            text-align: center;
                                                                                                                                            letter-spacing: 1px;
                                                                                                                                        ">
                                                                                                                                    iamgenius
                                                                                                                                </td>
                                                                                                                            </tr>
                                                                                                                        </tbody>
                                                                                                                    </table>
                                                                                                                </td>
                                                                                                            </tr>
                                                                                                        </tbody>
                                                                                                    </table>
                                                                                                </td>
                                                                                            </tr>
                                                                                        </tbody>
                                                                                    </table>
                                                                                    <table border="0" width="100%"
                                                                                        cellspacing="0" cellpadding="0">
                                                                                        <tbody>
                                                                                            <tr>
                                                                                                <td class="text-18 c-white pb-20"
                                                                                                    style="
                                                                                                            font-size: 18px;
                                                                                                            line-height: 25px;
                                                                                                            font-family: Arial,
                                                                                                                sans-serif,
                                                                                                                'Motiva Sans';
                                                                                                            text-align: left;
                                                                                                            color: #dbdbdb;
                                                                                                            padding-bottom: 20px;
                                                                                                        ">
                                                                                                    这是一份由系统自动发送的邮件。
                                                                                                </td>
                                                                                            </tr>
                                                                                        </tbody>
                                                                                    </table>
                                                                                    <table border="0" width="100%"
                                                                                        cellspacing="0" cellpadding="0">
                                                                                        <tbody>
                                                                                            <tr>
                                                                                                <td class="pt-30" style="
                                                                                                            padding-top: 30px;
                                                                                                        ">
                                                                                                    <table border="0"
                                                                                                        width="100%"
                                                                                                        cellspacing="0"
                                                                                                        cellpadding="0">
                                                                                                        <tbody>
                                                                                                            <tr>
                                                                                                                <td class="img"
                                                                                                                    style="
                                                                                                                            font-size: 0pt;
                                                                                                                            line-height: 0pt;
                                                                                                                            text-align: left;
                                                                                                                        "
                                                                                                                    bgcolor="#3a9aed"
                                                                                                                    width="3">
                                                                                                                    &nbsp;
                                                                                                                </td>
                                                                                                                <td class="img"
                                                                                                                    style="
                                                                                                                            font-size: 0pt;
                                                                                                                            line-height: 0pt;
                                                                                                                            text-align: left;
                                                                                                                        "
                                                                                                                    width="37">
                                                                                                                    &nbsp;
                                                                                                                </td>
                                                                                                                <td>
                                                                                                                    <table
                                                                                                                        border="0"
                                                                                                                        width="100%"
                                                                                                                        cellspacing="0"
                                                                                                                        cellpadding="0">
                                                                                                                        <tbody>
                                                                                                                            <tr>
                                                                                                                                <td class="text-16 py-20 c-grey4 fallback-font"
                                                                                                                                    style="
                                                                                                                                            font-size: 16px;
                                                                                                                                            line-height: 22px;
                                                                                                                                            font-family: Arial,
                                                                                                                                                sans-serif,
                                                                                                                                                'Motiva Sans';
                                                                                                                                            text-align: left;
                                                                                                                                            padding-top: 20px;
                                                                                                                                            padding-bottom: 20px;
                                                                                                                                            color: #f1f1f1;
                                                                                                                                        ">
                                                                                                                                    祝您愉快，<br />精弘网络
                                                                                                                                </td>
                                                                                                                            </tr>
                                                                                                                        </tbody>
                                                                                                                    </table>
                                                                                                                </td>
                                                                                                            </tr>
                                                                                                        </tbody>
                                                                                                    </table>
                                                                                                </td>
                                                                                            </tr>
                                                                                        </tbody>
                                                                                    </table>
                                                                                </td>
                                                                            </tr>
                                                                        </tbody>
                                                                    </table>
                                                                </td>
                                                            </tr>
                                                            <tr>
                                                                <td class="py-60 px-90 mpy-40 mpx-15" style="
                                                                            padding: 60px
                                                                                90px
                                                                                60px
                                                                                90px;
                                                                        ">
                                                                    <table border="0" width="100%" cellspacing="0"
                                                                        cellpadding="0">
                                                                        <tbody>
                                                                            <tr>
                                                                                <td class="text-18 pb-60 mpb-40 fallback-font"
                                                                                    style="
                                                                                            font-size: 18px;
                                                                                            line-height: 25px;
                                                                                            color: #000001;
                                                                                            font-family: Arial,
                                                                                                sans-serif,
                                                                                                'Motiva Sans';
                                                                                            text-align: left;
                                                                                            padding-bottom: 60px;
                                                                                        ">
                                                                                    此通知已发送至与您的报名信息关联的电子邮件地址。
                                                                                    <br /><br />此邮件为系统自动生成，请勿回复。如需帮助，请联系精弘网络客服。
                                                                                </td>
                                                                            </tr>
                                                                            <tr>
                                                                                <td class="pb-60" style="
                                                                                            padding-bottom: 60px;
                                                                                        ">
                                                                                    <table border="0" width="100%"
                                                                                        cellspacing="0" cellpadding="0">
                                                                                        <tbody>
                                                                                            <tr>
                                                                                                <th class="column"
                                                                                                    style="
                                                                                                            font-size: 0pt;
                                                                                                            line-height: 0pt;
                                                                                                            padding: 0;
                                                                                                            margin: 0;
                                                                                                            font-weight: normal;
                                                                                                        " width="270">
                                                                                                    <table border="0"
                                                                                                        width="100%"
                                                                                                        cellspacing="0"
                                                                                                        cellpadding="0">
                                                                                                        <tbody>
                                                                                                            <tr>
                                                                                                                <td class="text-18 mpb-40 fallback-font"
                                                                                                                    style="
                                                                                                                            font-size: 18px;
                                                                                                                            line-height: 25px;
                                                                                                                            color: #000001;
                                                                                                                            font-family: Arial,
                                                                                                                                sans-serif,
                                                                                                                                'Motiva Sans';
                                                                                                                            text-align: left;
                                                                                                                        ">
                                                                                                                </td>
                                                                                                            </tr>
                                                                                                        </tbody>
                                                                                                    </table>
                                                                                                </th>
                                                                                            </tr>
                                                                                        </tbody>
                                                                                    </table>
                                                                                </td>
                                                                            </tr>
                                                                        </tbody>
                                                                    </table>
                                                                </td>
                                                            </tr>
                                                        </tbody>
                                                    </table>
                                                </td>
                                            </tr>
                                        </tbody>
                                    </table>
                                </td>
                            </tr>
                        </tbody>
                    </table>
                </div>
            </div>
            <!-- -->
        </div>
    </div>
</body>

</html>
