from tencentcloud.common import credential
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.sms.v20190711 import sms_client, models
from miniProject import settings

def send_message(phone,random_code,template_id="1038077"):
    phone = "{}{}".format("+86", phone)
    try:
        cred = credential.Credential(settings.TENCENT_SECRET_ID,settings.TENCENT_SECRET_KEY)
        client = sms_client.SmsClient(cred, settings.TENCENT_CITY)
        req = models.SendSmsRequest()
        req.SmsSdkAppid = settings.TENCENT_SDK_APP_ID
        # 短信签名内容: 使用 UTF-8 编码，必须填写已审核通过的签名，签名信息可登录 [短信控制台] 查看
        req.Sign = settings.TENCENT_SIGN
        req.PhoneNumberSet = [phone,]
        # 模板 ID: 必须填写已审核通过的模板 ID。模板ID可登录 [短信控制台] 查看
        req.TemplateID = template_id
        # 模板参数: 若无模板参数，则设置为空
        req.TemplateParamSet = [random_code,]

        resp = client.SendSms(req)

        print(resp.to_json_string(indent=2))

    except TencentCloudSDKException as err:
        print(err)