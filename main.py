import pandas as pd
import os

# --- 1️⃣ Leer el archivo CSV que está en la misma carpeta ---
nombre_archivo = input("📄 Ingresá el nombre del archivo CSV (ejemplo: datos.csv): ")

if not os.path.exists(nombre_archivo):
    print(f"❌ No se encontró el archivo '{nombre_archivo}' en la carpeta actual.")
    print("📁 Archivos disponibles en la carpeta:")
    print(os.listdir())
    exit()

df = pd.read_csv(nombre_archivo)
print("\n✅ Archivo leído correctamente.\n")
print("Vista previa del DataFrame:")
print(df.head())

# --- 2️⃣ Funciones de modificación ---
def agregar_fila(df):
    """Agrega una fila pidiendo al usuario los valores."""
    print("\n👉 Ingresá los valores para una nueva fila:")
    nueva_fila = {}
    for col in df.columns:
        valor = input(f"{col}: ")
        nueva_fila[col] = valor
    df.loc[len(df)] = nueva_fila
    print("\n✅ Fila agregada correctamente.\n")
    return df

def eliminar_fila(df):
    """Elimina una fila por índice."""
    print("\n📋 Índices actuales del DataFrame:")
    print(df.index.tolist())
    try:
        indice = int(input("🗑️ Ingresá el índice de la fila que querés eliminar: "))
        if indice in df.index:
            df = df.drop(indice).reset_index(drop=True)
            print("\n✅ Fila eliminada correctamente.\n")
        else:
            print("❌ Índice no encontrado.")
    except ValueError:
        print("❌ Debes ingresar un número válido.")
    return df

def mostrar_menu_modificacion(df):
    """Menú interactivo para modificar el DataFrame."""
    while True:
        print("\n🔧 Menú de modificaciones:")
        print("1 - Agregar una fila")
        print("2 - Eliminar una fila")
        print("3 - Agregar columna de ejemplo")
        print("4 - Ver DataFrame")
        print("0 - Terminar modificaciones")

        opcion = input("Elegí una opción: ")

        if opcion == "1":
            df = agregar_fila(df)
        elif opcion == "2":
            df = eliminar_fila(df)
        elif opcion == "3":
            df["Nueva_Columna"] = range(1, len(df) + 1)
            print("✅ Columna 'Nueva_Columna' agregada.")
        elif opcion == "4":
            print(df)
        elif opcion == "0":
            break
        else:
            print("❌ Opción inválida.")
    return df

# --- 3️⃣ Ejecutar modificaciones ---
df = mostrar_menu_modificacion(df)

# --- 4️⃣ Elegir formato de salida ---
print("\n¿En qué formato querés guardar el archivo modificado?")
print("1 - CSV")
print("2 - JSON")

opcion = input("Elegí una opción (1 o 2): ")

if opcion == "1":
    salida = "archivo_modificado.csv"
    df.to_csv(salida, index=False)
    print(f"✅ Archivo guardado como CSV: '{salida}'")
elif opcion == "2":
    salida = "archivo_modificado.json"
    df.to_json(salida, orient="records", indent=4)
    print(f"✅ Archivo guardado como JSON: '{salida}'")
else:
    print("❌ Opción no válida. No se guardó el archivo.")
