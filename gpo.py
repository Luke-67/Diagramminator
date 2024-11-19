import os
import subprocess
import tkinter as tk
from tkinter import messagebox
from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()
# Client initialization
client = OpenAI(api_key = os.getenv('OPENAI_API_KEY'))

def generate_dot_diagram(structure, activity):
    prompt = f"""
    Crea un diagramma in linguaggio DOT (Graphviz) per l'organigramma di un'azienda {structure} nel settore di {activity}. 
    Segui rigorosamente queste regole di formattazione:
    1. Usa solo sintassi DOT valida
    2. Inizia con 'digraph G {{' e termina con '}}' 
    3. Utilizza connessioni gerarchiche chiare con ->
    4. Usa layout dall'alto verso il basso con rankdir=TB
    5. Formatta i nodi con shape=box
    6. Esempio di formato:
    digraph G {{
        rankdir=TB;
        node [shape=box];
        CEO -> "Vice Presidente";
        "Vice Presidente" -> "Responsabile Dipartimento";
    }}
    L'intera risposta deve essere SOLO UN DIAGRAMMA VALIDO IN LINGUAGGIO DOT. Nessun testo o spiegazione aggiuntiva.
    """
    try:
        chat_completion = client.chat.completions.create(
            messages=[{"role": "user", "content": prompt}],
            model="gpt-4",
        )
        
        diagram = chat_completion.choices[0].message.content.strip()
        return diagram
    except Exception as e:
        return f"Si è verificato un errore: {e}"

def save_and_render_dot(diagram_text, output_image_path, summary_text):
    try:
        # Write the diagram to a .dot file
        dot_file = os.path.join(os.getcwd(), "diagramma.dot")
        with open(dot_file, "w", encoding='utf-8') as file:
            file.write(diagram_text)
        
        # Save the summary text to a .txt file
        summary_file = os.path.join(os.getcwd(), "summary.txt")
        with open(summary_file, "w", encoding='utf-8') as file:
            file.write(summary_text)
        
        # Use fixed Graphviz path for rendering
        dot_path = r"C:\Program Files\Graphviz\bin\dot.exe"
        
        # Full command to be executed
        command = [dot_path, "-Tpng", dot_file, "-o", output_image_path]
        
        # Render the .dot file using Graphviz
        result = subprocess.run(command, capture_output=True, text=True, check=False)
        
        # Check the result
        if result.returncode != 0:
            messagebox.showerror("Error", f"Errore di Graphviz: {result.stderr}")
            return False
        
        # Check if the output image file was created
        if os.path.exists(output_image_path):
            file_size = os.path.getsize(output_image_path)
            messagebox.showinfo("Success", f"Diagramma creato con successo: {output_image_path}\nFile size: {file_size} bytes")
            return True
        else:
            messagebox.showerror("Error", "Il file immagine non è stato creato.")
            return False
        
    except Exception as e:
        messagebox.showerror("Error", f"Errore durante il rendering: {e}")
        return False

def on_submit():
    structure = entry_structure.get()
    activity = entry_activity.get()

    # Generate the diagram
    diagram = generate_dot_diagram(structure, activity)

    if not diagram.startswith("Si è verificato un errore"):
        # Define output image path
        output_image_path = os.path.join(os.getcwd(), "diagramma.png")

        # Generate a simple summary
        summary_text = f"Organigramma di un'azienda con struttura '{structure}' nel settore '{activity}'.\n"

        # Save and render the diagram
        if save_and_render_dot(diagram, output_image_path, summary_text):
            # Optionally, show the rendered image or proceed further
            pass
    else:
        messagebox.showerror("Error", diagram)

# Create the GUI window
root = tk.Tk()
root.title("Diagramm-inator di Luca")

# Add a label for the structure
label_structure = tk.Label(root, text="Struttura azienda (es. 'funzionale'):")
label_structure.pack(pady=5)

# Add an entry field for the structure
entry_structure = tk.Entry(root, width=30)
entry_structure.pack(pady=5)

# Add a label for the activity type
label_activity = tk.Label(root, text="Tipo di attività (es. 'produzione industriale'):")
label_activity.pack(pady=5)

# Add an entry field for the activity
entry_activity = tk.Entry(root, width=30)
entry_activity.pack(pady=5)

# Add a submit button
submit_button = tk.Button(root, text="Genera Diagramma", command=on_submit)
submit_button.pack(pady=20)

# Start the GUI event loop
root.mainloop()
