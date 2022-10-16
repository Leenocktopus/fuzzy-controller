import tkinter as tk
from tkinter import *

from src.service import model
from src.service.service import Service


class UI:
    def __init__(self, root, service: Service):
        self.root = root
        self.service = service
        self.calculate_button = tk.Button(root,
                                          font=('Arial', 14),
                                          text="Calculate",
                                          width=30,
                                          command=lambda: self.process_input())

        self.size_label = Label(root, text="Area in square meters")
        self.size_entry = Scale(root,
                                from_=19,
                                to=200,
                                resolution=1,
                                orient=HORIZONTAL,
                                length=180,
                                width=10
                                )

        self.proximity_to_metro_label = Label(root, text="Proximity to metro station, km")
        self.proximity_to_metro_entry = Scale(root,
                                              from_=0,
                                              to=15,
                                              resolution=0.1,
                                              orient=HORIZONTAL,
                                              length=180,
                                              width=10
                                              )

        self.proximity_to_center_label = Label(root, text="Proximity to city center, km")
        self.proximity_to_center_entry = Scale(root,
                                               from_=0,
                                               to=20,
                                               resolution=0.1,
                                               orient=HORIZONTAL,
                                               length=180,
                                               width=10
                                               )

        self.ceiling_height_label = Label(root, text="Ceiling height, m")
        self.ceiling_height_entry = Scale(root,
                                          from_=2.8,
                                          to=5,
                                          resolution=0.1,
                                          orient=HORIZONTAL,
                                          length=180,
                                          width=10
                                          )

        self.result_label = Label(root, text="Input data and hit `Calculate` button to get a result")
        self.size_label.grid(row=1, column=0, sticky=SW)
        self.size_entry.grid(row=0, column=1, rowspan=2)

        self.proximity_to_metro_label.grid(row=3, column=0, sticky=W)
        self.proximity_to_metro_entry.grid(row=2, column=1, rowspan=2)

        self.proximity_to_center_label.grid(row=5, column=0, sticky=W)
        self.proximity_to_center_entry.grid(row=4, column=1, rowspan=2)

        self.ceiling_height_label.grid(row=7, column=0, sticky=W)
        self.ceiling_height_entry.grid(row=6, column=1, rowspan=2)

        self.calculate_button.grid(row=8, column=0, columnspan=2, pady=(20, 10))
        self.result_label.grid(row=11, column=0, rowspan=4, columnspan=3)

    def process_input(self):
        size = self.size_entry.get()
        proximity_to_metro = self.proximity_to_metro_entry.get()
        proximity_to_center = self.proximity_to_center_entry.get()
        ceiling_height = self.ceiling_height_entry.get()
        crisp_values = (size, proximity_to_metro, proximity_to_center, ceiling_height)
        (crisp, word) = self.service.get_fuzzy_result(crisp_values)
        self.result_label.config(text="{crisp}$, {word}".format(crisp=int(crisp), word=word))
