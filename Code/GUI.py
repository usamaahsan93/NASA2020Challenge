from tkinter import *
from tkinter.ttk import *
import numpy as np
import matplotlib
import matplotlib.pyplot
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.animation as anim
import pandas as pd
from sklearn.decomposition import PCA
from sklearn.feature_selection import VarianceThreshold
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import RobustScaler
import warnings
import datetime

matplotlib.use("TkAgg")


def main():
    # list of countries
    countries = ["Countries", "China", "Italy", "Vietnam", "UK", "Sweden", "Finland", "India", "NewZealand"]

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

    warnings.filterwarnings("ignore")
    # close all graphs
    plt.close('all')

    # analyze the csv file
    # and create data frames to store the data
    df = pd.read_csv(chosen_country+'.csv')
    dates = df['date']
    dates = np.array(dates)
    df = df.drop(columns=['Country', 'WHO_region', 'date', 'tests_units'])

    # scale the data frames
    scaling = MinMaxScaler()
    scaled = scaling.fit_transform(df)
    df_scaled = pd.DataFrame(scaled, columns=df.columns, index=df.index)

    # create an empty graph (figure)
    cases_figure = plt.Figure(figsize=(10, 10), dpi=100)
    cases_axis = cases_figure.add_subplot(111)

    # plot the cases vs. the dates
    cases_axis.plot(df_scaled['total_cases'], '*', label='Total Cases')

    xx = np.arange(0, 120, 10)
    x_dates = dates[xx]
    cases_axis.set_xticks(xx, np.all(x_dates))

    cases_axis.set_xlabel('Time', fontsize=14)
    cases_axis.set_title(chosen_country, fontsize=18)
    cases_axis.legend()
    cases_axis.grid()

    def transport_clicked():
        # show transport curve
        cases_axis.plot(df_scaled['Close public transport (OxBSG)'], 'o', label='Public Transport')

    def event_clicked():
        # show public events cancelation curve
        cases_axis.plot(df_scaled['Cancel public events (OxBSG)'], '1', label='Cancel public events')

    def travel_clicked():
        # show international travel curve curve
        cases_axis.plot(df_scaled['International travel controls (OxBSG)'], 'h', label='International Travel Controls')

    def workplace_clicked():
        # show workplace closure curve
        cases_axis.plot(df_scaled['Workplace Closures (OxBSG)'], 's', label='Workplace Closures')

    def gathering_clicked():
        # show restriction on gathering control's curve
        cases_axis.plot(df_scaled['Restrictions on gatherings (OxBSG)'], 'd', label='Restrictions on gatherings')

    def internal_movement_clicked():
        # show internal movement restriction curve
        cases_axis.plot(df_scaled['Restrictions on internal movement (OxBSG)'], 'x',
                        label='Restrictions on internal movement')

    def stay_home_clicked():
        # show stay at home curve
        cases_axis.plot(df_scaled['Stay at home requirements (OxBSG)'], 'D', label='Stay at home requirements')

    transport_button = Button(window, text="Public Transport", command=transport_clicked)
    transport_button.place(anchor=NW, rely=0.1)

    events_button = Button(window, text="Cancel public events", command=event_clicked)
    events_button.place(anchor=NW, rely=0.2)

    travel_button = Button(window, text="International Travel Controls", command=travel_clicked)
    travel_button.place(anchor=NW, rely=0.3)

    workplace_button = Button(window, text="Workplace Closures", command=workplace_clicked)
    workplace_button.place(anchor=NW, rely=0.4)

    gathering_button = Button(window, text="Cancel public events", command=gathering_clicked)
    gathering_button.place(anchor=NW, rely=0.5)

    internal_movement_button = Button(window, text="Restrictions on internal movement", command=internal_movement_clicked)
    internal_movement_button.place(anchor=NW, rely=0.6)

    stay_home_button = Button(window, text="Stay at home requirements", command=stay_home_clicked)
    stay_home_button.place(anchor=NW, rely=0.7)

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
