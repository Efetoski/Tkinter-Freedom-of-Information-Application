# OGHARA EFETOBORE AKPOMEDAYE
# B1093078

# The GUI

from CovidFunctions import *
from StopnSearchFunctions import *
from functions import *


# COVID-19

def subwindow():
    new_window = Toplevel(my_window)
    new_window.geometry("1200x700")
    subpart = Label(new_window, text="Daily and Cummulative Number of Cases by Area", bg="blue", fg="white")
    subpart.grid(row=0, column=1)
    partition_5 = LabelFrame(new_window, bg="gray", padx=50, pady=20)
    partition_5.grid(row=1, column=0)

    L1 = Label(partition_5, text="Start Day:")
    L1.grid(row=0, column=0, sticky="w")
    L2 = Label(partition_5, text="Start Month:")
    L2.grid(row=1, column=0, pady=12, sticky="w")
    L3 = Label(partition_5, text="Start Year:")
    L3.grid(row=2, column=0, pady=12, sticky="w")
    L4 = Label(partition_5, text="End Day:")
    L4.grid(row=3, column=0, pady=12, sticky="w")
    L5 = Label(partition_5, text="End Month:")
    L5.grid(row=4, column=0, pady=12, sticky="w")
    L6 = Label(partition_5, text="End Year:")
    L6.grid(row=5, column=0, pady=12, sticky="w")
    L7 = Label(partition_5, text="AREA:")
    L7.grid(row=6, column=0, pady=12, sticky="w")

    B6 = Button(partition_5, text="BACK", command=new_window.destroy)
    B6.grid(row=7, column=0, pady=12, sticky="w")
    B7 = Button(partition_5, text="QUIT", command=new_window.destroy)
    B7.grid(row=8, column=0, pady=12, sticky="w")

    combo1 = ttk.Combobox(partition_5,
                          values=["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14",
                                  "15",
                                  "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29",
                                  "30"])
    combo1.grid(row=0, column=1)

    combo2 = ttk.Combobox(partition_5, values=["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"])
    combo2.grid(row=1, column=1)

    combo3 = ttk.Combobox(partition_5, values=["2019", "2020"])
    combo3.grid(row=2, column=1)

    combo4 = ttk.Combobox(partition_5,
                          values=["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14",
                                  "15",
                                  "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29",
                                  "30"])
    combo4.grid(row=3, column=1)

    combo5 = ttk.Combobox(partition_5, values=["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"])
    combo5.grid(row=4, column=1)

    combo6 = ttk.Combobox(partition_5, values=["2019", "2020"])
    combo6.grid(row=5, column=1)

    # collect the Areaname
    Area_Name = [i for i in df_covid["areaName"].unique()]
    combo7 = ttk.Combobox(partition_5, values=Area_Name)
    combo7.grid(row=6, column=1)

    partition_6 = Frame(new_window, bg="white", padx=50, pady=80)
    partition_6.grid(row=1, column=1)

    # Create a figure
    figure1 = plt.Figure(figsize=(10, 4), dpi=100)

    # Add a canvas
    canvas_1 = FigureCanvasTkAgg(figure1, partition_6)
    canvas_1.get_tk_widget().grid(row=0, column=0)

    # Collect the Values from the combobox and call the plot functions
    B8 = Button(partition_5, text="Daily Cases Query", command=lambda: total_cases_by_area(df_covid, combo3.get(),
                                                                                           combo2.get(), combo1.get(),
                                                                                           combo6.get(), combo5.get(),
                                                                                           combo4.get(), combo7.get(),
                                                                                           figure1, canvas_1))
    B8.grid(row=7, column=1, pady=12, sticky="w")

    B9 = Button(partition_5, text="Infection Rate Query", command=lambda: rolling_sum(df_covid, combo3.get(),
                                                                                      combo2.get(), combo1.get(),
                                                                                      combo6.get(), combo5.get(),
                                                                                      combo4.get(), combo7.get(),
                                                                                      figure1, canvas_1))
    B9.grid(row=8, column=1, pady=12, sticky="w")

    new_window.mainloop


def subwindow1():
    new_window_1 = Toplevel(my_window)
    new_window_1.geometry("1200x700")
    subpart1 = Label(new_window_1, text="Compare Between two Areas", bg="blue", fg="white")
    subpart1.grid(row=0, column=1)
    partition_7 = LabelFrame(new_window_1, bg="gray", padx=50, pady=20)
    partition_7.grid(row=1, column=0)

    L8 = Label(partition_7, text="Start Day:")
    L8.grid(row=0, column=0, sticky="w")
    L9 = Label(partition_7, text="Start Month:")
    L9.grid(row=1, column=0, pady=12, sticky="w")
    L10 = Label(partition_7, text="Start Year:")
    L10.grid(row=2, column=0, pady=12, sticky="w")
    L11 = Label(partition_7, text="End Day:")
    L11.grid(row=3, column=0, pady=12, sticky="w")
    L12 = Label(partition_7, text="End Month:")
    L12.grid(row=4, column=0, pady=12, sticky="w")
    L13 = Label(partition_7, text="End Year:")
    L13.grid(row=5, column=0, pady=12, sticky="w")
    L14 = Label(partition_7, text="AREA1:")
    L14.grid(row=6, column=0, pady=12, sticky="w")
    L15 = Label(partition_7, text="AREA2:")
    L15.grid(row=7, column=0, pady=12, sticky="w")

    B10 = Button(partition_7, text="BACK", command=new_window_1.destroy)
    B10.grid(row=8, column=0, pady=12, sticky="w")
    B11 = Button(partition_7, text="QUIT", command=new_window_1.destroy)
    B11.grid(row=9, column=0, pady=12, sticky="w")
    B12 = Button(partition_7, text="Compare Daily Cases")
    B12.grid(row=8, column=1, pady=12, sticky="w")
    B13 = Button(partition_7, text="Compare by Age")
    B13.grid(row=9, column=1, pady=12, sticky="w")

    combo8 = ttk.Combobox(partition_7,
                          values=["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14",
                                  "15",
                                  "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29",
                                  "30"])
    combo8.grid(row=0, column=1)
    combo9 = ttk.Combobox(partition_7, values=["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"])
    combo9.grid(row=1, column=1)
    combo10 = ttk.Combobox(partition_7, values=["2019", "2020"])
    combo10.grid(row=2, column=1)
    combo11 = ttk.Combobox(partition_7,
                           values=["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14",
                                   "15",
                                   "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29",
                                   "30"])
    combo11.grid(row=3, column=1)
    combo12 = ttk.Combobox(partition_7, values=["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"])
    combo12.grid(row=4, column=1)
    combo13 = ttk.Combobox(partition_7, values=["2019", "2020"])

    Area_Name = [i for i in df_covid["areaName"].unique()]
    combo13.grid(row=5, column=1)
    combo14 = ttk.Combobox(partition_7, values=Area_Name)
    combo14.grid(row=6, column=1)
    combo15 = ttk.Combobox(partition_7, values=Area_Name)
    combo15.grid(row=7, column=1)

    partition_8 = Frame(new_window_1, bg="white", padx=50, pady=80)
    partition_8.grid(row=1, column=1)

    # Create a figure
    figure1 = plt.Figure(figsize=(10, 4), dpi=100)

    # Add a canvas
    canvas_1 = FigureCanvasTkAgg(figure1, partition_8)
    canvas_1.get_tk_widget().grid(row=0, column=0)

    B12 = Button(partition_7, text="Compare Daily Cases",
                 command=lambda: compare_areas(df_covid, combo10.get(), combo9.get(),
                                               combo8.get(), combo13.get(),
                                               combo12.get(), combo11.get(),
                                               combo14.get(), combo15.get(),
                                               figure1, canvas_1))
    B12.grid(row=8, column=1, pady=12, sticky="w")
    B13 = Button(partition_7, text="Compare by Age")
    B13.grid(row=9, column=1, pady=12, sticky="w")

    new_window_1.mainloop


def subwindow2():
    new_window_2 = Toplevel(my_window)
    new_window_2.geometry("1200x700")
    subpart2 = Label(new_window_2, text="Covid Information", bg="blue", fg="white")
    subpart2.grid(row=0, column=1)
    partition_9 = LabelFrame(new_window_2, bg="gray", padx=50, pady=20)
    partition_9.grid(row=1, column=0)

    L16 = Label(partition_9, text="Start Day:")
    L16.grid(row=0, column=0, sticky="w")
    L17 = Label(partition_9, text="Start Month:")
    L17.grid(row=1, column=0, pady=12, sticky="w")
    L18 = Label(partition_9, text="Start Year:")
    L18.grid(row=2, column=0, pady=12, sticky="w")
    L19 = Label(partition_9, text="End Day:")
    L19.grid(row=3, column=0, pady=12, sticky="w")
    L20 = Label(partition_9, text="End Month:")
    L20.grid(row=4, column=0, pady=12, sticky="w")
    L21 = Label(partition_9, text="End Year:")
    L21.grid(row=5, column=0, pady=12, sticky="w")

    B14 = Button(partition_9, text="Back", command=new_window_2.destroy)
    B14.grid(row=7, column=0, pady=12, sticky="w")
    B15 = Button(partition_9, text="QUIT", command=new_window_2.destroy)
    B15.grid(row=8, column=0, pady=12, sticky="w")

    combo16 = ttk.Combobox(partition_9,
                           values=["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14",
                                   "15",
                                   "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29",
                                   "30"])
    combo16.grid(row=0, column=1)
    combo17 = ttk.Combobox(partition_9, values=["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"])
    combo17.grid(row=1, column=1)
    combo18 = ttk.Combobox(partition_9, values=["2019", "2020"])
    combo18.grid(row=2, column=1)
    combo19 = ttk.Combobox(partition_9,
                           values=["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14",
                                   "15",
                                   "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29",
                                   "30"])
    combo19.grid(row=3, column=1)
    combo20 = ttk.Combobox(partition_9, values=["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"])
    combo20.grid(row=4, column=1)
    combo21 = ttk.Combobox(partition_9, values=["2019", "2020"])
    combo21.grid(row=5, column=1)

    partition_10 = Frame(new_window_2, bg="white", padx=50, pady=80)
    partition_10.grid(row=1, column=1, sticky="nsew")
    # Create a figure
    figure1 = plt.Figure(figsize=(10, 4), dpi=100)

    # Add a canvas
    canvas_1 = FigureCanvasTkAgg(figure1, partition_10)
    canvas_1.get_tk_widget().grid(row=0, column=0)

    B16 = Button(partition_9, text="Region Query",
                 command=lambda: highest_5(df_covid, combo18.get(), combo17.get(), combo16.get(),
                                           combo21.get(), combo20.get(), combo19.get(),
                                           'region', figure1, canvas_1))
    B16.grid(row=7, column=1, pady=12, sticky="w")
    B17 = Button(partition_9, text="Top 5 UTLA Query",
                 command=lambda: highest_5(df_covid, combo18.get(), combo17.get(), combo16.get(),
                                           combo21.get(), combo20.get(), combo19.get(),
                                           'utla', figure1, canvas_1))
    B17.grid(row=8, column=1, pady=12, sticky="w")
    B18 = Button(partition_9, text="Top 5 ITLA Query",
                 command=lambda: highest_5(df_covid, combo18.get(), combo17.get(), combo16.get(),
                                           combo21.get(), combo20.get(), combo19.get(),
                                           'ltla', figure1, canvas_1))
    B18.grid(row=9, column=1, pady=12, sticky="w")
    B19 = Button(partition_9, text="Daily Cases in the UK",
                 command=lambda: total_cases(df_covid, combo18.get(), combo17.get(), combo16.get(),
                                             combo21.get(), combo20.get(), combo19.get(),
                                             figure1, canvas_1))
    B19.grid(row=10, column=1, pady=12, sticky="w")

    new_window_2.mainloop


# STOP and SEARCH

def subwindow3():
    new_window_3 = Toplevel(my_window)
    new_window_3.geometry("1200x700")
    subpart1 = Label(new_window_3,
                     text="Stop and Search for a Period of Time\n Please choose a period between 12/2019 and 11/2020",
                     bg="blue", fg="white")
    subpart1.grid(row=0, column=1)
    partition_11 = LabelFrame(new_window_3, bg="gray", padx=50, pady=20)
    partition_11.grid(row=1, column=0)

    L16 = Label(partition_11, text="Start Month:")
    L16.grid(row=0, column=0, sticky="w")
    L17 = Label(partition_11, text="Start Year:")
    L17.grid(row=1, column=0, pady=12, sticky="w")
    L18 = Label(partition_11, text="End Month:")
    L18.grid(row=2, column=0, pady=12, sticky="w")
    L19 = Label(partition_11, text="End Year:")
    L19.grid(row=3, column=0, pady=12, sticky="w")
    L20 = Label(partition_11, text="Police Force:")
    L20.grid(row=4, column=0, pady=12, sticky="w")

    B20 = Button(partition_11, text="Back", command=new_window_3.destroy)
    B20.grid(row=7, column=0, pady=12, sticky="w")
    B21 = Button(partition_11, text="QUIT", command=new_window_3.destroy)
    B21.grid(row=8, column=0, pady=12, sticky="w")

    combo22 = ttk.Combobox(partition_11,
                           values=["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14",
                                   "15",
                                   "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29",
                                   "30", "31"])
    combo22.grid(row=0, column=1)
    combo23 = ttk.Combobox(partition_11, values=["2019", "2020"])
    combo23.grid(row=1, column=1)
    combo24 = ttk.Combobox(partition_11,
                           values=["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14",
                                   "15",
                                   "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29",
                                   "30", "31"])
    combo24.grid(row=2, column=1)
    combo25 = ttk.Combobox(partition_11, values=["2019", "2020"])
    combo25.grid(row=3, column=1)
    cities = {"Bedfordshire": "bedfordshire", "City of London": "city-of-london", "Kent": "kent",
              "British Transport": "british-transport", "Cleveland": "cleveland", "Derbyshire": "derbyshire",
              "Essex": "essex", "Sussex": "sussex", "Suffolk": "suffolk", "Durham": "durham", "Hampshire": "hampshire",
              "Hertfordshire":"hertfordhsire","Northumbria": "northumbria", "North-Wales": "north-wales",
              "Cumbria": "cumbria", "Wiltshire": "wiltshire", "Norfolk": "norfolk", "Lancashire": "lancashire"}
    combo26 = ttk.Combobox(partition_11, values=list(cities.keys()))
    combo26.grid(row=4, column=1)

    B22 = Button(partition_11, text="Query",
                 command=lambda: period_query(combo22.get(), combo23.get(), combo24.get(), combo25.get(),
                                              cities[combo26.get()], figure1, canvas_1))
    B22.grid(row=7, column=1, pady=12, sticky="w")

    partition_12 = Frame(new_window_3, bg="white", padx=50, pady=80)
    partition_12.grid(row=1, column=1)

    figure1 = plt.Figure(figsize=(8, 5), dpi=100)

    canvas_1 = FigureCanvasTkAgg(figure1, partition_12)
    canvas_1.get_tk_widget().grid(row=0, column=0)

    new_window_3.mainloop


def subwindow4():
    new_window_4 = Toplevel(my_window)
    new_window_4.geometry("1200x700")
    subpart3 = Label(new_window_4, text="Stop and Search by Month\n Please choose a period between 12/2019 and 11/2020",
                     bg="blue", fg="white")
    subpart3.grid(row=0, column=1)
    partition_12 = LabelFrame(new_window_4, bg="gray", padx=50, pady=20)
    partition_12.grid(row=1, column=0)

    L17 = Label(partition_12, text="Start Month:")
    L17.grid(row=0, column=0, sticky="w")
    L18 = Label(partition_12, text="Start Year:")
    L18.grid(row=1, column=0, pady=12, sticky="w")
    L19 = Label(partition_12, text="Cities")
    L19.grid(row=2, column=0, pady=12, sticky="w")

    B23 = Button(partition_12, text="Back", command=new_window_4.destroy)
    B23.grid(row=7, column=0, pady=12, sticky="w")
    B24 = Button(partition_12, text="QUIT", command=new_window_4.destroy)
    B24.grid(row=8, column=0, pady=12, sticky="w")

    combo27 = ttk.Combobox(partition_12,
                           values=["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14",
                                   "15",
                                   "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29",
                                   "30", "31"])
    combo27.grid(row=0, column=1)
    combo28 = ttk.Combobox(partition_12, values=["2019", "2020"])
    combo28.grid(row=1, column=1)
    cities = {"Bedfordshire": "bedfordshire", "City of London": "city-of-london", "Kent": "kent",
              "British Transport": "british-transport", "Cleveland": "cleveland", "Derbyshire": "derbyshire",
              "Essex": "essex", "Sussex": "sussex", "Suffolk": "suffolk", "Durham": "durham", "Hampshire": "hampshire",
              "Hertfordshire":"hertfordhsire","Northumbria": "northumbria", "North-Wales": "north-wales",
              "Cumbria": "cumbria", "Wiltshire": "wiltshire", "Norfolk": "norfolk", "Lancashire": "lancashire"}
    combo29 = ttk.Combobox(partition_12, values=list(cities.keys()))
    combo29.grid(row=2, column=1)
    B25 = Button(partition_12, text="Age Query",
                 command=lambda: age_query(combo27.get(), combo28.get(), cities[combo29.get()], figure1, canvas_1))

    B25.grid(row=7, column=1, pady=12, sticky="w")
    B26 = Button(partition_12, text="Gender Query",
                 command=lambda: gender_query(combo27.get(), combo28.get(), cities[combo29.get()], figure1, canvas_1))

    B26.grid(row=8, column=1, pady=12, sticky="w")
    B27 = Button(partition_12, text="Ethnicity Query",
                 command=lambda: ethnicity_query(combo27.get(), combo28.get(), cities[combo29.get()], figure1,
                                                 canvas_1))
    B27.grid(row=9, column=1, pady=12, sticky="w")
    B28 = Button(partition_12, text="Stop Purpose Query",
                 command=lambda: purpose_query(combo27.get(), combo28.get(), cities[combo29.get()], figure1, canvas_1))
    B28.grid(row=10, column=1, pady=12, sticky="w")
    B29 = Button(partition_12, text="Result Outcome Query",
                 command=lambda: outcome_query(combo27.get(), combo28.get(), cities[combo29.get()], figure1, canvas_1))
    B29.grid(row=11, column=1, pady=12, sticky="w")

    partition_13 = LabelFrame(new_window_4, bg="white", padx=50, pady=20)
    partition_13.grid(row=1, column=1)
    figure1 = plt.Figure(figsize=(8, 5), dpi=100)

    canvas_1 = FigureCanvasTkAgg(figure1, partition_13)
    canvas_1.get_tk_widget().grid(row=0, column=0)

    new_window_4.mainloop


my_window = Tk()
"""Re-enable the picture later"""
image = Image.open("TeessideUniLogo.jpg")
photo = ImageTk.PhotoImage(image)
my_window.title("STUDENT ID: B1093078")

partition_1 = Label(my_window, text="Welcome to Freedom of Information System \n Please choose a type of query",
                    bg="blue", fg="white")

partition_1.grid(row=0, column=1)

partition_2 = LabelFrame(my_window, text="STOP & SEARCH", padx=50, pady=60, highlightbackground="blue", highlightthicknes=5)
partition_2.grid(row=1, column=0)
B1 = Button(partition_2, text="Stop and Search in Period", command=subwindow3)
B1.grid(row=0, column=0)
B2 = Button(partition_2, text="Stop and Search by Month", command=subwindow4)
B2.grid(row=1, column=0, pady=20)

imageLabel = Label(my_window, image=photo)
imageLabel.image = photo
imageLabel.grid(row=1, column=1, rowspan=4, pady=4)

partition_3 = LabelFrame(my_window, text="COVID-19 CONFIRMED CASES", padx=15, pady=40, highlightbackground="blue", highlightthicknes=5)
partition_3.grid(row=1, column=2)
B3 = Button(partition_3, text="Daily and Cummulative Number of Cases by Area", command=subwindow)
B3.grid(row=0, column=0)
B4 = Button(partition_3, text="Compare between two Area", command=subwindow1)
B4.grid(row=1, column=0, pady=20)
B5 = Button(partition_3, text="Covid General Information for a given Period", command=subwindow2)
B5.grid(row=2, column=0, pady=2)

partition_4 = Button(my_window, text="Quit", command=my_window.destroy, padx=100, border=2, bg="blue", fg="white")
partition_4.grid(row=2, column=1, rowspan=8, pady=4)

my_window.mainloop()
