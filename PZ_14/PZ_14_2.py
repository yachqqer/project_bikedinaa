# Вариант 5. Скорость первого автомобиля Vi км/ч, второго - V2 км/ч, расстояние
# между ними S км. Определить расстояние между ними через Т часов, если автомобили
# первоначально движутся навстречу друг другу. Данное расстояние равно модулю разности
# начального расстояния и общего пути, проделанного автомобилями; общий путь = время
# суммарная скорость.

import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

def calculate_distance():
    try:
        v1 = float(entry_v1.get())
        v2 = float(entry_v2.get())
        s = float(entry_s.get())
        t = float(entry_t.get())

        if v1 < 0 or v2 < 0 or s < 0 or t < 0:
            messagebox.showerror("Ошибка ввода", "Значения не могут быть отрицательными!")
            return

        total_speed = v1 + v2
        total_path = t * total_speed
        remaining_distance = abs(s - total_path)

        label_result.config(text=f"Расстояние через {t:g} ч.: {remaining_distance: } км", foreground="#1e7e34",)

    except ValueError:
        messagebox.showerror("Ошибка ввода", "Пожалуйста, введите корректные числовые значения!")


root = tk.Tk()
root.title("Движение автомобилей")
root.geometry("400x320")
root.resizable(False, False)

style = ttk.Style()
style.theme_use("clam")
style.configure("TLabel", font=("Arial", 11))
style.configure("TButton", font=("Arial", 11, "bold"))
style.configure("TEntry", font=("Arial", 11))

main_frame = ttk.Frame(root, padding="20 20 20 20")
main_frame.pack(fill=tk.BOTH, expand=True)


ttk.Label(main_frame, text="Скорость 1-го авто (V1, км/ч):").grid(
    row=0, column=0, sticky=tk.W, pady=8
)
entry_v1 = ttk.Entry(main_frame, width=15)
entry_v1.grid(row=0, column=1, sticky=tk.E, pady=8)

ttk.Label(main_frame, text="Скорость 2-го авто (V2, км/ч):").grid(row=1, column=0, sticky=tk.W, pady=8)
entry_v2 = ttk.Entry(main_frame, width=15)
entry_v2.grid(row=1, column=1, sticky=tk.E, pady=8)

ttk.Label(main_frame, text="Начальное расстояние (S, км):").grid(row=2, column=0, sticky=tk.W, pady=8)
entry_s = ttk.Entry(main_frame, width=15)
entry_s.grid(row=2, column=1, sticky=tk.E, pady=8)


ttk.Label(main_frame, text="Время движения (Т, ч):").grid(row=3, column=0, sticky=tk.W, pady=8)
entry_t = ttk.Entry(main_frame, width=15)
entry_t.grid(row=3, column=1, sticky=tk.E, pady=8)


btn_calc = ttk.Button(main_frame, text="Рассчитать", command=calculate_distance)
btn_calc.grid(row=4, column=0, columnspan=2, pady=20, sticky=tk.EW)

label_result = ttk.Label(
    main_frame,
    text="Введите данные и нажмите 'Рассчитать'",
    font=("Arial", 12, "bold"),
    foreground="#555555",
    anchor="center",
)
label_result.grid(row=5, column=0, columnspan=2, pady=5, sticky=tk.EW)

root.mainloop()