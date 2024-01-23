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
