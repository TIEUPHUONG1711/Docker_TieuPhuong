from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)
app.secret_key = "supersecretkey"

# Mô tả vui vẻ theo cung hoàng đạo
descriptions = {
    "Bạch Dương": "Bạn năng động, thích khám phá và có tinh thần lãnh đạo.",
    "Kim Ngưu": "Bạn kiên nhẫn, ổn định và rất đáng tin cậy.",
    "Song Tử": "Bạn thông minh, linh hoạt và giao tiếp rất giỏi.",
    "Cự Giải": "Bạn sống tình cảm, quan tâm người khác và giàu cảm xúc.",
    "Sư Tử": "Bạn tự tin, mạnh mẽ và luôn tỏa sáng.",
    "Xử Nữ": "Bạn tỉ mỉ, logic và chăm chỉ.",
    "Thiên Bình": "Bạn hòa đồng, yêu cái đẹp và sống cân bằng.",
    "Bọ Cạp": "Bạn bí ẩn, mạnh mẽ và rất đam mê.",
    "Nhân Mã": "Bạn thích tự do, khám phá và sống rất tích cực.",
    "Ma Kết": "Bạn nghiêm túc, kiên trì và có trách nhiệm.",
    "Bảo Bình": "Bạn độc đáo, sáng tạo và thích giúp đỡ người khác.",
    "Song Ngư": "Bạn nhạy cảm, sáng tạo và giàu lòng trắc ẩn."
}

# Hàm tính cung hoàng đạo
def zodiac_sign(day, month):
    zodiac = [
        (120, "Ma Kết"), (218, "Bảo Bình"), (320, "Song Ngư"),
        (420, "Bạch Dương"), (521, "Kim Ngưu"), (621, "Song Tử"),
        (722, "Cự Giải"), (823, "Sư Tử"), (923, "Xử Nữ"),
        (1023, "Thiên Bình"), (1122, "Bọ Cạp"), (1222, "Nhân Mã"),
        (1231, "Ma Kết")
    ]
    mmdd = month * 100 + day
    for cutoff, sign in zodiac:
        if mmdd <= cutoff:
            return sign
    return "Ma Kết"

# Tính số ngày đến sinh nhật tiếp theo
def days_to_birthday(birth):
    today = datetime.today()
    next_birthday = datetime(today.year, birth.month, birth.day)

    if next_birthday < today:
        next_birthday = datetime(today.year + 1, birth.month, birth.day)

    return (next_birthday - today).days


@app.route('/', methods=['GET', 'POST'])
def index():
    zodiac_message = ""
    age_message = ""
    birthday_message = ""
    description_message = ""

    if request.method == 'POST':
        birthdate = request.form.get('birthdate')
        if birthdate:
            try:
                birth = datetime.strptime(birthdate, "%Y-%m-%d")
                today = datetime.today()

                # Tính tuổi
                age = today.year - birth.year - ((today.month, today.day) < (birth.month, birth.day))
                age_message = f"Tuổi của bạn: {age}"

                # Cung hoàng đạo
                zodiac = zodiac_sign(birth.day, birth.month)
                zodiac_message = f"Cung hoàng đạo của bạn: {zodiac}"

                # Số ngày đến sinh nhật
                days_left = days_to_birthday(birth)
                birthday_message = f"Còn {days_left} ngày nữa là đến sinh nhật của bạn 🎉"

                # Mô tả tính cách
                description_message = descriptions.get(zodiac, "Không tìm thấy mô tả phù hợp.")

            except ValueError:
                age_message = "Ngày tháng không hợp lệ. Hãy nhập theo dạng YYYY-MM-DD."

    return render_template(
        'index.html',
        age_message=age_message,
        zodiac_message=zodiac_message,
        birthday_message=birthday_message,
        description_message=description_message
    )


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
