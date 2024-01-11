import pandas as pd


def append_airport_code_data(city_cn: str, code3: str, code4: str, airport_name_cn: str, airport_name_en: str):
    # Load existing CSV file into a DataFrame
    file_path = 'airport_data.csv'
    df = pd.read_csv(file_path)

    # Create a new row of data as a dictionary
    new_data = {'城市名': city_cn,
                '机场三字码': code3,
                '机场四字码': code4,
                '机场名称': airport_name_cn,
                '英文名称': airport_name_en}

    df = df.append(new_data, ignore_index=True)

    # Save the updated DataFrame back to the CSV file
    df.to_csv(file_path, index=False)


if __name__ == '__main__':

    citycn = '信阳'
    code3 = 'XAI'
    code4 = 'ZHXY'
    airportname_cn = '信阳明港机场'
    airportname_en = 'Xinyang '
    append_airport_code_data(citycn, code3, code4, airportname_cn, airportname_en)
