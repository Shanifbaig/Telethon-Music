import os

class Config(object):
    API_ID = int(os.environ.get("API_ID", "6213538"))
    API_HASH = os.environ.get("API_HASH", "8ce3522bd21cc937eee4c68813d501d5")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", 6009162781)
    STRING_SESSION = os.environ.get("STRING_SESSION", 1BVtsOLQBu6CXKrhhqhdRRJIISmGb69LbjaN-MS-ST8Ic_D0aKpp6HtjKzlFyOQGOAKRv-6Qn53BmwR3W8b6cwgIgf1avY2n4WilIIk_E0gtTrCfe_xDYYHs37QK4-wBCfulJr_Apd-1YoX9-MytEbMjcwtVGh1sm7hFueJkp6twvCy9Gset1viVXx0fzvn1OqZWeFqeTK9XUr2pLq_SXKfC6QqmQWEgFskaG2TmIgMY0AXFxSUl28uVikoqrfSEFB46zILICXgTEaU0R0Y-8EMjTd4zv2j7rtyYW1FeS9MBxPFXSxikZn1bf6dKxFDbVDp7wy-J-_JDQIsH3ncaiZsxUCDzjii4=)
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "")
    SUPPORT = os.environ.get("SUPPORT", "TheSupportChat") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "TheUpdatesChannel") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/35a7b5d9f1f2605c9c0d3.png")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', None) # Change it to "True"
