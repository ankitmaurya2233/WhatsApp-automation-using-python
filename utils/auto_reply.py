from selenium import webdriver
import pywhatkit as kit

def auto_reply():
    driver = webdriver.Chrome()
    driver.get('https://web.whatsapp.com')

    input("Scan QR code and press Enter")

    # Logic to check incoming messages and respond to keywords
    while True:
        # Example placeholder logic: Replace with real detection
        received_message = driver.find_element_by_xpath("MESSAGE_XPATH").text
        if "hi" in received_message or "hello" in received_message:
            phone_no = "EXTRACTED_PHONE_NUMBER"  # Extract this dynamically
            kit.sendwhatmsg_instantly(phone_no, "I will connect with you soon.")
