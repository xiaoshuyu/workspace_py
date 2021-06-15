
def 
class GetSourceData:
    def __init__(self):
        pass

    def get_stocks_data(self):
        pass

    def get_index_future_data(self):
        pass

    def get_index_data(self):
        pass

    def get_bond_data(self):
        pass

    def get_commodity_future_data(self):
        pass

import threading
class ClearData:
    def __init__(self):
        pass

    def clear_stock_data(self):
        pass

    def clear_index_future_data(self):
        pass

    def clear_index_data(self):
        pass

    def clear_commodity_future_data(self):
        pass

    # ---------1------------

    def _clear_fundamental_data(self):
        pass

    def _clear_market_data(self):
        pass

    def _clear_trade_data(self):
        pass

    def _clear_order_data(self):
        pass

    def _clear_order_queue_data(self):
        pass

    # ---------2------------
    def __cal_kline_index(self):
        pass

    def __cal_tick_index(self):
        pass


class TradingSystem:
    def __init__(self):
        pass

    def get_position(self):
        pass

    def get_trade(self):
        pass

    def get_order(self):
        pass

    def trade_to_target_position(self):
        pass

    def get_log(self):
        pass

    def get_indicator(self):
        pass


class FactorAnalyze:
    def __init__(self):
        pass

    def create_signal(self):
        pass

    def test_signal(self):
        pass

    def optimize_signal(self):
        pass

    def trading_signal(self):
        pass

    # ----------------1------------------
    def _create_signal_from_market(self):
        pass

    def _create_signal_from_other_markets(self):
        pass

    def _create_signal_from_fundamental_data(self):
        pass

    def _create_signal_from_other_data(self):
        pass

    # ----------------2------------------

    def __create_signal_from_market_level2(self):
        pass

    def __create_signal_from_fund_data(self):
        pass

    def __create_signal_from_news_data(self):
        pass


class Career(ClearData, FactorAnalyze, TradingSystem):
    def __init__(self):
        pass

    def get_source_data(self):
        pass

    def clear_data(self):
        pass

    def factor_analyze(self):
        pass

    def trading_strategies(self):
        pass
