from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import parsing as ps
import pandas as pd
import numpy as np

def get_image_links(links):

    # Starts a new weddriver window and puts in the site
    driver = webdriver.Firefox()
    img_link = []
    err_link = []
    for link in links:
        try:
            driver.get(link)
            if len(driver.find_elements(By.CLASS_NAME, 'media-item')) > 0:
                img = driver.find_element(By.CLASS_NAME, 'media-item')
                img = img.find_element(By.CSS_SELECTOR, 'img')
                # print(img.get_attribute('src'))
                img_link.append(img.get_attribute('src'))
                
            else:
                img_link.append(None)
            
        except Exception as e:
            img_link.append(None)
            print(link)
            # err_link.append(link)
        finally:
            continue
    
    return img_link


def get():
    data, _ = ps.get_year_data(2024)
    col = data['link']
    ims = get_image_links(col)
    df = pd.DataFrame(np.array(ims), columns=['img'])

    pca = pd.read_csv('./pca_data/2023-2024full-2D-pca.csv', sep=',')
    pca['img'] = df['img']
    # print(pca)
    pca.to_json('./pca_data/2023-2024full-2D-pca.json', orient='records')

def get_2():
    pca = pd.read_json('./pca_data/2024-2025-full-2D-pca.json', orient='records')
    emp = pca[pca['img'].isna()]
    col = emp['link']
    ims = get_image_links(col)
    # df = pd.DataFrame(np.array(ims), columns=['img'])
    emp['img'] = np.array(ims)
    c = pd.concat([emp['img'], emp['Name']], axis=1)
    g = pd.concat([pca['img'], pca["Name"]], axis=1)
    g = g.dropna()
    out = pd.concat([c, g])

    total = pd.merge(pca, out, left_on="Name", right_on="Name", how='left')
    total.drop(columns=['img_x'], axis=1, inplace=True)
    total.rename(columns={'img_y':'img'}, inplace=True)
    # print(emp)
    # total = pd.merge(pca, emp, left_on="Name", right_on="names", how='left')

    total.to_json('./pca_data/2024-2025total.json', orient='records')


# get_2()
def get_3():
    raw = pd.read_csv('./raw_data/2023-2024comp.csv', sep=',')
    pca = pd.read_json('./pca_data/2023-2024full-2D-pca.json', orient='records')
    total = pd.merge(raw, pca, left_on="Name", right_on="names", how='left')
    total.drop(columns=[ 'names'], axis=1, inplace=True) 
    # print(total.iloc[0])
    # print(raw)
    total.to_json('./pca_data/2023-2024full-2D-pca.json', orient='records')


# get_3()

def mergesa():
    pca = pd.read_json('./pca_data/2023-2024full-2D-pca.json', orient='records')
    extra = pd.read_json('./pca_data/2023-2024extra.json', orient='records')
    c = pd.concat([pca['img'], pca['Name']], axis=1)
    g = pd.concat([extra['img'], extra['Name']], axis=1)
    c = c.dropna()
    out = pd.concat([c, g])
    total = pd.merge(pca, out, left_on="Name", right_on="Name", how='left')
    # print(total['img_x'])
    total.drop(columns=['img_x'], axis=1, inplace=True)
    total.rename(columns={'img_y':'img'}, inplace=True)
    total.to_json('./pca_data/2023-2024full-2D-pca.json', orient='records')

# mergesa()

def mergesa():
    old = pd.read_json('./pca_data/2023-2024full-2D-pca.json', orient='records')
    new = pd.read_json('./pca_data/2024-2025-full-2D-pca.json', orient='records')
    print(new)
    c = pd.concat([old['img'], old['Name']], axis=1)
    # g = pd.concat([extra['img'], extra['Name']], axis=1)
    # c = c.dropna()
    # out = pd.concat([c, g])
    total = pd.merge(new, c, left_on="Name", right_on="Name", how='left')
    # total = total.drop(['names'], axis=1)
    # print(total['img_x'])
    # total.drop(columns=['img_x'], axis=1, inplace=True)
    # total.rename(columns={'img_y':'img'}, inplace=True)
    print(total)
    total.to_json('./pca_data/2024-2025-full-2D-pca.json', orient='records')

# mergesa()

def hel():
    # extra = pd.read_json('./pca_data/2024-2025total.json', orient='records')
    # # extra.to_json('./pca_data/2023-2024-450-2D-pca.json', orient='records')
    # extra.to_csv('./pca_data/2024-2025total.csv')
    extra = pd.read_csv('./pca_data/2024-2025total.csv')
    # extra.to_json('./pca_data/2023-2024-450-2D-pca.json', orient='records')
    extra.to_json('./pca_data/2024-2025total.json', orient='records')


hel()
