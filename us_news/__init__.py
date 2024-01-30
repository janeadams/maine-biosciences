import httpx
import argparse
import pandas as pd
import random
import time

headers = {
    'authority': 'www.usnews.com',
    'accept': '*/*',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'referer': 'https://www.usnews.com/',
    'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
}


def get_schools(schooltype):

    lookups = {
        'colleges': {
            'url': 'https://www.usnews.com/best-colleges/me?format=json',
            'param': 'items',
            'tp': 'total_pages'
        },
        'community': {
            'url': 'https://www.usnews.com/education/community-colleges/maine?format=json',
            'param': 'results',
            'tp': 'totalPages'
        },
        'gradschools': {
            'url': 'https://www.usnews.com/best-graduate-schools/search/?format=json',
            'param': 'items',
            'tp': 'total_pages'
        },
        'online': {
            'url': 'https://www.usnews.com/education/online-education/maine-online-schools?format=json',
            'param': 'items',
            'tp': 'total_pages'
        },
        'highschools': {
            'url': 'https://www.usnews.com/education/best-high-schools/maine?format=json',
            'param': 'items',
            'tp': 'total_pages'
        },
        'private': {
            'url': 'https://www.usnews.com/education/k12/private-k12/maine?format=json',
            'param': 'items',
            'tp': 'total_pages'
        }
    }


    r = httpx.get(lookups[schooltype]['url'], headers=headers).json()['data']

    print(r)
    
    last_page = r.get(lookups[schooltype]['tp'])

    if last_page == '1':
        results = r.get(lookups[schooltype]['param'])
    else:

        results = []

        results += r.get(lookups[schooltype]['param'])

        for p in range(2, int(last_page)+1):
            
            r = httpx.get(f"{lookups[schooltype]['url']}&page={p}", headers=headers).json()['data']

            results += r.get(lookups[schooltype]['param'])

            time.sleep(random.randint(2,4))

    df = pd.DataFrame(results)

    expanded_dfs = []

    for col in df:
        expanded_dfs.append(pd.json_normalize(df[col]))

    expanded_df = pd.concat(expanded_dfs, axis=1)

    for col in expanded_df.columns:
        try:
            n = expanded_df[col].nunique()
            try:
                if n < 2:
                    expanded_df.drop(col, axis=1, inplace=True)
            except:
                pass
        except:
            expanded_df.drop(col, axis=1, inplace=True)

    return expanded_df

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-st', '--schooltype', help='Choose school type: colleges, community, gradschools, online, highschools, private', default='colleges')

    args = parser.parse_args()

    schooltype = args.schooltype

    final = get_schools(schooltype)

    final.to_csv(f'{schooltype}.csv', encoding='utf-8-sig', index=False)




