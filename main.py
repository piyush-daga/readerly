"""The main file for readerly class."""
import csv
from typing import List, Dict, Generator, Union, Any


class Reader:
    def read_csv(ip_fpath: str, stream: bool = True) -> Union[Generator, List[Dictp[str, Any]]]:
        with open(ip_fpath) as fp:
            reader = csv.DictReader(fp)

            if not stream:
                return [row for row in reader]

            for row in reader:
                yield row