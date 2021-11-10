from abc import ABC, abstractmethod
import gzip  # compactamento do gzip é mais eficiente que o zip
import json
from zipfile import ZipFile


class ZipCompressor:  # comprimi arquivos em zip
    """Nossos compressores terão fixado o local de salvamento
    do arquivo, então vamos defini-lo nos construtores"""

    def __init__(self, filepath="./"):
        self.filepath = filepath

    def compress(self, file_name):
        with ZipFile(file_name + ".zip", "w") as zip_file:
            zip_file.write(file_name)


class GzCompressor:  # comprimi arquivos em gz
    def __init__(self, filepath="./"):
        self.filepath = filepath

    def compress(self, file_name):
        with open(file_name, "rb") as content:
            with gzip.open(file_name + ".gz", "wb") as gzip_file:
                gzip_file.writelines(content)


class SalesReport(ABC):
    def __init__(self, export_file):
        self.export_file = export_file

    def build(self):
        return [
            {"Coluna 1": "Dado 1", "Coluna 2": "Dado 2", "Coluna 3": "Dado 3"},
            {"Coluna 1": "Dado A", "Coluna 2": "Dado B", "Coluna 3": "Dado C"},
        ]

    def compress(self):  # método não abstrato(concreto) - não são obrigatórios
        binary_content = json.dumps(self.build()).encode("utf-8")

        with gzip.open(self.export_file + ".gz", "wb") as compressed_file:
            compressed_file.write(binary_content)

    @abstractmethod  # método abstrato deve ser implementado - obrigatórios
    def serialize(self):
        raise NotImplementedError


class SalesReportJSON(SalesReport):
    def serialize(self):
        with open(self.export_file + ".json", "w") as file:
            json.dump(self.build(), file)


class SalesReportCSV(SalesReport):
    # Sua implementação vai aqui
    pass
