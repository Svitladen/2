from kivy.app import App
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.screenmanager import ScreenManager, Screen

# Импортируем все наши экраны из файлов
from trainer_1_nomen import NomenScreen
from trainer_1_1_1_theory import TheoryScreen
from trainer_1_1_2_practice import PracticeScreen

Window.size = (400, 700)
Window.clearcolor = (0.94, 0.96, 0.98, 1)


class MainMenuScreen(Screen):

  def __init__(self, **kwargs):
    super().__init__(**kwargs)
    root = BoxLayout(orientation="vertical", padding=15, spacing=10)

    header_layout = BoxLayout(
        orientation="vertical", size_hint_y=None, height=90, spacing=5
    )
    title_label = Label(
        text="Немецкая грамматика",
        font_size=22,
        bold=True,
        color=(0.1, 0.2, 0.3, 1),
    )
    subtitle_label = Label(
        text="Выберите раздел для тренировки:",
        font_size=14,
        color=(0.4, 0.45, 0.5, 1),
    )
    header_layout.add_widget(title_label)
    header_layout.add_widget(subtitle_label)
    root.add_widget(header_layout)

    sections = [
        (
            "1. ИМЕННИК И АРТИКЛЬ\n(Nomen und Artikel)",
            self.open_nomen_section,
        ),
        (
            "2. МЕСТОИМЕНИЯ И СВЯЗУЮЩИЕ СЛОВА\n(Pronomina)",
            self.coming_soon,
        ),
        (
            "3. ПРИЛАГАТЕЛЬНОЕ И НАРЕЧИЕ\n(Adjektive und Adverbien)",
            self.coming_soon,
        ),
        ("4. ПАДЕЖИ И ПРЕДЛОГИ\n(Kasus und Präpositionen)", self.coming_soon),
        ("5. ГЛАГОЛ И ВРЕМЕННЫЕ ФОРМЫ\n(Verben und Zeitformen)", self.coming_soon),
        ("6. МОДАЛЬНОСТЬ И НАКЛОНЕНИЕ\n(Modalität und Modi)", self.coming_soon),
        (
            "7. СИНТАКСИС И СЛОЖНЫЕ КОНСТРУКЦИИ\n(Satzbau und Syntax)",
            self.coming_soon,
        ),
    ]

    scroll = ScrollView(do_scroll_x=False, bar_width=6)
    btn_container = BoxLayout(
        orientation="vertical", spacing=12, size_hint_y=None, height=620
    )

    for text, callback in sections:
      btn = Button(
          text=text,
          font_size=13,
          bold=True,
          size_hint_y=None,
          height=75,
          background_normal="",
          background_color=(0.12, 0.53, 0.9, 1),
          color=(1, 1, 1, 1),
      )
      btn.bind(on_press=callback)
      btn_container.add_widget(btn)

    scroll.add_widget(btn_container)
    root.add_widget(scroll)

    btn_close = Button(
        text="Закрыть приложение",
        font_size=15,
        bold=True,
        size_hint_y=None,
        height=55,
        background_normal="",
        background_color=(0.88, 0.27, 0.27, 1),
        color=(1, 1, 1, 1),
    )
    btn_close.bind(on_press=App.get_running_app().stop)
    root.add_widget(btn_close)

    self.add_widget(root)

  def open_nomen_section(self, instance):
    self.manager.current = "nomen_menu"

  def coming_soon(self, instance):
    print("Раздел в разработке")


class GermanTrainerApp(App):

  def build(self):
    sm = ScreenManager()
    # Регистрируем все экраны приложения в одном окне
    sm.add_widget(MainMenuScreen(name="main_menu"))
    sm.add_widget(NomenScreen(name="nomen_menu"))
    sm.add_widget(TheoryScreen(name="theory_screen"))
    sm.add_widget(PracticeScreen(name="practice_screen"))
    return sm


if __name__ == "__main__":
  GermanTrainerApp().run()