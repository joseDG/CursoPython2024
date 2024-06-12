import os 

#ruta del archivo donde se guardo las tareas
TASKS_FILE = 'tasks.txt'

def load_tasks():
  """Carga las tareas desde el archivo."""
  if not os.path.exists(TASKS_FILE):
    return []
  with open(TASKS_FILE, 'r') as file:
    tasks = file.readlines()
  return [task.strip() for task in tasks]

def save_tasks(tasks):
  """Guardar las tareas en el archivo"""
  with open(TASKS_FILE, 'w') as file:
    for task in tasks:
      file.write(task + '\n')


def add_task(task):
  """Agrear una nueva tarea"""
  tasks = load_tasks()
  tasks.append(task)
  save_tasks(tasks)
  print(f"Tarea {task} agregada.")


def view_tasks():
  """Muestra todas las tareas."""
  tasks = load_tasks()
  if not tasks:
    print("No hay tareas pendientes.")
    return
  print("Tareas pendientes:")
  for i, task in enumerate(tasks, 1):
    print(f'{i}, {task}')

def  update_task(task_number, new_task):
  """Actualiza una tareas existente."""
  tasks = load_tasks()
  if task_number < 1 or task_number > len(tasks):
    print("Numero de tarea invalida.")
    return
  tasks[task_number - 1] = new_task
  save_tasks(tasks)
  print(f'Tarea {task_number} actualizada a "{new_task}".')


def delete_task(task_number):
  """Elimina una tarea."""
  tasks = load_tasks()
  if task_number < 1 or task_number > len(tasks):
    print("Numero de tarea invalida.")
    return
  deleted_task = tasks.pop(task_number - 1)
  save_tasks(tasks)
  print(f'Tarea "{deleted_task}" eliminada.')


def show_menu():
  """Muestra el menu de opciones."""
  print('\n--- Menú de Tareas ---')
  print('1. Ver tareas')
  print('2. Agregar tarea')
  print('3. Actualizar tarea')
  print('4. Eliminar tarea')
  print('5. Salir')


def main():
  while True:
    show_menu()
    choice = input("Seleccione una opcion: ")
    if choice == '1':
      view_tasks()
    elif choice == '2':
      task = input('Escribe la nueva tarea: ')
      add_task(task)
    elif choice == '3':
      view_tasks()
      task_number = int(input('Numero de tarea a actualizar: '))
      new_task = input('Nueva descripcion de la tarea: ')
      update_task(task_number, new_task)
    elif choice == '4':
      view_tasks()
      task_number = int(input('Numero de tarea a eliminar: '))
      delete_task(task_number)
    elif choice == '5':
      print('¡Adios!')
      break
    else:
      print('Opcion no valida, Intente de nuevo. ')



if __name__ == '__main__':
  main()