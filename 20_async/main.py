import asyncio


async def crawl_page(url):
    print('crawling {}'.format(url))
    sleep_time = int(url.split('_')[-1])
    await asyncio.sleep(sleep_time)
    print('OK {}'.format(url))


async def main(urls):
    tasks = [asyncio.create_task(crawl_page(url)) for url in urls]
    # 2
    await asyncio.gather(*tasks)
    # for task in tasks: #1
    #     await task #1


asyncio.run(main(['url_1', 'url_2', 'url_3', 'url_4']))
