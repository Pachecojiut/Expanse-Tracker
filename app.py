import argparse
import json
from datetime import date

def load_expanse():
    try:
        with open('task.json', 'r') as f:
            return json.load(f, indent=4)
    except FileNotFoundError:
        return []

def save_expanse(expenses):
    with open('task.json', 'w',encoding='utf-8') as f:
        json.dump(expenses,f,ensure_ascii=False)

# Parser esta pronto
parser = argparse.ArgumentParser(prog='expanse-tracker')
subparser = parser.add_subparsers(dest='command', required=True)

add_parser = subparser.add_parser('add', help='Adiciona um gasto')
add_parser.add_argument('--description', required=True)
add_parser.add_argument('--amount',  type=float, required=True)

update_parser = subparser.add_parser('update', help='Atualiza um gasto')
update_parser.add_argument('--description')
update_parser.add_argument('--amount', type=float)
update_parser.add_argument('--id',type=int, required=True)

delete_parser = subparser.add_parser('delete', help='Deleta um gasto')
delete_parser.add_argument('--id',type=int, required=True)

listar_parser = subparser.add_parser('list')
args = parser.parse_args()

# Agora vamos para as funções.

def cmd_add(args):
    expenses = load_expanse()   # Chamamos a função la em cima e armazenamos em uma variavel, tenho que usar ela em todas as funções
    ids = [e['ID'] for e in expenses] # Os IDs.
    new_id = max(ids, default=0) + 1
    today = date.today().isoformat()
    tracker = {'ID': new_id, 'Date': today, 'Description': args.description, 'Amount': args.amount}
    expenses.append(tracker)
    save_expanse(expenses)
    print(f'Dispesa adicionada com sucesso (ID : {new_id})')






