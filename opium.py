import pystyle
import requests

def getLeakOsinit(token, data):
    for database, info in requests.post("https://leakosintapi.com", json={"token":token, "request":data, "limit": 100, "lang":"ru"}).json()['List'].items():
        if "No results found" in database:
            pystyle.Write.Print("\n[!] Ничего не найдено\n", pystyle.Colors.blue_to_white, interval = 0.0001)
            break
        if "error" in database.lower() or "error" in info.lower():
            pystyle.Write.Print("\n[!] Ошибка: " + database + info, pystyle.Colors.red, interval = 0.0001)
            break
        pystyle.Write.Print("\n[+] База данных -> ", pystyle.Colors.blue_to_white, interval = 0.0001)
        pystyle.Write.Print(database, pystyle.Colors.white, interval = 0.0001)
        pystyle.Write.Print("\n\n[+] Описание -> ", pystyle.Colors.blue_to_white, interval = 0.0001)
        pystyle.Write.Print(f"{info['InfoLeak']}\n", pystyle.Colors.white, interval = 0.0001)
        for record in info['Data']:
            for key, value in record.items():
                pystyle.Write.Print(f"\n[+] {key} -> ", pystyle.Colors.green_to_white, interval = 0.0001)
                pystyle.Write.Print({value}, pystyle.Colors.blue_to_white, interval = 0.0001)
        


def menu():
    pystyle.Write.Print('''
                         ░▒▓██████▓▒░  ░▒▓███████▓▒░  ░▒▓█▓▒░ ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓██████████████▓▒░  
                        ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░ ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░ 
                        ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░ ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░ 
                        ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓███████▓▒░  ░▒▓█▓▒░ ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░ 
                        ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░        ░▒▓█▓▒░ ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░ 
                        ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░        ░▒▓█▓▒░ ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░ 
                         ░▒▓██████▓▒░  ░▒▓█▓▒░        ░▒▓█▓▒░  ░▒▓██████▓▒░  ░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░ 
                                                    MINI DOXX TOOLKIT
                                            by wndkx; tg: @wndkx, @the_wndkx; 
                                            ______________________________
                                            |    Пробивает по:           |
                                            |  [+] Instagram username    |
                                            |  [+] Telegram username/id  |
                                            |  [+] Twitter username      |
                                            |  [+] Facebook              |
                                            |  [+] Номер телефона        |
                                            |  [+] Email                 |
                                            |  [+] VK                    |
                                            |  [+] Снилс                 |
                                            |  [+] Имя                   |
                                            |  [+] ИНН                   |                                
                                            |  [+] Номер паспорта        |                    
                                            |  [+] Код подразделения     |
                                            |  [+] Номер машины          |
                                            |  [+] Номер удостоверения   |
                                            |   и многое другое...       |
                                            |____________________________|
''', pystyle.Colors.blue_to_white, interval = 0.0001)
if __name__ == "__main__":
    while True:
        try:
            pystyle.System.Clear()
            menu()
            queries = pystyle.Write.Input('''
            [+] Введите запрос(; чтобы вписать несколько данных): ''', pystyle.Colors.blue_to_white, interval = 0.0001)
            if queries == '':
                continue
            else:
                token = pystyle.Write.Input('''
            [+] Введите токен от LeakOsint: ''', pystyle.Colors.blue_to_white, interval = 0.0001)
                getLeakOsinit(token, queries)
                pystyle.Write.Input('\n[+] Нажмите Enter для продолжения...', pystyle.Colors.blue_to_white, interval = 0.0001)
        except Exception as e:
            pystyle.Write.Print(f'[!] Ошибка: {e}', pystyle.Colors.red, interval = 0.0001)
            pystyle.Write.Input('\n[+] Нажмите Enter для продолжения...', pystyle.Colors.blue_to_white, interval = 0.0001)
        except KeyboardInterrupt:
            pystyle.Write.Print('[-] Выход...', pystyle.Colors.red, interval = 0.0001)
            exit()