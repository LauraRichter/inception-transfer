from imagesoup import ImageSoup
from pathlib import Path
import click


@click.command()
@click.argument('image_search_query')
@click.option('--number', default=5, help='Number of images to download.')
@click.option(
    '--max-height',
    type=int,
    help='Max height to download image at (images with larger height will be downscaled).')
def download_images(image_search_query, number, max_height=None):
    """Do google image search for supplied query string and save specified number of results."""
    soup = ImageSoup()
    # do google image search for given query
    images = soup.search(image_search_query, n_images=number)
    # make folder to put images into
    im_dir = Path('images', image_search_query.replace(' ', '_'))
    im_dir.mkdir(exist_ok=True, parents=True)
    # loop through images and save
    n_downloaded = 0
    for im in images:
        try:
            im_format = im.format
            im_path = str(im_dir / '{}.{}'.format(n_downloaded, im_format))
            # resize, if necessary, then save
            xsize, ysize = im.size
            if max_height is not None and ysize > max_height:
                im_to_save = im.reduce(new_height=max_height)
                im_to_save.save(im_path)
            else:
                with open(im_path, 'wb') as f:
                    f.write(im.content.getvalue())
            n_downloaded += 1
        except Exception as err:
            print('Failed download of image {}: {}'.format(im.URL, err))
    print('Number of successful downloads: {}'.format(n_downloaded))


if __name__ == '__main__':
    download_images()
