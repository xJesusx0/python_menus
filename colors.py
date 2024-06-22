colors = {
    'reset' : "\u001B[0m",
    'black' : "\u001B[30m",
    'red'  : "\u001B[31m",
    'green' : "\u001B[32m",
    'yellow' : "\u001B[33m",
    'blue' : "\u001B[34m",
    'purple' : "\u001B[35m",
    'cyan' : "\u001B[36m",
    'white' : "\u001B[37m"
}

styles = {
    'bold' : "\u001B[1m",
    'italic' : "\u001B[3m",
    'underline' : "\u001B[4m"
} 

backgrounds = {
    'black' : "\u001B[40m",
    'red' : "\u001B[41m",
    'green' : "\u001B[42m",
    'yellow' : "\u001B[43m",
    'blue' : "\u001B[44m",
    'purple' : "\u001B[45m",
    'cyan' : "\u001B[46m",
    'white' : "\u001B[47m"
}

def print_color(text='',color='white',style='',background='',end='\n'):

    COLOR = colors.get(color,'white')
    STYLE = styles.get(style,'')
    BACKGROUND = backgrounds.get(background,'')

    print(f'{BACKGROUND}{COLOR}{STYLE}{text}{colors["reset"]}',end=end)