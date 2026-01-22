# if-elif-else statement
from pyscript import display, document


def julias_answer(e):
    document.getElementById('output').innerHTML = ''

    response = document.getElementById('input1').value.lower()

    if response == 'yes':
        display(f'Kian will be her valentine', target='output')
    elif response == 'no':
        display(f'Kian will be rejected/heart broken.', target='output')
    elif response == 'maybe':
        display(f'Do not give up, try again!', target='output')
    else:
        display(f'Invalid input', target='output')