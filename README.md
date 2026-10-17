# Expense Tracker 

Um aplicativo rastreador de despesas via terminal para gerenciar finanças.
Permitindo poder adicionar, excluir, atualizar, visualizar, e até mesmo exportar suas despesas.

## Requisitos
Python3, sem instalar nada (somente as bibliotecas padrão)

## Como usar
### Comandos
- **add**: Adiciona uma despesa com `--description` e `--amount` para o valor.Também é possivel definir uma categoria com '--category'. Se não for informada, a categoria padrão é 'Geral'.

- **list**: lista todas as despesas. Com a opção `--category`, lista somente as despesas da categoria desejada (a busca não diferencia maiúsculas de minúsculas).

- **update**: Atualiza uma despesa, mudando sua descrição, e valor. Voce deve informar o ID da despesa com `--id`. As opções de mudança da `--description` e `--amount` são opcionais: será mudado apenas o que for informado.

- **delete**: Deleta uma despesa de acordo com o seu ID (`--id`). Não pede confirmação

- **summary**: Mostra o total dos gastos. Sem opções, soma todas as despesas. Com `--month`, soma somente as despesas do mês informado (1 a 12), considerando o ano atual.

- **export**: Grava uma copia das despesas num arquivo CSV novo, sem mexer no `expenses.csv`. Tende-se a opção `--file` que é o nome do arquivo de saida. Se não passar, o padrão é `export.csv`


### Exemplos
```bash
python3 app.py add --description "Almoço" --amount 20 --category Comida
python3 app.py list
python3 app.py list --category comida
python3 app.py update --id 1 --amount 25
python3 app.py delete --id 1
python3 app.py summary
python3 app.py summary --month 10
python3 app.py export --file backup.csv
```
As despesas são salvas no arquivo `expenses.csv`, que é criado automaticamente no primeiro `add`, caso ainda não exista. O arquivo que acompanha o repositório contém apenas dados de exemplo.
