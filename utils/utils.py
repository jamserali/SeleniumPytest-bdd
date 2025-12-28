import csv


class Utils:

    @staticmethod
    def read_csv(file_path):
        data = []
        try:
            with open(file_path, mode='r', encoding='utf-8') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    clean_row = {
                        key.strip(): value.strip()
                        for key, value in row.items()
                    }
                    data.append(clean_row)

        except FileNotFoundError:
            print(f"Error: CSV file is not found at {file_path}")
        except Exception as e:
            print(f"Error reading CSV file: {e}")

        return data
