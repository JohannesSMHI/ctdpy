# -*- coding: utf-8 -*-
"""
Created on Thu Jul 19 13:38:35 2018

@author: a002028
"""

import pandas as pd
# from core.writers.with_style import with_style


class XlsxWriter(object):
    """ """
    def __init__(self, with_style=False, in_template=None):
        self.with_style = with_style
        self.in_template = in_template
        self._load_xlsx_writer()

    def _load_xlsx_writer(self, save_path, engine='openpyxl'):
        """
        Create a Pandas Excel writer using engine.
        :param save_path: str, path to file
        :param engine: Engine for the writer
        :return: Pandas Excel writer using engine.
        """
        self.xlsx_writer = pd.ExcelWriter(save_path, engine=engine)

    def write(self, df, save_path, sheet_name='Data', na_rep='', index=False,  encoding='cp1252'):
        """
        :param df: pd.DataFrame
        :param save_path: str
        :param sheet_name: str
        :param na_rep: str, np.nan, None
        :param index: False or True
        :param encoding: str
        :return: Saved excel file
        """
        df.to_excel(save_path,
                    na_rep=na_rep,
                    sheet_name=sheet_name,
                    index=index,
                    encoding=encoding)

    @staticmethod
    def write_dataframe(df, save_path, sheet_name='Data', na_rep='', index=False,  encoding='cp1252'):
        """
        :param df: pd.DataFrame
        :param save_path: str
        :param sheet_name: str
        :param na_rep: str, np.nan, None
        :param index: False or True
        :param encoding: str
        :return: Saved excel file
        """
        df.to_excel(save_path,
                    na_rep=na_rep,
                    sheet_name=sheet_name,
                    index=index,
                    encoding=encoding)

    def close_writer(self):
        """
        Close the Pandas Excel writer and save the Excel file.
        :return:
        """
        self.xlsx_writer.save()


# writer = pd.ExcelWriter('pandas_multiple.xlsx', engine='xlsxwriter')
#
# # Write each dataframe to a different worksheet.
# df1.to_excel(writer, sheet_name='Sheet1')
# df2.to_excel(writer, sheet_name='Sheet2')
# df3.to_excel(writer, sheet_name='Sheet3')














