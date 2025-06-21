# ✅ โค้ดสมัคร Gmail แบบจำลอง (ข้ามเบอร์โทร) ด้วย Python + Selenium

# ❗ หมายเหตุ: โค้ดนี้ "จำลองขั้นตอนการสมัคร Gmail" โดยไม่กรอกเบอร์โทร
# → เหมาะสำหรับทดลองหรือสาธิต เพราะ Google จะไม่ให้สมัครจริงจนใส่เบอร์โทร
# → ใช้ได้เพื่อศึกษาหรือเทสต์หน้าเว็บอัตโนมัติเท่านั้น

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import random
import string

# ===== 1. ฟังก์ชันสุ่มชื่อ, รหัสผ่าน =====
def random_name():
    return ''.join(random.choices(string.ascii_lowercase, k=6))

def random_password():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=10))

# ===== 2. เริ่มกระบวนการสมัคร Gmail (ข้าม OTP) =====
def create_gmail_demo():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options)

    try:
        driver.get("https://accounts.google.com/signup")
        time.sleep(3)

        firstname = random_name()
        lastname = random_name()
        username = firstname + lastname + str(random.randint(10, 99))
        password = random_password()

        # กรอกชื่อ นามสกุล อีเมล
        driver.find_element(By.ID, "firstName").send_keys(firstname)
        driver.find_element(By.ID, "lastName").send_keys(lastname)
        driver.find_element(By.ID, "username").send_keys(username)

        # รหัสผ่าน
        driver.find_element(By.NAME, "Passwd").send_keys(password)
        driver.find_element(By.NAME, "ConfirmPasswd").send_keys(password)
        driver.find_element(By.ID, "accountDetailsNext").click()

        print("✅ กำลังจำลองบัญชี:", username + "@gmail.com")
        print("🔐 รหัสผ่าน:", password)

        # หน้า OTP จะขึ้น แต่เราข้าม ไม่กรอกเบอร์
        print("⚠️ ข้ามขั้นตอนเบอร์โทรแล้วหยุดที่หน้า OTP (สมัครจริงจะไม่ได้)")
        time.sleep(10)

    except Exception as e:
        print("❌ เกิดข้อผิดพลาด:", e)
    finally:
        driver.quit()

# ===== 3. เรียกใช้ฟังก์ชัน =====
create_gmail_demo()
