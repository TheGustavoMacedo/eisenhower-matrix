from panel import check
from assistant import user_input, table_extract, assistant_ia

def main_menu():
    print('\n' + '╔' + '═' * 48 + '╗')
    print('║            EISENHOWER MATRIX MANAGER           ║')  
    print('╠' + '═' * 48 + '╣')
    print('║ [1] Task Management                            ║')
    print('║ [2] Atlas - AI                                 ║')
    print('║ [0] Exit                                       ║')
    print('╚' + '═' * 48 + '╝')
    choice = int(input('Choose an option: '))

    if choice == 1:
        check()
        main_menu()
    elif choice == 2:
        ai_assistant()
        main_menu() 
    elif choice == 0:
        print('\n┌' + '─' * 20 + '┐')
        print('│   Goodbye! 👋        │')
        print('└' + '─' * 20 + '┘\n')
        exit()
    else:
        print('❌ Invalid option!')
        main_menu()

def ai_assistant():
    print('=' * 20, 'AI Assistant - Atlas', '=' * 20)
    while True:
        question = user_input()
        if question == "EXIT":
            main_menu()
        elif question:
            data = table_extract()
            response = assistant_ia(data, question)
            print("🤖 Atlas:", response)
        else:
            break

if __name__ == "__main__":
    main_menu()
