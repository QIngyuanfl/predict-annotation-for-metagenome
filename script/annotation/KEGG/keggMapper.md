# 异步爬取kegg数据库
此脚本用于绘制KEGG带颜色的通路图 \
非冗余基因集与KEGG数据库比对之后，会把Unigenes ID mapping到KID上 \
每个KID在1个通路图上代表1个蛋白, 如果mapping到的KID存在于相应的通路图，就将该蛋白涂上颜色, 通过提交KID到KEGG的Color_pathway_object API，将会返回带颜色的通路图。
## 库
- aiohttp
- asyncio
- argparse
- BeautifulSoup
- re, os, sys, time

## 使用方法
```sh
python keggMapper.py --ko gene2ko.txt -o Map 
```

##  样张
![颜色通路图](/test_space/test4annotation/4.annotation/Unigenes/KEGG/Map/map00010.png)

## FAQ
问: 如何处理连接超时的情况？\
答：一般这种情况比较少见，当运行30分钟后还没有进展的话，说明网络链接不稳定。实际上， 本地的网络比服务器端的网络要稳定的多，如果着急出结果的话，可以放到本地运行，本地实测20-40分钟可以完成。
