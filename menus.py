from colors import print_color

def menu1(opciones: list):

    foreground = 'red'


    print_color('────────────────────────┐', foreground, 'bold')
    print_color('┌───────── Menu ────────┘', foreground, 'bold')
    for i in range(len(opciones)):
        print_color(f'├─[{i}] ', foreground, 'bold', end='')
        print_color(opciones[i])

    print_color('└─────────────────────────', foreground, 'bold')

def menu2(opciones: list):

    foreground = 'cyan'

    print_color('========== Menu ==========', foreground, 'bold')
    for i, opcion in enumerate(opciones):
        estilo = 'bold' if i % 2 == 0 else 'italic'
        print_color(f'{i + 1}. {opcion}', foreground, estilo)

    print_color('==========================', foreground, 'bold')

def menu3(opciones:list):

    background = 'white'
    foreground = 'black'

    print_color('┌─────┬──── Menu ────',foreground,'bold',background)

    for i in range(len(opciones)):
        print_color(f'├─ {i} ─┤ {opciones[i]} ',foreground,'bold',background,end='')

        if len(f'├─ {i} ─┤ {opciones[i]}) ') < len('┌─┤×├─┬──── Menu ────'):
            for j in range(len('┌─┤×├─┬──── Menu ────') - len(f'├─ {i} ─┤ {opciones[i]}) ')):
                print_color('-',foreground,'bold',background,'')
            print_color('-',foreground,'bold',background)
    print_color('└─────┴──── Menu ────',foreground,'bold',background)

def menu4(opciones:list):

    foreground = 'purple'
    background = ''

    print_color('█▀▀▀█▀▀▀▀▀▀█▀▀▀█',foreground,'bold',background)
    print_color('█▄▄▄█ Menu █▄▄▄█',foreground,'bold',background)

    for i in range(len(opciones)):

        print_color(f'█ {i} █ {opciones[i]}',foreground,'bold',background)
    
    print_color('█▄▄▄█▄▄▄▄▄▄▄▄▄▄█',foreground,'bold',background)

def menu5(opciones: list):

    foreground = 'blue'

    print_color('╔════════════════════╗', foreground, 'bold')
    print_color('║      Menu          ║', foreground, 'bold')
    for i in range(len(opciones)):
        print_color(f'╠═ [{i}] {opciones[i]}', foreground, 'bold')
    print_color('╚════════════════════╝', foreground, 'bold')

def menu6(opciones: list):

    foreground = 'yellow'
    background = ''

    print_color('┌──────────────────────┐', foreground, 'bold', background)
    print_color('│        Menu          │', foreground, 'bold', background)
    for i in range(len(opciones)):
        print_color(f'├─ {i} ─┤ {opciones[i]}', foreground, 'bold', background)
    print_color('└──────────────────────┘', foreground, 'bold', background)

def menu7(opciones: list):

    foreground = 'green'
    background = ''

    print_color('┌──────────────────────┐', foreground, 'bold', background)
    print_color('│       Menu           │', foreground, 'bold', background)
    for i in range(len(opciones)):
        print_color(f'│ {i}. {opciones[i]}', foreground, 'bold', background)
    print_color('└──────────────────────┘', foreground, 'bold', background)

def menu8(opciones: list):

    foreground = 'white'
    background = ''

    print_color('┌───────────────┐', foreground, 'bold', background)
    print_color('│     Menu      │', foreground, 'bold', background)
    for i in range(len(opciones)):
        print_color(f'├─ [{i}] {opciones[i]}', foreground, 'bold', background)
    print_color('└───────────────┘', foreground, 'bold', background)

def menu9(opciones: list):

    foreground = 'cyan'
    background = ''

    print_color('╭───────────────╮', foreground, 'bold', background)
    print_color('│     Menu      │', foreground, 'bold', background)
    for i in range(len(opciones)):
        print_color(f'│ {i}. {opciones[i]}', foreground, 'bold', background)
    print_color('╰───────────────╯', foreground, 'bold', background)

def menu10(opciones: list):

    foreground = 'blue'
    background = ''

    print_color('╓───────────────╖', foreground, 'bold', background)
    print_color('║     Menu      ║', foreground, 'bold', background)
    for i in range(len(opciones)):
        print_color(f'║ {i}. {opciones[i]}', foreground, 'bold', background)
    print_color('╙───────────────╜', foreground, 'bold', background)


def menu11(opciones: list):
    foreground = 'red'
    background = ''
    
    print_color('  Menu',foreground,'bold',background)

    for i in range(len(opciones)):
        print_color('•',foreground,'bold',background,'')
        print_color(f' {opciones[i]}')
    
