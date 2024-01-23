from products import process_products_based_on_category
from menu_utils import select_category_and_navigate
import time


def main():
    chosen_category = select_category_and_navigate()
    process_products_based_on_category(chosen_category)
    


if __name__ == "__main__":
    initial_time  = time.time()
    main()
    end_time = time.time()
    print(f"O Código levou {int(end_time - initial_time)} segundos para finalizar")