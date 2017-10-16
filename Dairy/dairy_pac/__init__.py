

import os.path as Path
import sys
from dairy_pac import storage
import datetime
get_connection = lambda : storage.connect('dairy.sqlite')


def acton_show_menu():
    """ Показать все исходное меню"""
    print("""
        Here is your dairy. Welcome!

            1. Show the task list for today.
            2. Add the task.
            3. Edit the task.
            4. Finish the task
            5. Begin the task again
            m. Show this menu
            q. Exit.

        """
        )



def action_show_today_tasks():
    """ Показать спсок всех задач  со статусом 'в работе' на текущую дату"""
    with get_connection() as conn:
        date = datetime.date.today()
        today_task = storage.find_task_by_date(conn, date)
        template = """{row[task_name]} - {row[task_description]} -
                    {row[task_status]} - {row[task_craeted]} -
                    {row[task_realizer]} - {row[task_time]}
                    """


        for row in today_task:
            print(template.format(row = row))



def action_add_task():
    """ Добавить задачу  """
    name_new = input('\n Add the name of new task: ')
    description = input('\n Please describe the task: ')
    realizer = input('\n Who will do? ')
    year = int(input('Deadline: \nyear: '))
    month = int(input('\nmonth: '))
    date = int(input('\ndate: '))


    try:
        date = datetime.date(year, month, date)
    except ValueError:
        print('The date failed')
    else:
        with get_connection() as conn:
            new_task = storage.add_task(conn, name_new, description, realizer, date)
        print('The task "{}" was added'.format(name_new))


def action_edit_task():
    """ отредактировать задачу """
    with get_connection() as conn:
        tasks = storage.find_all(conn)
        template = """{row[id]} - {row[task_name]} - {row[task_description]} -
                    {row[task_status]} - {row[task_realizer]} -
                    {row[task_time]}
                    """
        for row in tasks:
            print(template.format(row = row))
        pk = input('\n\n Inter the id of the task to edit ')
        name_new = input('\n Add the name of new task: ')
        description = input('\n Please describe the task: ')
        realizer = input('\n Who will do? ')
        year = int(input('Deadline: \nyear: '))
        month = int(input('\nmonth: '))
        date = int(input('\ndate: '))

        try:
            date = datetime.date(year, month, date)
        except ValueError:
            print('The date failed')
        else:
            print('\n Which status you want to choose:  ')
            st = {"1":'working',"2":'finished'}
            print("\n1 - 'working'; 2 - 'finished' ")
            s = input()
            status = st[s]

            with get_connection() as conn:
                new_task = storage.edit_task(conn, name_new, description,
                                             status, realizer, date, pk)
            print('The task id={} was changed'.format(pk))


def action_finish_task():
    """ Поменять статус выбранной задачи на 'завершена' """
    with get_connection() as conn:
        status = 'working'
        tasks = storage.find_task_by_status(conn, status)
        template = """{row[id]} - {row[task_name]} - {row[task_description]} -
                    {row[task_status]} - {row[task_realizer]} -
                    {row[task_time]}
                    """
        for row in tasks:
            print(template.format(row = row))
    pk = input('\n\n Inter the id of the task to finish ')
    with get_connection() as conn:
        new_status = 'finished'
        storage.change_status(conn, pk, new_status)
    print('The task id {} was cnanged to {}'. format(pk, new_status))





def action_begin_again():
    """ Возобновить задачу из статуса 'завершена' """
    with get_connection() as conn:
        status = 'finished'
        tasks = storage.find_task_by_status(conn, status)
        template = """{row[id]} - {row[task_name]} - {row[task_description]} -
                    {row[task_status]} - {row[task_realizer]} -
                    {row[task_time]}
                    """
        for row in tasks:
            print(template.format(row = row))
    pk = input('\n\n Inter the id of the task to begin again ')
    with get_connection() as conn:
        new_status = 'working'
        storage.change_status(conn, pk,new_status)
    print('The task id {} was cnanged to {}'. format(pk, new_status))



def action_exit():
    """  Выход из программы"""
    sys.exit(0)


def main():
    creation_schema = Path.join(
        Path.dirname(__file__), 'schema.sql'
    )
    with get_connection() as conn:
        storage.initialize(conn, creation_schema)

    actions = {
        '1': action_show_today_tasks,
        '2': action_add_task,
        '3': action_edit_task,
        '4': action_finish_task,
        '5': action_begin_again,
        'm': acton_show_menu,
        'q': action_exit
    }

    acton_show_menu()

    while True:
        cmd = input('\nChoose your activity from the list:')
        action = actions.get(cmd)
        if action:
            action()
        else:
            print ('Нет такой команды')
