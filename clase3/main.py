todo = [
    {'id': 2, 'name': 'aprender ingles'},
    {'id': 3, 'name': 'aprender un framework de python'},
    {'id': 4, 'name': 'aprender a cocinar'},
    {'id': 5, 'name': 'aprender una nueva skill'},
    {'id': 1, 'name': 'aprender programacion'},
]

def get_task(id_task: str) -> dict:
    for task in todo:
        if id_task == task.get('id'):
            return task
    
    return {}

task_found = get_task(1)

if not task_found: 
    print('Tarea no encontrada')
else:
    print(task_found)


# [] == false, () == false, {} == false, '' == false
# {con datos} == true, [con datos] == true, (con datos) == true, 'con letras' == true
