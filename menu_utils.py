from webdriver_setup import webdriver_configurations
from categories import get_categories
from time import sleep


def select_category_and_navigate():
    driver = webdriver_configurations()
    url = 'https://www.marchio.com/'

    name_category, all_links = get_categories(driver, url)
    category_name_and_links = dict(zip(name_category, all_links))
    user_choice = category_menu(name_category)

    if 1 <= user_choice <= len(name_category):
        chosen_category = name_category[user_choice - 1]
        chosen_link = category_name_and_links[chosen_category]

        print(f"Você escolheu: {chosen_category} - Link: {chosen_link}")

        driver.get(chosen_link)
        # sleep(3)
        return chosen_link
    return None


def category_menu(options):
    user_choice = 0
    while user_choice == 0:
        print("Escolha uma opção:")
        for i, option in enumerate(options, start=1):
            print(f"{i}. {option}")
        try:
            user_choice = int(input("Digite o número da opção desejada: "))
            if not (1 <= user_choice <= len(options)):
                user_choice = 0
                print("Opção inválida. Por favor, escolha um número válido.")
        except ValueError:
            user_choice = 0
            print("Digite um número válido.")
    print(user_choice)
    return user_choice
