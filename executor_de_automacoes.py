import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import subprocess
import os
import emoji
import time

class Application(tk.Tk):
    def __init__(self):
        super().__init__()

        # Obtém o diretório do arquivo Python principal
        script_dir = os.path.dirname(os.path.abspath(__file__))

        # Define o caminho da imagem para o fundo da aplicação
        self.background_image_path = os.path.join(script_dir, "imagem_de_fundo/The Eras Tour.jpg")

        self.title("Automação de dados - Taylor Swift")
        self.configure(background='white')

        # Define o ícone da aplicação
        icon_path = os.path.join(script_dir, "imagem_de_fundo/icone_ts.png")  # Atualize o caminho para sua imagem
        if os.path.exists(icon_path):
            self.icon_photo = tk.PhotoImage(file=icon_path)
            self.iconphoto(False, self.icon_photo)
        else:
            messagebox.showerror("Erro", "Arquivo de ícone não encontrado.")

        # Abre a janela maximizada
        self.state('zoomed')

        # Canvas para desenhar a imagem de fundo
        self.canvas = tk.Canvas(self, highlightthickness=0)
        self.canvas.pack(fill=tk.BOTH, expand=True)
        
        # Define a imagem de fundo da aplicação
        if self.background_image_path:
            self.set_background_image()

        # Frame para os botões à esquerda
        self.button_frame_left = tk.Frame(self.canvas, bg='white')
        self.canvas.create_window(20, 20, anchor="nw", window=self.button_frame_left)  # Posição do frame da esquerda

        # Título do frame da esquerda
        self.title_left = tk.Label(self.button_frame_left, text="Automações DB", bg='white', font=('Helvetica', 14, 'bold'))
        self.title_left.pack(pady=10)

        # Scripts para o frame da esquerda
        self.scripts_left = {
            "Songs": os.path.join(script_dir, "RPA/Taylor Swift/ts_web_db_songs/ts_web_db_songs.py"),
            "Albums": os.path.join(script_dir, "RPA/Taylor Swift/ts_web_db_albums/ts_web_db_albums.py"),
            "Youtube": os.path.join(script_dir, "RPA/Taylor Swift/ts_web_db_youtube/yt_ts.py"),
            "Dashboard": os.path.join(script_dir, "update_publish_powerbi.py"),
            # Adicione mais scripts conforme necessário
        }
        self.create_buttons(self.button_frame_left, self.scripts_left)

        # Frame para os botões à direita
        self.button_frame_right = tk.Frame(self.canvas, bg='white')
        self.canvas.create_window(1330, 20, anchor="nw", window=self.button_frame_right)  # Posição do frame da direita

        # Título do frame da direita
        self.title_right = tk.Label(self.button_frame_right, text="Automações Excel", bg='white', font=('Helvetica', 14, 'bold'))
        self.title_right.pack(pady=10)

        # Scripts para o frame da direita
        self.scripts_right = {
            "Songs": os.path.join(script_dir, "RPA/Taylor Swift/ts_web_db_songs/ts_web_excel_songs.py"),
            "Albums": os.path.join(script_dir, "RPA/Taylor Swift/ts_web_db_albums/ts_web_excel_albums.py"),
            "Youtube": os.path.join(script_dir, "RPA/Taylor Swift/ts_web_db_youtube/Excel-yt_ts.py"),
        }
        self.create_buttons(self.button_frame_right, self.scripts_right)

        # Botão "Executar todas as automações" com quebra de linha
        self.run_all_button = tk.Button(self.canvas, text="Executar\n todas as automações", 
                                        command=self.run_all_automations, bg='#ADD8E6', bd=0, 
                                        relief='solid', font=('Helvetica', 12, 'bold'), 
                                        fg='black', padx=10, pady=10, activebackground='#87CEEB', 
                                        width=15, height=2)
        self.canvas.create_window(20, 590, anchor="nw", window=self.run_all_button)  # Botão 10cm acima do botão Fechar

        # Botão para fechar a aplicação
        self.close_button = tk.Button(self.canvas, text=emoji.emojize(":snake: Fechar", variant="emoji_type"), 
                                      command=self.confirm_close, bg='#ADD8E6', bd=0, relief='solid', 
                                      font=('Helvetica', 12, 'bold'), fg='black', padx=10, pady=10, 
                                      activebackground='#87CEEB', width=15, height=2)
        self.canvas.create_window(20, 700, anchor="nw", window=self.close_button)  # Ajuste a posição aqui

        # Bloquear o botão de fechar da janela do Windows
        self.protocol("WM_DELETE_WINDOW", self.on_closing)

        # Ajustar a imagem de fundo quando a janela for redimensionada
        self.bind("<Configure>", self.resize_background_image)

    def set_background_image(self):
        """Define a imagem de fundo do widget."""
        if os.path.exists(self.background_image_path):
            self.original_image = Image.open(self.background_image_path)
            self.background_image = ImageTk.PhotoImage(self.original_image)
            self.background_label = tk.Label(self.canvas, image=self.background_image)
            self.background_label.image = self.background_image
            self.background_label.place(x=0, y=0, relwidth=1, relheight=1)
        else:
            messagebox.showerror("Erro", "Arquivo de imagem não encontrado.")

    def resize_background_image(self, event):
        """Redimensiona a imagem de fundo conforme o tamanho da janela."""
        if hasattr(self, 'original_image'):
            new_width = event.width
            new_height = event.height
            resized_image = self.original_image.resize((new_width, new_height), Image.Resampling.LANCZOS)
            self.background_image = ImageTk.PhotoImage(resized_image)
            self.background_label.config(image=self.background_image)
            self.background_label.image = self.background_image

    def create_buttons(self, frame, scripts):
        """Cria botões com base nos scripts fornecidos e os adiciona ao frame."""
        for script_name, script_file in scripts.items():
            button = tk.Button(frame, text=script_name, command=lambda f=script_file, name=script_name: self.confirm_and_run_script(f, name), 
                               width=15, height=2, font=('Helvetica', 12, 'bold'), bg='#ADD8E6', fg='black')
            button.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)

    def confirm_and_run_script(self, script_file, script_name):
        """Exibe uma mensagem de confirmação antes de executar o script."""
        result = messagebox.askokcancel("Confirmação", f"Confirma a execução de '{script_name}'?")
        if result:
            try:
                self.run_script(script_file)
            except Exception as e:
                self.show_error_message(str(e))

    def run_script(self, script_file):
        """Executa o script e trata erros potenciais."""
        try:
            if os.path.exists(script_file):
                # Executa o script usando subprocess
                subprocess.Popen(["python", script_file])
            else:
                self.show_error_message(f"O arquivo {script_file} não foi encontrado.")
        except Exception as e:
            self.show_error_message(str(e))

    def show_error_message(self, message):
        """Exibe uma mensagem de erro."""
        messagebox.showerror("Erro", message)

    def confirm_close(self):
        result = messagebox.askokcancel("Confirmação", "Tem certeza que deseja fechar a aplicação?")
        if result:
            self.quit()

    def on_closing(self):
        # Intercepta a ação de fechar a janela do Windows
        self.confirm_close()

    def run_all_automations(self):
        """Executa todas as automações em sequência com atraso entre elas."""
        all_scripts = list(self.scripts_left.values()) + list(self.scripts_right.values())
        for script_file in all_scripts:
            try:
                if os.path.exists(script_file):
                    subprocess.run(["python", script_file], check=True)
                    time.sleep(7)  # Espera de 7 segundos entre as execuções
                else:
                    self.show_error_message(f"O arquivo {script_file} não foi encontrado.")
                    return  # Se um script falhar, interrompe a execução de todos
            except subprocess.CalledProcessError as e:
                self.show_error_message(f"Erro ao executar {script_file}: {str(e)}")
                return  # Interrompe a execução se um script falhar
        # Se todos os scripts forem executados com sucesso
        messagebox.showinfo("Sucesso", "Finalizado com sucesso!")
        self.after(3000, self.confirm_close)  # Aguarda 3 segundos e fecha o app

if __name__ == "__main__":
    app = Application()
    app.mainloop()
