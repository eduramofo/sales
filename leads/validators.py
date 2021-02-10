from django.core.exceptions import ValidationError


def validate_telefone(num):

    num = remove_telefone_trash_characters(num)

    if not num.isdigit():
        raise ValidationError('Apenas números são permitidos.', 'digit')
    
    if not len(num) == 11:
        raise ValidationError('Número de telefone inválido.', 'invalido')
    
    ddds_list = [
            '11', '12', '13', '14', '15', '16', '17', '18', '19',
            '21', '22', '24', '27', '28',
            '31', '32', '33', '34', '35', '37', '38',
            '41', '42', '43','44', '45', '46', '47', '48', '49',
            '51', '53', '54', '55',
            '61', '62', '63', '64', '65', '66', '67', '68', '69',
            '71', '73', '74', '75', '77', '79',
            '81', '82', '83', '84', '85', '86', '87', '88', '89',
            '91', '92', '93', '94', '95', '96', '97', '98', '99'
    ]

    ddd = num[:2]

    if not ddd in ddds_list:
        raise ValidationError('Informe um DDD válido.', 'ddd_invalido')


def remove_telefone_trash_characters(row_string):
    clean_string = row_string.replace('(', '').replace(')', '').replace('-', '').replace(' ', '')
    return clean_string
