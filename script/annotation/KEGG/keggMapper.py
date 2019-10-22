#!/usr/bin/env python
import re, os, sys, time
import asyncio,aiohttp
import argparse
from bs4 import BeautifulSoup

__author__ = 'Qingyuan Zhang'
__data__ = '2019-09-28'
__version__ = 'V-2.0 '
__description__ = f'{sys.argv[0]} {__version__} draw KEGG Map'

def get_parameters():
    parser = argparse.ArgumentParser(usage="python %(prog)s [options]", description = __description__)
    parser.add_argument('--ko', dest='ko', help=f'result of blast4ko.pl, gene_ko.tab')
    parser.add_argument('-o', '--out_dir', dest = 'out_dir', default='.', help = 'The output directory')
    return parser.parse_args(), parser
class ColorPathwaySpider:
    def __init__(self, outdir, **kwargs):
        self.User_Agent = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"}
        self.outdir = outdir
        for key, value in kwargs.items():
            setattr(self, key, value)

    async def handle_get(self, url):
        file_name = url.split('/')[-1]
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as resp:
                if resp.status == 200:
                    with open(f'{os.path.join(self.outdir, file_name)}', 'wb') as f:
                        while True:
                            chunk = await resp.content.read(64*1024)
                            if not chunk:
                                break
                            f.write(chunk)
                else:
                    print(f'Error: Disconnect with {url}')

    async def handle_post(self, url):
        Agent = self.User_Agent
        if hasattr(self, 'file_name'):
            self.data['file'] = open(self.file_name, 'rb')
        async with aiohttp.ClientSession() as session:
            if not hasattr(self, 'headers'):
                async with session.post(url, headers = Agent) as resp:
                    with open(f'{os.path.join(self.outdir,"requests.html")}', 'wb') as f:
                        while True:
                            chunk = await resp.content.read(64*1024)
                            if not chunk:
                                break
                            f.write(chunk) 
            else:
                async with session.post(url, data = self.data, headers = self.headers )  as resp:
                    with open(f'{os.path.join(self.outdir,"requests.html")}', 'wb') as f:
                        while True:
                            chunk = await resp.content.read(64*1024)
                            if not chunk:
                                break
                            f.write(chunk) 
    
    async def download_map_png(self, url, out_dir):
        file_name = url.split('/')[-1]
        flag = True
        retry = 0
        while flag:
            try:
                await self.handle_get(url)
                flag = False
            except Exception as e:
                retry += 1
                print(f'retrying connect with {url} {retry} times\n')
                time.sleep(1)
                flag = True
        soup = BeautifulSoup(open(os.path.join(self.outdir, file_name)), 'html.parser')
        img_style = soup.find_all("img",usemap="#mapdata")[0]['src']
        img_url = "https://www.kegg.jp" + img_style
        img_name = re.findall(r'map\d*', img_style)[0]+'.png'
        flag = True
        retry = 0
        while flag:
            try:
                async with aiohttp.ClientSession() as session:
                    async with session.get(img_url) as resp:
                        with open(f'{os.path.join(self.outdir, img_name)}', 'wb') as pic:
                            while True:
                                chunk = await resp.content.read(64*1024)
                                if not chunk:
                                    break
                                pic.write(chunk)
                flag = False
            except Exception as e:
                retry +=  1
                time.sleep(1)
                flag = True    
                print(f'retrying connect with {img_url} {retry} times\n')
        return img_url
            
def main():

#decode gene2ko
    ko_file = args.ko
    KO_list = []
    with open(ko_file) as f:
        for line in f:
            if line == '\n' or line[0] == '#':
                continue
            fields = line.strip().split('\t')
            if len(fields) < 2 or fields[1] == '':
                continue
            if '!' in fields[1]:
                KO = fields[1].split('!')[0]
            if '!' not in fields[1]:
                KO = fields[1]
            if KO not in KO_list:
                KO_list.append(KO)
    unclassified = '\n'.join(KO_list)
    del(KO_list)
    #get free proxy
    
    #prepare html data & format
    url = 'https://www.kegg.jp/kegg-bin/color_pathway_object'
    headers = { "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            "Accept-Encoding":"gzip, deflate, br",
            "Accept-Language":"zh-CN,zh;q=0.9",
            "Referer":"https://www.kegg.jp/kegg/tool/map_pathway2.html",
            "User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"
            }
    data = {
            "org_name":"map",
            "sort":"object",
            "target":"alias",
            "default":"pink", 
            "unclassified": unclassified
            }
    # add headers and data to url
    color_pathway_spider = ColorPathwaySpider(out_dir,headers = headers, data = data)
    retry = 0
    flag = True
    while flag:
        try: 
            color_pathway_object = asyncio.run(color_pathway_spider.handle_post(url))
            flag = False 
        except Exception as e:
            retry += 1
            print(f'retrying color_pathway_object {retry} times...\n')
            flag = True
    soup = BeautifulSoup(open(os.path.join(out_dir,"requests.html")), 'html.parser')
    pathways = soup.find_all('li')
    #get kegg map url
    map_url = []
    for pathway in pathways:
        pathway_url = pathway.find('a', target='_blank', text=re.compile("map"))
        if pathway_url == None:continue
        pathway_url = 'https://www.kegg.jp/' + pathway_url.get('href')
        map_url.append(pathway_url)
    del (pathways)
    tasks = []
    flag = True
    for i in range(len(map_url)):
        if flag:
            loop = asyncio.new_event_loop()
            flag = False
        tasks.append(loop.create_task(color_pathway_spider.download_map_png(map_url[i], out_dir)))
        tasks.append(loop.create_task(asyncio.sleep(1)))
        if i % 3 == 0:
            flag = True 
            loop.run_until_complete(asyncio.gather(*tasks))
            loop.run_until_complete(asyncio.sleep(1))
            tasks = []
            loop.close()
if __name__ == "__main__":
    args, parser = get_parameters()
    out_dir = args.out_dir
    if not args.ko:
        sys.exit(parser.print_help())
#check input file
    exit = 0
    container = [args.ko]
    for i in container:
        if not os.path.exists(i):
            print(f'file {i} not exists')
            exit = 1
    if exit == 1:sys.exit(parser.print_help())
    if not os.path.exists(args.out_dir):os.system(f'mkdir -p {args.out_dir}')
#main_program
    main()
