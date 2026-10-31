import subprocess
import tkinter as tk


class GenusSubMenuApp:

  def __init__(self, root):
    self.root = root
    self.root.title("1.1. Род существительного (Genus)")
    self.root.geometry("480x480")
    self.root.configure(bg="#f4f4f4")

    # Заголовок раздела
    lbl_title = tk.Label(
        self.root,
        text="1.1. РОД СУЩЕСТВИТЕЛЬНОГО\n(Genus)",
        font=("Arial", 14, "bold"),
        bg="#f4f4f4",
        fg="#333333",
        justify=tk.CENTER,
    )
    lbl_title.pack(pady=25)

    # Кнопка 1.1.1: Теория
    btn_theory = tk.Button(
        self.root,
        text="1.1.1. Теория\n(Правила и подсказки)",
        font=("Arial", 11, "bold"),
        bg="#e0f0ff",
        width=35,
        height=3,
        command=self.open_theory,
    )
    btn_theory.pack(pady=10)

    # Кнопка 1.1.2: Тренажер (наш тренажер артиклей)
    btn_trainer = tk.Button(
        self.root,
        text="1.1.2. Тренажер\n(Практика der / die / das)",
        font=("Arial", 11, "bold"),
        bg="#e8f8e8",
        width=35,
        height=3,
        command=self.open_trainer,
    )
    btn_trainer.pack(pady=10)

    # Кнопка возврата назад
    btn_back = tk.Button(
        self.root,
        text="Назад в меню разделов",
        font=("Arial", 11, "bold"),
        bg="#dddddd",
        width=35,
        height=2,
        command=self.root.destroy,
    )
    btn_back.pack(pady=25)

  def open_theory(self):
    # Открывает файл с теорией для рода существительных
    try:
      subprocess.Popen(["python", "trainer_1_1_1_theory.py"])
    except Exception as e:
      print(f"Не удалось открыть теорию: {e}")

  def open_trainer(self):
    # Запускает сам тренажер артиклей
    try:
      subprocess.Popen(["python", "trainer_1_1_2_practice.py"])
    except Exception as e:
      print(f"Не удалось запустить тренажер: {e}")


if __name__ == "__main__":
  root = tk.Tk()
  app = GenusSubMenuApp(root)
  root.mainloop()