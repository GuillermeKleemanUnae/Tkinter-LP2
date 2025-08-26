"""
Ejemplo 10: Operaciones CRUD Básicas con SQLite
Un ejemplo simple y directo de operaciones de base de datos

Este ejemplo muestra de manera sencilla cómo implementar:
- CREATE: Crear nuevos registros
- READ: Leer registros existentes  
- UPDATE: Actualizar registros
- DELETE: Eliminar registros

Sin usar clases complejas, solo SQLite puro con Tkinter.
"""

import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3
import os
from datetime import datetime

class SimpleCRUDExample:
    def __init__(self, root):
        self.root = root
        self.root.title("Ejemplo Simple: Operaciones CRUD con SQLite")
        self.root.geometry("800x600")
        
        # Crear base de datos simple
        self.setup_database()
        
        # Configurar interfaz
        self.setup_ui()
        
        # Cargar datos iniciales
        self.load_data()
    
    def setup_database(self):
        """Crea y configura la base de datos"""
        self.db_path = "ejemplo_simple.db"
        
        # Conectar a la base de datos
        self.conn = sqlite3.connect(self.db_path)
        self.conn.row_factory = sqlite3.Row  # Para acceder por nombre de columna
        
        # Crear tabla si no existe
        cursor = self.conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS personas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                apellido TEXT NOT NULL,
                edad INTEGER,
                email TEXT UNIQUE,
                fecha_registro TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        
        # Insertar datos de ejemplo si la tabla está vacía
        cursor.execute("SELECT COUNT(*) FROM personas")
        if cursor.fetchone()[0] == 0:
            personas_ejemplo = [
                ("Juan", "Pérez", 25, "juan@email.com"),
                ("María", "García", 30, "maria@email.com"),
                ("Carlos", "López", 22, "carlos@email.com"),
                ("Ana", "Martínez", 28, "ana@email.com")
            ]
            
            cursor.executemany(
                "INSERT INTO personas (nombre, apellido, edad, email) VALUES (?, ?, ?, ?)",
                personas_ejemplo
            )
        
        self.conn.commit()
        print("✓ Base de datos configurada")
    
    def setup_ui(self):
        """Configura la interfaz de usuario"""
        
        # Frame principal dividido en dos partes
        main_frame = ttk.Frame(self.root)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Panel izquierdo: Formulario
        self.setup_form_panel(main_frame)
        
        # Panel derecho: Lista y operaciones
        self.setup_list_panel(main_frame)
        
        # Panel inferior: Información SQL
        self.setup_sql_panel()
    
    def setup_form_panel(self, parent):
        """Panel de formulario para CRUD"""
        form_frame = ttk.LabelFrame(parent, text="Formulario de Persona")
        form_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 5))
        
        # Campo ID (solo para UPDATE y DELETE)
        ttk.Label(form_frame, text="ID (para editar/eliminar):").pack(anchor=tk.W, padx=5, pady=2)
        self.id_var = tk.StringVar()
        ttk.Entry(form_frame, textvariable=self.id_var, width=10).pack(anchor=tk.W, padx=5, pady=2)
        
        # Separador
        ttk.Separator(form_frame, orient=tk.HORIZONTAL).pack(fill=tk.X, padx=5, pady=10)
        
        # Campo Nombre
        ttk.Label(form_frame, text="Nombre:").pack(anchor=tk.W, padx=5, pady=2)
        self.nombre_var = tk.StringVar()
        ttk.Entry(form_frame, textvariable=self.nombre_var).pack(fill=tk.X, padx=5, pady=2)
        
        # Campo Apellido
        ttk.Label(form_frame, text="Apellido:").pack(anchor=tk.W, padx=5, pady=2)
        self.apellido_var = tk.StringVar()
        ttk.Entry(form_frame, textvariable=self.apellido_var).pack(fill=tk.X, padx=5, pady=2)
        
        # Campo Edad
        ttk.Label(form_frame, text="Edad:").pack(anchor=tk.W, padx=5, pady=2)
        self.edad_var = tk.StringVar()
        ttk.Entry(form_frame, textvariable=self.edad_var).pack(fill=tk.X, padx=5, pady=2)
        
        # Campo Email
        ttk.Label(form_frame, text="Email:").pack(anchor=tk.W, padx=5, pady=2)
        self.email_var = tk.StringVar()
        ttk.Entry(form_frame, textvariable=self.email_var).pack(fill=tk.X, padx=5, pady=2)
        
        # Botones de operaciones CRUD
        buttons_frame = ttk.Frame(form_frame)
        buttons_frame.pack(fill=tk.X, padx=5, pady=20)
        
        # CREATE
        ttk.Button(buttons_frame, text="➕ CREATE", command=self.create_person, 
                  style="Accent.TButton").pack(fill=tk.X, pady=2)
        
        # READ
        ttk.Button(buttons_frame, text="🔍 READ (Buscar por ID)", command=self.read_person).pack(fill=tk.X, pady=2)
        
        # UPDATE
        ttk.Button(buttons_frame, text="✏️ UPDATE", command=self.update_person).pack(fill=tk.X, pady=2)
        
        # DELETE
        ttk.Button(buttons_frame, text="🗑️ DELETE", command=self.delete_person).pack(fill=tk.X, pady=2)
        
        # Separador
        ttk.Separator(buttons_frame, orient=tk.HORIZONTAL).pack(fill=tk.X, pady=10)
        
        # Botones de utilidad
        ttk.Button(buttons_frame, text="🔄 Limpiar Formulario", command=self.clear_form).pack(fill=tk.X, pady=2)
        ttk.Button(buttons_frame, text="📝 Cargar desde Lista", command=self.load_from_list).pack(fill=tk.X, pady=2)
    
    def setup_list_panel(self, parent):
        """Panel de lista de registros"""
        list_frame = ttk.LabelFrame(parent, text="Lista de Personas")
        list_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=(5, 0))
        
        # Treeview para mostrar datos
        columns = ("ID", "Nombre", "Apellido", "Edad", "Email", "Fecha Registro")
        self.tree = ttk.Treeview(list_frame, columns=columns, show="headings", height=15)
        
        # Configurar columnas
        for col in columns:
            self.tree.heading(col, text=col)
            if col == "ID":
                self.tree.column(col, width=50)
            elif col == "Edad":
                self.tree.column(col, width=60)
            elif col in ["Nombre", "Apellido"]:
                self.tree.column(col, width=100)
            else:
                self.tree.column(col, width=120)
        
        # Scrollbar para el Treeview
        scrollbar = ttk.Scrollbar(list_frame, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)
        
        # Empaquetar
        self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        # Evento de selección
        self.tree.bind("<<TreeviewSelect>>", self.on_select)
        
        # Botón de refrescar
        ttk.Button(list_frame, text="🔄 Refrescar Lista", command=self.load_data).pack(pady=5)
    
    def setup_sql_panel(self):
        """Panel para mostrar las consultas SQL ejecutadas"""
        sql_frame = ttk.LabelFrame(self.root, text="Consultas SQL Ejecutadas")
        sql_frame.pack(fill=tk.X, padx=10, pady=(0, 10))
        
        self.sql_text = tk.Text(sql_frame, height=6, font=("Courier", 9))
        sql_scrollbar = ttk.Scrollbar(sql_frame, orient=tk.VERTICAL, command=self.sql_text.yview)
        self.sql_text.configure(yscrollcommand=sql_scrollbar.set)
        
        self.sql_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        sql_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        # Agregar mensaje inicial
        self.log_sql("-- Bienvenido al ejemplo de operaciones CRUD con SQLite")
        self.log_sql("-- Las consultas SQL aparecerán aquí")
    
    # ===========================================
    # OPERACIONES CRUD
    # ===========================================
    
    def create_person(self):
        """CREATE: Crea una nueva persona"""
        try:
            # Validar campos obligatorios
            nombre = self.nombre_var.get().strip()
            apellido = self.apellido_var.get().strip()
            email = self.email_var.get().strip()
            
            if not all([nombre, apellido, email]):
                messagebox.showerror("Error", "Nombre, apellido y email son obligatorios")
                return
            
            # Validar edad
            try:
                edad = int(self.edad_var.get()) if self.edad_var.get().strip() else None
            except ValueError:
                messagebox.showerror("Error", "La edad debe ser un número")
                return
            
            # Ejecutar INSERT
            cursor = self.conn.cursor()
            sql = "INSERT INTO personas (nombre, apellido, edad, email) VALUES (?, ?, ?, ?)"
            cursor.execute(sql, (nombre, apellido, edad, email))
            self.conn.commit()
            
            # Log SQL
            self.log_sql(f"INSERT INTO personas (nombre, apellido, edad, email) VALUES ('{nombre}', '{apellido}', {edad}, '{email}');")
            
            # Obtener ID del nuevo registro
            new_id = cursor.lastrowid
            
            messagebox.showinfo("Éxito", f"Persona creada exitosamente con ID: {new_id}")
            
            # Limpiar formulario y recargar datos
            self.clear_form()
            self.load_data()
            
        except sqlite3.IntegrityError as e:
            if "UNIQUE constraint failed" in str(e):
                messagebox.showerror("Error", "El email ya existe en la base de datos")
            else:
                messagebox.showerror("Error", f"Error de integridad: {e}")
        except Exception as e:
            messagebox.showerror("Error", f"Error al crear persona: {e}")
    
    def read_person(self):
        """READ: Lee una persona por ID"""
        try:
            person_id = self.id_var.get().strip()
            if not person_id:
                messagebox.showerror("Error", "Ingrese un ID para buscar")
                return
            
            # Ejecutar SELECT
            cursor = self.conn.cursor()
            sql = "SELECT * FROM personas WHERE id = ?"
            cursor.execute(sql, (int(person_id),))
            result = cursor.fetchone()
            
            # Log SQL
            self.log_sql(f"SELECT * FROM personas WHERE id = {person_id};")
            
            if result:
                # Mostrar datos en el formulario
                self.nombre_var.set(result['nombre'])
                self.apellido_var.set(result['apellido'])
                self.edad_var.set(str(result['edad']) if result['edad'] else "")
                self.email_var.set(result['email'])
                
                messagebox.showinfo("Encontrado", f"Persona encontrada: {result['nombre']} {result['apellido']}")
            else:
                messagebox.showwarning("No encontrado", f"No se encontró persona con ID: {person_id}")
                
        except ValueError:
            messagebox.showerror("Error", "El ID debe ser un número")
        except Exception as e:
            messagebox.showerror("Error", f"Error al buscar persona: {e}")
    
    def update_person(self):
        """UPDATE: Actualiza una persona existente"""
        try:
            # Validar ID
            person_id = self.id_var.get().strip()
            if not person_id:
                messagebox.showerror("Error", "Ingrese un ID para actualizar")
                return
            
            # Validar campos
            nombre = self.nombre_var.get().strip()
            apellido = self.apellido_var.get().strip()
            email = self.email_var.get().strip()
            
            if not all([nombre, apellido, email]):
                messagebox.showerror("Error", "Nombre, apellido y email son obligatorios")
                return
            
            # Validar edad
            try:
                edad = int(self.edad_var.get()) if self.edad_var.get().strip() else None
            except ValueError:
                messagebox.showerror("Error", "La edad debe ser un número")
                return
            
            # Verificar que el registro existe
            cursor = self.conn.cursor()
            cursor.execute("SELECT * FROM personas WHERE id = ?", (int(person_id),))
            if not cursor.fetchone():
                messagebox.showerror("Error", f"No existe persona con ID: {person_id}")
                return
            
            # Ejecutar UPDATE
            sql = "UPDATE personas SET nombre = ?, apellido = ?, edad = ?, email = ? WHERE id = ?"
            cursor.execute(sql, (nombre, apellido, edad, email, int(person_id)))
            self.conn.commit()
            
            # Log SQL
            self.log_sql(f"UPDATE personas SET nombre = '{nombre}', apellido = '{apellido}', edad = {edad}, email = '{email}' WHERE id = {person_id};")
            
            if cursor.rowcount > 0:
                messagebox.showinfo("Éxito", f"Persona ID {person_id} actualizada exitosamente")
                self.load_data()
            else:
                messagebox.showwarning("Advertencia", "No se realizaron cambios")
                
        except ValueError:
            messagebox.showerror("Error", "El ID debe ser un número")
        except sqlite3.IntegrityError as e:
            if "UNIQUE constraint failed" in str(e):
                messagebox.showerror("Error", "El email ya existe en la base de datos")
            else:
                messagebox.showerror("Error", f"Error de integridad: {e}")
        except Exception as e:
            messagebox.showerror("Error", f"Error al actualizar persona: {e}")
    
    def delete_person(self):
        """DELETE: Elimina una persona"""
        try:
            person_id = self.id_var.get().strip()
            if not person_id:
                messagebox.showerror("Error", "Ingrese un ID para eliminar")
                return
            
            # Confirmar eliminación
            if not messagebox.askyesno("Confirmar", f"¿Está seguro de eliminar la persona con ID {person_id}?"):
                return
            
            # Ejecutar DELETE
            cursor = self.conn.cursor()
            sql = "DELETE FROM personas WHERE id = ?"
            cursor.execute(sql, (int(person_id),))
            self.conn.commit()
            
            # Log SQL
            self.log_sql(f"DELETE FROM personas WHERE id = {person_id};")
            
            if cursor.rowcount > 0:
                messagebox.showinfo("Éxito", f"Persona ID {person_id} eliminada exitosamente")
                self.clear_form()
                self.load_data()
            else:
                messagebox.showwarning("Advertencia", f"No se encontró persona con ID: {person_id}")
                
        except ValueError:
            messagebox.showerror("Error", "El ID debe ser un número")
        except Exception as e:
            messagebox.showerror("Error", f"Error al eliminar persona: {e}")
    
    # ===========================================
    # MÉTODOS DE UTILIDAD
    # ===========================================
    
    def load_data(self):
        """Carga todos los datos en el Treeview"""
        try:
            # Limpiar Treeview
            for item in self.tree.get_children():
                self.tree.delete(item)
            
            # Ejecutar SELECT para obtener todos los registros
            cursor = self.conn.cursor()
            cursor.execute("SELECT * FROM personas ORDER BY id")
            results = cursor.fetchall()
            
            # Log SQL
            self.log_sql("SELECT * FROM personas ORDER BY id;")
            
            # Insertar datos en el Treeview
            for row in results:
                # Formatear fecha para mostrar solo fecha y hora sin microsegundos
                fecha_registro = row['fecha_registro']
                if fecha_registro:
                    # Parsear y reformatear la fecha
                    try:
                        dt = datetime.fromisoformat(fecha_registro)
                        fecha_formateada = dt.strftime("%Y-%m-%d %H:%M")
                    except:
                        fecha_formateada = fecha_registro
                else:
                    fecha_formateada = ""
                
                self.tree.insert("", tk.END, values=(
                    row['id'],
                    row['nombre'],
                    row['apellido'],
                    row['edad'] if row['edad'] else "",
                    row['email'],
                    fecha_formateada
                ))
            
            # Actualizar título con contador
            total_registros = len(results)
            self.root.title(f"Ejemplo Simple: Operaciones CRUD con SQLite - {total_registros} registros")
            
        except Exception as e:
            messagebox.showerror("Error", f"Error al cargar datos: {e}")
    
    def clear_form(self):
        """Limpia todos los campos del formulario"""
        self.id_var.set("")
        self.nombre_var.set("")
        self.apellido_var.set("")
        self.edad_var.set("")
        self.email_var.set("")
    
    def load_from_list(self):
        """Carga datos del registro seleccionado en la lista al formulario"""
        selection = self.tree.selection()
        if not selection:
            messagebox.showwarning("Advertencia", "Seleccione un registro de la lista")
            return
        
        # Obtener datos del registro seleccionado
        item = self.tree.item(selection[0])
        values = item['values']
        
        # Cargar en el formulario
        self.id_var.set(str(values[0]))
        self.nombre_var.set(values[1])
        self.apellido_var.set(values[2])
        self.edad_var.set(str(values[3]) if values[3] else "")
        self.email_var.set(values[4])
    
    def on_select(self, event):
        """Maneja la selección en el Treeview"""
        # Este método se puede usar para acciones automáticas cuando se selecciona un registro
        pass
    
    def log_sql(self, sql_query):
        """Registra las consultas SQL ejecutadas"""
        timestamp = datetime.now().strftime("%H:%M:%S")
        self.sql_text.insert(tk.END, f"[{timestamp}] {sql_query}\n")
        self.sql_text.see(tk.END)
    
    def __del__(self):
        """Cierra la conexión al destruir el objeto"""
        if hasattr(self, 'conn'):
            self.conn.close()

def main():
    """Función principal"""
    print("Iniciando ejemplo simple de CRUD con SQLite...")
    
    root = tk.Tk()
    
    # Configurar estilo
    style = ttk.Style()
    
    # Crear aplicación
    app = SimpleCRUDExample(root)
    
    # Centrar ventana
    root.update_idletasks()
    x = (root.winfo_screenwidth() // 2) - (root.winfo_width() // 2)
    y = (root.winfo_screenheight() // 2) - (root.winfo_height() // 2)
    root.geometry(f"+{x}+{y}")
    
    # Manejar cierre de aplicación
    def on_closing():
        if hasattr(app, 'conn'):
            app.conn.close()
        root.destroy()
    
    root.protocol("WM_DELETE_WINDOW", on_closing)
    
    print("✓ Aplicación iniciada exitosamente")
    print("Base de datos: ejemplo_simple.db")
    print("Tabla: personas")
    
    root.mainloop()

if __name__ == "__main__":
    main()
