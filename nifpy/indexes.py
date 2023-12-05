from .constants import *
import pandas as pd


class indices:

    @staticmethod
    def get_nifty() -> pd.DataFrame:
        nifty = pd.read_html(BASE_URL)[2]
        return nifty

    @staticmethod
    def nifty_media() -> list:
        media = pd.read_html(NIFTY_MEDIA)[0]
        media_list = list(media[media.columns[2]])
        return media_list[1:]

    @staticmethod
    def nifty_fmcg() -> list:
        fmcg = pd.read_html(NIFTY_FMCG)[0]
        fmcg_list = list(fmcg[fmcg.columns[2]])
        return fmcg_list[1:]

    @staticmethod
    def nifty_auto() -> list:
        auto = pd.read_html(NIFTY_AUTO)[0]
        auto_list = list(auto[auto.columns[2]])
        return auto_list[1:]

    @staticmethod
    def nifty_pharma() -> list:
        pharma = pd.read_html(NIFTY_PHARMA)[0]
        pharma_list = list(pharma[pharma.columns[2]])
        return pharma_list[1:]

    @staticmethod
    def nifty_metal() -> list:
        metal = pd.read_html(NIFTY_METAL)[0]
        metal_list = list(metal[metal.columns[2]])
        return metal_list[1:]

    @staticmethod
    def nifty_it() -> list:
        it = pd.read_html(NIFTY_IT)[0]
        it_list = list(it[it.columns[2]])
        return it_list[1:]

    @staticmethod
    def nifty_bank() -> list:
        bank = pd.read_html(NIFTY_BANK)[0]
        bank_list = list(bank[bank.columns[2]])
        return bank_list[1:]

# todo create a module for technical charts that will contain rsi, money flow index, MACD etc
