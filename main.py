from telegram import Update, ChatPermissions
from telegram.ext import Updater, CommandHandler, CallbackContext
import random
import os

TOKEN = os.getenv("BOT_TOKEN")  # or put your token directly here

# --- Moderation commands ---

def mute(update: Update, context: CallbackContext):
    if not update.message.reply_to_message:
        update.message.reply_text("Reply to a user to mute them.")
        return
    user = update.message.reply_to_message.from_user
    chat = update.effective_chat
    chat.restrict_member(user.id, permissions=ChatPermissions(can_send_messages=False))
    update.message.reply_text(f"{user.first_name} has been muted.")

def unmute(update: Update, context: CallbackContext):
    if not update.message.reply_to_message:
        update.message.reply_text("Reply to a user to unmute them.")
        return
    user = update.message.reply_to_message.from_user
    chat = update.effective_chat
    chat.restrict_member(user.id, permissions=ChatPermissions(can_send_messages=True))
    update.message.reply_text(f"{user.first_name} has been unmuted.")

def ban(update: Update, context: CallbackContext):
    if not update.message.reply_to_message:
        update.message.reply_text("Reply to a user to ban them.")
        return
    user = update.message.reply_to_message.from_user
    chat = update.effective_chat
    chat.ban_member(user.id)
    update.message.reply_text(f"{user.first_name} has been banned.")

def unban(update: Update, context: CallbackContext):
    if len(context.args) != 1:
        update.message.reply_text("Usage: /unban <user_id>")
        return
    user_id = int(context.args[0])
    chat = update.effective_chat
    chat.unban_member(user_id)
    update.message.reply_text(f"User with ID {user_id} has been unbanned.")

def warn(update: Update, context: CallbackContext):
    if not update.message.reply_to_message:
        update.message.reply_text("Reply to a user to warn them.")
        return
    user = update.message.reply_to_message.from_user
    update.message.reply_text(f"{user.first_name}, consider this your warning.")

def rules(update: Update, context: CallbackContext):
    rules_text = (
        "1. Be respectful.\n"
        "2. No spam or flooding.\n"
        "3. No hate speech or offensive language.\n"
        "4. Follow admins’ instructions.\n"
        "Break the rules, face the consequences."
    )
    update.message.reply_text(rules_text)

# --- Fun commands ---

def vibecheck(update: Update, context: CallbackContext):
    vibes = ["Chill", "Fire", "Confused", "Energized", "Mystic", "Dark Energy"]
    vibe = random.choice(vibes)
    update.message.reply_text(f"Vibecheck: {update.message.from_user.first_name}’s vibe is **{vibe}**.")

def roasty(update: Update, context: CallbackContext):
    roasts = [
        "You bring everyone so much joy... when you leave the room.",
        "You have something on your chin… no, the third one down.",
        "You’re as bright as a black hole, and twice as dense.",
        "You’re like a cloud. When you disappear, it’s a beautiful day."
    ]
    roast = random.choice(roasts)
    update.message.reply_text(roast)

def ping(update: Update, context: CallbackContext):
    update.message.reply_text("Pong.")

def start(update: Update, context: CallbackContext):
    update.message.reply_text("MorpheusBot online. I see all.")

def unknown(update: Update, context: CallbackContext):
    update.message.reply_text("I do not comprehend this command...")

def main():
    updater = Updater(TOKEN)
    dp = updater.dispatcher

    # Moderation
    dp.add_handler(CommandHandler("mute", mute))
    dp.add_handler(CommandHandler("unmute", unmute))
    dp.add_handler(CommandHandler("ban", ban))
    dp.add_handler(CommandHandler("unban", unban))
    dp.add_handler(CommandHandler("warn", warn))
    dp.add_handler(CommandHandler("rules", rules))

    # Fun
    dp.add_handler(CommandHandler("vibecheck", vibecheck))
    dp.add_handler(CommandHandler("roasty", roasty))
    dp.add_handler(CommandHandler("ping", ping))

    # Misc
    dp.add_handler(CommandHandler("start", start))

    # Unknown commands
    from telegram.ext import MessageHandler, Filters
    dp.add_handler(MessageHandler(Filters.command, unknown))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
