import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    Application, CommandHandler, CallbackQueryHandler,
    MessageHandler, filters, ContextTypes
)

# ===================== SOZLAMALAR =====================
TOKEN = "8714899870:AAGLOulu-f-Xxga33Fic4Txd6bExkBaUIfI"
ADMIN_ID = 1086464991

# ===================== TILLAR =====================
TEXTS = {
    "uz": {
        "welcome": "🎮 Donat xizmatiga xush kelibsiz!\n\nXizmat tanlang:",
        "choose_product": "Mahsulot tanlang:",
        "choose_bank": "💳 To'lov turini tanlang:",
        "bank_info": "💳 To'lov rekviziti:\n\n{name}\n💳 Karta: {card}\n📞 Telefon: {phone}\n\n📸 To'lov qilgandan so'ng chek SKRINSHOT qilib yuboring!\n\n⚠️ Cheksiz buyurtma tasdiqlanmaydi!",
        "send_receipt": "📸 Chek (skrinshot) yuboring!",
        "enter_id_pubg": "📝 PUBG Mobile ID raqamingizni yuboring:\n(Masalan: 5234567890)",
        "enter_id_tiktok": "📝 TikTok username yuboring:\n(Masalan: @username)",
        "order_received": "✅ Buyurtmangiz qabul qilindi!\n\n🔢 Buyurtma №{order_id}\n⏳ Ko'rib chiqilmoqda...",
        "order_processing": "⏳ UC tushmoqda, kuting...",
        "order_done": "🎮 UC tushdi! Rahmat! 🙏",
        "order_failed": "😔 Muammo yuz berdi, tez hal qilamiz.",
        "order_rejected": "❌ Buyurtma rad etildi. Muammo bo'lsa @mynameisakuw ga yozing.",
        "no_orders": "📋 Hozircha buyurtma yo'q.",
        "my_orders_title": "📋 BUYURTMALARINGIZ:\n\n",
        "help_text": "❓ YORDAM\n\n1️⃣ Xizmat tanlang\n2️⃣ To'lov turini tanlang\n3️⃣ To'lov qiling\n4️⃣ Chek yuboring\n5️⃣ ID kiriting\n6️⃣ Tasdiqlashni kuting\n\n📞 Muammo: @mynameisakuw",
        "back": "🔙 Orqaga",
        "cancel": "❌ Bekor qilish",
        "my_orders": "📋 Buyurtmalarim",
        "help": "❓ Yordam",
        "status_pending": "⏳ Kutmoqda",
        "status_confirmed": "✅ Bajarildi",
        "status_rejected": "❌ Rad etildi",
        "order_summary": "📌 Buyurtma:\n━━━━━━━━━━━━━\n🎮 {item}\n💰 {price} TJS\n━━━━━━━━━━━━━\n\n",
        "enter_game_id": "Endi o'yin ID ni yuboring:",
        "game_id_received": "✅ ID qabul qilindi: {game_id}",
    },
    "ru": {
        "welcome": "🎮 Добро пожаловать в сервис доната!\n\nВыберите услугу:",
        "choose_product": "Выберите товар:",
        "choose_bank": "💳 Выберите способ оплаты:",
        "bank_info": "💳 Реквизиты для оплаты:\n\n{name}\n💳 Карта: {card}\n📞 Телефон: {phone}\n\n📸 После оплаты сделайте СКРИНШОТ чека и отправьте!\n\n⚠️ Заказ без чека не подтверждается!",
        "send_receipt": "📸 Отправьте скриншот чека!",
        "enter_id_pubg": "📝 Отправьте ваш PUBG Mobile ID:\n(Пример: 5234567890)",
        "enter_id_tiktok": "📝 Отправьте ваш TikTok username:\n(Пример: @username)",
        "order_received": "✅ Заказ принят!\n\n🔢 Заказ №{order_id}\n⏳ Обрабатывается...",
        "order_processing": "⏳ UC отправляется, подождите...",
        "order_done": "🎮 UC зачислен! Спасибо! 🙏",
        "order_failed": "😔 Возникла проблема, скоро решим.",
        "order_rejected": "❌ Заказ отклонён. Проблемы пишите @mynameisakuw.",
        "no_orders": "📋 Заказов пока нет.",
        "my_orders_title": "📋 ВАШИ ЗАКАЗЫ:\n\n",
        "help_text": "❓ ПОМОЩЬ\n\n1️⃣ Выберите услугу\n2️⃣ Выберите способ оплаты\n3️⃣ Оплатите\n4️⃣ Отправьте чек\n5️⃣ Введите ID\n6️⃣ Ждите подтверждения\n\n📞 Проблемы: @mynameisakuw",
        "back": "🔙 Назад",
        "cancel": "❌ Отмена",
        "my_orders": "📋 Мои заказы",
        "help": "❓ Помощь",
        "status_pending": "⏳ Ожидает",
        "status_confirmed": "✅ Выполнен",
        "status_rejected": "❌ Отклонён",
        "order_summary": "📌 Заказ:\n━━━━━━━━━━━━━\n🎮 {item}\n💰 {price} TJS\n━━━━━━━━━━━━━\n\n",
        "enter_game_id": "Теперь отправьте ваш игровой ID:",
        "game_id_received": "✅ ID принят: {game_id}",
    },
    "tj": {
        "welcome": "🎮 Хуш омадед ба хидмати донат!\n\nХидматро интихоб кунед:",
        "choose_product": "Молро интихоб кунед:",
        "choose_bank": "💳 Намуди пардохтро интихоб кунед:",
        "bank_info": "💳 Реквизитҳои пардохт:\n\n{name}\n💳 Карта: {card}\n📞 Телефон: {phone}\n\n📸 Пас аз пардохт СКРИНШОТ қабзро фиристед!\n\n⚠️ Фармоиш бе қабз тасдиқ намешавад!",
        "send_receipt": "📸 Скриншоти қабзро фиристед!",
        "enter_id_pubg": "📝 ID-и PUBG Mobile-и худро фиристед:\n(Мисол: 5234567890)",
        "enter_id_tiktok": "📝 Номи корбарии TikTok-и худро фиристед:\n(Мисол: @username)",
        "order_received": "✅ Фармоиши шумо қабул шуд!\n\n🔢 Фармоиш №{order_id}\n⏳ Дар ҳоли баррасӣ...",
        "order_processing": "⏳ UC дар ҳоли фиристодан, интизор бошед...",
        "order_done": "🎮 UC расид! Ташаккур! 🙏",
        "order_failed": "😔 Мушкилот пеш омад, зуд ҳал мекунем.",
        "order_rejected": "❌ Фармоиш рад шуд. Мушкилот @mynameisakuw.",
        "no_orders": "📋 Ҳоло фармоише нест.",
        "my_orders_title": "📋 ФАРМОИШҲОИ ШУМО:\n\n",
        "help_text": "❓ КУМАК\n\n1️⃣ Хидматро интихоб кунед\n2️⃣ Намуди пардохтро интихоб кунед\n3️⃣ Пардохт кунед\n4️⃣ Қабзро фиристед\n5️⃣ ID ворид кунед\n6️⃣ Тасдиқро интизор шавед\n\n📞 Мушкилот: @mynameisakuw",
        "back": "🔙 Бозгашт",
        "cancel": "❌ Бекор кардан",
        "my_orders": "📋 Фармоишҳоям",
        "help": "❓ Кумак",
        "status_pending": "⏳ Интизор",
        "status_confirmed": "✅ Иҷро шуд",
        "status_rejected": "❌ Рад шуд",
        "order_summary": "📌 Фармоиш:\n━━━━━━━━━━━━━\n🎮 {item}\n💰 {price} TJS\n━━━━━━━━━━━━━\n\n",
        "enter_game_id": "Акнун ID-и бозии худро фиристед:",
        "game_id_received": "✅ ID қабул шуд: {game_id}",
    }
}

def t(lang, key, **kwargs):
    text = TEXTS.get(lang, TEXTS["uz"]).get(key, key)
    if kwargs:
        text = text.format(**kwargs)
    return text

# ===================== NARXLAR =====================
PRODUCTS = {
    "pubg": {
        "name": "🎮 PUBG Mobile UC",
        "items": [
            {"id": "pubg_60", "name": "60 UC", "price": 13},
            {"id": "pubg_325", "name": "325 UC", "price": 55},
            {"id": "pubg_660", "name": "660 UC", "price": 110},
            {"id": "pubg_2100", "name": "1800+300 UC (2100)", "price": 290},
            {"id": "pubg_3850", "name": "3850 UC", "price": 560},
            {"id": "pubg_8100", "name": "8100 UC", "price": 1150},
        ]
    },
    "tiktok": {
        "name": "🎵 TikTok Monetalari",
        "items": [
            {"id": "tt_100", "name": "100 Moneta", "price": 13},
            {"id": "tt_500", "name": "500 Moneta", "price": 65},
            {"id": "tt_1000", "name": "1000 Moneta", "price": 130},
            {"id": "tt_3000", "name": "3000 Moneta", "price": 380},
            {"id": "tt_5000", "name": "5000 Moneta", "price": 620},
            {"id": "tt_10000", "name": "10000 Moneta", "price": 1230},
        ]
    }
}

# ===================== BANKLAR =====================
BANKS = {
    "dcb": {"name": "🏦 Dushanbe City Bank", "card": "9762 0001 6511 8307", "phone": "+992000033534"},
    "eskhata": {"name": "🏦 Eskhata Bank", "card": "5058 2704 3234 4405", "phone": "+992000033534"},
    "spitamen": {"name": "🏦 Spitamen Bank", "card": "4607 6555 0075 6697", "phone": "+992000033534"},
    "sber": {"name": "🏦 Sberbank 🇷🇺", "card": "2202 2084 0905 7859", "phone": "+79808748143"},
    "tinkoff": {"name": "🏦 Tinkoff 🇷🇺", "card": "2200 7020 0460 8944", "phone": "+79808748143"},
    "alfa": {"name": "🏦 Alfa Bank 🇷🇺", "card": "2200 1536 7125 8177", "phone": "+79808748143"},
}

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

orders = {}
order_counter = [0]

# ===================== TIL TANLASH =====================
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("🇺🇿 O'zbek", callback_data="lang_uz")],
        [InlineKeyboardButton("🇷🇺 Русский", callback_data="lang_ru")],
        [InlineKeyboardButton("🇹🇯 Тоҷикӣ", callback_data="lang_tj")],
    ]
    await update.message.reply_text(
        "🌐 Tilni tanlang / Выберите язык / Забонро интихоб кунед:",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

# ===================== ASOSIY MENYU =====================
async def show_main_menu(query, lang):
    keyboard = [
        [InlineKeyboardButton("🎮 PUBG UC", callback_data="cat_pubg"),
         InlineKeyboardButton("🎵 TikTok Moneta", callback_data="cat_tiktok")],
        [InlineKeyboardButton(t(lang, "my_orders"), callback_data="my_orders"),
         InlineKeyboardButton(t(lang, "help"), callback_data="help")]
    ]
    await query.edit_message_text(
        t(lang, "welcome"),
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

# ===================== CALLBACKLAR =====================
async def callback_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    data = query.data
    user_id = query.from_user.id
    lang = context.user_data.get("lang", "uz")

    # Til tanlash
    if data.startswith("lang_"):
        lang = data.replace("lang_", "")
        context.user_data["lang"] = lang
        keyboard = [
            [InlineKeyboardButton("🎮 PUBG UC", callback_data="cat_pubg"),
             InlineKeyboardButton("🎵 TikTok Moneta", callback_data="cat_tiktok")],
            [InlineKeyboardButton(t(lang, "my_orders"), callback_data="my_orders"),
             InlineKeyboardButton(t(lang, "help"), callback_data="help")]
        ]
        await query.edit_message_text(
            t(lang, "welcome"),
            reply_markup=InlineKeyboardMarkup(keyboard)
        )

    # Kategoriya
    elif data.startswith("cat_"):
        cat = data.replace("cat_", "")
        product = PRODUCTS[cat]
        keyboard = []
        for item in product["items"]:
            keyboard.append([InlineKeyboardButton(
                f"{item['name']} — {item['price']} TJS",
                callback_data=f"buy_{cat}_{item['id']}"
            )])
        keyboard.append([InlineKeyboardButton(t(lang, "back"), callback_data="back_main")])
        await query.edit_message_text(
            t(lang, "choose_product"),
            reply_markup=InlineKeyboardMarkup(keyboard)
        )

    # Mahsulot tanlash
    elif data.startswith("buy_"):
        parts = data.split("_")
        cat = parts[1]
        item_id = "_".join(parts[2:])
        item = next((i for i in PRODUCTS[cat]["items"] if i["id"] == item_id), None)
        if not item:
            return
        context.user_data["selected_item"] = item
        context.user_data["selected_cat"] = cat

        # To'lov turini ko'rsat
        keyboard = [
            [InlineKeyboardButton("🇹🇯 Dushanbe City Bank", callback_data="bank_dcb")],
            [InlineKeyboardButton("🇹🇯 Eskhata Bank", callback_data="bank_eskhata")],
            [InlineKeyboardButton("🇹🇯 Spitamen Bank", callback_data="bank_spitamen")],
            [InlineKeyboardButton("🇷🇺 Sberbank", callback_data="bank_sber")],
            [InlineKeyboardButton("🇷🇺 Tinkoff", callback_data="bank_tinkoff")],
            [InlineKeyboardButton("🇷🇺 Alfa Bank", callback_data="bank_alfa")],
            [InlineKeyboardButton(t(lang, "cancel"), callback_data="back_main")]
        ]
        await query.edit_message_text(
            t(lang, "order_summary", item=item["name"], price=item["price"]) +
            t(lang, "choose_bank"),
            reply_markup=InlineKeyboardMarkup(keyboard)
        )

    # Bank tanlash
    elif data.startswith("bank_"):
        bank_key = data.replace("bank_", "")
        bank = BANKS.get(bank_key)
        if not bank:
            return
        context.user_data["selected_bank"] = bank_key
        context.user_data["step"] = "waiting_receipt"
        await query.edit_message_text(
            t(lang, "bank_info",
              name=bank["name"],
              card=bank["card"],
              phone=bank["phone"])
        )

    # 2-bosqich: UC tushdi/tushmadi (admin uchun)
    elif data.startswith("done_"):
        if user_id != ADMIN_ID:
            return
        order_id = int(data.replace("done_", ""))
        if order_id in orders:
            order = orders[order_id]
            order["status"] = "confirmed"
            await context.bot.send_message(
                chat_id=order["user_id"],
                text=t(order.get("lang", "uz"), "order_done")
            )
            await query.edit_message_reply_markup(reply_markup=None)
            await query.message.reply_text(f"✅ #{order_id} — bajarildi!")

    elif data.startswith("notdone_"):
        if user_id != ADMIN_ID:
            return
        order_id = int(data.replace("notdone_", ""))
        if order_id in orders:
            order = orders[order_id]
            order["status"] = "failed"
            await context.bot.send_message(
                chat_id=order["user_id"],
                text=t(order.get("lang", "uz"), "order_failed")
            )
            await query.edit_message_reply_markup(reply_markup=None)
            await query.message.reply_text(f"❌ #{order_id} — bajarilmadi!")

    # 1-bosqich: chekni tasdiqlash (admin)
    elif data.startswith("confirm_"):
        if user_id != ADMIN_ID:
            return
        order_id = int(data.replace("confirm_", ""))
        if order_id in orders:
            order = orders[order_id]
            order["status"] = "processing"
            await context.bot.send_message(
                chat_id=order["user_id"],
                text=t(order.get("lang", "uz"), "order_processing")
            )
            # 2-bosqich tugmalari
            keyboard = [
                [InlineKeyboardButton("✅ UC tushdi", callback_data=f"done_{order_id}"),
                 InlineKeyboardButton("❌ Tushmadi", callback_data=f"notdone_{order_id}")]
            ]
            await query.edit_message_caption(
                caption=query.message.caption + "\n\n⏳ JARAYONDA",
                reply_markup=InlineKeyboardMarkup(keyboard)
            )

    elif data.startswith("reject_"):
        if user_id != ADMIN_ID:
            return
        order_id = int(data.replace("reject_", ""))
        if order_id in orders:
            order = orders[order_id]
            order["status"] = "rejected"
            await context.bot.send_message(
                chat_id=order["user_id"],
                text=t(order.get("lang", "uz"), "order_rejected")
            )
            await query.edit_message_caption(
                caption=query.message.caption + "\n\n❌ RAD ETILDI",
                reply_markup=None
            )

    elif data == "back_main":
        await show_main_menu(query, lang)

    elif data == "my_orders":
        user_orders = [o for o in orders.values() if o["user_id"] == user_id]
        if not user_orders:
            await query.edit_message_text(
                t(lang, "no_orders"),
                reply_markup=InlineKeyboardMarkup([[
                    InlineKeyboardButton(t(lang, "back"), callback_data="back_main")
                ]])
            )
        else:
            text = t(lang, "my_orders_title")
            for o in user_orders[-5:]:
                s = t(lang, "status_" + o.get("status", "pending").replace("processing", "pending").replace("failed", "rejected"))
                text += f"#{o['id']} | {o['item']['name']} | {s}\n"
            await query.edit_message_text(
                text,
                reply_markup=InlineKeyboardMarkup([[
                    InlineKeyboardButton(t(lang, "back"), callback_data="back_main")
                ]])
            )

    elif data == "help":
        await query.edit_message_text(
            t(lang, "help_text"),
            reply_markup=InlineKeyboardMarkup([[
                InlineKeyboardButton(t(lang, "back"), callback_data="back_main")
            ]])
        )

    # Admin panel
    elif data == "admin_pending":
        if user_id != ADMIN_ID:
            return
        pending = [o for o in orders.values() if o["status"] == "pending"]
        text = "⏳ KUTAYOTGANLAR:\n\n" if pending else "Kutayotgan buyurtma yo'q."
        for o in pending:
            text += f"#{o['id']} | {o['item']['name']} | {o['game_id']} | @{o['username']}\n"
        await query.edit_message_text(text)

    elif data == "admin_done":
        if user_id != ADMIN_ID:
            return
        done = [o for o in orders.values() if o["status"] == "confirmed"]
        text = "✅ BAJARILGANLAR:\n\n" if done else "Bajarilgan buyurtma yo'q."
        for o in done:
            text += f"#{o['id']} | {o['item']['name']} | {o['game_id']} | @{o['username']}\n"
        await query.edit_message_text(text)

    elif data == "admin_prices":
        if user_id != ADMIN_ID:
            return
        text = "💰 NARXLAR:\n\n"
        for cat, d in PRODUCTS.items():
            text += f"{d['name']}:\n"
            for item in d["items"]:
                text += f"  • {item['name']} — {item['price']} TJS\n"
        await query.edit_message_text(text)

# ===================== XABARLAR =====================
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    step = context.user_data.get("step")
    lang = context.user_data.get("lang", "uz")

    if step == "waiting_receipt":
        if update.message.photo or update.message.document:
            item = context.user_data.get("selected_item")
            cat = context.user_data.get("selected_cat")

            order_counter[0] += 1
            order_id = order_counter[0]

            order = {
                "id": order_id,
                "user_id": user.id,
                "username": user.username or user.first_name,
                "cat": cat,
                "item": item,
                "game_id": "",
                "status": "pending",
                "lang": lang
            }
            orders[order_id] = order
            context.user_data["current_order_id"] = order_id
            context.user_data["step"] = "waiting_game_id"

            await update.message.reply_text(t(lang, "enter_game_id"))

            # Adminga chek yuborish
            keyboard = [
                [InlineKeyboardButton("✅ Tasdiqlash", callback_data=f"confirm_{order_id}"),
                 InlineKeyboardButton("❌ Rad etish", callback_data=f"reject_{order_id}")]
            ]
            bank_key = context.user_data.get("selected_bank", "")
            bank = BANKS.get(bank_key, {})
            caption = (
                f"🔔 YANGI BUYURTMA #{order_id}\n\n"
                f"👤 Mijoz: @{user.username or user.first_name} (ID: {user.id})\n"
                f"🎮 Mahsulot: {item['name']}\n"
                f"💰 Narx: {item['price']} TJS\n"
                f"🏦 Bank: {bank.get('name', '-')}\n"
                f"🆔 O'yin ID: (kutilmoqda...)"
            )
            if update.message.photo:
                await context.bot.send_photo(
                    chat_id=ADMIN_ID,
                    photo=update.message.photo[-1].file_id,
                    caption=caption,
                    reply_markup=InlineKeyboardMarkup(keyboard)
                )
            else:
                await context.bot.send_document(
                    chat_id=ADMIN_ID,
                    document=update.message.document.file_id,
                    caption=caption,
                    reply_markup=InlineKeyboardMarkup(keyboard)
                )
        else:
            await update.message.reply_text(t(lang, "send_receipt"))

    elif step == "waiting_game_id":
        game_id = update.message.text
        order_id = context.user_data.get("current_order_id")
        if order_id and order_id in orders:
            orders[order_id]["game_id"] = game_id
            context.user_data["step"] = None
            await update.message.reply_text(
                t(lang, "order_received", order_id=order_id) + f"\n🆔 ID: {game_id}"
            )
            # Adminga ID xabari
            await context.bot.send_message(
                chat_id=ADMIN_ID,
                text=f"🆔 Buyurtma #{order_id} uchun ID keldi: {game_id}"
            )

# ===================== ADMIN PANEL =====================
async def admin_panel(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id != ADMIN_ID:
        await update.message.reply_text("❌ Ruxsat yo'q!")
        return
    pending = len([o for o in orders.values() if o["status"] == "pending"])
    done = len([o for o in orders.values() if o["status"] == "confirmed"])
    keyboard = [
        [InlineKeyboardButton("⏳ Kutayotganlar", callback_data="admin_pending")],
        [InlineKeyboardButton("✅ Bajarilganlar", callback_data="admin_done")],
        [InlineKeyboardButton("💰 Narxlar", callback_data="admin_prices")],
    ]
    await update.message.reply_text(
        f"🔧 ADMIN PANEL\n\n⏳ Kutayotgan: {pending}\n✅ Bajarilgan: {done}\n📦 Jami: {len(orders)}",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

# ===================== ISHGA TUSHIRISH =====================
def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("admin", admin_panel))
    app.add_handler(CallbackQueryHandler(callback_handler))
    app.add_handler(MessageHandler(filters.ALL & ~filters.COMMAND, handle_message))
    print("✅ Bot ishga tushdi!")
    app.run_polling()

if __name__ == "__main__":
    main()
