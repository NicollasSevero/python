import speech_recognition as sr
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import os
import string
import imageio
import threading

class VoiceTranslatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Tradutor de Voz para Libras")
        
        self.label_text = tk.Label(root, text="Clique em 'Traduzir' para começar a falar", font=("Helvetica", 12))
        self.label_text.pack(pady=10)
        
        self.btn_translate = tk.Button(root, text="Traduzir", command=self.start_translation)
        self.btn_translate.pack(side=tk.LEFT, padx=20, pady=20)
        
        self.btn_close = tk.Button(root, text="Fechar", command=self.close_app)
        self.btn_close.pack(side=tk.RIGHT, padx=20, pady=20)
        
        self.gif_label = tk.Label(root)
        self.gif_label.pack(pady=10)
        
        self.recognizer = sr.Recognizer()
        self.vocabulary = {
            "nosso projeto tem um valor": "Projeto/Scripts/Tradutor_de_voz/Arquivos_Gifs/1 Nosso.gif",
            "a solução proposta traduz a": "Projeto/Scripts/Tradutor_de_voz/Arquivos_Gifs/2 A solução.gif",
            "ao aplicar o reconhecimento de": "Projeto/Scripts/Tradutor_de_voz/Arquivos_Gifs/3 Ao aplicar.gif",
            "facilitando a comunicação em diversos": "Projeto/Scripts/Tradutor_de_voz/Arquivos_Gifs/4 Além disso.gif",
        }

    def match_initial_words(self, text):
        words = text.lower().split()
        if len(words) >= 5:
            initial_words = ' '.join(words[:5])
            for key in self.vocabulary.keys():
                if initial_words in key:
                    return self.vocabulary[key]
        return None

    def show_gif(self, image_path):
        print(f"Tentando abrir o GIF no caminho: {image_path}")  # Depuração
        
        try:
            # Carrega o GIF
            gif = imageio.mimread(image_path)
            gif_len = len(gif)
            
            # Função para atualizar o GIF na tela
            def update_gif(frame_num):
                frame = Image.fromarray(gif[frame_num])
                photo = ImageTk.PhotoImage(frame)
                self.gif_label.config(image=photo)
                self.gif_label.image = photo
                
                # Verifica se já exibimos todos os frames do GIF
                if frame_num + 1 < gif_len:
                    self.root.after(50, update_gif, frame_num + 1)
                else:
                    self.gif_label.config(image='')  # Limpa a imagem quando o GIF terminar
            
            # Inicia a atualização do GIF
            update_gif(0)
            
        except FileNotFoundError:
            print(f"Arquivo não encontrado: {image_path}")
        except Exception as e:
            print(f"Erro ao carregar GIF: {e}")

    def recognize_speech(self):
        with sr.Microphone() as source:
            self.recognizer.adjust_for_ambient_noise(source)
            print('Diga algo')
            audio = self.recognizer.listen(source)
            try:
                # Reconhecimento de fala em português
                recognized_text = self.recognizer.recognize_google(audio, language="pt-BR")
                print("Você disse:", recognized_text)
                
                for c in string.punctuation:
                    recognized_text = recognized_text.replace(c, "")
                
                # Atualiza o texto na interface
                self.label_text.config(text=f"Você disse: {recognized_text}")
                
                # Verifica se a frase reconhecida começa com as cinco primeiras palavras de uma chave no vocabulário
                gif_path = self.match_initial_words(recognized_text)
                if gif_path:
                    print("Exibindo GIF:", gif_path)
                    self.show_gif(gif_path)
                    
                elif recognized_text.lower() == 'adeus':
                    print("Tempo de dizer adeus!")
                    self.close_app()
                else:
                    print("Frase não reconhecida.")
                    self.label_text.config(text="Frase não reconhecida.")
                    
            except sr.UnknownValueError:
                print("Não foi possível entender o áudio")
                self.label_text.config(text="Não foi possível entender o áudio")
            except sr.RequestError as e:
                print("Erro ao solicitar resultados; {0}".format(e))
                self.label_text.config(text=f"Erro ao solicitar resultados; {e}")

    def start_translation(self):
        threading.Thread(target=self.recognize_speech).start()

    def close_app(self):
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = VoiceTranslatorApp(root)
    root.mainloop()