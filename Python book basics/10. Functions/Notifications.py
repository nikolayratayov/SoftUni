def show_success_message(operation, message):
    print(f'Successfully executed {operation}.')
    print('=' * (len(operation) + 22) + '=')
    print(f'{message}.')


def show_warning_message(operation):
    print(f'Warning: {operation}.')
    print('=' * (len(operation) + 9) + '=')


def show_error_message(operation, message, error_code):
    print(f'Error: Failed to execute {operation}.')
    print('=' * (len(operation) + 25) + '=')
    print(f'Reason: {message}.')
    print(f'Error code: {error_code}.')


def read_and_process_message():
    a = input()
    if a == 'error':
        operation = input()
        message = input()
        error_code = int(input())
        show_error_message(operation, message, error_code)
    elif a == 'warning':
        operation = input()
        show_warning_message(operation)
    elif a == 'success':
        operation = input()
        message = input()
        show_success_message(operation, message)
    print()
    return


n = int(input())
for i in range(n):
    read_and_process_message()
