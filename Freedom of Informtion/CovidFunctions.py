# OGHARA EFETOBORE AKPOMEDAYE
# B1093078

from functions import *


df_covid = pd.read_csv( os.path.join(main_dir,'specimenDate_ageDemographic-unstacked.csv'), parse_dates=['date'])
df_covid.head()

df_covid["Total_Daily_Cases"]= df_covid["newCasesBySpecimenDate-0_59"] + df_covid["newCasesBySpecimenDate-60+"] + df_covid["newCasesBySpecimenDate-unassigned"]
df_covid["Rolling_Sum"]= df_covid["newCasesBySpecimenDateRollingSum-0_59"] + df_covid["newCasesBySpecimenDate-60+"] + df_covid["newCasesBySpecimenDateRollingSum-unassigned"]


# Covid Plot Functions

def date_filter(df, s_year, s_month, s_day, e_year, e_month, e_day):
    """
    df: Dataframe
    s_year: Start Year
    s_month: Start Month
    s_day: Start Day
    e_year: End Year
    e_month: End Month
    e_day: End Day

    """
    s_y = int(s_year)
    s_m = int(s_month)
    s_d = int(s_day)
    e_y = int(e_year)
    e_m = int(e_month)
    e_d = int(e_day)

    filtered_df = df.loc[
        (df['date'] >= str(datetime.date(s_y, s_m, s_d))) & (df['date'] < str(datetime.date(e_y, e_m, e_d)))]

    return filtered_df


def groupby2(df, col1, col2, dur, fig, canvas):
    """
    This function takes the dataframe
    col1 = The column to plot
    Col2 = The column to groupby
    dur = The Interval to plot with e.g("M", "W", "D")
    fig = The figure create for the canvas on the GUI
    canvas = The canvas created on the GUI

    """
    # clear the area and plot again
    fig.clear()

    # create and axis
    ax_2 = fig.add_subplot(111)

    # sum the rows on the dataframe
    pf = df[col1].groupby(df[col2].dt.to_period(str(dur))).sum()

    # plot the graph
    pf.plot(kind='bar', ax=ax_2)
    plt.locator_params(axis='x', nbins=12)
    canvas.draw()
    return


# Total Cases (for general covid plotting)
def total_cases(df, s_year, s_month, s_day, e_year, e_month, e_day, fig, canvas):
    """
    df: Dataframe
    s_year: Start Year
    s_month: Start Month
    s_day: Start Day
    e_year: End Year
    e_month: End Month
    e_day: End Day
    fig: Figure created on the GUI
    canvas: Canvas created on the GUI

    """
    # use the date filter function to slice the dataframe by dates
    filtered_df = pd.DataFrame(date_filter(df, s_year, s_month, s_day, e_year, e_month, e_day))

    # use the groupby function to plot with dates
    groupby2(filtered_df, "Total_Daily_Cases", "date", "D", fig, canvas)


# for specific area
def total_cases_by_area(df, s_year, s_month, s_day, e_year, e_month, e_day, area, fig, canvas):
    """
    df: Dataframe
    s_year: Start Year
    s_month: Start Month
    s_day: Start Day
    e_year: End Year
    e_month: End Month
    e_day: End Day
    fig: Figure created on the GUI
    canvas: Canvas created on the GUI

    """

    df1 = df[df['areaName'] == str(area)].copy()
    # use the date filter function to slice the dataframe by dates
    filtered_df = pd.DataFrame(date_filter(df1, s_year, s_month, s_day, e_year, e_month, e_day))

    # use the groupby function to plot with dates
    groupby2(filtered_df, "Total_Daily_Cases", "date", "D", fig, canvas)


# Rolling Sum
def rolling_sum(df, s_year, s_month, s_day, e_year, e_month, e_day, area, fig, canvas):
    """
    df: Dataframe
    s_year: Start Year
    s_month: Start Month
    s_day: Start Day
    e_year: End Year
    e_month: End Month
    e_day: End Day
    fig: Figure created on the GUI
    canvas: Canvas created on the GUI

    """

    df1 = df[df['areaName'] == str(area)].copy()
    # use the date filter function to slice the dataframe by dates
    filtered_df = pd.DataFrame(date_filter(df1, s_year, s_month, s_day, e_year, e_month, e_day))

    # use the groupby function to plot with dates
    groupby2(filtered_df, "Rolling_Sum", "date", "D", fig, canvas)


# function to comapre 2 areas
def compare_areas(df, s_year, s_month, s_day, e_year, e_month, e_day, area1, area2, fig, canvas):
    """
    df: Dataframe
    area1: The first one
    area2: The second one
    """
    """
    #for date filtering
    s_year: Start Year
    s_month: Start Month
    s_day: Start Day
    e_year: End Year
    e_month: End Month
    e_day: End Day
    fig: Figure created on the GUI
    canvas: Canvas created on the GUI

    """

    filtered_df = pd.DataFrame(date_filter(df, s_year, s_month, s_day, e_year, e_month, e_day))

    df1 = filtered_df[filtered_df["areaName"] == str(area1)].copy()
    df2 = filtered_df[filtered_df["areaName"] == str(area2)].copy()

    df1 = pd.DataFrame(df1, columns=["date", "areaName", "Total_Daily_Cases"])
    df2 = pd.DataFrame(df2, columns=["date", "areaName", "Total_Daily_Cases"])

    df1['key'] = df1["areaName"].unique()[0]
    df2['key'] = df2["areaName"].unique()[0]

    DF = pd.concat([df1, df2], keys=['Area1', 'Area2'])

    DFGroup = DF.groupby([DF['date'].dt.to_period("D"), "key"])

    # clear the canvas
    fig.clear()

    # create and axis
    ax_2 = fig.add_subplot(111)

    DFGPlot = DFGroup.sum().unstack('key').plot(kind='bar', ax=ax_2)

    # ax_2.locator_params(axis='x', nbins=12)
    canvas.draw()


# function for highest area by regions
def highest_5(df, s_year, s_month, s_day, e_year, e_month, e_day, areatype, fig, canvas):
    """
    #for date filtering
    s_year: Start Year
    s_month: Start Month
    s_day: Start Day
    e_year: End Year
    e_month: End Month
    e_day: End Day
    """
    """
    areaType: ("ltla","utla","region")
    fig: Figure created on the GUI
    canvas: Canvas created on the GUI

    """

    # use the date filter function to slice the dataframe by dates
    filtered_df = pd.DataFrame(date_filter(df, s_year, s_month, s_day, e_year, e_month, e_day))

    df_region = filtered_df[filtered_df["areaType"] == str(areatype)].copy()

    # clear the canvas
    fig.clear()

    # create and axis
    ax_2 = fig.add_subplot(111)

    # group the dataframe by areaName (Sample 3 columns to compare on and sum them)
    DFGroup = df_region.groupby('areaName')[
        'Total_Daily_Cases', 'newCasesBySpecimenDate-0_59', 'newCasesBySpecimenDate-60+'].sum()

    # sort the dataframe to get the highest at the top and pick the top 5 then plot it
    DFGroup.sort_values('Total_Daily_Cases', ascending=False).tail(10).plot(kind='bar',
                                                                            color=['blue', 'green', 'red'], ax=ax_2)
    plt.xlabel('AreaName')
    plt.ylabel('Total_Daily_Cases')
    plt.title('5 Areas With The Lowest Cases and Their Age_Distribution')
    plt.tight_layout()
    canvas.draw()


