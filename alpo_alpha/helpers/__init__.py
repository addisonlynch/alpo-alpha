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
    if "3 UNIT PLAY" not in df.columns:
        raise Exception(
            "'3 UNIT PLAY' column not found. Ensure column is spelled and capitalized correctly."
        )

    if "2 UNIT PLAY" not in df.columns:
        raise Exception(
            "'2 UNIT PLAY' column not found. Ensure column is spelled and capitalized correctly."
        )

    if "1 UNIT PLAY" not in df.columns:
        raise Exception(
            "'1 UNIT PLAY' column not found. Ensure column is spelled and capitalized correctly."
        )


def validate_results_fmt(df: pd.DataFrame) -> None:

    # Ensure that the columns are correct
    if df.columns[0] != "Play":
        raise Exception("Invalid results file format. First column must be 'Play'.")

    if df.columns[1] != "Result":
        raise Exception("Invalid results file format. Second column must be 'Result'.")

    # Ensure that all results are valid entries
    for result in df["Result"]:
        if result.lower() not in ("win", "lose", "push"):
            raise Exception(
                "Invalid results file format. All results must be 'win', 'lose', or 'push'"
            )

    # Ensure that there are no duplicate results
    if df.duplicated(subset=["Play"]).any():
        raise Exception(
            "Invalid results file format. One or more plays appear more than once."
        )


def parse_choice_string(choice_str: str) -> str:

    if len(choice_str) == 0:
        raise ValueError("Empty choice_str received.")

    return choice_str.rstrip("*")[choice_str.rfind("(") + 1 : -1]


def process_results(series: str, weight: float, results: pd.DataFrame) -> float:
    results.set_index(results["Play"], inplace=True)
    result = results.loc[series, "Result"].lower()

    if result == "lose":
        return -weight
    elif result == "push":
        return float(0)
    elif result == "win":
        return odds_to_decimal(parse_choice_string(series))
    else:
        raise Exception("Invalid results file format.")


def validate_results(picks: pd.DataFrame, results: pd.DataFrame) -> None:
    missing_in_entries = []
    missing_in_results = []

    for play in picks:
        if play not in results["Play"].tolist():
            missing_in_results.append(play)

    for play in results["Play"]:
        if play not in picks and play not in missing_in_entries:
            missing_in_entries.append(play)

    ERROR_MSG = "WARNING: Mismatch between spreadsheet and results file.\n\n"

    if missing_in_entries:
        ERROR_MSG += " Values missing in picks spreadsheet: {}\n\n".format(
            ", ".join(missing_in_entries)
        )
        if missing_in_results:
            ERROR_MSG += " Values missing in results: {}".format(
                ", ".join(missing_in_results)
            )

        raise Exception(ERROR_MSG)
