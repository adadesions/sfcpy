'''
Hilbert Curve Generator
'''

import os

inverse_table = {
    'd': 'u', 'u': 'd',
    'l': 'r', 'r': 'l',
    'o': 'o'
}
pairing_table = {
    'd': 'r', 'r': 'd',
    'u': 'l', 'l': 'u',
    'o': 'o'
}

connector = lambda header: ''.join(map(lambda ch: pairing_table[ch], header))
assert connector('dru') == 'rdl'
assert connector('lur') == 'uld'

inversor = lambda header: ''.join(map(lambda ch: inverse_table[ch], header))
assert inversor('dru') == 'uld'
assert inversor('urd') == 'dlu'

build_body = lambda conn: conn.join(map(str, conn))
assert build_body('rdl') == 'rrdldrdll'
assert build_body('dru') == 'ddrurdruu'

def split_seq(tape):
    splited = []
    len_tape = len(tape)//4
    for i in range(len_tape):
        start = i*4
        end = start+4
        temp = tape[start:end]
        splited.append(temp)

    return splited


def hc_builder(genesis):
    the_first = pairing_table[genesis[0]]
    header = genesis[1:]
    conn_str = connector(header)
    inv_str = inversor(header)
    body_str = build_body(conn_str)
    genesis = ''.join([the_first, header])
    tape = ''.join([genesis, body_str, inv_str])

    yield tape


def hc_generator(genesis, order, destination):
    tape = ''

    if os.path.isfile(destination):
        os.remove(destination)

    for lv in range(1, order):
        tape = ''
        label_order = 'Order {}\n'.format(lv+1)
        for header in genesis:
            sub_tape = hc_builder(header)
            tape += ''.join([*sub_tape])
            genesis = split_seq(tape)

        with open(destination, 'a') as file:
            file.writelines(label_order)
            file.writelines(tape)
            file.writelines('\n')

    return tape


if __name__ == '__main__':
    the_tape = hc_generator(['odru'], 4, 'test_table.txt')
    print(the_tape)
