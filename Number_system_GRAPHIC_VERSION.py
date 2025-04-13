import tkinter as tk
from tkinter import messagebox
import random

def generate_question():
    operation = operation_var.get()
    
    # Случайное основание от 2 до 16 (можно расширить до 36, но это сложнее для пользователя)
    p = random.randint(2, 16)
    entry_p.delete(0, tk.END)
    entry_p.insert(0, str(p))
    
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    current_digits = digits[:p]
    
    if operation == 1:  # 10 -> p
        num = random.randint(1, 1000)
        question = f"Переведите число {num} (10) в систему с основанием {p}:"
        answer = ""
        temp_num = num
        while temp_num > 0:
            remainder = temp_num % p
            answer = current_digits[remainder] + answer
            temp_num = temp_num // p
        if num == 0:
            answer = "0"
        return question, answer, p
    
    elif operation == 2:  # p -> 10
        length = random.randint(1, 4)  # Ограничим длину для удобства
        num_p = current_digits[random.randint(1, p-1)]  # Первая цифра не 0
        for _ in range(length-1):
            num_p += current_digits[random.randint(0, p-1)]
        question = f"Переведите число {num_p} (основание {p}) в десятичную систему:"
        answer = 0
        for char in num_p:
            answer = answer * p + current_digits.index(char)
        return question, str(answer), p
    
    elif operation == 3:  # сумма в p
        num1_p = current_digits[random.randint(1, p-1)]  # Первая цифра не 0
        num2_p = current_digits[random.randint(1, p-1)]
        for _ in range(random.randint(0, 2)):  # Максимум 3 цифры
            num1_p += current_digits[random.randint(0, p-1)]
            num2_p += current_digits[random.randint(0, p-1)]
        
        question = f"Сложите числа {num1_p} и {num2_p} в системе с основанием {p}:"
        
        # Функции преобразования
        def p_to_dec(num):
            return sum(current_digits.index(c) * (p ** i) for i, c in enumerate(reversed(num)))
        
        def dec_to_p(num):
            if num == 0: return "0"
            res = ""
            while num > 0:
                res = current_digits[num % p] + res
                num = num // p
            return res
        
        answer = dec_to_p(p_to_dec(num1_p) + p_to_dec(num2_p))
        return question, answer, p
    
    elif operation == 4:  # разность в p
        # Генерируем два числа, гарантируя, что первое больше
        while True:
            num1_p = current_digits[random.randint(1, p-1)]
            num2_p = current_digits[random.randint(1, p-1)]
            for _ in range(random.randint(0, 1)):  # Максимум 2 цифры
                num1_p += current_digits[random.randint(0, p-1)]
                num2_p += current_digits[random.randint(0, p-1)]
            
            if p_to_dec(num1_p) > p_to_dec(num2_p):
                break
        
        question = f"Вычтите число {num2_p} из {num1_p} в системе с основанием {p}:"
        
        # Функции преобразования (те же, что и для сложения)
        def p_to_dec(num):
            return sum(current_digits.index(c) * (p ** i) for i, c in enumerate(reversed(num)))
        
        def dec_to_p(num):
            if num == 0: return "0"
            res = ""
            while num > 0:
                res = current_digits[num % p] + res
                num = num // p
            return res
        
        answer = dec_to_p(p_to_dec(num1_p) - p_to_dec(num2_p))
        return question, answer, p

def check_answer():
    user_answer = entry_answer.get().strip().upper()
    if not hasattr(check_answer, 'correct_answer'):
        messagebox.showinfo("Информация", "Сначала сгенерируйте вопрос!")
        return
    
    if user_answer == check_answer.correct_answer:
        messagebox.showinfo("Правильно!", "Отличная работа! ✅\n\n" + random.choice([
            "Вы гений систем счисления!",
            "Превосходно!",
            "Идеальный ответ!",
            "Так держать!",
            "Вы мастер преобразований!"
        ]))
        update_score(True)
    else:
        messagebox.showerror("Ошибка", 
            f"Неправильно. Правильный ответ: {check_answer.correct_answer}\n\n" + 
            random.choice([
                "Попробуйте еще раз!",
                "Ошибка - это шаг к успеху!",
                "Не сдавайтесь!",
                "В следующий раз получится!",
                "Проверьте свои вычисления!"
            ]))
        update_score(False)
    
    generate_new_question()

def update_score(is_correct):
    if is_correct:
        scoreboard['correct'] += 1
    else:
        scoreboard['incorrect'] += 1
    label_score.config(text=f"Правильно: {scoreboard['correct']} | Ошибки: {scoreboard['incorrect']}")
    
    # Обновляем процент правильных ответов
    total = scoreboard['correct'] + scoreboard['incorrect']
    if total > 0:
        percentage = (scoreboard['correct'] / total) * 100
        label_percentage.config(text=f"Процент правильных: {percentage:.1f}%")

def generate_new_question():
    try:
        question, answer, p = generate_question()
        label_question.config(text=question)
        label_p_value.config(text=f"Основание: {p}")
        entry_answer.delete(0, tk.END)
        check_answer.correct_answer = answer
        check_answer.current_p = p
    except ValueError as e:
        messagebox.showerror("Ошибка", str(e))

# Создание главного окна
root = tk.Tk()
root.title("Тренажер систем счисления")
root.geometry("550x350")

# Стилизация
root.configure(bg='#f0f0f0')
font_question = ('Arial', 12)
font_button = ('Arial', 10, 'bold')

# Переменные
operation_var = tk.IntVar(value=1)
scoreboard = {'correct': 0, 'incorrect': 0}

# Основной фрейм
main_frame = tk.Frame(root, bg='#f0f0f0')
main_frame.pack(pady=10, padx=10, fill='both', expand=True)

# Панель выбора операции
tk.Label(main_frame, text="Выберите тип задачи:", bg='#f0f0f0').pack(anchor='w')

operation_frame = tk.Frame(main_frame, bg='#f0f0f0')
operation_frame.pack(fill='x')

operations = [
    ("10 → p", 1),
    ("p → 10", 2),
    ("Сумма в p", 3),
]

for text, val in operations:
    tk.Radiobutton(operation_frame, text=text, variable=operation_var, value=val, 
                  bg='#f0f0f0').pack(side='left', padx=5)

# Панель основания системы (только для отображения)
p_frame = tk.Frame(main_frame, bg='#f0f0f0')
p_frame.pack(pady=5)
label_p_value = tk.Label(p_frame, text="Основание: -", bg='#f0f0f0')
label_p_value.pack()

# Скрытое поле для основания (нужно для функций)
entry_p = tk.Entry(p_frame, width=5)
entry_p.pack_forget()

# Кнопка генерации вопроса
btn_generate = tk.Button(main_frame, text="Сгенерировать задание", command=generate_new_question,
                        bg='#4CAF50', fg='white', font=font_button)
btn_generate.pack(pady=10)

# Вопрос
question_frame = tk.Frame(main_frame, bg='#f0f0f0')
question_frame.pack(fill='x', pady=10)
label_question = tk.Label(question_frame, text="", wraplength=500, justify='left', 
                         bg='#f0f0f0', font=font_question)
label_question.pack()

# Поле ответа
answer_frame = tk.Frame(main_frame, bg='#f0f0f0')
answer_frame.pack(pady=10)
tk.Label(answer_frame, text="Ваш ответ:", bg='#f0f0f0').pack(side='left')
entry_answer = tk.Entry(answer_frame, width=20, font=font_question)
entry_answer.pack(side='left', padx=5)
btn_check = tk.Button(answer_frame, text="Проверить", command=check_answer,
                     bg='#2196F3', fg='white', font=font_button)
btn_check.pack(side='left', padx=5)

# Статистика
stats_frame = tk.Frame(main_frame, bg='#f0f0f0')
stats_frame.pack(pady=10)
label_score = tk.Label(stats_frame, text="Правильно: 0 | Ошибки: 0", bg='#f0f0f0')
label_score.pack()
label_percentage = tk.Label(stats_frame, text="Процент правильных: 0%", bg='#f0f0f0')
label_percentage.pack()

# Подсказка по клавише Enter
tk.Label(main_frame, text="Нажмите Enter для проверки ответа", bg='#f0f0f0', fg='gray').pack()

# Привязка Enter к проверке ответа
root.bind('<Return>', lambda event: check_answer())

root.mainloop()