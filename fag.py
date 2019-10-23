import pandas as pd
import numpy as np
def main():
    features_data = pd.read_csv("features_data.csv")
    equity_value_data = pd.read_csv("equity_value_data.csv")
    chunked_user_list = []
    current_user = equity_value_data["user_id"][0]
    count = 0
    for index in range(len(equity_value_data["user_id"])-1):
        if equity_value_data["user_id"][index]!=current_user:
            if count >= 28:
                chunked_user_list.append(current_user)
            count = 0
            current_user = equity_value_data["user_id"][index]

        else:
            if equity_value_data["close_equity"][index] < 100:
                count += 1
            else:
                if count >= 28:
                    chunked_user_list.append(current_user)
                    count = 0
                else:
                    count = 0
        chunked_header_list = []
        for i in range(len(features_data.user_id)):
            if features_data.user_id[i] in chunked_user_list:
                chunked_header_list.append(1)
            else:
                chunked_header_list.append(0)
    features_data["chunked"] = chunked_header_list
    features_data.to_csv(r"features_data_with_chunked.csv")
    any_dict = {"risk_tolerance":{"low_risk_tolerance":-1,
                              "med_risk_tolerance":0,
                              "high_risk_tolerance":1
                              },

            "investment_experience":{"no_investment_exp":0,
                                     "limited_investment_exp":1,
                                     "good_investment_exp":2,
                                     "extensive_investment_exp":3
                                     },

             "liquidity_needs":{
                "not_important_liq_need":0,
                "somewhat_important_liq_need":1,
                "very_important_liq_need":2
            },

            "platform":{
                "Android":-1,
                "both":0,
                "iOS":1
            },

                "instrument_type_first_traded":{
                    "0":0,
                    "tracking":1,
                    "ept":2,
                    "reit":3,
                    "wtr":4,
                    "adr":5,
                    "rlt":6,
                    "stock":7,
                    "cef":8,
                    "mlp":9,
                    "lp":10
                },

                    "time_horizon":{
                        "short_time_horizon":-1,
                        "med_time_horizon":0,
                        "long_time_horizon":1
                    }}

headers = features_data.columns

if __name__ == '__main__':
    main()
