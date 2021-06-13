import pandas as pd


def odds_to_decimal(odds_str: str) -> float:

    if len(odds_str) == 0:
        raise ValueError("Empty odds_str received.")

    plusminus = odds_str[0]

    if plusminus == "+":
        decimal = int(odds_str[1:]) / 100
    elif plusminus == "-":
        decimal = 100 / int(odds_str[1:])
    else:
        raise ValueError("Invalid odds_str format received")

    # Cast to float in case +100
    return round(float(decimal), 2)


def validate_picks_fmt(df: pd.DataFrame) -> None:
    # Ensure the column names are spelled correctly
    if "3 Unit Pick" not in df.columns:
        raise Exception(
            "'3 Unit Pick' column not found. Ensure column is spelled and capitalized correctly."
        )

    if "2 Unit Pick" not in df.columns:
        raise Exception(
            "'2 Unit Pick' column not found. Ensure column is spelled and capitalized correctly."
        )

    if "1 Unit Pick" not in df.columns:
        raise Exception(
            "'1 Unit Pick' column not found. Ensure column is spelled and capitalized correctly."
        )


def validate_results_fmt(df: pd.DataFrame) -> None:

    # Ensure that the columns are correct
    if df.columns[0] != "Pick":
        raise Exception("Invalid results file format. First column must be 'Pick'.")

    if df.columns[1] != "Result":
        raise Exception("Invalid results file format. Second column must be 'Result'.")

    # Ensure that all results are valid entries
    for result in df["Result"]:
        if result.lower() not in ("win", "lose", "push"):
            raise Exception(
                "Invalid results file format. All results must be 'win', 'lose', or 'push'"
            )

    # Ensure that there are no duplicate results
    if df.duplicated(subset=["Pick"]).any():
        raise Exception(
            "Invalid results file format. One or more Picks appear more than once."
        )


def parse_choice_string(choice_str: str) -> str:

    if len(choice_str) == 0:
        raise ValueError("Empty choice_str received.")

    return choice_str.rstrip("*")[choice_str.rfind("(") + 1 : -1]


def process_results(series: str, weight: float, results: pd.DataFrame) -> float:
    results.set_index(results["Pick"], inplace=True)
    result = results.loc[series, "Result"].lower()

    if result == "lose":
        return -weight
    elif result == "push":
        return float(0)
    elif result == "win":
        return odds_to_decimal(parse_choice_string(series)) + weight
    else:
        raise Exception("Invalid results file format.")


def validate_results(picks: list, results: pd.DataFrame) -> None:
    missing_in_results = []

    for Pick in picks:
        if Pick not in results["Pick"].tolist():
            missing_in_results.append(Pick)

    ERROR_MSG = "ERROR: Picks were made in the Google Forms spreadsheet which do not appear in the results spreadsheet. See below for missing picks:\n\n"

    if missing_in_results:
        ERROR_MSG += "{}\n".format(", ".join(missing_in_results))
        raise Exception(ERROR_MSG)


# REWROTE BECAUSE WE DON'T NEED TO WORRY ABOUT RESULTS NOT IN THE PICKS

# def validate_results(picks: list, results: pd.DataFrame) -> None:
#     missing_in_entries = []
#     missing_in_results = []

#     for Pick in picks:
#         if Pick not in results["Pick"].tolist():
#             missing_in_results.append(Pick)

#     for Pick in results["Pick"]:
#         if Pick not in picks and Pick not in missing_in_entries:
#             missing_in_entries.append(Pick)

#     ENTRIES_ERROR_MSG = ""
#     RESULTS_ERROR_MSG = ""
#     ERRORS = False
#     ERROR_MSG = "WARNING: Mismatch between spreadsheet and results file.\n\n"

#     if missing_in_entries:
#         ENTRIES_ERROR_MSG = "Values missing in picks spreadsheet: {}\n\n".format(
#             ", ".join(missing_in_entries)
#         )
#         ERRORS = True
#     if missing_in_results:
#         RESULTS_ERROR_MSG = "Values missing in results: {}".format(
#             ", ".join(missing_in_results)
#         )
#         ERRORS = True

#     if ERRORS:
#         raise Exception(ERROR_MSG + ENTRIES_ERROR_MSG + RESULTS_ERROR_MSG)
