import time
import tkinter as tk
from tkinter import ttk, messagebox
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PIL import Image, ImageTk
import threading
import customtkinter as ctk

class PostalCodeApp:
    def __init__(self, root):
        self.root = root
        self.frame = tk.Frame(root)
        self.frame.pack(fill='both', expand=True, padx=10, pady=10)

        self.driver = None
        self.initialize_driver()

        self.selected_option = None

        self.create_widgets()

    def initialize_driver(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        try:
            self.driver = webdriver.Chrome(options=chrome_options)
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo iniciar el navegador Chrome: {str(e)}")
            self.root.quit()

    def create_widgets(self):
        frame = tk.Frame(self.frame)
        frame.pack(pady=20)

        self.cp_label = tk.Label(frame, text="Código Postal: ")
        self.cp_label.grid(row=0, column=0, padx=5)

        self.cp_entry = tk.Entry(frame)
        self.cp_entry.grid(row=0, column=1, padx=5)
        self.cp_entry.bind("<Return>", lambda event: self.start_search_thread())

        self.search_button = tk.Button(frame, text="Buscar", command=self.start_search_thread)
        self.search_button.grid(row=0, column=2, padx=5)

        self.option_label = tk.Label(self.frame, text="Seleccione una opción de población: ")
        self.option_combobox = ttk.Combobox(self.frame, state="readonly")
        self.select_button = tk.Button(self.frame, text="Seleccionar y Buscar", command=self.select_option)
        self.selected_option_label = tk.Label(self.frame, text="")

        self.result_frame = tk.Frame(self.frame)
        self.result_frame.pack(pady=10)

        self.image_label = tk.Label(self.frame)
        self.image = None

    def start_search_thread(self):
        threading.Thread(target=self.search_postal_code).start()

    def search_postal_code(self):
        self.clear_previous_results()
        self.root.geometry("600x250")

        codigo_postal = self.cp_entry.get().strip()
        url = "https://televisiondigital.mineco.gob.es/2DD-5G/Paginas/Que-tengo-que-hacer.aspx"
        self.driver.get(url)

        try:
            cp_input = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.ID, "cp"))
            )
            cp_input.clear()
            cp_input.send_keys(codigo_postal)

            buscar_btn = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.ID, "btnBuscar"))
            )
            self.driver.execute_script("arguments[0].click();", buscar_btn)

            select_element = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.ID, "cmbPoblaciones"))
            )
            select = Select(select_element)

            options = [option.text for option in select.options if option.text.strip()]
            if options:
                self.option_combobox['values'] = options
                self.option_combobox.current(0)
                self.option_label.pack(pady=5, padx=10)
                self.option_combobox.pack(pady=5, padx=10)
                self.select_button.pack(pady=5, padx=10)
            else:
                self.show_message("No se encontraron opciones en el desplegable.\n\n")
                self.root.geometry("800x700")
        except Exception as e:
            self.show_message("No se encontraron opciones en el desplegable o hubo un error.")
            self.root.geometry("800x700")
            self.extract_results()

    def clear_previous_results(self):
        for widget in self.result_frame.winfo_children():
            widget.destroy()
        self.selected_option = None
        self.selected_option_label.config(text="")
        self.selected_option_label.pack_forget()
        self.option_combobox.pack_forget()
        self.option_combobox.set("")
        self.option_label.pack_forget()
        self.select_button.pack_forget()
        self.image_label.pack_forget()

    def show_message(self, message):
        label = tk.Label(self.result_frame, text=message)
        label.pack(pady=5)

    def select_option(self):
        try:
            self.selected_option = self.option_combobox.get()
            self.selected_option_label.config(text=f"Seleccionado: {self.selected_option}")

            self.selected_option_label.pack(pady=5)
            self.option_combobox.pack_forget()
            self.option_label.pack_forget()
            self.select_button.pack_forget()

            self.start_perform_search_thread()
        except Exception as e:
            messagebox.showerror("Error", f"Error al seleccionar la opción: {str(e)}")

    def start_perform_search_thread(self):
        threading.Thread(target=self.perform_search).start()

    def perform_search(self):
        try:
            select_element = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.ID, "cmbPoblaciones"))
            )
            select = Select(select_element)
            select.select_by_visible_text(self.selected_option)

            buscar_btn = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.ID, "btnBuscar"))
            )
            self.driver.execute_script("arguments[0].click();", buscar_btn)

            self.extract_results()
        except Exception as e:
            messagebox.showerror("Error", f"Error al realizar la búsqueda: {str(e)}")

    def extract_results(self):
        try:
            resultados = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.CLASS_NAME, "resultados"))
            ).find_element(By.TAG_NAME, "dl")
            if resultados is not None:
                self.show_message(resultados.text.replace("Código Postal:", "Código Postal: ").replace("Población:", " Población: ") + "\n\n")
            else:
                self.show_message("No se encontraron resultados de Código Postal y Población.\n\n")
        except Exception as e:
            self.show_message("No se encontraron resultados de Código Postal y Población.")

        try:
            seguir_leyendo = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.CLASS_NAME, "seguirLeyendo"))
            )
            if seguir_leyendo:
                resultados = seguir_leyendo.find_element(By.CLASS_NAME, "resultados")
                tablas = resultados.find_elements(By.TAG_NAME, "table")

                for widget in self.result_frame.winfo_children():
                    if isinstance(widget, ttk.Treeview):
                        widget.destroy()

                if tablas:
                    table_frame = tk.Frame(self.result_frame)
                    table_frame.pack(pady=10)

                    for i, tabla in enumerate(tablas):
                        columns = ["Múltiple digital", "Centro", "Canal"]
                        data = []
                        for row in tabla.find_elements(By.TAG_NAME, "tr"):
                            cols = row.find_elements(By.TAG_NAME, "td")
                            data.append([col.text for col in cols])

                        if data:
                            tree = ttk.Treeview(table_frame, columns=columns, show='headings')
                            tree.grid(row=0, column=i, padx=10)

                            for col in columns:
                                tree.heading(col, text=col)
                                tree.column(col, anchor='center')

                            for item in data:
                                tree.insert("", "end", values=item)
                else:
                    self.show_message("No se encontraron tablas de resultados.\n\n")
        except Exception as e:
            self.show_message("No se encontraron tablas de resultados.")

        self.display_image()
        self.root.geometry("800x800")  # Ajustar tamaño para mostrar todos los resultados

    def display_image(self):
        try:
            self.image = Image.open("Organización-de-canales-TDT.jpg")
            self.image = self.image.resize((550, 350), Image.Resampling.LANCZOS)
            self.photo = ImageTk.PhotoImage(self.image)
            self.image_label.config(image=self.photo)
            self.image_label.pack(pady=5)
        except Exception as e:
            self.show_message("No se pudo cargar la imagen.")

    def on_closing(self):
        if self.driver:
            self.driver.quit()
        self.root.quit()

def main():
    root = tk.Tk()
    root.title("Consulta de cobertura TDT")
    root.geometry("600x150")

    app = PostalCodeApp(root)

    root.protocol("WM_DELETE_WINDOW", app.on_closing)
    root.mainloop()

if __name__ == "__main__":
    main()


