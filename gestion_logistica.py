import time

# 1. Base de datos del Almacén (Usamos un diccionario para simular stock)
almacen = {
    "PROD001": {"nombre": "Palets de Madera", "stock": 45, "zona": "A"},
    "PROD002": {"nombre": "Cajas de Cartón RE", "stock": 120, "zona": "B"},
    "PROD003": {"nombre": "Film Estirable", "stock": 12, "zona": "A"}
}

def mostrar_inventario():
    print("\n📦 --- ESTADO DEL ALMACÉN ---")
    for codigo, info in almacen.items():
        print(f"[{codigo}] {info['nombre']} | Stock: {info['stock']} unidades | Zona: {info['zona']}")
    print("-----------------------------\n")

def optimizar_ruta(zona_destino):
    print(f"🚛 Calculando ruta de recogida optimizada para Zona {zona_destino}...")
    time.sleep(1.5) # Simula que el ordenador está pensando
    print("✅ ¡Ruta generada! Prioridad de carga: Contenedor Principal -> Muelle de salida.")

# --- SIMULACIÓN DEL PROGRAMA ---
print("🚀 INICIANDO SISTEMA DE GESTIÓN LOGÍSTICA v1.0 🚀")
time.sleep(1)

# Mostramos el inventario inicial
mostrar_inventario()

# Simulamos la recepción de un pedido (salida de stock)
print("📥 Alerta: Procesando orden de salida para 'Film Estirable'...")
time.sleep(1)
almacen["PROD003"]["stock"] -= 5 # Restamos 5 unidades
print("🛒 Stock actualizado con éxito.")

# Mostramos el inventario actualizado
mostrar_inventario()

# Ejecutamos el módulo de rutas para la Zona A
optimizar_ruta("A")

print("\n🏁 Simulación finalizada correctamente.")
