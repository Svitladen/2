from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen
from kivy.uix.scrollview import ScrollView


class TheoryScreen(Screen):

  def __init__(self, **kwargs):
    super().__init__(**kwargs)
    root = BoxLayout(orientation="vertical", padding=15, spacing=10)

    # Заголовок
    title = Label(
        text="1.1.1. Теория: Род существительного (Genus)",
        font_size=15,
        bold=True,
        size_hint_y=None,
        height=50,
        color=(0.1, 0.2, 0.3, 1),
    )
    root.add_widget(title)

    # Текстовый справочник с прокруткой
    scroll = ScrollView()
    rules_text = """ОПРЕДЕЛЕНИЕ РОДА В НЕМЕЦКОМ ЯЗЫКЕ (GENUS)

В немецком языке у каждого существительного есть один из трех артиклей: DER (мужской), DIE (женский) или DAS (средний). Хотя род не всегда поддается логике, есть множество четких правил по суффиксам и значению.

--------------------------------------------------
1. МУЖСКОЙ РОД (DER) — Синий цвет
--------------------------------------------------
📌 По смыслу (значению):
• Дни недели, месяцы, времена года: der Montag (понедельник), der Januar (январь), der Sommer (лето).
• Стороны света и ветра: der Norden (север), der Süden (юг), der Föhn (фен/ветер).
• Названия осадков и погоды: der Regen (дождь), der Schnee (снег), der Wind (ветер). (Исключение: das Gewitter — гроза).
• Названия марок автомобилей: der BMW, der Audi, der Mercedes.
• Денежные единицы: der Euro, der Dollar, der Franken. (Исключение: das Pfund — фунт).
• Названия гор: der Mount Everest, der Harz.

📌 По суффиксам и окончаниям:
• -er (лица по профессии или действию, а также приборы): der Lehrer (учитель), der Fahrer (водитель), der Drucker (принтер). (Исключения: das Fenster, das Zimmer, die Butter, das Wasser).
• -ling: der Lehrling (ученик), der Frühling (весна), der Schmetterling (бабочка).
• -ismus: der Tourismus (туризм), der Optimismus (оптимизм).
• -ist: der Polizist (полицейский), der Journalist (журналист).
• -or: der Motor (мотор), der Direktor (директор).
• -ant / -ent: der Emigrant (эмигрант), der Student (студент).
• -eur / -är: der Ingenieur (инженер), der Sekretär (секретарь).
• -ig / -ich (как существительные): der Honig (мед), der Rettich (редис).

--------------------------------------------------
2. ЖЕНСКИЙ РОД (DIE) — Красный цвет
--------------------------------------------------
📌 По смыслу (значению):
• Названия деревьев, цветов и фруктов: die Eiche (дуб), die Rose (роза), die Banane (банан). (Главное исключение: der Apfel — яблоко).
• Названия рек (в основном в Германии и Европе): die Donau (Дунай), die Elbe (Эльба), die Weser (Везер). (Исключения: der Rhein, der Main).
• Названия мотоциклов, кораблей и самолетов: die Titanic, die Boeing.
• Количественные числительные как существительные: die Eins (единица), die Million (миллион).

📌 По суффиксам и окончаниям (самый продуктивный род):
• -ung: die Zeitung (газета), die Wohnung (квартира), die Rechnung (счет).
• -heit / -keit: die Freiheit (свобода), die Möglichkeit (возможность), die Sicherheit (безопасность).
• -schaft: die Freundschaft (дружба), die Mannschaft (команда).
• -tät / -ität: die Universität (университет), die Qualität (качество).
• -ion: die Nation (нация), die Information (информация), die Funktion (функция).
• -ik: die Musik (музыка), die Politik (политика), die Technik (техника).
• -in (женские профессии и лица): die Lehrerin (учительница), die Ärztin (врач-женщина).
• -ei: die Bäckerei (булочная), die Bücherei.
• -ur: die Kultur (культура), die Natur (природа).
• -enz / -anz: die Tendenz (тенденция), die Toleranz (толерантность).
• -ie: die Energie (энергия), die Garantie (гарантия).

--------------------------------------------------
3. СРЕДНИЙ РОД (DAS) — Зеленый цвет
--------------------------------------------------
📌 По смыслу (значению):
• Детеныши людей и животных: das Kind (ребенок), das Kalb (теленок), das Ferkel (поросенок).
• Металлы и химические элементы: das Gold (золото), das Silber (серебро), das Eisen (железо). (Исключения: der Stahl — сталь, die Bronze — бронза).
• Буквы алфавита, цвета и музыкальные ноты: das A, das Blau (синий цвет), das C.
• Дроби: das Drertel (треть), das Viertel (четверть).
• Названия отелей, кафе, кинотеатров.
• Субстантивированные инфинитивы (глаголы в роли существительных): das Lesen (чтение), das Essen (еда), das Lernen (учеба).

📌 По суффиксам и окончаниям:
• -chen / -lein (уменьшительно-ласкательные суффиксы — ВСЕГДА средний род!): das Mädchen (девочка), das Büchlein (книжечка), das Häuschen (домик).
• -ment: das Dokument (документ), das Instrument (инструмент), das Apartment (апартаменты).
• -tum: das Eigentum (имущество), das Altertum (древность). (Главные исключения: der Reichtum — богатство, der Irrtum — заблуждение).
• -um: das Zentrum (центр), das Museum (музей), das Datum (дата).
"""

    lbl_content = Label(
        text=rules_text,
        font_size=12,
        size_hint_y=None,
        halign="left",
        valign="top",
        color=(0.2, 0.2, 0.2, 1),
    )
    # Автоматическая адаптация высоты текста под объем для корректного скролла
    lbl_content.bind(
        texture_size=lambda instance, value: setattr(instance, "height", value[1])
    )
    lbl_content.text_size = (360, None)

    scroll.add_widget(lbl_content)
    root.add_widget(scroll)

    # Кнопка возврата в подменю
    btn_back = Button(
        text="Назад к выбору",
        font_size=14,
        bold=True,
        size_hint_y=None,
        height=55,
        background_normal="",
        background_color=(0.7, 0.7, 0.7, 1),
        color=(1, 1, 1, 1),
    )
    btn_back.bind(on_press=self.go_back)
    root.add_widget(btn_back)

    self.add_widget(root)

  def go_back(self, instance):
    self.manager.current = "nomen_menu"