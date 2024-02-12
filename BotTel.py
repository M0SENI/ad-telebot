from telebot import TeleBot
from telebot import types
from telebot.types import InlineKeyboardButton , InlineKeyboardMarkup
from telebot.types import KeyboardButton , ReplyKeyboardMarkup
from config import channel, TOKEN
import time


mychatid = 963475140
bot = TeleBot(token=TOKEN)



"""
 UID = message.from_user.username
 UFN = message.from_user.firstname
"""



"""
if message.text == "لغو ❌":
    cncltct(message)
elif message.text == "شروع مجدد":
    start(message)
else:
"""





inbutton1 = InlineKeyboardButton(text="🔹چنل اول ما🔹", url="https://t.me/russie_tuday2024")
inbutton2 = InlineKeyboardButton(text="🔹چنل دوم ما🔹", url="https://t.me/havashi_russ_2022")
inbutton3 = InlineKeyboardButton(text="🔹چنل آگهی ما🔹", url="https://t.me/niazmndiha_2024_rus")
inbutton4 = InlineKeyboardButton(text="🔹بررسی عضویت🔹", callback_data="join")
markup1 = InlineKeyboardMarkup(row_width=1)
markup1.add(inbutton1, inbutton2 , inbutton3 , inbutton4)
markchnnl = InlineKeyboardMarkup(row_width=1)
markchnnl.add(inbutton1 , inbutton2 , inbutton3)

# options
button1 = KeyboardButton(text="ثبت آگهی 📮")
button2 = KeyboardButton(text="قوانین 📌")
button3 = KeyboardButton(text="پشتیبانی ⚠️")
button4 = KeyboardButton(text="کانال ها 📣")
button5 = KeyboardButton(text="آگهی های من 👀")
markup2 = ReplyKeyboardMarkup(row_width=2 , resize_keyboard=True)
markup2.row(button1)
markup2.row(button2 , button3)
markup2.row(button4)



# pending

# options - button7
inbutton17 = InlineKeyboardButton(text="آگهی های درحال تایید من📌" , callback_data="pending")
inbutton18 = InlineKeyboardButton(text="آگهی های فعال من✅" , callback_data="active")
inbutton19 = InlineKeyboardButton(text="آگهی های منقضی شده من❌" , callback_data="cancled")
markup5 = InlineKeyboardMarkup(row_width=1)
markup5.add(inbutton17 , inbutton18 , inbutton19)


 #daste

inbutton6 = types.KeyboardButton(text="اجاره تخت" )
inbutton7 = types.KeyboardButton(text="اجاره اتاق" )
inbutton8 = types.KeyboardButton(text="اجاره خانه" ,)
inbutton9 = types.KeyboardButton(text="متقاضی تخت")
inbutton10 = types.KeyboardButton(text="متقاضی اتاق")
inbutton11 = types.KeyboardButton(text="متقاضی خانه",)
inbutton12 = types.KeyboardButton(text="نیازمندی ها" )
inbutton13 = types.KeyboardButton(text="خرید کالا" )
inbutton14 = types.KeyboardButton(text="فروش کالا")
inbutton15 = types.KeyboardButton(text="خرید بار")
inbutton16 = types.KeyboardButton(text="فروش بار")
inbutton17 = types.KeyboardButton(text="خرید روبل" )
inbutton18 = types.KeyboardButton(text="فروش روبل")
inbutton19 = types.KeyboardButton(text="خرید ارز دیجیتال",)
inbutton20 = types.KeyboardButton(text="فروش ارز دیجیتال" )
#inbutton21 = types.KeyboardButton(text="خدمات" )
inbuttoncn = KeyboardButton(text="لغو ❌" )
markupdaste = ReplyKeyboardMarkup(resize_keyboard=True)
markupdaste.row(inbutton6, inbutton7, inbutton8)
markupdaste.row(inbutton9, inbutton10, inbutton11)
markupdaste.row(inbutton12, inbutton13, inbutton14)
markupdaste.row(inbutton15, inbutton16)
markupdaste.row(inbutton17, inbutton18)
markupdaste.row(inbutton19, inbutton20)
#markupdaste.row(inbutton21)
markupdaste.row(inbuttoncn)


buttoncn = KeyboardButton(text="لغو ❌")
buttoncnmarkup = ReplyKeyboardMarkup(resize_keyboard=True)
buttoncnmarkup.add(buttoncn)


 #gharardad
inbuttongharardad1 = KeyboardButton(text="کوتاه مدت" )
inbuttongharardad2 = KeyboardButton(text="بلند مدت" )
inbuttongharardad3 = KeyboardButton(text="بدون قرارداد" )
markupgharardad = ReplyKeyboardMarkup(row_width=2 , resize_keyboard=True)
markupgharardad.add(inbuttongharardad1 , inbuttongharardad2 , inbuttongharardad3)

buttonprice = KeyboardButton(text="ماهانه")
buttonprice2 = KeyboardButton(text="روزانه")
markupprice = ReplyKeyboardMarkup(row_width=2 , resize_keyboard=True)
markupprice.add(buttonprice , buttonprice2)

buttontavafogh = KeyboardButton(text="توافقی")
marktavafogh = ReplyKeyboardMarkup(row_width=1 , resize_keyboard=True)
marktavafogh.add(buttontavafogh , buttoncn)

buttonacept = KeyboardButton(text="تایید آگهی")
buttonreject = KeyboardButton(text="لغو آگهی")
accorejmarkup = ReplyKeyboardMarkup(row_width=2 , resize_keyboard=True)
accorejmarkup.add(buttonacept , buttonreject)

irtoit = KeyboardButton(text="ایران به روسیه")
ittoir = KeyboardButton(text="روسیه به ایران")
country = ReplyKeyboardMarkup(row_width=2 , resize_keyboard=True)
country.add(irtoit , ittoir , buttoncn)


inbutton24 = KeyboardButton(text="مسکو")
inbutton25 = KeyboardButton(text="نووسیبیرسک" )
inbutton26 = KeyboardButton(text="سن_پترزبورک" )
inbutton27 = KeyboardButton(text="نیژنووگراد")
inbutton28 = KeyboardButton(text="کازان")
inbutton29 = KeyboardButton(text="اولیانوفسک")
inbutton30 = KeyboardButton(text="سامارا")
inbutton31 = KeyboardButton(text="روستوف")
inbutton32 = KeyboardButton(text="اومسک")
inbutton33 = KeyboardButton(text="اوفا")
inbutton34 = KeyboardButton(text="ولگوگراد")
inbutton35 = KeyboardButton(text="پرم")
inbutton36 = KeyboardButton(text="ورونژ")
inbutton37 = KeyboardButton(text="ولادی_وستوک")
inbutton38 = KeyboardButton(text="سایر")
inbuttoncn = KeyboardButton(text="لغو ❌")
markupcity = ReplyKeyboardMarkup(row_width=3)
markupcity.add(inbutton24, inbutton25, inbutton26, inbutton27, inbutton28, inbutton29, inbutton30, inbutton31, inbutton32, inbutton33,inbutton34, inbutton35)
markupcity.row(inbutton36, inbutton37)
markupcity.add(inbutton38)
markupcity.row(inbuttoncn)


irancity1 = KeyboardButton(text="تهران")
irancity2 = KeyboardButton(text="مشهد")
irancity3 = KeyboardButton(text="اصفهان")
irancity4 = KeyboardButton(text="تبریز")
irancity5 = KeyboardButton(text="شیراز")
irancity6 = KeyboardButton(text="کرج")
irancity7 = KeyboardButton(text="کرمانشاه")
irancity8 = KeyboardButton(text="اهواز")
irancity9 = KeyboardButton(text="قم")
irancity10 = KeyboardButton(text="زاهدان")
irancity11 = KeyboardButton(text="رشت")
irancity12 = KeyboardButton(text="ارومیه")
irancity13 = KeyboardButton(text="یزد")
irancity14 = KeyboardButton(text="کرمان")
irancity15 = KeyboardButton(text="همدان")
irancity16 = KeyboardButton(text="اراک")
irancity17 = KeyboardButton(text="بندرعباس")
irancity18 = KeyboardButton(text="اردبیل")
irancity19 = KeyboardButton(text="قزوین")
irancity20 = KeyboardButton(text="سنندج")
irancity21 = KeyboardButton(text="زنجان")
irancity22 = KeyboardButton(text="ساری")
irancity23 = KeyboardButton(text="گرگان")
irancity24 = KeyboardButton(text="سایر")
irancitymarkup = ReplyKeyboardMarkup(resize_keyboard=True , row_width=4)
irancitymarkup.add(irancity1 , irancity2 , irancity3 , irancity4 , irancity5 , irancity6 , irancity7 , irancity8 , irancity9 , irancity10 , irancity11 , irancity12 , irancity13 , irancity14 , irancity15 , irancity16 , irancity17 , irancity18 , irancity19 , irancity20)
irancitymarkup.row(irancity21 , irancity22 , irancity23)
irancitymarkup.row(irancity24)

foreuro2 = KeyboardButton(text="انتخاب روش ها")
foreuro2mark = ReplyKeyboardMarkup(resize_keyboard=True , row_width=1)
foreuro2mark.add(foreuro2 , buttoncn)

paymethod1 = KeyboardButton(text="PayPal")
paymethod2 = KeyboardButton(text="ارز دیجیتال")
paymethod3 = KeyboardButton(text="Monse")
paymethod4 = KeyboardButton(text="IBAN")
paymethod5 = KeyboardButton(text="نقدی حضوری")
paymethod6 = KeyboardButton(text="سایر")
paymethod = ReplyKeyboardMarkup(resize_keyboard=True , row_width=3)
paymethod.add(paymethod1 , paymethod2 , paymethod3)
paymethod.row(paymethod4, paymethod5)
paymethod.row(paymethod6)


paymethodtwo = ReplyKeyboardMarkup(resize_keyboard=True , row_width=3)
paymethodtwo.add(paymethod1 , paymethod2 , paymethod3)
paymethodtwo.row(paymethod4, paymethod5)



notozih  = KeyboardButton(text="بدون توضیحات")
tozihmark = ReplyKeyboardMarkup(row_width=1)
tozihmark.add(notozih , buttoncn )



startagain = KeyboardButton(text="شروع مجدد")
main = ReplyKeyboardMarkup (row_width=1)
main.add(startagain , buttoncn)

main2 = ReplyKeyboardMarkup (row_width=1)
main2.add(buttontavafogh,startagain , buttoncn)

tron = KeyboardButton(text="ترون , TRON")
theter = KeyboardButton(text="تتر , USDT")
btcm = ReplyKeyboardMarkup(row_width=1)
btcm.add(tron , theter)

withoutax = KeyboardButton(text="بدون عکس")
axmark = ReplyKeyboardMarkup(row_width=1)
axmark.add(withoutax , buttoncn)

@bot.message_handler(commands=['start'])
def start(m):
    bot.send_message(m.chat.id, text="""
        ♾️ کاربر عزیز ! سلام👋. به ربات نیازمندی های Rus bazar خوش آمدید. 🤩

✅ توجه داشته باشید که آگهی های شما پس از تایید در کانال روس بازار منتشر خواهد شد. لطفا با معرفی روس بازار به دوستان خود از این فعالیت حمایت کنید.

🔴 تایید صحت آگهی ها و درخواست های ثبت شده در روس بازار به عهده کاربران عزیز میباشد و Rus bazar هیچگونه مسئولیتی را در قبال آگهی ها نمی پذیرد.

🌐 خدمت رسانی به هم وطنان و هم زبانان عزیز از افتخارات ماست.


❌این ربات توسط گروه راشسان (Rush sun) توسعه یافته است!❌


        """, reply_markup=markup1)




@bot.message_handler(func=lambda m:m.text == "ثبت آگهی 📮")
def agahirig(message):
    global msgdaste
    msgdaste=bot.send_message(message.chat.id , reply_markup=markupdaste , text="لطفا یکی از دسته های زیر را انتخاب کنید")
    bot.register_next_step_handler(msgdaste , getdaste )


@bot.message_handler(func=lambda m: True)
def getdaste(message):
    global daste
    daste = message.text
    if message.text == "اجاره تخت" or message.text == "اجاره اتاق" or message.text == "اجاره خانه":
        bot.delete_message(chat_id=message.chat.id, message_id=msgdaste.message_id)
        bot.send_message(message.chat.id, text=f"📦 دسته بندی : {daste}")
        msg = bot.send_message(message.chat.id,
                               text="لطفا یک عکس مربوط به آگهی خود ارسال کنید (مکانی که میخواهید اجاره دهید) :",
                               reply_markup=axmark)
        bot.register_next_step_handler(msg, getimgcol1)

    elif message.text == "متقاضی تخت" or message.text == "متقاضی اتاق" or message.text == "متقاضی خانه":
        bot.delete_message(chat_id=message.chat.id, message_id=msgdaste.message_id)
        bot.send_message(message.chat.id, text=f"📦 دسته بندی : {daste}")
        msg = bot.send_message(message.chat.id, text="لطفا شهر خود را انتخاب کنید:", reply_markup=markupcity)
        bot.register_next_step_handler(msg, getcityrent)

    elif message.text == "خرید کالا" or message.text == "فروش کالا" or message.text == "نیازمندی ها":
        bot.delete_message(chat_id=message.chat.id, message_id=msgdaste.message_id)
        bot.send_message(chat_id=message.chat.id, text=f"📦 دسته بندی : {daste}")
        msg4 = bot.send_message(message.chat.id, text="لطفا شهر خود را انتخاب کنید:", reply_markup=markupcity)
        bot.register_next_step_handler(msg4, getcitycol3)

    elif message.text == "فروش بار" or message.text == "خرید بار":
        bot.delete_message(chat_id=message.chat.id, message_id=msgdaste.message_id)
        bot.send_message(chat_id=message.chat.id, text=f"📦 دسته بندی : {daste}")
        msgcountry = bot.send_message(message.chat.id, text="کشور را از مبدا به مقصد انتخاب کنید:",
                                      reply_markup=country)
        bot.register_next_step_handler(msgcountry, getcountrystuffittoir)

    elif message.text == "خرید روبل" or message.text == "فروش روبل":
        bot.delete_message(chat_id=message.chat.id, message_id=msgdaste.message_id)
        bot.send_message(chat_id=message.chat.id, text=f"📦 دسته بندی : {daste}")
        msgbuyeuro = bot.send_message(message.chat.id, text="""
        چند روبل برای معامله دارید؟

        فقط عدد وارد کنید.

        مثال : 615
        """)
        bot.register_next_step_handler(msgbuyeuro, euro1)
    elif message.text == "خرید ارز دیجیتال" or message.text == "فروش ارز دیجیتال":
        bot.delete_message(chat_id=message.chat.id, message_id=msgdaste.message_id)
        bot.send_message(chat_id=message.chat.id, text=f"📦 دسته بندی : {daste}")
        msgbuybtc = bot.send_message(message.chat.id, text="یک ارز را برای معامله انتخاب کنید:", reply_markup=btcm)
        bot.register_next_step_handler(msgbuybtc, witchbtc)

    elif message.text == "لغو ❌":
        cncltct(message)



def checkmember(user, channel):
    for i in channel:
        is_member = bot.get_chat_member(chat_id=i, user_id=user)
        if is_member.status in ['kicked', 'left']:
            return False
    return True



@bot.callback_query_handler(func=lambda call: call.data == "join")
def joinm(call):
    global is_member
    is_member = checkmember(user=call.from_user.id, channel=channel)
    if is_member is False:
        bot.send_message(chat_id=call.message.chat.id, text="برای استفاده از ربات لطفا عضو کانال ها و گروه های ما شوید")
    else:
        bot.send_message(chat_id=call.message.chat.id, text="""
        عضویت شما در کانال با موفقیت تایید شد ✅

        از حالا شما میتوانید از خدمات ربات استفاده کنید.
        """, reply_markup=markup2)


@bot.message_handler(content_types=['photo'])
def getimgcol1(message):
    if message.text == "لغو ❌":
        cncltct(message)
    elif message.text == "سایر":
        othercityrent(message)
    elif message.text == "بدون عکس":
        msg = bot.send_message(message.chat.id, text="لطفا شهر خود را انتخاب کنید:", reply_markup=markupcity)
        bot.register_next_step_handler(msg, getcityrent)
    else:
        global imgcol1
        imgcol1 = message.photo[-1].file_id
        msg = bot.send_message(message.chat.id, text="حال شهر خود را انتخاب کنید:", reply_markup=markupcity)
        bot.register_next_step_handler(msg, getcityrent1)


def getcityrent1(message):
    if message.text == "لغو ❌":
        cncltct(message)
    elif message.text == "سایر":
        othercityrent(message)
    else:
        global cityrent
        cityrent = message.text
        bot.send_message(message.chat.id, text=f"شهر : {cityrent}")
        msg = bot.send_message(message.chat.id, text="محدوده مورد نظر را وارد نمایید :", reply_markup=main)
        bot.register_next_step_handler(msg, getmahdooderent1)


def getmahdooderent1(message):
    if message.text == "لغو ❌":
        cncltct(message)
    elif message.text == "شروع مجدد":
        start(message)
    else:
        global mahdoode
        mahdoode = message.text
        msg = bot.send_message(message.chat.id, text="""

    تاریخ شروع مورد نظرتان را به میلادی وارد نمایید : 

فرمت : dd/mm/yyyy مثال : 05/02/2024
        """)
        bot.register_next_step_handler(msg, getstartdate1)


def getstartdate1(message):
    if message.text == "لغو ❌":
        cncltct(message)
    elif message.text == "شروع مجدد":
        start(message)
    else:
        global startdate
        startdate = message.text
        msg = bot.send_message(message.chat.id, text="""
    تاریخ پایان مورد نظرتان را به میلادی وارد نمایید : 

فرمت : dd/mm/yyyy مثال : 05/02/2024

پی نوشت : یا میتوانید با ارسال کلمه "توافقی" تاریخ پایان را توافقی ثبت کنید

    """, reply_markup=main2)
        bot.register_next_step_handler(msg, enddate1)


def enddate1(message):
    if message.text == "لغو ❌":
        cncltct(message)
    elif message.text == "شروع مجدد":
        start(message)
    else:
        global enddatee
        enddatee = message.text
        msg = bot.send_message(message.chat.id, text="وضعیت قرارداد را مشخص نمایید :", reply_markup=markupgharardad)
        bot.register_next_step_handler(msg, gharardadrent1)


def gharardadrent1(message):
    if message.text == "لغو ❌":
        cncltct(message)
    elif message.text == "شروع مجدد":
        start(message)
    else:
        global vaziat
        vaziat = message.text
        bot.send_message(message.chat.id, text=f"وضعیت قرارداد بصورت : {vaziat}")
        msg = bot.send_message(message.chat.id, text="""
    مایلید قیمت را به چه صورت اعلام کنید؟
    """, reply_markup=markupprice)
        bot.register_next_step_handler(msg, europrice1)


def europrice1(message):
    if message.text == "لغو ❌":
        cncltct(message)
    elif message.text == "شروع مجدد":
        start(message)
    else:
        global eprice
        eprice = message.text
        msg = bot.send_message(message.chat.id, text=f"""
         بصورت : {eprice}

         حاضرید چند روبل پرداخت کنید؟
         پی نوشت : فقط عدد وارد کنید یا با ارسال کلمه "توافقی" اطلاعات را ثبت کنید
""", reply_markup=marktavafogh)
        bot.register_next_step_handler(msg, gheymat1)


def gheymat1(message):
    global gheymateu
    gheymateu = message.text
    if message.text == "توافقی":
        bot.send_message(message.chat.id, text=f"""
        قیمت بصورت : {gheymateu}
        """)
        msg = bot.send_message(message.chat.id, text="توضیحات آگهی خود را وارد کنید:", reply_markup=tozihmark)
    elif message.text == "لغو ❌":
        cncltct(message)
    else:
        bot.send_message(message.chat.id, text=f"""
        قیمت بصورت : {eprice}
        """)
        msg = bot.send_message(message.chat.id, text="توضیحات آگهی خود را وارد کنید:", reply_markup=tozihmark)
    bot.register_next_step_handler(msg, toozihatimg)


def toozihatimg(message):
    global tozih
    UID = message.from_user.username
    tozih = message.text
    global captioncol1
    captioncol1 = f"""
🌀✅ {daste} ✅🌀

📍 مربوط به شهر:{cityrent} 

🔎 محدوده:
{mahdoode} 

🗓 تاریخ شروع:
{startdate}     

🗓  تاریخ پایان :
{enddatee}

📑 نوع قرارداد:{vaziat} 

💰 قیمت به روبل:{eprice} {gheymateu} 

👤 تماس با آگهی دهنده:
@{UID}

توضیحات آگهی :{tozih}

📎 @Rusbazar_bot  
📣 @rednews2022 @havashi_russ_2022 @niazmndiha_2024_rus

        """
    bot.send_photo(message.chat.id, photo=imgcol1, caption=captioncol1)
    msg = bot.send_message(message.chat.id, text="آیا آگهی خود را تایید میکنید؟", reply_markup=accorejmarkup)
    bot.register_next_step_handler(msg, concol1img)


def concol1img(message):
    if message.text == "تایید آگهی":
        bot.send_photo(chat_id=963475140, caption=captioncol1, photo=imgcol1)
        bot.send_message(message.chat.id, text="آگهی شما ثبت شد و پس از تایید در کانال قرار داده میشود✅",
                         reply_markup=markup2)
    elif message.text == "لغو آگهی":
        bot.send_message(message.chat.id, text="آگهی شما لغو شد❌", reply_markup=markup2)


@bot.message_handler(func=lambda m: True)
def getcityrent(message):
    if message.text == "لغو ❌":
        cncltct(message)
    elif message.text == "سایر":
        othercityrent(message)
    else:
        global cityrent
        cityrent = message.text
        bot.send_message(message.chat.id, text=f"شهر : {cityrent}")
        msg = bot.send_message(message.chat.id, text="محدوده مورد نظر را وارد نمایید :", reply_markup=main)
        bot.register_next_step_handler(msg, getmahdooderent)


@bot.message_handler(func=lambda m: True)
def getmahdooderent(message):
    if message.text == "لغو ❌":
        cncltct(message)
    elif message.text == "شروع مجدد":
        start(message)
    else:
        global mahdoode
        mahdoode = message.text
        msg = bot.send_message(message.chat.id, text="""

    تاریخ شروع مورد نظرتان را به میلادی وارد نمایید : 

فرمت : dd/mm/yyyy مثال : 05/02/2024
        """)
        bot.register_next_step_handler(msg, getstartdate)


def getstartdate(message):
    if message.text == "لغو ❌":
        cncltct(message)
    elif message.text == "شروع مجدد":
        start(message)
    else:
        global startdate
        startdate = message.text
        msg = bot.send_message(message.chat.id, text="""
    تاریخ پایان مورد نظرتان را به میلادی وارد نمایید : 

فرمت : dd/mm/yyyy مثال : 05/02/2024

پی نوشت : یا میتوانید با ارسال کلمه "توافقی" تاریخ پایان را توافقی ثبت کنید

    """, reply_markup=main2)
        bot.register_next_step_handler(msg, enddate)


def enddate(message):
    if message.text == "لغو ❌":
        cncltct(message)
    elif message.text == "شروع مجدد":
        start(message)
    else:
        global enddatee
        enddatee = message.text
        msg = bot.send_message(message.chat.id, text="وضعیت قرارداد را مشخص نمایید :", reply_markup=markupgharardad)
        bot.register_next_step_handler(msg, gharardadrent)


def gharardadrent(message):
    if message.text == "لغو ❌":
        cncltct(message)
    elif message.text == "شروع مجدد":
        start(message)
    else:
        global vaziat
        vaziat = message.text
        bot.send_message(message.chat.id, text=f"وضعیت قرارداد بصورت : {vaziat}")
        msg = bot.send_message(message.chat.id, text="""
    مایلید قیمت را به چه صورت اعلام کنید؟
    """, reply_markup=markupprice)
        bot.register_next_step_handler(msg, europrice)


def europrice(message):
    if message.text == "لغو ❌":
        cncltct(message)
    elif message.text == "شروع مجدد":
        start(message)
    else:
        global eprice
        eprice = message.text
        msg = bot.send_message(message.chat.id, text=f"""
         بصورت : {eprice}

         حاضرید چند روبل پرداخت کنید؟
         پی نوشت : فقط عدد وارد کنید یا با ارسال کلمه "توافقی" اطلاعات را ثبت کنید
""", reply_markup=marktavafogh)
        bot.register_next_step_handler(msg, gheymat)


def gheymat(message):
    global gheymateu
    gheymateu = message.text
    if message.text == "توافقی":
        bot.send_message(message.chat.id, text=f"""
        قیمت بصورت : {gheymateu}
        """)
        msg = bot.send_message(message.chat.id, text="توضیحات آگهی خود را وارد کنید:", reply_markup=tozihmark)
    elif message.text == "لغو ❌":
        cncltct(message)
    else:
        bot.send_message(message.chat.id, text=f"""
        قیمت بصورت : {eprice}
        """)
        msg = bot.send_message(message.chat.id, text="توضیحات آگهی خود را وارد کنید:", reply_markup=tozihmark)
    bot.register_next_step_handler(msg, toozihat)


def toozihat(message):
    global tozih
    UID = message.from_user.username
    tozih = message.text
    text = f"""
🌀✅ {daste} ✅🌀

📍 مربوط به شهر:{cityrent} 

🔎 محدوده:
{mahdoode} 

🗓 تاریخ شروع:
{startdate}     

🗓  تاریخ پایان :
{enddatee}

📑 نوع قرارداد:{vaziat} 

💰 قیمت به روبل:{eprice} {gheymateu} 

👤 تماس با آگهی دهنده:
@{UID}

توضیحات آگهی :{tozih}

📎 @Rusbazar_bot  
📣 @rednews2022 @havashi_russ_2022 @niazmndiha_2024_rus

    """
    bot.send_message(message.chat.id, text=text, reply_markup=accorejmarkup)
    msg = bot.send_message(message.chat.id, text="آیا آگهی خود را تایید میکنید؟", reply_markup=accorejmarkup)
    bot.register_next_step_handler(msg, final)


def final(message):
    global finalask
    finalask = message.text
    UID = message.from_user.username
    text = f"""
🌀✅ {daste} ✅🌀

📍 مربوط به شهر:{cityrent} 

🔎 محدوده:
{mahdoode} 

🗓 تاریخ شروع:
{startdate}     

🗓  تاریخ پایان :
{enddatee}

📑 نوع قرارداد:{vaziat} 

💰 قیمت به روبل: {eprice} {gheymateu} 

👤 تماس با آگهی دهنده:
@{UID}

    توضیحات آگهی :    {tozih}

📎 @Rusbazar_bot  
📣 @rednews2022 @havashi_russ_2022 @niazmndiha_2024_rus

        """

    if message.text == "تایید آگهی":
        bot.send_message(chat_id=963475140, text=text)
        bot.send_message(message.chat.id, text="آگهی شما ثبت شد و پس از تایید در کانال قرار داده میشود✅",
                         reply_markup=markup2)
    elif message.text == "لغو آگهی":
        bot.send_message(message.chat.id, text="آگهی شما لغو شد❌", reply_markup=markup2)


def getcitycol3(message):
    if message.text == "لغو ❌":
        cncltct(message)
    elif message.text == "شروع مجدد":
        start(message)
    elif message.text == "سایر":
        othercitycol3(message)
    else:
        global citycol3
        citycol3 = message.text
        bot.send_message(message.chat.id, text=f"📍 شهر :{citycol3}")
        msg = bot.send_message(message.chat.id, text=f"""
      قیمت مورد نظر خود را برای , {daste}, وارد کنید

(فقط عدد وارد کنید مانند : 8 یا 8.50)
یا میتوانید توافقی ثبت کنید. 

    """, reply_markup=main2)
        bot.register_next_step_handler(msg, getpricecol3)


def othercitycol3(message):
    msg = bot.send_message(message.chat.id, text="نام شهر خود را بنویسید و ارسال نمایید:", reply_markup=main)
    bot.register_next_step_handler(msg, othercitycol3two)


def othercitycol3two(message):
    if message.text == "لغو ❌":
        cncltct(message)
    elif message.text == "شروع مجدد":
        start(message)
    else:
        global citycol3
        citycol3 = message.text
        bot.send_message(message.chat.id, text=f"📍 شهر :{citycol3}")
        msg = bot.send_message(message.chat.id, text=f"""
      قیمت مورد نظر خود را برای , {daste}, وارد کنید

(فقط عدد وارد کنید مانند : 8 یا 8.50)
یا میتوانید توافقی ثبت کنید. 

    """, reply_markup=main2)
        bot.register_next_step_handler(msg, getpricecol3)


def getpricecol3(message):
    if message.text == "لغو ❌":
        cncltct(message)
    elif message.text == "شروع مجدد":
        start(message)
    else:
        global pricecol3
        pricecol3 = message.text
        if message.text == "توافقی":
            bot.send_message(message.chat.id, text=f"💶 قیمت :{pricecol3}")
            msg = bot.send_message(message.chat.id, text="توضیحات مربوط به اگهی خود را ارسال نمایید :",
                                   reply_markup=tozihmark)
        elif message.text == "لغو ❌":
            cncltct(message)
        else:
            bot.send_message(message.chat.id, text=f"💶 قیمت :{pricecol3}")
            msg = bot.send_message(message.chat.id, text="توضیحات مربوط به اگهی خود را ارسال نمایید :",
                                   reply_markup=tozihmark)
        bot.register_next_step_handler(msg, imgcol3)


def imgcol3(message):
    if message.text == "لغو ❌":
        cncltct(message)
    elif message.text == "شروع مجدد":
        start(message)
    else:
        global tozih
        tozih = message.text
        msg = bot.send_message(message.chat.id, text="یک عکس مربوط به آگهی خود ارسال کنید:", reply_markup=axmark)
        bot.register_next_step_handler(msg, img2)


@bot.message_handler(content_types=['photo'])
def img2(message):
    if message.text == "لغو ❌":
        cncltct(message)
    elif message.text == "بدون عکس":
        toozihatcol3two(message)
    else:
        UID = message.from_user.username
        global photocol3
        photocol3 = message.photo[-1].file_id
        global captioncol3
        captioncol3 = f"""

    🌀✅ {daste} ✅🌀

📍 مربوط به شهر:{citycol3} 

💰 قیمت به روبل: {pricecol3} 🙌

📋 توضیحات:
{tozih} 


👤 تماس با آگهی دهنده:
@{UID}


📎 @Rusbazar_bot  

📣 @rednews2022 @havashi_russ_2022 @niazmndiha_2024_rus




    """
        bot.send_photo(message.chat.id, caption=captioncol3, photo=photocol3)
        msg = bot.send_message(message.chat.id, text="آیا آگهی خود را تایید میکنید؟", reply_markup=accorejmarkup)
        bot.register_next_step_handler(msg, conimgcol3)


def conimgcol3(message):
    if message.text == "تایید آگهی":
        bot.send_photo(chat_id=963475140, caption=captioncol3, photo=photocol3, reply_markup=cnandcon)
        bot.send_message(message.chat.id, text="آگهی شما ثبت شد و پس از تایید در کانال قرار داده میشود✅",
                         reply_markup=markup2)

    elif message.text == "لغو آگهی":
        bot.send_message(message.chat.id, text="آگهی شما لغو شد❌", reply_markup=markup2)


inlinecon = InlineKeyboardButton(text="تایید", callback_data="تایید")
inlinecn = InlineKeyboardButton(text="لغو", callback_data="لغو")
cnandcon = InlineKeyboardMarkup(row_width=2)
cnandcon.add(inlinecon, inlinecn)


def toozihatcol3two(message):
    msg = bot.send_message(message.chat.id, text="لطفا مجددا توضیحات آگهی را وارد کنید.", reply_markup=tozihmark)
    bot.register_next_step_handler(msg, toozihatcol3)


def toozihatcol3(message):
    if message.text == "لغو ❌":
        cncltct(message)
    elif message.text == "شروع مجدد":
        start(message)
    else:
        global tozihcol3
        UID = message.from_user.username
        tozihcol3 = message.text
        bot.send_message(message.chat.id, text="""
     در حال ساخت آگهی شما . . .🪧📝

لطفا کمی صبور باشید🙏🏻   


    """)
        bot.send_chat_action(chat_id=message.chat.id, action="typing")
        time.sleep(1)
        bot.send_message(message.chat.id, text=f"""

    🌀✅ {daste} ✅🌀

📍 مربوط به شهر:{citycol3} 

💰 قیمت به روبل: {pricecol3} 🙌

📋 توضیحات:
{tozihcol3} 


👤 تماس با آگهی دهنده:
@{UID}


📎 @Rusbazar_bot  

📣 @rednews2022 @havashi_russ_2022 @niazmndiha_2024_rus




    """, reply_markup=accorejmarkup)
        msg = bot.send_message(message.chat.id, text="آیا آگهی خود را تایید میکنید؟", reply_markup=accorejmarkup)
        bot.register_next_step_handler(msg, finalcol3)


def finalcol3(message):
    global finalaskcol3
    finalaskcol3 = message.text
    UID = message.from_user.username
    text = f"""
        🌀✅ {daste} ✅🌀

📍 مربوط به شهر:{citycol3} 

💰 قیمت به روبل: {pricecol3} 🙌

📋 توضیحات:
{tozihcol3} 


👤 تماس با آگهی دهنده:
@{UID}


📎 @Rusbazar_bot  
📣 @rednews2022 @havashi_russ_2022 @niazmndiha_2024_rus
    """
    if message.text == "تایید آگهی":
        bot.send_message(chat_id=963475140, text=text)
        bot.send_message(message.chat.id, text="آگهی شما ثبت شد و پس از تایید در کانال قرار داده میشود✅",
                         reply_markup=markup2)
    elif message.text == "لغو آگهی":
        bot.send_message(message.chat.id, text="آگهی شما لغو شد❌", reply_markup=markup2)