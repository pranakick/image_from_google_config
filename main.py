from icrawler.builtin import GoogleImageCrawler


def image_from_google_config():
    filters = dict(
        type='photo', # alternativ 'face', 'clipart' ...
        color='blackandwhite',
        size='large', # alternativ 'icon', '=1024x768' ...
        # license='noncommercial, commercial',
        # date=((2020, 1, 1), (2023, 1, 1)) # alternativ 'pastweek'
    )
    crawler = GoogleImageCrawler(storage={'root_dir': './img'})
    # crawler.crawl(keyword='futurama', max_num=5)
    # crawler.crawl(keyword='spongebob', max_num=5, min_size=(1000,1000), overwrite=True)
    
    crawler.crawl(
        keyword='Buddha',
        max_num=3,
        min_size=(1000,1000),
        overwrite=True, #to overwrite the existing images
        filters=filters,
        file_idx_offset='auto'
    )

def main():
    image_from_google_config()
    
    
if __name__ == '__main__':
    main()