#Search TODO in this file and edit only those fields

import requests
import datetime


def today():
    day_list = ["Monday", "Tuesday", "Wednesday",
                "Thursday", "Friday", "Saturday", "Sunday"]
    day = day_list[datetime.datetime.today().weekday()]
    return f'{day} : {str(datetime.datetime.today().date())}'


def quote_of_the_day():
    url = "https://quotel-quotes.p.rapidapi.com/quotes/qod"

    payload = {"topicId": 100}
    headers = {
        "content-type": "application/json",
        "X-RapidAPI-Key": "",# TODO (go to the rapid api website and get a api key)
        "X-RapidAPI-Host": "quotel-quotes.p.rapidapi.com"
    }
    if headers["X-RapidAPI-Key"] == '':
        assert 'No API key given'
    response = requests.request("POST", url, json=payload, headers=headers)
    quote_json = response.json()
    return quote_json['quote'], quote_json['name']


def news():

    # there do exist newapi module but this also works
    api_url = 'https://newsapi.org/v2/top-headlines?country=in&apiKey='#TODO (Add newapi key at the end of it) 
    response = requests.get(api_url)
    unformatted_news = response.json()
    # as json is basically dic in python we will handle it as dic
    # news formatter
    html_elements_list = []



    with open('constants/site_1') as file:#TODO put the full file location of site_1 here should be in constants folder
        firstportion = file.read()
    with open('constants/site_2') as file:#TODO put the full file location of site_2 here should be in constants folder
        lastportion = file.read()


    middleportion = ''
    for position, info in enumerate(unformatted_news['articles']):
        if position > 12:
            break



        imageurl = 'https://cutewallpaper.org/21/space-background-1280x720/Download-1280x720-wallpaper-galaxy,-stars,-clouds,-space-.jpg'
        if info['urlToImage'] != None:
            imageurl=info['urlToImage']
        title = ''
        if info['title'] != None:
            title = info['title']
        description = ''
        if info['description'] != None:
            description = info['description']
        if info['url'] != None:
            url = info['url']  
    
            cards = f'''
  
    <div class="chaigaram--card" style="background-image: url({imageurl});background-repeat: no-repeat;background-size: 100% 100%;">
      <h3 >{title}</h3>
      <div id="url">{url}</div>
      <p>{description}</p>
    </div>

'''
        middleportion += cards




        middle_news = f'''



		          <div id="u_row_7" class="u-row-container v-row-background-color"
            style="padding: 0px;background-color: #3598db">
            <div class="u-row"
              style="Margin: 0 auto;min-width: 320px;max-width: 500px;overflow-wrap: break-word;word-wrap: break-word;word-break: break-word;background-color: transparent;">
              <div
                style="border-collapse: collapse;display: table;width: 100%;height: 100%;background-color: transparent;">
                <!--[if (mso)|(IE)]><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td class="v-row-background-color" style="padding: 0px;background-color: #3598db;" align="center"><table cellpadding="0" cellspacing="0" border="0" style="width:500px;"><tr style="background-color: transparent;"><![endif]-->

                <!--[if (mso)|(IE)]><td align="center" width="494" class="v-col-border" style="width: 494px;padding: 0px;border-top: 0px solid transparent;border-left: 3px solid #000000;border-right: 3px solid #000000;border-bottom: 3px solid #000000;border-radius: 0px;-webkit-border-radius: 0px; -moz-border-radius: 0px;" valign="top"><![endif]-->
                <div id="u_column_7" class="u-col u-col-100"
                  style="max-width: 320px;min-width: 500px;display: table-cell;vertical-align: top;">
                  <div
                    style="height: 100%;width: 100% !important;border-radius: 0px;-webkit-border-radius: 0px; -moz-border-radius: 0px;">
                    <!--[if (!mso)&(!IE)]><!-->
                    <div class="v-col-border"
                      style="height: 100%; padding: 0px;border-top: 0px solid transparent;border-left: 3px solid #000000;border-right: 3px solid #000000;border-bottom: 3px solid #000000;border-radius: 0px;-webkit-border-radius: 0px; -moz-border-radius: 0px;">
                      <!--<![endif]-->

                      <table style="font-family:arial,helvetica,sans-serif;" role="presentation" cellpadding="0"
                        cellspacing="0" width="100%" border="0">
                        <tbody>
                          <tr>
                            <td
                              style="overflow-wrap:break-word;word-break:break-word;padding:10px;font-family:arial,helvetica,sans-serif;"
                              align="left">

                              <h1 class="v-color v-text-align"
                                style="margin: 0px; line-height: 140%; text-align: center; word-wrap: break-word; font-weight: normal; font-family: 'Bitter'; font-size: 22px;">{info['title']}</h1>

                            </td>
                          </tr>
                        </tbody>
                      </table>

                      <table style="font-family:arial,helvetica,sans-serif;" role="presentation" cellpadding="0"
                        cellspacing="0" width="100%" border="0">
                        <tbody>
                          <tr>
                            <td
                              style="overflow-wrap:break-word;word-break:break-word;padding:10px;font-family:arial,helvetica,sans-serif;"
                              align="left">

                              <div class="v-color v-text-align"
                                style="line-height: 140%; text-align: center; word-wrap: break-word;">
                                <p style="font-size: 14px; line-height: 140%;"><span
                                    style="font-family: 'book antiqua', palatino; font-size: 14px; line-height: 19.6px;">{info['description']}</span></p>
                              </div>

                            </td>
                          </tr>
                        </tbody>
                      </table>

                      <table style="font-family:arial,helvetica,sans-serif;" role="presentation" cellpadding="0"
                        cellspacing="0" width="100%" border="0">
                        <tbody>
                          <tr>
                            <td
                              style="overflow-wrap:break-word;word-break:break-word;padding:10px;font-family:arial,helvetica,sans-serif;"
                              align="left">

                              <table width="100%" cellpadding="0" cellspacing="0" border="0">
                                <tr>
                                  <td class="v-text-align" style="padding-right: 0px;padding-left: 0px;" align="center">
                                    <a href="{info['url']}" target="_blank">
                                      <img align="center" border="0" src="{info['urlToImage']}" alt="{info['url']}" title=""
                                        style="outline: none;text-decoration: none;-ms-interpolation-mode: bicubic;clear: both;display: inline-block !important;border: none;height: auto;float: none;width: 100%;max-width: 480px;"
                                        width="480" />
                                    </a>
                                  </td>
                                </tr>
                              </table>

                            </td>
                          </tr>
                        </tbody>
                      </table>

                      <table id="u_content_text_10" style="font-family:arial,helvetica,sans-serif;" role="presentation"
                        cellpadding="0" cellspacing="0" width="100%" border="0">
                        <tbody>
                          <tr>
                            <td
                              style="overflow-wrap:break-word;word-break:break-word;padding:10px;font-family:arial,helvetica,sans-serif;"
                              align="left">

                              <div class="v-color v-text-align"
                                style="line-height: 140%; text-align: center; word-wrap: break-word;">
                                <p style="font-size: 14px; line-height: 140%;"><span
                                    style="font-family: Anton; font-size: 14px; line-height: 19.6px;">{info['source']['name']}</span></p>
                              </div>

                            </td>
                          </tr>
                        </tbody>
                      </table>

                      <!--[if (!mso)&(!IE)]><!-->
                    </div>
                    <!--<![endif]-->
                  </div>
                </div>
                <!--[if (mso)|(IE)]></td><![endif]-->
                <!--[if (mso)|(IE)]></tr></table></td></tr></table><![endif]-->
              </div>
            </div>
          </div>

		'''
        html_elements_list.append(middle_news)

    data = firstportion+middleportion+lastportion
    with open('templates/main.html','w') as file:#TODO put the full file location of main.html here should be in templates folder
        file.write(data)

    #Pythonanywhere reloader
    api_token = '5133d789a88769e06e0c6c859605a99eb6afd347'#TODO (get a api token from pythonanywhere)
    webapp_url = 'https://www.pythonanywhere.com/api/v0/user/AmitBasuri/webapps/amitbasuri.pythonanywhere.com/reload/' #TODO (get the reload link)
    response = requests.post(webapp_url,headers={'Authorization': f'Token {api_token}'})

    news_html_element = ''.join(html_elements_list)
    return news_html_element


def emailer(message, sbtyp='html'):
    import smtplib
    from email.message import EmailMessage

    EMAIL_ADDRESS = ''#TODO (senders email address)
    EMAIL_PASSWORD = ''#TODO (password for senders email address)

    msg = EmailMessage()
    msg['Subject'] = 'Chai Garam'
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = ''#TODO(receivers email address)(This can be a list() of email addresses, like ['acb@d.com','123@e.com'] )
    msg.set_content(message, subtype=sbtyp)

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
      
        login_msg = smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        msg_log = smtp.send_message(msg)
        print(login_msg,msg_log)
    return 'Email sent'


def chai_garam():
    constant_html = [r'''	<!DOCTYPE HTML  PUBLIC "-//W3C//DTD XHTML 1.0 Transitional //EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd"><html xmlns="http://www.w3.org/1999/xhtml" xmlns:v="urn:schemas-microsoft-com:vml"  xmlns:o="urn:schemas-microsoft-com:office:office"><head>  <!--[if gte mso 9]><xml>  <o:OfficeDocumentSettings>    <o:AllowPNG/>    <o:PixelsPerInch>96</o:PixelsPerInch>  </o:OfficeDocumentSettings></xml><![endif]-->  <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">  <meta name="viewport" content="width=device-width, initial-scale=1.0">  <meta name="x-apple-disable-message-reformatting">  <!--[if !mso]><!-->  <meta http-equiv="X-UA-Compatible" content="IE=edge">  <!--<![endif]-->  <title></title>  <style type="text/css">    @media only screen and (min-width: 520px) {      .u-row {        width: 500px !important;      }      .u-row .u-col {        vertical-align: top;      }      .u-row .u-col-100 {        width: 500px !important;      }    }    @media (max-width: 520px) {      .u-row-container {        max-width: 100% !important;        padding-left: 0px !important;        padding-right: 0px !important;      }      .u-row .u-col {        min-width: 320px !important;        max-width: 100% !important;        display: block !important;      }      .u-row {        width: 100% !important;      }      .u-col {        width: 100% !important;      }      .u-col>div {        margin: 0 auto;      }    }    body {      margin: 0;      padding: 0;    }    table,    tr,    td {      vertical-align: top;      border-collapse: collapse;    }    p {      margin: 0;    }    .ie-container table,    .mso-container table {      table-layout: fixed;    }    * {      line-height: inherit;    }    a[x-apple-data-detectors='true'] {      color: inherit !important;      text-decoration: none !important;    }    table,    td {      color: #000000;    }    #u_body a {      color: #0000ee;      text-decoration: underline;    }    @media (max-width: 480px) {      #u_content_heading_8 .v-color {        color: #ffffff !important;      }      #u_content_heading_8 .v-text-align {        text-align: center !important;      }      #u_content_heading_7 .v-color {        color: #ffffff !important;      }      #u_content_heading_7 .v-text-align {        text-align: center !important;      }      #u_content_text_8 .v-color {        color: #ffffff !important;      }      #u_content_heading_4 .v-color {        color: #3598db !important;      }      #u_content_heading_4 .v-text-align {        text-align: center !important;      }      #u_row_7 .v-row-background-color {        background-color: #3598db !important;      }      #u_row_7.v-row-background-color {        background-color: #3598db !important;      }      #u_column_7 .v-col-border {        border-top: 3px solid #000000 !important;        border-left: 3px solid #000000 !important;        border-right: 3px solid #000000 !important;        border-bottom: 3px solid #000000 !important;      }      #u_row_5 .v-row-background-color {        background-color: #3598db !important;      }      #u_row_5.v-row-background-color {        background-color: #3598db !important;      }      #u_column_5 .v-col-border {        border-top: 0px solid transparent !important;        border-left: 3px solid #000000 !important;        border-right: 3px solid #000000 !important;        border-bottom: 3px solid #000000 !important;      }      #u_row_11 .v-row-background-color {        background-color: #3598db !important;      }      #u_row_11.v-row-background-color {        background-color: #3598db !important;      }      #u_column_12 .v-col-border {        border-top: 0px solid transparent !important;        border-left: 3px solid #000000 !important;        border-right: 3px solid #000000 !important;        border-bottom: 3px solid #000000 !important;      }      #u_content_text_7 .v-color {        color: #ffffff !important;      }      #u_content_text_7 .v-text-align {        text-align: center !important;      }    }  </style>  <!--[if !mso]><!-->  <link href="https://fonts.googleapis.com/css?family=Crimson+Text:400,700" rel="stylesheet" type="text/css">  <link href="https://fonts.googleapis.com/css2?family=Fredoka+One&display=swap" rel="stylesheet" type="text/css">  <link href="https://fonts.googleapis.com/css?family=Pacifico" rel="stylesheet" type="text/css">  <!--<![endif]--></head><body class="clean-body u_body"  style="margin: 0;padding: 0;-webkit-text-size-adjust: 100%;background-color: #000000;color: #000000">  <!--[if IE]><div class="ie-container"><![endif]-->  <!--[if mso]><div class="mso-container"><![endif]-->  <table id="u_body"    style="border-collapse: collapse;table-layout: fixed;border-spacing: 0;mso-table-lspace: 0pt;mso-table-rspace: 0pt;vertical-align: top;min-width: 320px;Margin: 0 auto;background-color: #000000;width:100%"    cellpadding="0" cellspacing="0">    <tbody>      <tr style="vertical-align: top">        <td style="word-break: break-word;border-collapse: collapse !important;vertical-align: top">          <!--[if (mso)|(IE)]><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td align="center" style="background-color: #000000;"><![endif]-->          <div class="u-row-container v-row-background-color" style="padding: 0px;background-color: transparent">            <div class="u-row"              style="Margin: 0 auto;min-width: 320px;max-width: 500px;overflow-wrap: break-word;word-wrap: break-word;word-break: break-word;background-color: transparent;">              <div                style="border-collapse: collapse;display: table;width: 100%;height: 100%;background-color: transparent;">                <!--[if (mso)|(IE)]><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td class="v-row-background-color" style="padding: 0px;background-color: transparent;" align="center"><table cellpadding="0" cellspacing="0" border="0" style="width:500px;"><tr style="background-color: transparent;"><![endif]-->                <!--[if (mso)|(IE)]><td align="center" width="500" class="v-col-border" style="width: 500px;padding: 0px;border-top: 0px solid transparent;border-left: 0px solid transparent;border-right: 0px solid transparent;border-bottom: 0px solid transparent;border-radius: 0px;-webkit-border-radius: 0px; -moz-border-radius: 0px;" valign="top"><![endif]-->                <div class="u-col u-col-100"                  style="max-width: 320px;min-width: 500px;display: table-cell;vertical-align: top;">                  <div                    style="height: 100%;width: 100% !important;border-radius: 0px;-webkit-border-radius: 0px; -moz-border-radius: 0px;">                    <!--[if (!mso)&(!IE)]><!-->                    <div class="v-col-border"                      style="height: 100%; padding: 0px;border-top: 0px solid transparent;border-left: 0px solid transparent;border-right: 0px solid transparent;border-bottom: 0px solid transparent;border-radius: 0px;-webkit-border-radius: 0px; -moz-border-radius: 0px;">                      <!--<![endif]-->                      <table id="u_content_heading_8" style="font-family:arial,helvetica,sans-serif;"                        role="presentation" cellpadding="0" cellspacing="0" width="100%" border="0">                        <tbody>                          <tr>                            <td                              style="overflow-wrap:break-word;word-break:break-word;padding:10px;font-family:arial,helvetica,sans-serif;"                              align="left">                              <h1 class="v-color v-text-align"                                style="margin: 0px; color: #ffffff; line-height: 140%; text-align: center; word-wrap: break-word; font-weight: normal; font-family: Fredoka One; font-size: 22px;">                                <strong><a href='https://amitbasuri.pythonanywhere.com/'>Chai Garam</a></strong></h1>                            </td>                          </tr>                        </tbody>                      </table>                      <!--[if (!mso)&(!IE)]><!-->                    </div>                    <!--<![endif]-->                  </div>                </div>                <!--[if (mso)|(IE)]></td><![endif]-->                <!--[if (mso)|(IE)]></tr></table></td></tr></table><![endif]-->              </div>            </div>          </div>''', r'''          <!--[if (mso)|(IE)]></td></tr></table><![endif]-->        </td>      </tr>    </tbody>  </table>  <!--[if mso]></div><![endif]-->  <!--[if IE]></div><![endif]--></body></html>''']
    date = today()
    quote, author_of_quote = quote_of_the_day()

    #quotes and date
    first_html = f'''

          <div class="u-row-container v-row-background-color" style="padding: 0px;background-color: transparent">
            <div class="u-row"
              style="Margin: 0 auto;min-width: 320px;max-width: 500px;overflow-wrap: break-word;word-wrap: break-word;word-break: break-word;background-color: transparent;">
              <div
                style="border-collapse: collapse;display: table;width: 100%;height: 100%;background-color: transparent;">
                <!--[if (mso)|(IE)]><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td class="v-row-background-color" style="padding: 0px;background-color: transparent;" align="center"><table cellpadding="0" cellspacing="0" border="0" style="width:500px;"><tr style="background-color: transparent;"><![endif]-->

                <!--[if (mso)|(IE)]><td align="center" width="500" class="v-col-border" style="width: 500px;padding: 0px;border-top: 0px solid transparent;border-left: 0px solid transparent;border-right: 0px solid transparent;border-bottom: 0px solid transparent;border-radius: 0px;-webkit-border-radius: 0px; -moz-border-radius: 0px;" valign="top"><![endif]-->
                <div class="u-col u-col-100"
                  style="max-width: 320px;min-width: 500px;display: table-cell;vertical-align: top;">
                  <div
                    style="height: 100%;width: 100% !important;border-radius: 0px;-webkit-border-radius: 0px; -moz-border-radius: 0px;">
                    <!--[if (!mso)&(!IE)]><!-->
                    <div class="v-col-border"
                      style="height: 100%; padding: 0px;border-top: 0px solid transparent;border-left: 0px solid transparent;border-right: 0px solid transparent;border-bottom: 0px solid transparent;border-radius: 0px;-webkit-border-radius: 0px; -moz-border-radius: 0px;">
                      <!--<![endif]-->

                      <table id="u_content_heading_7" style="font-family:arial,helvetica,sans-serif;"
                        role="presentation" cellpadding="0" cellspacing="0" width="100%" border="0">
                        <tbody>
                          <tr>
                            <td
                              style="overflow-wrap:break-word;word-break:break-word;padding:10px;font-family:arial,helvetica,sans-serif;"
                              align="left">

                              <h1 class="v-color v-text-align"
                                style="margin: 0px; color: #ffffff; line-height: 140%; text-align: center; word-wrap: break-word; font-weight: normal; font-family: 'Pacifico',cursive; font-size: 22px;">{date}</h1>

                            </td>
                          </tr>
                        </tbody>
                      </table>

                      <table id="u_content_text_8" style="font-family:arial,helvetica,sans-serif;" role="presentation"
                        cellpadding="0" cellspacing="0" width="100%" border="0">
                        <tbody>
                          <tr>
                            <td
                              style="overflow-wrap:break-word;word-break:break-word;padding:10px;font-family:arial,helvetica,sans-serif;"
                              align="left">

                              <div class="v-color v-text-align"
                                style="color: #ffffff; line-height: 140%; text-align: justify; word-wrap: break-word;">
                                <p style="font-size: 14px; line-height: 140%;"><span
                                    style="font-family: Epilogue; font-size: 14px; line-height: 19.6px;">{quote}</span></p>
                              </div>

                            </td>
                          </tr>
                        </tbody>
                      </table>

                      <table style="font-family:arial,helvetica,sans-serif;" role="presentation" cellpadding="0"
                        cellspacing="0" width="100%" border="0">
                        <tbody>
                          <tr>
                            <td
                              style="overflow-wrap:break-word;word-break:break-word;padding:10px;font-family:arial,helvetica,sans-serif;"
                              align="left">

                              <div class="v-color v-text-align"
                                style="color: #ecf0f1; line-height: 140%; text-align: center; word-wrap: break-word;">
                                <p style="font-size: 14px; line-height: 140%;"><span
                                    style="font-family: verdana, geneva; font-size: 14px; line-height: 19.6px;">{author_of_quote}</span>
                                </p>
                              </div>

                            </td>
                          </tr>
                        </tbody>
                      </table>

                      <!--[if (!mso)&(!IE)]><!-->
                    </div>
                    <!--<![endif]-->
                  </div>
                </div>
                <!--[if (mso)|(IE)]></td><![endif]-->
                <!--[if (mso)|(IE)]></tr></table></td></tr></table><![endif]-->
              </div>
            </div>
          </div>
'''

    first_html_const = r'''
          <div class="u-row-container v-row-background-color" style="padding: 0px;background-color: transparent">
            <div class="u-row"
              style="Margin: 0 auto;min-width: 320px;max-width: 500px;overflow-wrap: break-word;word-wrap: break-word;word-break: break-word;background-color: transparent;">
              <div
                style="border-collapse: collapse;display: table;width: 100%;height: 100%;background-color: transparent;">
                <!--[if (mso)|(IE)]><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td class="v-row-background-color" style="padding: 0px;background-color: transparent;" align="center"><table cellpadding="0" cellspacing="0" border="0" style="width:500px;"><tr style="background-color: transparent;"><![endif]-->

                <!--[if (mso)|(IE)]><td align="center" width="500" class="v-col-border" style="width: 500px;padding: 0px;border-top: 0px solid transparent;border-left: 0px solid transparent;border-right: 0px solid transparent;border-bottom: 0px solid transparent;border-radius: 0px;-webkit-border-radius: 0px; -moz-border-radius: 0px;" valign="top"><![endif]-->
                <div class="u-col u-col-100"
                  style="max-width: 320px;min-width: 500px;display: table-cell;vertical-align: top;">
                  <div
                    style="height: 100%;width: 100% !important;border-radius: 0px;-webkit-border-radius: 0px; -moz-border-radius: 0px;">
                    <!--[if (!mso)&(!IE)]><!-->
                    <div class="v-col-border"
                      style="height: 100%; padding: 0px;border-top: 0px solid transparent;border-left: 0px solid transparent;border-right: 0px solid transparent;border-bottom: 0px solid transparent;border-radius: 0px;-webkit-border-radius: 0px; -moz-border-radius: 0px;">
                      <!--<![endif]-->

                      <table style="font-family:arial,helvetica,sans-serif;" role="presentation" cellpadding="0"
                        cellspacing="0" width="100%" border="0">
                        <tbody>
                          <tr>
                            <td
                              style="overflow-wrap:break-word;word-break:break-word;padding:10px;font-family:arial,helvetica,sans-serif;"
                              align="left">

                              <table height="0px" align="center" border="0" cellpadding="0" cellspacing="0" width="100%"
                                style="border-collapse: collapse;table-layout: fixed;border-spacing: 0;mso-table-lspace: 0pt;mso-table-rspace: 0pt;vertical-align: top;border-top: 1px solid #BBBBBB;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%">
                                <tbody>
                                  <tr style="vertical-align: top">
                                    <td
                                      style="word-break: break-word;border-collapse: collapse !important;vertical-align: top;font-size: 0px;line-height: 0px;mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%">
                                      <span>&#160;</span>
                                    </td>
                                  </tr>
                                </tbody>
                              </table>

                            </td>
                          </tr>
                        </tbody>
                      </table>

                      <!--[if (!mso)&(!IE)]><!-->
                    </div>
                    <!--<![endif]-->
                  </div>
                </div>
                <!--[if (mso)|(IE)]></td><![endif]-->
                <!--[if (mso)|(IE)]></tr></table></td></tr></table><![endif]-->
              </div>
            </div>
          </div>

          <div class="u-row-container v-row-background-color" style="padding: 0px;background-color: transparent">
            <div class="u-row"
              style="Margin: 0 auto;min-width: 320px;max-width: 500px;overflow-wrap: break-word;word-wrap: break-word;word-break: break-word;background-color: transparent;">
              <div
                style="border-collapse: collapse;display: table;width: 100%;height: 100%;background-color: transparent;">
                <!--[if (mso)|(IE)]><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td class="v-row-background-color" style="padding: 0px;background-color: transparent;" align="center"><table cellpadding="0" cellspacing="0" border="0" style="width:500px;"><tr style="background-color: transparent;"><![endif]-->

                <!--[if (mso)|(IE)]><td align="center" width="500" class="v-col-border" style="width: 500px;padding: 0px;border-top: 0px solid transparent;border-left: 0px solid transparent;border-right: 0px solid transparent;border-bottom: 0px solid transparent;" valign="top"><![endif]-->
                <div class="u-col u-col-100"
                  style="max-width: 320px;min-width: 500px;display: table-cell;vertical-align: top;">
                  <div style="height: 100%;width: 100% !important;">
                    <!--[if (!mso)&(!IE)]><!-->
                    <div class="v-col-border"
                      style="height: 100%; padding: 0px;border-top: 0px solid transparent;border-left: 0px solid transparent;border-right: 0px solid transparent;border-bottom: 0px solid transparent;">
                      <!--<![endif]-->

                      <table id="u_content_heading_4" style="font-family:arial,helvetica,sans-serif;"
                        role="presentation" cellpadding="0" cellspacing="0" width="100%" border="0">
                        <tbody>
                          <tr>
                            <td
                              style="overflow-wrap:break-word;word-break:break-word;padding:10px;font-family:arial,helvetica,sans-serif;"
                              align="left">

                              <h1 class="v-color v-text-align"
                                style="margin: 0px; color: #3598db; line-height: 140%; text-align: center; word-wrap: break-word; font-weight: normal; font-family: andale mono,times; font-size: 22px;">
                                Top Headlines</h1>

                            </td>
                          </tr>
                        </tbody>
                      </table>

                      <!--[if (!mso)&(!IE)]><!-->
                    </div>
                    <!--<![endif]-->
                  </div>
                </div>
                <!--[if (mso)|(IE)]></td><![endif]-->
                <!--[if (mso)|(IE)]></tr></table></td></tr></table><![endif]-->
              </div>
            </div>
          </div>


	'''

    # news
    second_html = news()
    second_html_const = r'''
	          <div class="u-row-container v-row-background-color" style="padding: 0px;background-color: transparent">
            <div class="u-row"
              style="Margin: 0 auto;min-width: 320px;max-width: 500px;overflow-wrap: break-word;word-wrap: break-word;word-break: break-word;background-color: transparent;">
              <div
                style="border-collapse: collapse;display: table;width: 100%;height: 100%;background-color: transparent;">
                <!--[if (mso)|(IE)]><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td class="v-row-background-color" style="padding: 0px;background-color: transparent;" align="center"><table cellpadding="0" cellspacing="0" border="0" style="width:500px;"><tr style="background-color: transparent;"><![endif]-->

                <!--[if (mso)|(IE)]><td align="center" width="500" class="v-col-border" style="width: 500px;padding: 0px;border-top: 0px solid transparent;border-left: 0px solid transparent;border-right: 0px solid transparent;border-bottom: 0px solid transparent;border-radius: 0px;-webkit-border-radius: 0px; -moz-border-radius: 0px;" valign="top"><![endif]-->
                <div class="u-col u-col-100"
                  style="max-width: 320px;min-width: 500px;display: table-cell;vertical-align: top;">
                  <div
                    style="height: 100%;width: 100% !important;border-radius: 0px;-webkit-border-radius: 0px; -moz-border-radius: 0px;">
                    <!--[if (!mso)&(!IE)]><!-->
                    <div class="v-col-border"
                      style="height: 100%; padding: 0px;border-top: 0px solid transparent;border-left: 0px solid transparent;border-right: 0px solid transparent;border-bottom: 0px solid transparent;border-radius: 0px;-webkit-border-radius: 0px; -moz-border-radius: 0px;">
                      <!--<![endif]-->

                      <table style="font-family:arial,helvetica,sans-serif;" role="presentation" cellpadding="0"
                        cellspacing="0" width="100%" border="0">
                        <tbody>
                          <tr>
                            <td
                              style="overflow-wrap:break-word;word-break:break-word;padding:10px;font-family:arial,helvetica,sans-serif;"
                              align="left">

                              <table height="0px" align="center" border="0" cellpadding="0" cellspacing="0" width="100%"
                                style="border-collapse: collapse;table-layout: fixed;border-spacing: 0;mso-table-lspace: 0pt;mso-table-rspace: 0pt;vertical-align: top;border-top: 1px solid #BBBBBB;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%">
                                <tbody>
                                  <tr style="vertical-align: top">
                                    <td
                                      style="word-break: break-word;border-collapse: collapse !important;vertical-align: top;font-size: 0px;line-height: 0px;mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%">
                                      <span>&#160;</span>
                                    </td>
                                  </tr>
                                </tbody>
                              </table>

                            </td>
                          </tr>
                        </tbody>
                      </table>

                      <!--[if (!mso)&(!IE)]><!-->
                    </div>
                    <!--<![endif]-->
                  </div>
                </div>
                <!--[if (mso)|(IE)]></td><![endif]-->
                <!--[if (mso)|(IE)]></tr></table></td></tr></table><![endif]-->
              </div>
            </div>
          </div>
	'''
    constant_html.insert(1, first_html+first_html_const +
                         second_html+second_html_const)
    final_html = ''.join(constant_html)

    return final_html





if __name__ == '__main__':
  emailer(chai_garam())