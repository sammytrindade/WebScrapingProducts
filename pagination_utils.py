from selenium.webdriver.common.by import By
from time import sleep
from selenium.common.exceptions import NoSuchElementException


def check_pagination(driver):
    """
    Verifica se há uma seção de paginação na página.

    Args:
        driver (WebDriver): Instância do driver Selenium.

    Returns:
        bool: True se a paginação estiver presente, False se não encontrar o elemento 'catalog-footer'.
    """
    try:
        driver.find_element(By.CLASS_NAME, 'catalog-footer')
        return True
    except NoSuchElementException:
        return False


def has_products(driver):
    """
    Verifica se há produtos na página.

    Args:
        driver (WebDriver): Instância do driver Selenium.

    Returns:
        bool: True se houver produtos, False caso apareça a class 'catalog-empty'.
    """
    try:
        driver.find_element(By.CLASS_NAME, 'catalog-empty')
        return False
    except NoSuchElementException:
        return True


def get_total_pages(driver):
    """
    Obtém o número total de páginas disponíveis na paginação.

    Args:
        driver (WebDriver): Instância do driver Selenium.

    Returns:
        int: Número total de páginas, 0 se não houver paginação.
    """
    try:
        pagination = driver.find_element(By.CLASS_NAME, 'catalog-footer')
        pages = pagination.find_elements(By.CLASS_NAME, 'page')
        return len(pages) - 1
    except NoSuchElementException:
        return 0


def navigate_to_page(driver, category_link, page_number):
    """
    Navega para a página especificada.
    Verifica se a URL tem parâmetros, tendo parâmetros a url é construída 
    com a página especificada. Não tendo, é adicionado e construído.

    Args:
        driver (WebDriver): Instância do driver Selenium.
        category_link (str): URL base da categoria.
        page_number (int): Número da página para navegar.
    """
    try:
        if '?' in category_link:
            page_link = f"{category_link}&pg={page_number}"
        else:
            page_link = f"{category_link}?pg={page_number}"

        driver.get(page_link)
        # sleep(2) 
    except Exception as e:
        print(f"Erro ao navegar para a página {page_number}: {e}")
