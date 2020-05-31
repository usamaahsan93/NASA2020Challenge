from tkinter import *
from tkinter.ttk import *
import numpy as np
from sklearn.decomposition import PCA
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.animation as anim
import pandas as pd
from sklearn.feature_selection import VarianceThreshold
from sklearn.preprocessing import MinMaxScaler

matplotlib.use("TkAgg")


def main():
    # list of countries
    countries = ["Countries", "China", "Italy", "Vietnam"]

    window = make_window("COVID-19")

    variable = StringVar(window)
    variable.set("Countries")  # default value
    drop_down_menu = OptionMenu(window, variable, *countries)
    drop_down_menu.pack()

    def ok():
        user_selection = variable.get()
        # empty the window from all widgets
        widget_list = window.winfo_children()
        for item in widget_list:
            item.pack_forget()
        window.quit()
        return user_selection

    ok_button = Button(window, text="OK", command=ok)
    ok_button.pack()

    window.mainloop()

    chosen_country = ok()

    # close all graphs
    plt.close('all')

    # analyze the csv file
    # and create data frames to store the data
    df = pd.read_csv(chosen_country+'.csv')
    df = df.drop(columns=['Date_repor', 'Country', 'WHO_region', 'date'])

    # scale the data frames
    scaling = MinMaxScaler()
    scaled = scaling.fit_transform(df)
    df_scaled = pd.DataFrame(scaled, columns=df.columns, index=df.index)

    # create an empty graph (figure)
    cases_figure = plt.Figure(figsize=(10, 10), dpi=100)
    cases_axis = cases_figure.add_subplot(111)

    # plot the cases vs. the dates
    cases_axis.plot(df_scaled['total_cases'], label='Total Cases')

    #cases_axis.xlabel('Time', fontsize=14)
    #cases_axis.title("china", fontsize=18)

    def transport_clicked():
        # show transport curve
        cases_axis.plot(df_scaled['Close public transport (OxBSG)'], label='Public Transport')

    def event_clicked():
        # show international travel control's curve
        cases_axis.plot(df_scaled['International travel controls (OxBSG)'], label='International Travel Controls')

    """def school_clicked():
        # show transport curve
        print("School curve")"""

    """def workplace_clicked():
        # show transport curve
        print("workplace curve")"""

    transport_button = Button(window, text="Public Transport", command=transport_clicked)
    transport_button.place(anchor=NW, rely=0.1)

    events_button = Button(window, text="Event Cancel", command=event_clicked)
    events_button.place(anchor=NW, rely=0.2)

    """school_button = Button(window, text="School Lock-down", command=school_clicked)
    school_button.place(anchor=NW, rely=0.3)

    workplace_button = Button(window, text="Workplace Lock-down", command=workplace_clicked)
    workplace_button.place(anchor=NW, rely=0.4)"""

    cases_axis.legend()
    cases_axis.grid()

    cases_graph = FigureCanvasTkAgg(cases_figure, window)
    cases_graph.get_tk_widget().pack(side=RIGHT, fill=BOTH)

    window.mainloop()


def make_window(title):
    """
    function : make canvas
    creates a canvas of width and height
    as passed and gives it a title
    :param title: title of the canvas
    :return: returns the canvas with specified parameters
    """
    # creating a window so that we
    # could create a canvas on it
    window = Tk()
    # giving the window a title
    window.title(title)
    # makes it full screen
    window.geometry("{0}x{1}+0+0".format(window.winfo_screenwidth(), window.winfo_screenheight()))
    return window


if __name__ == '__main__':
    main()
