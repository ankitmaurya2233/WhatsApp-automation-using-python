import pywhatkit as kit

def send_message(phone_no, message):
    # Send a message immediately
    kit.sendwhatmsg_instantly(phone_no, message)
    print(f"Message sent to {phone_no}")

def send_image(phone_no, image_path, message=""):
    # Send an image along with an optional message
    kit.sendwhats_image(phone_no, image_path, message)
    print(f"Image sent to {phone_no}")
