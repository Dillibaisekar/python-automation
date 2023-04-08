import requests
from bs4 import BeautifulSoup
url=[]
valid=[]
partial_url=[]
validurlfromlink1=[]
validurlfromlink2=[]
validurlfromlink3=[]
partialvalid=[]
partial_urlset1=[]
partial_urlset2=[]
partial_urlset3=[]

adress=requests.get('https://www.shriramfinance.in/')
# address = urllib.request.urlopen('https://www.shriramfinance.in/')
# html = adress.read()
soup = BeautifulSoup(adress.text, "html.parser")
a_tag = soup.findAll('a')
for link in a_tag:
    if 'href' in link.attrs:
        href = link.attrs['href']
        # duplicate_remove(url)
        if href not in link:
            url.append(href)
        if 'shriramfinance.in' in href and href not in valid:
            valid.append(href)
            # print(href)

            set1=requests.get(href)
            soup = BeautifulSoup(set1.text, "html.parser")
            a_tag = soup.findAll('a')
            for link in a_tag :
                if 'href' in link.attrs:
                    href = link.attrs['href']
                    if 'shriramfinance.in' in href and '@shriramfinance.in' not in href:
                        if href not in validurlfromlink1:
                            validurlfromlink1.append(href)
                            if href not in valid:
                                valid.append(href)

                        set2=requests.get(href)
                        soup = BeautifulSoup(set2.text, "html.parser")
                        a_tag = soup.findAll('a')
                        for link in a_tag:
                            if 'href' in link.attrs:
                                href = link.attrs['href']
                                if 'shriramfinance.in' in href and '@shriramfinance.in' not in href:
                                    if href and validurlfromlink1  in validurlfromlink2:
                                        validurlfromlink2.append(href)
                                        if href not in valid:
                                            valid.append(href)

                                        set3=requests.get(href)
                                        soup = BeautifulSoup(set3.text, "html.parser")
                                        a_tag = soup.findAll('a')
                                        for link in a_tag:
                                            if 'href' in link.attrs:
                                                href = link.attrs['href']
                                                if 'shriramfinance.in' in href and href not in validurlfromlink3:
                                                    if validurlfromlink2  in validurlfromlink3:
                                                        validurlfromlink3.append(href)
                                                    if href not in valid:
                                                        valid.append(href)

        if href.startswith('/') and href not in partial_url:
            partial_url.append(href)
            Domain='https://www.shriramfinance.in'
            hrefurl="{}{}".format(Domain,href)
            if 'shriramfinance.in' in hrefurl and href not in partialvalid:
                partialvalid.append(href)

                partialset1 = requests.get(hrefurl)
                soup = BeautifulSoup(partialset1.text, "html.parser")
                a_tag = soup.findAll('a')
                for link in a_tag:
                    if 'href' in link.attrs:
                        href = link.attrs['href']

                        if 'shriramfinance.in' in hrefurl and hrefurl not in partial_urlset1:
                            partial_urlset1.append(hrefurl)
                            if href and hrefurl not in valid:
                                partialvalid.append(hrefurl)

                            partialset2 = requests.get(hrefurl)
                            soup = BeautifulSoup(partialset2.text, "html.parser")
                            a_tag = soup.findAll('a')
                            for link in a_tag:
                                if 'href' in link.attrs:
                                    href = link.attrs['href']

                                    if 'shriramfinance.in' in hrefurl and hrefurl not in partial_urlset2:
                                        if partial_urlset1 not in partial_urlset2:
                                            partial_urlset2.append(hrefurl)
                                            if href and hrefurl not in valid:
                                                partialvalid.append(hrefurl)

                                        partialset3 = requests.get(hrefurl)
                                        soup = BeautifulSoup(partialset3.text, "html.parser")
                                        a_tag = soup.findAll('a')
                                        for link in a_tag:
                                            if 'href' in link.attrs:
                                                href = link.attrs['href']

                                                if 'shriramfinance.in' in hrefurl and hrefurl not in partial_urlset3:
                                                    if partial_urlset2 in partial_urlset3:
                                                        partial_urlset3.append(hrefurl)
                                                        if hrefurl and href not in valid:
                                                            partialvalid.append(hrefurl)

print('All valids URLs',valid)
print('Valid URLs from set1',validurlfromlink1)
print('Valid URLs from set2',validurlfromlink2)
print('Valid URLs from set3',validurlfromlink3)

print("All valid URLs from partial URls",partialvalid)
print('Valid URLs from partial URLs set1',partial_urlset1)
print('Valid URLs from partial URLs set2',partial_urlset2)
print('Valid URLs from partial URLs set3',partial_urlset3)









