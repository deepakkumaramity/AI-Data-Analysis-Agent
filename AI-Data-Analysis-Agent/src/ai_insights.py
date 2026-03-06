
def generate_insights(df):
    insights = []
    
    top_region = df.groupby("Region")["Sales"].sum().idxmax()
    insights.append(f"Top performing region is {top_region}")
    
    top_category = df.groupby("Category")["Sales"].sum().idxmax()
    insights.append(f"Most profitable category is {top_category}")
    
    avg_sales = df["Sales"].mean()
    insights.append(f"Average sales value is {avg_sales}")
    
    return insights
