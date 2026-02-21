def process_price_input(price_input):
    try:
        # Validate and convert BDT to USD
        if price_input.endswith(' BDT'):
            price_bdt = float(price_input.replace(' BDT', '').strip())
            exchange_rate = get_exchange_rate()  # Placeholder for a function to get exchange rate
            price_usd = price_bdt / exchange_rate
            return price_usd
        else:
            return float(price_input)  # Assuming input is in USD
    except ValueError:
        raise ValueError('Invalid price input. Please enter a valid amount.')


def add_price(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text='Please enter the price in BDT (e.g., 1000 BDT) or USD (e.g., 10.0):')
    return "HANDLE_PRICE_INPUT"


def handle_price_input(update, context):
    price_input = update.message.text
    price_usd = process_price_input(price_input)
    exchange_rate = get_exchange_rate()
    # Display formatted price with exchange rate
    formatted_price = f'{price_usd:.2f} USD'
    context.bot.send_message(chat_id=update.effective_chat.id, text=f'Price: {formatted_price} (based on an exchange rate of {exchange_rate:.2f} BDT/USD)')
    context.bot.send_message(chat_id=update.effective_chat.id, text='Preview your input before confirmation:')
    # Ask for confirmation
    confirm_keyboard = [[InlineKeyboardButton('Confirm', callback_data='confirm_price')]]
    reply_markup = InlineKeyboardMarkup(confirm_keyboard)
    context.bot.send_message(chat_id=update.effective_chat.id, text='Do you want to confirm this price?', reply_markup=reply_markup)