import argparse
import os
import xml.etree.ElementTree as ET

from openpyxl import Workbook


def convert(input_path, output_path):
    with open(input_path, 'r') as f:
        root = ET.fromstring(f.read())
    data = []
    for child in root:
        for item in child:
            data.append(item.attrib)
    wb = Workbook()
    ws = wb.active
    ws.title = "data"
    headers = []
    for key, value in data[0].items():
        headers.append(key)
    ws.append(headers)
    for item in data:
        tmp = []
        for key, value in item.items():
            tmp.append(value)
        ws.append(tmp)
    wb.save(output_path)


def main(args):
    os.makedirs(args.output_path, exist_ok=True)
    output_path = os.path.join(args.output_path, os.path.basename(args.input_path).split('.')[0] + ".xlsx")
    convert(args.input_path, output_path)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--input_path', type=str, default='data.xml')
    parser.add_argument('--output_path', type=str, default='./data')
    args_ = parser.parse_args()
    main(args_)
