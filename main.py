# Jonnier Cadena
from min_heap import MinHeap

heap = MinHeap()

heap.insert("Estudiar para el examen", 3)
heap.insert("Lavar los platos", 1)
heap.insert("Hacer ejercicio", 4)
heap.insert("Responder correos", 2)

heap.print_heap()

print("\nTareas extraídas por prioridad:")
while True:
    task = heap.extract_min()
    if not task:
        break
    priority, name = task
    print(f"Tarea: {name}, Prioridad: {priority}")
