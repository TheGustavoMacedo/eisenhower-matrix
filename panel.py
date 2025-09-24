import sqlite3

conn = sqlite3.connect('matrix.db')
c = conn.cursor()

def check():
    print('=' * 20, 'Menu', '=' * 20)
    print('[1] Add task\n[2] Remove task\n[3] All tasks (AI)\n[0] Return')
    print('')
    choose = int(input('Choose an option: '))
    if choose == 1:
        add()
    elif choose == 2:
        remove()
    elif choose == 3:
        view()
    elif choose == 0:
        conn.commit()
        return
    else:
        print('Invalid option!')
        print('')
        check()

def add():
    print('')
    print('=' * 20, 'Add task', '=' * 20)
    task = input('Enter the task name: ')
    print('Status: [1] Do [2] Decide [3] Delegate [4] Delete')
    status = int(input('Choice: '))
    if status == 1:
        status = 'Do'
    elif status == 2:
        status = 'Decide'
    elif status == 3:
        status = 'Delegate'
    elif status == 4:
        status = 'Delete'
    else:
        print('Invalid option!')
        print('')
    
    print('Do you have a date to start?: ')
    date_choice = int(input('[1] Yes [2] No\nChoice: '))
    if date_choice == 1:
        date = input('Date: ')
    else:
        date = None
    description = input('Enter a brief description of the task: ')
    c.execute('INSERT INTO eisenhower (task, description, status, date) VALUES (?, ?, ?, ?)', (task, description, status, date))
    conn.commit()
    print('Task added successfully!')

def remove():
    print('=' * 20, 'Remove task', '=' * 20)
    print('')
    task = input('Task Name: ')
    c.execute('DELETE FROM eisenhower WHERE task = ?', (task,))
    conn.commit()
    print('Task removed successfully!')
    print('')

def view():
    print('=' * 20, 'View All Tasks', '=' * 20)
    print('')
    c.execute('SELECT * FROM eisenhower')
    tasks = c.fetchall()
    
    if tasks:
        print(f"{'ID':<5} {'Task':<20} {'Description':<30} {'Status':<10} {'Date':<12}")
        print('-' * 80)
        for task in tasks:
            id_task = task[0]
            task_name = task[1][:18] if len(task[1]) > 18 else task[1]
            description = task[2][:28] if len(task[2]) > 28 else task[2]
            status = task[3]
            date = task[4] if task[4] else 'No date'
            
            print(f"{id_task:<5} {task_name:<20} {description:<30} {status:<10} {date:<12}")
    else:
        print("No tasks found in the database.")
    
    print('')
