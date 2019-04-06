#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Name: Salapense
Author: K4YT3X
Date Created: March 27, 2019
Last Modified: April 6, 2019

Description: Calculate how much time I need to work
to buy something.
"""

from tkinter import *

VERSION = '1.0.0'

SALARY_PER_HOUR = 15
HOURS_PER_WEEK = 40


class Salapense:

    def __init__(self):
        self.item_price = None
        self.salary_per_hour = SALARY_PER_HOUR
        self.hours_per_week = HOURS_PER_WEEK

    def get_hours(self):
        return self.item_price / self.salary_per_hour

    def get_weeks(self):
        return self.item_price / (self.salary_per_hour * self.hours_per_week)

    def get_months(self):
        return self.item_price / (self.salary_per_hour * self.hours_per_week * 4)

    def get_years(self):
        return self.item_price / (self.salary_per_hour * self.hours_per_week * 52)


def calculate():
    """
    # process arguments
    args = process_arguments()
    """
    global item_price
    global salary_per_hour
    global hours_per_week

    global hours_needed
    global weeks_needed
    global months_needed
    global years_needed

    # initialize salapense object
    salapense = Salapense()

    # pass values
    salapense.item_price = item_price.get()
    salapense.salary_per_hour = salary_per_hour.get()
    salapense.hours_per_week = hours_per_week.get()

    # calculate time needed
    hours_needed.set(salapense.get_hours())
    weeks_needed.set(salapense.get_weeks())
    months_needed.set(salapense.get_months())
    years_needed.set(salapense.get_years())


if __name__ == "__main__":
    # create a GUI window
    gui = Tk()
    gui.configure(background='white')
    gui.title('Salapense')
    # gui.geometry('300x300')
    # gui.grid_columnconfigure(1, weight=1)

    # item price
    item_price = DoubleVar()
    label_text = StringVar()
    label_text.set('Item Price: ')
    item_price_label = Label(gui, textvariable=label_text, relief=RIDGE, width=15)
    item_price_label.grid(row=0, column=0)

    item_price_field = Entry(gui, textvariable=item_price)
    item_price.set(0)
    item_price_field.grid(row=0, column=1)

    # salary per hour
    salary_per_hour = DoubleVar()
    label_text = StringVar()
    label_text.set('Salary Per Hour: ')
    salary_per_hour_label = Label(gui, textvariable=label_text, relief=RIDGE, width=15)
    salary_per_hour_label.grid(row=1, column=0)

    salary_per_hour_field = Entry(gui, textvariable=salary_per_hour)
    salary_per_hour.set(SALARY_PER_HOUR)
    salary_per_hour_field.grid(row=1, column=1)

    # hours per week
    hours_per_week = DoubleVar()
    label_text = StringVar()
    label_text.set('Hours Per Week: ')
    hours_per_week_label = Label(gui, textvariable=label_text, relief=RIDGE, width=15)
    hours_per_week_label.grid(row=2, column=0)

    hours_per_week_field = Entry(gui, textvariable=hours_per_week)
    hours_per_week.set(HOURS_PER_WEEK)
    hours_per_week_field.grid(row=2, column=1)

    # calculate button
    equal = Button(gui, text='Calculate', command=calculate, height=1, width=30)
    equal.grid(row=3, column=0, columnspan=2)

    # hours needed
    label_text = StringVar()
    label_text.set('Hours Needed: ')
    hours_needed_label = Label(gui, textvariable=label_text, relief=RIDGE, width=15)
    hours_needed_label.grid(row=4, column=0)

    hours_needed = IntVar()
    hours_needed_field = Entry(gui, textvariable=hours_needed)
    hours_needed_field.grid(row=4, column=1)

    # weeks needed
    label_text = StringVar()
    label_text.set('Weeks Needed: ')
    weeks_needed_label = Label(gui, textvariable=label_text, relief=RIDGE, width=15)
    weeks_needed_label.grid(row=5, column=0)

    weeks_needed = IntVar()
    weeks_needed_field = Entry(gui, textvariable=weeks_needed)
    weeks_needed_field.grid(row=5, column=1)

    # months needed
    label_text = StringVar()
    label_text.set('Months Needed: ')
    months_needed_label = Label(gui, textvariable=label_text, relief=RIDGE, width=15)
    months_needed_label.grid(row=6, column=0)

    months_needed = IntVar()
    months_needed_field = Entry(gui, textvariable=months_needed)
    months_needed_field.grid(row=6, column=1)

    # years needed
    label_text = StringVar()
    label_text.set('Years Needed: ')
    years_needed_label = Label(gui, textvariable=label_text, relief=RIDGE, width=15)
    years_needed_label.grid(row=7, column=0)

    years_needed = IntVar()
    years_needed_field = Entry(gui, textvariable=years_needed)
    years_needed_field.grid(row=7, column=1)

    gui.mainloop()
