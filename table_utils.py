from tabulate import tabulate
import os


def create_table(product_name, product_code, product_price, currency, product_link, date, screenshot_filename):
    return {
        'nome_produto_coleta': product_name,
        'código_produto': product_code,
        'preco_coleta': f'{currency} {product_price}',
        'url_coleta': product_link,
        'data_coleta': date,
        'arquivo_do_preco': screenshot_filename
    }


def print_table(data_df, chosen_category):
    table_headers = data_df[0].keys()
    data = tabulate(data_df, headers='keys', tablefmt='pretty',
                    colalign=['left']*len(table_headers))
    save_table_to_html(data_df, chosen_category)
    print(data)


def sanitize_filename(filename):
    filename = filename.replace('https://www.marchio.com/', '')
    return filename


def save_table_to_html(table, name_category):
    try:
        table_dir = 'table'
        if not os.path.exists(table_dir):
            os.makedirs(table_dir)
        sanitized_product_name = sanitize_filename(name_category)
        file_name = f"{sanitized_product_name}_table.html"
        file_path = os.path.join(table_dir, file_name)
        with open(file_path, 'w') as f:
            f.write(tabulate(table, headers='keys', tablefmt='html'))
        print(f"Tabela salva em: {file_path}")
    except Exception as e:
        print(f"Erro ao criar tabela: {e}")
