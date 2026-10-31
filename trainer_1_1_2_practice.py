import csv
import os
import random
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen

CSV_FILE = "dictionary.csv"

# Цвета для артиклей (der - синий, die - красный, das - зеленый)
ARTICLE_COLORS = {
    "der": (0.0, 0.35, 0.7, 1),
    "die": (0.7, 0.0, 0.0, 1),
    "das": (0.0, 0.45, 0.0, 1),
}


class PracticeScreen(Screen):

  def __init__(self, **kwargs):
    super().__init__(**kwargs)
    self.dictionary = self.load_dictionary()
    self.current_word = None

    # Компактный вертикальный макет с меньшими отступами
    root = BoxLayout(
        orientation="vertical", padding=(20, 10, 20, 10), spacing=10
    )

    # Немецкое слово поднято выше
    self.lbl_word = Label(
        text="Загрузка...",
        font_size=40,
        bold=True,
        size_hint_y=None,
        height=80,
        color=(0.1, 0.1, 0.1, 1),
    )
    root.add_widget(self.lbl_word)

    # Контейнер для кнопок артиклей (исчезает при выборе ответа)
    self.btn_box = BoxLayout(
        orientation="horizontal", spacing=12, size_hint_y=None, height=75
    )

    self.btn_der = Button(
        text="der",
        font_size=20,
        bold=True,
        background_normal="",
        background_color=(0.1, 0.4, 0.8, 1),
    )
    self.btn_der.bind(on_press=lambda x: self.check_answer("der"))
    self.btn_box.add_widget(self.btn_der)

    self.btn_die = Button(
        text="die",
        font_size=20,
        bold=True,
        background_normal="",
        background_color=(0.8, 0.2, 0.2, 1),
    )
    self.btn_die.bind(on_press=lambda x: self.check_answer("die"))
    self.btn_box.add_widget(self.btn_die)

    self.btn_das = Button(
        text="das",
        font_size=20,
        bold=True,
        background_normal="",
        background_color=(0.2, 0.6, 0.2, 1),
    )
    self.btn_das.bind(on_press=lambda x: self.check_answer("das"))
    self.btn_box.add_widget(self.btn_das)

    root.add_widget(self.btn_box)

    # Очень крупный, близкий и четкий блок для множественного числа (с артиклем die) и перевода
    self.lbl_result = Label(
        text="",
        font_size=22,
        bold=True,
        size_hint_y=None,
        height=140,
        halign="center",
        valign="middle",
        color=(0.15, 0.15, 0.15, 1),
    )
    self.lbl_result.bind(
        size=lambda s, w: setattr(s, "text_size", (s.width, None))
    )
    root.add_widget(self.lbl_result)

    # Кнопка «Далее»
    self.btn_next = Button(
        text="Далее ➡",
        font_size=18,
        bold=True,
        size_hint_y=None,
        height=55,
        background_normal="",
        background_color=(0.3, 0.5, 0.7, 1),
    )
    self.btn_next.bind(on_press=lambda x: self.load_next_word())
    root.add_widget(self.btn_next)

    # Кнопка возврата в подменю
    btn_back = Button(
        text="Назад в подменю",
        font_size=16,
        bold=True,
        size_hint_y=None,
        height=50,
        background_normal="",
        background_color=(0.7, 0.7, 0.7, 1),
    )
    btn_back.bind(on_press=self.go_back)
    root.add_widget(btn_back)

    self.add_widget(root)

    if self.dictionary:
      self.load_next_word()

  def load_dictionary(self):
    dictionary = []
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, CSV_FILE)

    if not os.path.exists(file_path):
      return dictionary

    encodings = ["utf-8-sig", "utf-8", "cp1251", "latin-1"]
    for enc in encodings:
      try:
        with open(file_path, mode="r", encoding=enc) as f:
          sample = f.read(2048)
          f.seek(0)
          delimiter = ";" if ";" in sample else ","

          reader = csv.DictReader(f, delimiter=delimiter)
          for row in reader:
            row = {
                k.strip().lower() if k else "": v.strip() if v else ""
                for k, v in row.items()
            }
            if "noun" in row and "article" in row and row["noun"]:
              noun = row["noun"]
              plural = row.get("plural", "")

              fixes = {
                  "M?rz": "März",
                  "M?nner": "Männer",
                  "H?user": "Häuser",
                  "St?dte": "Städte",
                  "L?nder": "Länder",
                  "W?rter": "Wörter",
                  "N?chte": "Nächte",
                  "F?lle": "Fälle",
                  "Gr?nde": "Gründe",
              }

              for wrong, right in fixes.items():
                noun = noun.replace(wrong, right)
                plural = plural.replace(wrong, right)

              translation = row.get("translation", "").strip()

              dictionary.append({
                  "noun": noun,
                  "article": row["article"],
                  "plural": plural,
                  "translation": translation,
              })
        if dictionary:
          break
      except Exception:
        continue

    return dictionary

  def load_next_word(self):
    if not self.dictionary:
      return

    # Сбрасываем фон в нейтральный
    Window.clearcolor = (0.94, 0.96, 0.98, 1)

    self.current_word = random.choice(self.dictionary)
    self.lbl_word.text = self.current_word["noun"]
    self.lbl_word.color = (0.1, 0.1, 0.1, 1)
    self.lbl_result.text = ""

    # Возвращаем кнопки на экран
    self.btn_box.height = 75
    self.btn_box.opacity = 1
    self.btn_box.disabled = False

  def check_answer(self, chosen):
    if not self.current_word:
      return

    correct_article = self.current_word["article"].strip().lower()
    is_correct = chosen == correct_article

    if is_correct:
      # Мягкий зеленоватый фон при правильном ответе
      Window.clearcolor = (0.85, 0.95, 0.85, 1)
    else:
      # Мягкий розоватый фон при ошибке
      Window.clearcolor = (0.98, 0.85, 0.85, 1)

    # Слово меняется на вариант с артиклем в цвете артикля
    self.lbl_word.text = f"{correct_article} {self.current_word['noun']}"
    self.lbl_word.color = ARTICLE_COLORS.get(correct_article, (0, 0, 0, 1))

    # Крупное множественное число (всегда с артиклем die) и крупный перевод
    plural_form = self.current_word["plural"]
    self.lbl_result.text = (
        f"die {plural_form}\n🇷🇺 {self.current_word['translation']}"
    )

    # Скрываем кнопки артиклей
    self.btn_box.height = 0
    self.btn_box.opacity = 0
    self.btn_box.disabled = True

  def go_back(self, instance):
    Window.clearcolor = (0.94, 0.96, 0.98, 1)
    self.manager.current = "nomen_menu"
    