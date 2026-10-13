import argparse
import json

def load_expanse():
    try:
        with open('task.json', 'r') as f:
            return json.load(f, indent=4)
    except FileNotFoundError:
        return []

def save_expanse(expenses):
    with open('task.json', 'w',encoding='utf-8') as f:
        json.dump(expenses,f, indent=4,ensure_ascii=False)

parser = argparse.ArgumentParser(prog='expanse-tracker')
subparser = parser.add_subparsers(dest='command', required=True)

add_parser = subparser.add_parser('add', help='Adiciona um gasto')
add_parser.add_argument('--description', required=True)
add_parser.add_argument('--amount',  type=float, required=True)

update_parser = subparser.add_parser('update', help='Atualiza um gasto')
update_parser.add_argument('--description')
update_parser.add_argument('--amount', type=float)
update_parser.add_argument('ID',type=int)

delete_parser = subparser.add_parser('delete', help='Deleta um gasto')
delete_parser.add_argument('ID', type=int)

listar_parser = subparser.add_parser('list')
args = parser.parse_args()

