import os
from collections import defaultdict
import pandas as pd

DIRECTORY = r'caminho da pasta onde estão os arquivos'
SPREADSHEET_PATH = r'caminho onde deseja salvar o arquivo'
DATABASE_SPREADSHEET = 'database.xlsx'
SCHOOLS_DB = {}

excel_file = pd.ExcelFile(DATABASE_SPREADSHEET)
for sheet_name in excel_file.sheet_names:
    df = excel_file.parse(sheet_name, dtype={"school_code": int})
    schools_database = df.to_json(orient='records')
    with open(f'{sheet_name}.json', 'w', encoding='utf-8') as f:
        f.write(schools_database)
        print(f'Arquivo {sheet_name}.json gerado com sucesso!')

def list_file(directory_path):
    file_list = []
    for file in os.listdir(directory_path):
        if os.path.isfile(os.path.join(directory_path, file)):
            file_list.append(file)
    return file_list

def process_files(file_list, school_database):
    school_data = defaultdict(
        lambda:
        {
            "year": 2025,
            "pages": set(),
            "school_name": None,
            "promoter": None
        })

    for file in file_list:
        file_parts = file.split('.')[0].split('_')

        if len(file_parts) == 3:
            school_code, year, page = file_parts
            try:
                school_code = int(school_code)
            except ValueError:
                print(f'Código da escola inválido (não é um número): {school_code}')
                continue

            if school_code in school_database:
                school_data[school_code]["school_name"] = school_database[school_code]["school_name"]
                school_data[school_code]["promoter"] = school_database[school_code]["promoter"]
            else:
                print(f'Código da escola não encontrado no banco de dados: {school_code}')
                continue

            if year == '2025':
                school_data[school_code]["pages"].add(page)

    for school_code, info in school_data.items():
        info['pages'] = len(info['pages'])

    return school_data

def save_to_spreadsheet(school_data, output_path):
    data = []
    for school_code, info in school_data.items():
        data.append([
            int(school_code),
            info['school_name'],
            info['promoter'],
            info['year'],
            info['pages']
        ])
    df = pd.DataFrame(data, columns=["school_code", "school_name", "promoter", "year", "pages"])
    df.to_excel(output_path, index=False)

files = list_file(DIRECTORY)
df_schools = pd.read_json('db_schools.json')
schools_list = df_schools.to_dict(orient='records')
school_db = {int(school["school_code"]): school for school in schools_list}
school_data = process_files(files, school_db)
save_to_spreadsheet(school_data, SPREADSHEET_PATH)

print(f'relatório gerado em {SPREADSHEET_PATH}')
