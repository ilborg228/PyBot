from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

bombPlace=0
bomb="💣"
cross="❌"
nums=[
    "1️⃣","2️⃣","3️⃣","4️⃣","5️⃣","6️⃣","7️⃣","8️⃣","9️⃣"
]

btn_1 = InlineKeyboardButton(nums[0], callback_data='btn1')
btn_2 = InlineKeyboardButton(nums[1], callback_data='btn2')
btn_3 = InlineKeyboardButton(nums[2], callback_data='btn3')
btn_4 = InlineKeyboardButton(nums[3], callback_data='btn4')
btn_5 = InlineKeyboardButton(nums[4], callback_data='btn5')
btn_6 = InlineKeyboardButton(nums[5], callback_data='btn6')
btn_7 = InlineKeyboardButton(nums[6], callback_data='btn7')
btn_8 = InlineKeyboardButton(nums[7], callback_data='btn8')
btn_9 = InlineKeyboardButton(nums[8], callback_data='btn9')
list_btn=[]
list_btn.append(btn_1)
list_btn.append(btn_2)
list_btn.append(btn_3)
list_btn.append(btn_4)
list_btn.append(btn_5)
list_btn.append(btn_6)
list_btn.append(btn_7)
list_btn.append(btn_8)
list_btn.append(btn_9)

kb = InlineKeyboardMarkup().row(btn_1,btn_2,btn_3)
kb.add(btn_4,btn_5,btn_6)
kb.add(btn_7,btn_8,btn_9)

def start():
    for i in range(9):
        list_btn[i].text=nums[i]