import telnyx as tlnx

def recive_msg():

    number = str(+212674309507)
    to = "number "

    url_api = "KEY017A9CBE884E29EC5A630F6C64A56B95_NZnX5T8P8mrBXQSysI0vmU"
    tlnx.api_key =  url_api

    try:
        tlnx.Message.create(
        from_= number,
        to= to,
        msg = "heey",
    )
    except:
        print("Error Message")

recive_msg()