import pandas as pd
import matplotlib.pyplot as plt

# Data
data = {
    "Serial Number": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28],
    "Authors and Year": ["Smith, M., & Henderson, C. (2018)", "Cheney, J. (2008)", "Rozo, B., Crook, J., & Andreeva, G. (2021)", 
                         "Fu, G., Sun, M., & Xu, Q. (2020)", "Zhou, J., Wang, C., Ren, F., & Chen, G. (2021)", 
                         "Djeundje, V., Crook, J., Calabrese, R., & Hamid, M. (2021)", "Sustersic, M., Mramor, D., & Zupan, J. (2007)", 
                         "Huang, C., Chen, M., & Wang, C. (2007)", "Jiang, J., Liao, L., Lu, X., Wang, Z., & Xiang, H. (2020)", 
                         "Dastile, X., Çelik, T., & Potsane, M. (2020)", "Bequé, A., & Lessmann, S. (2017)", 
                         "He, H., Zhang, W., & Zhang, S. (2018)", "Munkhdalai, L., Munkhdalai, T., Namsrai, O., Lee, J., & Ryu, K. (2019)", 
                         "Aggarwal, N. (2018)", "Zhu, B., Yang, W., Wang, H., & Yuan, Y. (2018)", "McCanless, M. (2023)", 
                         "Ala’raj, M., Abbod, M., & Majdalawieh, M. (2021)", "Saberi, M., Mirtalaei, M., Hussain, F., Azadeh, A., Hussain, O., & Ashjari, B. (2013)", 
                         "Wei, Y., Yildirim, P., Bulte, C., & Dellarocas, C. (2014)", "Wang, C., Han, D., Liu, Q., & Luo, S. (2019)", 
                         "West, D. (2000)", "Brown, I., & Mues, C. (2012)", "Lee, T., & Chen, I. (2005)", "Mahjoub, R., & Afsar, A. (2019)", 
                         "Arram, A., Ayob, M., Albadr, M., Sulaiman, A., & Albashish, D. (2023)", "Junior, L., Nardini, F., Renso, C., Trani, R., & Macêdo, J. (2020)", 
                         "Wiginton, J. (1980)", "Saberi, M., Mirtalaei, M., Hussain, F., Azadeh, A., Hussain, O., & Ashjari, B. (2013)"],
    "Datasets Used": ["Social media data", "Utility bills, rental payments", "Web browsing data", "Digital footprint data", "Online consumer credit data", "Telecom data", 
                      "Limited consumer credit data", "Credit scoring data", "Big data from multiple sources", "Not applicable (literature survey)", "Credit scoring data", 
                      "Credit scoring data with imbalanced ratios", "Bank client credit data", "Not specified", "Consumer credit data", "Alternative credit scores data", 
                      "Credit card usage data", "Credit scoring data", "Social network data", "Peer-to-peer lending data", "Credit scoring data", "Imbalanced credit scoring data", 
                      "Credit scoring data", "Credit data from stock brokerages", "New credit card score dataset", "Imbalanced credit scoring data", "Consumer credit data", "Credit scoring data"]
}

# Create DataFrame
df = pd.DataFrame(data)

# Define categories
categories = {
    "Social Media Data": ["Social media data", "Social network data"],
    "Web Browsing Behavior": ["Web browsing data"],
    "Digital Footprints": ["Digital footprint data", "Online consumer credit data", "Mobile usage data", "Digital payment history"],
    "Telecom Data": ["Telecom data", "Call records", "SMS usage", "Mobile payment history"],
    "Hybrid Data Approaches": ["Big data from multiple sources", "Various data sources", "Integrated data"]
}

# Initialize category count
category_count = {key: 0 for key in categories.keys()}

# Categorize datasets
for dataset in df["Datasets Used"]:
    for category, keywords in categories.items():
        if any(keyword in dataset for keyword in keywords):
            category_count[category] += 1

# Convert to DataFrame for visualization
category_df = pd.DataFrame(list(category_count.items()), columns=["Category", "Count"])

# Plotting
plt.figure(figsize=(10, 6))
plt.bar(category_df["Category"], category_df["Count"], color='skyblue')
plt.xlabel('Dataset Category')
plt.ylabel('Count')
plt.title('Distribution of Alternative Data Categories for Credit Scoring')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
