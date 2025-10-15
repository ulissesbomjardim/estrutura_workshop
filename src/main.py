from pipeline.extract import extract_from_excel
from pipeline.load import load_to_excel
from pipeline.transform import transform_data


def main() -> None:
    input_path = "data/input"
    output_path = "data/output"
    filename = "dados_concatenados"

    data_list = extract_from_excel(input_path)
    print(type(data_list))

    data_frame = transform_data(data_list)
    print(type(data_frame))

    message = load_to_excel(data_frame, output_path, filename)
    print(message)


if __name__ == "__main__":
    main()
