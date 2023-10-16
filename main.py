import tkinter as tk
from tkinter import messagebox, simpledialog
import smtplib
from email.mime.text import MIMEText

class CandidateApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Список кандидатов")

        self.candidates = []

        # Элементы интерфейса
        self.label = tk.Label(root, text="Имя кандидата:")
        self.label.pack(pady=10)

        self.entry = tk.Entry(root)
        self.entry.pack(pady=10)

        self.add_button = tk.Button(root, text="Добавить кандидата", command=self.add_candidate)
        self.add_button.pack(pady=10)

        self.listbox = tk.Listbox(root)
        self.listbox.pack(pady=10)

        self.remove_button = tk.Button(root, text="Удалить выбранного кандидата", command=self.remove_candidate)
        self.remove_button.pack(pady=10)

        self.email_button = tk.Button(root, text="Отправить приглашение", command=self.send_invitation)
        self.email_button.pack(pady=10)

    def add_candidate(self):
        candidate_name = self.entry.get().strip()
        if candidate_name:
            self.candidates.append(candidate_name)
            self.listbox.insert(tk.END, candidate_name)
            self.entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Внимание", "Введите имя кандидата")

    def remove_candidate(self):
        selected_index = self.listbox.curselection()
        if selected_index:
            index = selected_index[0]
            removed_candidate = self.candidates.pop(index)
            self.listbox.delete(index)
            messagebox.showinfo("Успех", f"Кандидат {removed_candidate} удален")
        else:
            messagebox.showwarning("Внимание", "Выберите кандидата для удаления")

    def send_invitation(self):
        selected_index = self.listbox.curselection()
        if selected_index:
            index = selected_index[0]
            selected_candidate = self.candidates[index]
            email = simpledialog.askstring("Отправить приглашение", f"Введите email для кандидата {selected_candidate}:")

            if email:
                subject = "Приглашение на собеседование"
                body = f"Уважаемый {selected_candidate}, приглашаем вас на собеседование. Мы ждем вас!"

                try:
                    self.send_email(email, subject, body)
                    messagebox.showinfo("Успех", "Приглашение успешно отправлено")
                except Exception as e:
                    messagebox.showerror("Ошибка", f"Ошибка при отправке письма: {e}")

        else:
            messagebox.showwarning("Внимание", "Выберите кандидата для отправки приглашения")

    def send_email(self, to_email, subject, body):
        # Здесь введите параметры для вашего SMTP-сервера
        smtp_server = 'smtp.example.com'
        smtp_port = 587
        smtp_username = 'your_username'
        smtp_password = 'your_password'

        msg = MIMEText(body)
        msg['Subject'] = subject
        msg['From'] = smtp_username
        msg['To'] = to_email

        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(smtp_username, smtp_password)
            server.sendmail(smtp_username, to_email, msg.as_string())

if __name__ == "__main__":
    root = tk.Tk()
    app = CandidateApp(root)
    root.mainloop()
