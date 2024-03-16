from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes, CallbackQueryHandler

from dotenv import dotenv_values    

from data_cleaning.text_preprocessing import TextProcessing
from bot.sql import Query
from bot.data_search import SearchData

data_temp = None

env = dotenv_values(".env")
bot_token = env['BOT_TOKEN']

def build_menu(buttons,n_cols,header_buttons=None,footer_buttons=None):
  menu = [buttons[i:i + n_cols] for i in range(0, len(buttons), n_cols)]
  if header_buttons:
    menu.insert(0, header_buttons)
  if footer_buttons:
    menu.append(footer_buttons)
  return menu

async def start(update:Update, context:ContextTypes.DEFAULT_TYPE):
    print(f"Handler start :\n{update.message.text}")
    print("_"*40)
    await context.bot.send_message(
        chat_id=update.effective_message.chat_id,
        text="Halo, selamat datang di bot resep makanan. Silahkan masukkan bahan masak yang ingin dimasak.\nFormat : /menu (bahan makanan)\nContoh : /menu ayam, kentang dan jamur."
    )

async def menu(update:Update, context:ContextTypes.DEFAULT_TYPE):
    global data_temp 
    data_temp = None

    print(f"Handler menu :\n{update.message.text}")
    print("_"*40)

    '''membersihkan data dan ubah sentence menjadi word(list)'''
    list_ingd = update.message.text[update.message.text.find(' ')+1:]
    tp = TextProcessing()
    ingd = tp.hapus_stopword(list_ingd)
    list_ingd = ingd.split()
    list_ingd = [tp.case_folding(word) for word in list_ingd]
    print(list_ingd)

    '''query untuk ambil menu dengan like bahan yang diinput'''
    qry = Query('recipe.db')
    df = qry.get_data(list_ingd)
    data_temp = df.copy()

    if df.empty:
        ans = f"Maaf, tidak ada menu dengan bahan {tp.camelcase(list_ingd)}."
        await context.bot.send_message(
            chat_id=update.effective_message.chat_id,
            text= ans
        )
    else:
        '''cari data dengan cosine_similarity terdekat dengan inputan user'''
        sd = SearchData(tp, df) 
        suggest = sd.cosine_similarity((' ').join(list_ingd))
        print(f"suggest = {suggest}")

        ans = f'''Bahan masakan yang diinput adalah {tp.camelcase(list_ingd)}.
Silahkan pilih salah satu menu yang ingin dimasak dari menu dibawah ini.
'''
    
        button_list = []
        for each in suggest:
            button_list.append(InlineKeyboardButton(df['judul'][each], callback_data = df['judul'][each]))
            reply_markup=InlineKeyboardMarkup(build_menu(button_list,n_cols=1)) #n_cols = 1 is for single column and mutliple rows

        await context.bot.send_message(
            chat_id=update.effective_message.chat_id,
            text= ans,reply_markup=reply_markup
        )

async def recipe(update:Update, context:ContextTypes.DEFAULT_TYPE):
    print(f"Handler recipe : {update.callback_query.data}")
    print("_"*40)
    # print(update)
    # print(data_temp)
    # print(data_temp.shape)
    df_recipe = data_temp[data_temp['judul'] == update.callback_query.data]
    # print("_"*40)
    # print(df_recipe)
    # print("_"*40)
    # print(f"df [1:2] : {df_recipe[0:1]['judul']}")
    # print('\n')
    # print(f"df [bumbu] :\n{df_recipe['bumbu']}")
    # print(f"df [bumbu] :\n{df_recipe['bahan'].values}")

    # ans = 'jawaban'

    if df_recipe.empty:
       ans = 'Pilihan menu tidak valid, silahkan pilih menu lainnya.'
    else:
        if df_recipe[0:1]['bumbu'].values != 'tanpa bumbu':
            ans = f'''{df_recipe['judul'].values[0]}
Bahan:
{df_recipe['bahan'].values[0]}

Bumbu:
{df_recipe['bumbu'].values[0]}

Cara Memasak:
{df_recipe['metode'].values[0]}'''
        else:
            ans = f'''{df_recipe['judul'].values[0]}
Bahan:
{df_recipe['bahan'].values[0]}

Cara Memasak:
{df_recipe['metode'].values[0]}'''
            
    print(ans)
    print("_"*40)

    await context.bot.send_message(
        chat_id=update.effective_message.chat_id,
        text=ans
    )



if __name__ == "__main__":
    #membuat object aplikasi
    application = Application.builder().token(bot_token).build()

    #membuat objek start handler
    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)

    #membuat objek menu handler
    menu_handler = CommandHandler('menu', menu)
    application.add_handler(menu_handler)

    #membuat objek recipe handler
    recipe_handler = CallbackQueryHandler(recipe)
    application.add_handler(recipe_handler)

    print("aplikasi berjalan")

    #menjalankan aplikasi secara streaming
    application.run_polling()
