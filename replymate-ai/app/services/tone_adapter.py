def adapt_tone(message, tone="formal"):
    if tone == "casual":
        return message + " 😎"
    elif tone == "friendly":
        return "Hey! " + message
    elif tone == "formal":
        return "Dear customer, " + message
    else:
        return message
