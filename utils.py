from kavenegar import *


def send_otp_code(phone_number, code):
    try:
        api = KavenegarAPI('706D523063594634552F6C4B69583451552B71504442514948657847344F544663584D6E6A6A4F38305A413D')
        params = {
            'sender': '',  # optional
            'receptor': phone_number,  # multiple mobile number, split by comma
            'message': f'{code} کد تایید شما : ',
        }
        response = api.sms_send(params)
        print(response)
    except APIException as e:
        print(e)

    except HTTPException as e:
        print(e)
