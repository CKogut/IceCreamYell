#
# Analysis of the ice cream dataset.
#
import pandas as pd


def run_analysis():
    ic = pd.csv('ice_cream')
    print(ic.head(10))
    pass


if __name__ == '__MAIN__':
    run_analysis()
