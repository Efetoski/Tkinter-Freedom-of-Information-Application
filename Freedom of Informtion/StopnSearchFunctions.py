# OGHARA EFETOBORE AKPOMEDAYE
# B1093078

from functions import *

# define an auxiliary function that will help in generating the dataframes
def generate_df(month, year, force):
    """ auxiliary function that helps to generate the main dataframes from the api url"""
    # use requests_cache so as to help with retention of data in event of network failure
    requests_cache.install_cache('uk_police_cache', expire_after=180)
    data = json.loads(requests.get(
        "https://data.police.uk/api/stops-force?force=" + force + "&date=" + str(year) + "-" + str(month)).text)

    # flattening json data
    df_force = pd.json_normalize(data)
    df_force.sort_values(by="datetime", inplace=True, ascending=True)
    df_force['force'] = str(force)
    df_force["year_month"] = df_force["datetime"].str[:7]

    return df_force


# create a function that gets all the dataframes for an area (for the 12months), then concats them into one dataframe
def generate_gen_df(year1, year2, force):
    """aux function that concats all the dataframes for each month for an area into one dataframe"""
    year1 = int(year1)
    year2 = int(year2)
    month_list = [i for i in range(1, 13)]
    list_of_dfs = []
    dict_of_dfs = {}
    for index in range(len(month_list)):
        if (index == 0):
            var = str("df" + str(index))
            dict_of_dfs[var] = generate_df(month_list[index], year1, force)

        else:
            var = str("df" + str(index))
            dict_of_dfs[var] = generate_df(month_list[index], year1, force)

            list_of_dfs = [values for key, values in dict_of_dfs.items()]
            list_of_dfs[0] = pd.concat((list_of_dfs[0], list_of_dfs[index]), axis=0, ignore_index=True)
    # assign the concatenated dataframe to df_force
    df_force = list_of_dfs[0]

    for index in range(len(month_list)):
        list_of_dfs[index] = generate_df(month_list[index], year2, force)
        df_force = pd.concat((df_force, list_of_dfs[index]), axis=0, ignore_index=True)
    return df_force


# This function is ready for The GUI
def age_query(month, year, force, fig, canvas):
    """
    This function plots for the Stop and Search Age Distribution per Month per Police force department

    month: The month to be queried
    year: The year to be queried
    force: The force department
    fig: The Fig Created in the GUI
    canvas: The Canvas on the GUI

    """

    df = generate_df(month, year, force)

    name_force = str(force)

    # clear the area and plot again
    fig.clear()

    # create and axis
    ax_3 = fig.add_subplot(111)

    # ax_3.xaxis.set_major_locator(MaxNLocator(11))
    # ax_3.set(title= "Age Distribution for " + str(name_force) + " Stop and Search Activities in " + month_name[int(month)]  + " "+str(year) )

    fig.tight_layout()

    sns.countplot(df["age_range"], hue=df["gender"], palette="rocket", ax=ax_3)

    canvas.draw()


def gender_query(month, year, force, fig, canvas):
    df = generate_df(month, year, force)

    # name_force = forces_names[force]
    # clear the area and plot again
    fig.clear()

    # create and axis
    ax_3 = fig.add_subplot(111)

    # ax_3.xaxis.set_major_locator(MaxNLocator(11))
    # ax_3.set(title= "Gender Distribution for " + str(name_force) + " Stop and Search Activities in " + str(month) + " "+str(year) )
    plt.rcParams['font.size'] = '9'
    fig.tight_layout()

    # create chart
    sns.countplot(df["gender"], palette="rocket", ax=ax_3)

    canvas.draw()


def purpose_query(month, year, force, fig, canvas):
    df = generate_df(month, year, force)

    # name_force = forces_names[force]
    # clear the area and plot again
    fig.clear()

    # create and axis
    ax_3 = fig.add_subplot(111)

    # ax_3.xaxis.set_major_locator(MaxNLocator(11))
    # ax_3.set(title= "Purpose for Stop and Search Purpose by " + str(name_force) + " in " + str(month)  + " "+str(year) )

    fig.tight_layout()

    sns.countplot(y="object_of_search", hue="gender", data=df, ax=ax_3)
    # sns.catplot(y="object_of_search", color = "purple", kind = "count", col = "gender", data = df)

    canvas.draw()


def outcome_query(month, year, force, fig, canvas):
    df = generate_df(month, year, force)

    # name_force = forces_names[force]
    # clear the area and plot again
    fig.clear()

    # create and axis
    ax_3 = fig.add_subplot(111)

    # ax_3.xaxis.set_major_locator(MaxNLocator(11))
    # ax_3.set(title= "Purpose for Stop and Search Purpose by " + str(name_force) + " in " + str(month)  + " "+str(year) )

    fig.tight_layout()

    sns.countplot(y="outcome", hue="gender", data=df, ax=ax_3)
    # sns.catplot(y="outcome", color = "green", kind = "count", col = "gender", data = df)

    canvas.draw()
    # plt.show()


def ethnicity_query(month, year, force, fig, canvas):
    df = generate_df(month, year, force)

    # name_force = forces_names[force]
    # clear the area and plot again
    fig.clear()

    # create and axis
    ax_3 = fig.add_subplot(111)

    # ax_3.xaxis.set_major_locator(MaxNLocator(11))
    # ax_3.set(title= "Purpose for Stop and Search Purpose by " + str(name_force) + " in " + str(month)  + " "+str(year) )

    fig.tight_layout()

    sns.countplot(y="self_defined_ethnicity", hue="gender", data=df, ax=ax_3)
    # sns.catplot(y="outcome", color = "green", kind = "count", col = "gender", data = df)

    canvas.draw()


def period_query(s_month, s_year, e_month, e_year, force, fig, canvas):
    df = generate_gen_df(s_year, e_year, force)

    datestart = str(str(s_year) + "-" + str(s_month))

    dateend = str(str(e_year) + "-" + str(e_month))

    df_n = df.loc[(df["year_month"] >= str(datestart)) & (df["year_month"] <= str(dateend))]

    # name_force = forces_names[force]
    # clear the area and plot again
    fig.clear()

    # create and axis
    ax_3 = fig.add_subplot(111)

    # ax_3.xaxis.set_major_locator(MaxNLocator(11))
    # ax_3.set(title= "Purpose for Stop and Search Purpose by " + str(force) + " between " + str((s_month)  + " "+str(s_year) + " and " + (s_month)  + " " +str(e_year)) )

    fig.tight_layout()

    sns.countplot("gender", data=df_n, ax=ax_3)
    # sns.catplot(y="outcome", color = "green", kind = "count", col = "gender", data = df)
    # sns.factorplot("year_month", color = "red", kind="count", col = "gender", data = df_2)
    ax_3.set_xticklabels(ax_3.get_xticklabels(), rotation=90)

    canvas.draw()

