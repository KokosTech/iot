import pandas as pd


def get_average_tests_marks(file):
    df = pd.read_csv(file)

    # cleanup
    df = df.dropna()
    df = df.drop_duplicates()

    # set data
    df = df.set_index('Name')
    df = df.astype(int)

    # calculate average & sort (mopr shit :P)
    df = df.mean(axis=0)
    df = df.round(2)
    df = df.sort_values(ascending=False)
    
    # add headers - name and average
    result = [{"Name": test, "Average": mark} for test, mark in df.items()]

    file.seek(0)
    return result


def _get_average_students_marks(file):
    df = pd.read_csv(file)

    # cleanup
    df = df.dropna()
    df = df.drop_duplicates()

    # set data
    df = df.set_index('Name')
    df = df.astype(int)

    # calculate average & sort, but this time for a student
    df['Average'] = df.mean(axis=1)
    df = df.round(2)

    # cut useless columns

    df = df[['Average']].reset_index()

    file.seek(0)
    return df.to_dict()

def get_failing_students(file):
    student_average = _get_average_students_marks(file)
    
    # cut everyone below an average of 50
    df = pd.DataFrame(student_average)
    df = df[df['Average'] < 50]

    file.seek(0)
    return df.to_dict(orient='records')
