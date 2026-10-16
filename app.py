import argparse
import csv
from datetime import date

CAMPOS = ['ID', 'Date', 'Description', 'Amount']
def load_expanse():
    try:
        with open('expenses.csv', 'r', newline='', encoding='utf-8') as f:
            leitor = csv.DictReader(f)
            despesas = []
            for linha in leitor:
                linha['ID'] = int(linha['ID'])
                linha['Amount'] = float(linha['Amount'])
                despesas.append(linha)
            return despesas
    except FileNotFoundError:
        return []

def save_expanse(expenses):
    with open('expenses.csv', 'w',newline='', encoding='utf-8') as f:
        escritor = csv.DictWriter(f, fieldnames=CAMPOS)
        escritor.writeheader()
        escritor.writerows(expenses)

# Parser esta pronto. Os comandos, e seus argumentos/Atributos.
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
    despesas = load_expanse()   # Chamamos a função la em cima e armazenamos em uma variavel, tenho que usar ela em todas as funções
    ids = [e['ID'] for e in despesas] 
    new_id = max(ids, default=0) + 1
    today = date.today().isoformat()
    tracker = {'ID': new_id, 'Date': today, 'Description': args.description, 'Amount': args.amount}
    despesas.append(tracker)
    save_expanse(despesas)
    print(f'Despesa adicionada com sucesso (ID: {new_id})')

def cmd_list(args):
    despesas = load_expanse()
    if not despesas:
        print('Nenhuma despesa encontrada')
    else:
        print(f"{'ID':<4}{'Date':<15}{'Description':<25}{'Amount'}")            # Cabeçalho
        for e in despesas:
            print(f"{e['ID']:<4}{e['Date']:<15}{e['Description']:<25}${e['Amount']:.2f}")   # Cabeçalho

def cmd_delete(args):
    despesas = load_expanse()
    nova_despesas = [e for e in despesas if e['ID'] != args.id]
    if len(despesas) == len(nova_despesas):
        print('ID não encontrado')
        return 
    else:
        save_expanse(nova_despesas)
        print('Despesa excluida com sucesso!')

def cmd_update(args):
    despesas = load_expanse()
    for e in despesas:
        if e['ID'] == args.id:
            if args.description is not None:
                e['Description'] = args.description
            if args.amount is not None:
                e['Amount'] = args.amount
            save_expanse(despesas)
            print('Despesa Atualizada')
            return
    print('ID não encontrado')


if args.command == 'add':
    cmd_add(args)
elif args.command == 'list':
    cmd_list(args)
elif args.command == 'delete':
    cmd_delete(args)
elif args.command == 'update':
    cmd_update(args)
