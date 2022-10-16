from tkinter import *

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from src.service.service import Service as Svc
from webdriver_manager.chrome import ChromeDriverManager

from src.repository.price_store import PriceStore
from src.service import inference_mamdani, model
from src.service import fuzzy_operators
from src.ui.ui import UI


def get_driver():
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    options.add_argument("--window-size=1450,1000")
    options.add_experimental_option("detach", True)
    return webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)


if __name__ == "__main__":

    store = PriceStore(get_driver())
    print(store.low)
    print(store.high)
    service = Svc(store)

    # for lv in model.input_lvs:
    #     fuzzy_operators.draw_lv(lv)
    #fuzzy_operators.draw_lv(model.output_lv)

    root = Tk()
    root.title('Fuzzy Apartment Price Calculator')
    root.geometry('390x241')
    root.resizable(width=False, height=False)
    root.protocol("WM_DELETE_WINDOW", sys.exit)
    UI(root, service)
    root.mainloop()
