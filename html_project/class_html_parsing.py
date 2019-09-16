

from bs4 import BeautifulSoup
import re

ITEM_HTML = '''<html><head></head><body>
<li class="col-xs-6 col-sm-4 col-md-3 col-lg-3">
    <article class="product_pod">
            <div class="image_container">
                    <a href="catalogue/a-light-in-the-attic_1000/index.html"><img src="media/cache/2c/da/2cdad67c44b002e7ead0cc35693c0e8b.jpg" alt="A Light in the Attic" class="thumbnail"></a>
            </div>
            <p class="star-rating Three">
                <i class="icon-star"></i>
                <i class="icon-star"></i>
                <i class="icon-star"></i>
                <i class="icon-star"></i>
                <i class="icon-star"></i>
            </p>
            <h3><a href="catalogue/a-light-in-the-attic_1000/index.html" title="A Light in the Attic">A Light in the ...</a></h3>
            <div class="product_price">
        <p class="price_color">£51.77</p>
<p class="instock availability">
    <i class="icon-ok"></i>
        In stock
</p>
    <form>
        <button type="submit" class="btn btn-primary btn-block" data-loading-text="Adding...">Add to basket</button>
    </form>
            </div>
    </article>
</li>
</body></html>
'''


class ParseItemLocators:
    """
    Locators for an item in HTML page

    This allows us to easily see what our code will be looking at
    as well as change it quickly if we notice it is now different.
    """
    NAME_LOCATOR = 'article.product_pod h3 a'
    LINK_LOCATOR = 'article.product_pod h3 a'
    PRICE_LOCATOR = 'article.product_pod div p.price_color'
    RATING_LOCATOR = 'article.product_pod p.star-rating'


class ParserItem:
    """
    A class to take in an HTML page (or part of it), and find properties of an
    item in it.
    """

    def __init__(self, page):
        self.soup = BeautifulSoup(page, 'html.parser')

    @property
    def name(self):
        locator = ParseItemLocators.NAME_LOCATOR
        item_link = self.soup.select_one(locator)
        item_name = item_link.attrs['title']
        # print(item_name)
        return item_name

    @property
    def link(self):
        locator = ParseItemLocators.LINK_LOCATOR
        item_link = self.soup.select_one(locator)
        item_name = item_link.attrs['href']
        # print(item_name)
        return item_name

    @property
    def price(self):
        locator = ParseItemLocators.PRICE_LOCATOR
        item_link = self.soup.select_one(locator).string

        pattern = "£([0-9]+\.[0-9]+)"

        matcher = re.search(pattern, item_link)
        # print(matcher.group(0))
        # print(matcher.group(1))

        price_val = float(item_link.strip('£'))
        # print(price_val)
        return price_val

    @property
    def rating(self):
        locator = ParseItemLocators.RATING_LOCATOR
        star_rating_tag = self.soup.select_one(locator)
        classes = star_rating_tag.attrs['class']
        # print(classes)
        rating = [c for c in classes if c != 'star-rating']
        # rating = filter(lambda x: x != 'star-rating', classes)

        # print(rating[0])
        return rating[0]


item = ParserItem(ITEM_HTML)
print(item.name)
print(item.link)
print(item.price)
print(item.rating)