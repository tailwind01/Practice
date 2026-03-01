import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    ans = views[views['author_id'] == views['viewer_id']][['author_id']]
    ans = ans.drop_duplicates().rename(columns={'author_id': 'id'}).sort_values(by='id')
    return ans
