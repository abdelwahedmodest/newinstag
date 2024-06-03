
from instapy import InstaPy, smart_run
import config
import schedule
import time


def wordPressSession():
    comments = [
        'Learn more from https://skolo.online',
        'Learn Wordpress https://skolo.online',
        'Learn WooCommerce from https://skolo.online',
        'Yes! Amazing stuff',
        'Just love wordpress',
        'Check us out https://skolo.online',
        'Check out Youtube https://rb.gy/n7tfbn',
        'dree Learning Videos https://rb.gy/n7tfbn',
        'Online Learning https://rb.gy/n7tfbn',
        'WooCommerce Series https://rb.gy/hgc8um',
        'Learn Wordpress https://rb.gy/hgc8um',
        'Learn WooCommerce https://rb.gy/hgc8um'
]



session = InstaPy(username=config.insta_username,
password=config.insta_password,
headless_browser=True)

try:
    with smart_run(session):
        session. like_by_tags(["wordpress", 'woocommerce'], amount=10)
        session.set_do_comment(True, percentage=50)
        session. set_comments(comments)
        session.set_do_follow(enabled=True, percentage=10, times=1)

except:
    import traceback
    print(traceback. format_exc())
pass

def followSomePeople():
    try:
        with smart_run(session):
        session[follow_user_followers(['udemy', 'gibsacademy', 'gibsbusinessschool'], amount=10, randomize=True, sleep_delay=20)]

except:
import traceback
print(traceback. format_exc())
pass


schedule.every().day.at("10:30").do(wordPressSession)

