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
