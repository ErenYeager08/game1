مرحله 1: نصب پایتون و pip (در صورت نیاز)
اول از همه، اطمینان حاصل کنید که Python و pip (مدیر بسته پایتون) روی سیستم شما نصب شده باشند. برای این کار از دستورهای زیر استفاده کنید:

بررسی نصب پایتون:

bash
Copy code
python3 --version
اگر پایتون نصب نیست، می‌توانید آن را با دستور زیر نصب کنید:

bash
Copy code
sudo apt update
sudo apt install python3
بررسی نصب pip:

bash
Copy code
pip3 --version
اگر pip نصب نیست، دستور زیر را اجرا کنید:

bash
Copy code
sudo apt install python3-pip
مرحله 2: دانلود و نصب Colorama بصورت دستی
دانلود Colorama از طریق pip: ابتدا می‌توانید Colorama را با استفاده از pip به صورت دستی نصب کنید:

bash
Copy code
pip3 install colorama
دانلود کد سورس از مخزن GitHub (در صورت نیاز به نصب دستی بدون استفاده از pip): اگر می‌خواهید نصب را بصورت دستی و بدون استفاده از pip انجام دهید، می‌توانید سورس کد Colorama را از مخزن گیت‌هاب دانلود کنید:

ابتدا مخزن Colorama را کلون کنید:

bash
Copy code
git clone https://github.com/tartley/colorama.git
سپس به پوشه‌ی مربوطه بروید:

bash
Copy code
cd colorama
و در نهایت کد را نصب کنید:

bash
Copy code
python3 setup.py install
مرحله 3: تایید نصب
برای اطمینان از نصب صحیح Colorama، می‌توانید یک اسکریپت پایتون ساده ایجاد کرده و تست کنید:

python
Copy code
from colorama import Fore, Back, Style, init

# Initialize colorama
init()

print(Fore.RED + 'This text is red')
print(Back.GREEN + 'This text has a green background')
print(Style.BRIGHT + 'This text is bright')
اگر این اسکریپت بدون مشکل اجرا شد و رنگ‌ها اعمال شدند، نصب شما موفقیت‌آمیز بوده است.

نکته:
اگر در طول فرایند نصب با مشکلاتی مواجه شدید، به احتمال زیاد مشکلی در نصب pip یا نسخه پایتون وجود دارد. در این صورت، نسخه‌های جدیدتر پایتون یا pip را نصب و دوباره تلاش کنید.
