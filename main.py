import multiprocessing
from defs import array
from defs import set_sity_data
from openpyxl import Workbook
if __name__ == '__main__':
	with multiprocessing.Pool(20) as pool:
		pool.map(set_sity_data, [f'https://dom.mingkh.ru/permskiy-kray/?page={i}' for i in range(1, 768)])
