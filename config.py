from telethon.sync import TelegramClient
from telethon.sessions import StringSession
import os
APP_ID = os.environ.get("APP_ID",
"17053751")
APP_HASH = os.environ.get("APP_HASH",
"6f90a1382848f5cc767a623f898ab23f")
BOT_USERNAME = os.environ.get("BOT_USERNAME",
                           "Qpqpa_bot")
session = os.environ.get("TERMUX",
                        "AQEEODcAgJ2YhFOVyw4Sr_3wYXFzgIxdYtovgbPqHTaVXlp286F5i2vEPtem35I-HijIb77NNv3TLRd0Y4K_rQXYBCmTrD0tytqYKjdlupQ2AicZz5Lj5fkyNsVNdtjAWJgROyZkHhyYOJtWNvFeu94AFx8t1t0xi9prHYKS9bNeTTBneSeBNe8uSP9IZfNYmB2C1kSzwFBzkz0Y-2RsOD3wb5ZpXqGGDqdyVXGSMi3cHIDuIpnFTfFQek9nhb2ihm5lOxILH9sm4msRVG4AcOF4hwKJCLlKj8YZQeRPhOiliGP0l2r24YBacEm0VDRuVCeJS01oa2151kbpnfL1jG5LtcUGNwAAAAEs3fMdAA")
SESSION = os.environ.get("TERMUX",
                        "AQEEODcAgJ2YhFOVyw4Sr_3wYXFzgIxdYtovgbPqHTaVXlp286F5i2vEPtem35I-HijIb77NNv3TLRd0Y4K_rQXYBCmTrD0tytqYKjdlupQ2AicZz5Lj5fkyNsVNdtjAWJgROyZkHhyYOJtWNvFeu94AFx8t1t0xi9prHYKS9bNeTTBneSeBNe8uSP9IZfNYmB2C1kSzwFBzkz0Y-2RsOD3wb5ZpXqGGDqdyVXGSMi3cHIDuIpnFTfFQek9nhb2ihm5lOxILH9sm4msRVG4AcOF4hwKJCLlKj8YZQeRPhOiliGP0l2r24YBacEm0VDRuVCeJS01oa2151kbpnfL1jG5LtcUGNwAAAAEs3fMdAA")
token = os.environ.get("TOKEN",
                      "5700874811:AAEgZ4OKHOLJ98Va_OO7Qr-Uuxg1f0BcFrg")
fifthon = TelegramClient(StringSession(session), APP_ID, APP_HASH)
bot = TelegramClient("bot", APP_ID, APP_HASH).start(bot_token=token)
ispay = ['yes']
ispay2 = ['yes']
bot.start()
