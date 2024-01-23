from products import process_products_based_on_category
from menu_utils import select_category_and_navigate

def main():
    chosen_category = select_category_and_navigate()
    process_products_based_on_category(chosen_category)

if __name__ == "__main__":
    main()
    