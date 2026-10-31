from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen


class NomenScreen(Screen):

  def __init__(self, **kwargs):
    super().__init__(**kwargs)
    root = BoxLayout(orientation="vertical", padding=20, spacing=15)

    title_label = Label(
        text="1. ИМЕННИК ТА АРТИКЛЬ\n(Nomen und Artikel)",
        font_size=18,
        bold=True,
        color=(0.1, 0.2, 0.3, 1),
        halign="center",
        size_hint_y=None,
        height=80,
    )
    root.add_widget(title_label)

    # Кнопка теории -> переключает на экран theory_screen
    btn_theory = Button(
        text="1.1.1. Теория (Правила и подсказки)",
        font_size=14,
        bold=True,
        size_hint_y=None,
        height=70,
        background_normal="",
        background_color=(0.2, 0.6, 0.8, 1),
        color=(1, 1, 1, 1),
    )
    btn_theory.bind(on_press=self.open_theory)
    root.add_widget(btn_theory)

    # Кнопка тренажера -> переключает на экран practice_screen
    btn_trainer = Button(
        text="1.1.2. Тренажер (Практика der / die / das)",
        font_size=14,
        bold=True,
        size_hint_y=None,
        height=70,
        background_normal="",
        background_color=(0.2, 0.7, 0.4, 1),
        color=(1, 1, 1, 1),
    )
    btn_trainer.bind(on_press=self.open_trainer)
    root.add_widget(btn_trainer)

    btn_back = Button(
        text="Назад в главное меню",
        font_size=14,
        bold=True,
        size_hint_y=None,
        height=60,
        background_normal="",
        background_color=(0.7, 0.7, 0.7, 1),
        color=(1, 1, 1, 1),
    )
    btn_back.bind(on_press=self.go_back)
    root.add_widget(btn_back)

    self.add_widget(root)

  def open_theory(self, instance):
    self.manager.current = "theory_screen"

  def open_trainer(self, instance):
    self.manager.current = "practice_screen"

  def go_back(self, instance):
    self.manager.current = "main_menu"