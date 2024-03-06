from db import DB


def delete_content(table_name):
    with DB() as db:
        db.execute(f'''
                    DELETE FROM {table_name}
        ''')
    print(f"Deleted content from {table_name}.")
    

if __name__ == "__main__":
    delete_content("thermometers")
    delete_content("temperature_reports")
