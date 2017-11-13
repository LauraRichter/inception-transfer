from imagesoup import ImageSoup
from pathlib import Path
import click


@click.command()
@click.argument('image_search_query')
@click.option('--number', default=5, help='Number of images to download.')
def download_images(image_search_query, number):
    """Do google image search for supplied query string and save specified number of results."""
    soup = ImageSoup()
    # do google image search for given query
    images = soup.search(image_search_query, n_images=number)
    # make folder to put images into
    im_dir = Path('images', image_search_query.replace(' ', '_'))
    im_dir.mkdir(exist_ok=True, parents=True)
    # loop through images and save
    for ii, im in enumerate(images):
        im_format = im.format
        im_path = im_dir / '{}.{}'.format(ii, im_format)
        im.to_file(str(im_path))


if __name__ == '__main__':
    download_images()
