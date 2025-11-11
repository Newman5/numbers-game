# generate_audio_gtts.py
from gtts import gTTS
import os

# -------- SETTINGS -------- #
OUTPUT_DIR = "audio/chinese/gTTS"
LANG_CODE = "zh"  # Mandarin Chinese

# Make sure output directory exists
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Chinese numerals for 1–10
chinese_digits = {
    0: "零", 1: "一", 2: "二", 3: "三", 4: "四", 5: "五",
    6: "六", 7: "七", 8: "八", 9: "九", 10: "十"
}

def number_to_chinese(n: int) -> str:
    """Convert numbers 1–100 into proper Chinese numerals."""
    if n <= 10:
        return chinese_digits[n]
    elif n < 20:
        # 11–19 = 十一, 十二, ...
        return "十" + chinese_digits[n % 10]
    elif n < 100:
        tens, ones = divmod(n, 10)
        result = chinese_digits[tens] + "十"
        if ones != 0:
            result += chinese_digits[ones]
        return result
    elif n == 100:
        return "一百"
    else:
        raise ValueError("Only supports numbers 1–100")

print("🔊 Generating Chinese number audio files (1–100) using gTTS...")

for n in range(1, 101):
    chinese_text = number_to_chinese(n)
    filename = f"{OUTPUT_DIR}/{n}.mp3"

    # Generate and save
    tts = gTTS(text=chinese_text, lang=LANG_CODE)
    tts.save(filename)
    print(f"✅ Saved {filename} ({chinese_text})")

print("\n🎉 Done! All audio files generated successfully.")
