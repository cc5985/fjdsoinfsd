class CurrencyPair:
    def __init__(self,base='btc', reference='usdt'):
        self.base=base
        self.reference=reference

    def get_currency_pair(self):
        return self.base+'_'+self.reference

