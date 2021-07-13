import telnyx as tlnx

file_name = input("file name :")

list_of_numbers = open(file_name + ".txt","r")

def receiv_sms():
    
    url_api = "KEY017A9CBE884E29EC5A630F6C64A56B95_NZnX5T8P8mrBXQSysI0vmU"
    tlnx.api_key = url_api
    your_telnyx_number = "+15732046266"

    
    for list in list_of_numbers :
        destination_number = list

    tlnx.Message.create(
        from_ =your_telnyx_number,
        to = destination_number,
        text ="Hello, world!",
    )
