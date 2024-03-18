import random

shop = {
    "3陽壽":[10500,3500,42],#原價 優惠max 出現機率
    "5陽壽":[17500,3500,18],
    "7陽壽":[24500,4000,12],
    "10陽壽":[35000,5000,5],
    "5萬眾神幣":[5000,500,10],
    "10萬眾神幣":[10000,1000,5],
    "50萬眾神幣":[45000,10000,5],
    "100萬眾神幣":[60000,10000,1],
    "舞者之書":[40000,5000,1],
    "魔法戰士之書":[70000,5000,1],
    }

# 从字典中随机选择一个键，基于权重
weighted_choices = [(item, item_info[2]) for item, item_info in shop.items()]
selected_item = random.choices(weighted_choices, weights=[w for _, w in weighted_choices])[0][0]

print(f"隨機選擇的商品: {selected_item}")
