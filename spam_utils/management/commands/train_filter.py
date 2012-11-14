from django.core.management.base import BaseCommand, CommandError
from spam_utils.utils import *
from spam_utils.spambayes.hammie import Hammie

class Command(BaseCommand):
    help = 'Does some default training.'

    def handle(self, *args, **options):
        db = get_bayes_db()
        bfilter = Hammie(db,'w')
        bfilter.train('FREE rolex enlargement pills! Click here', True)
        bfilter.train('Sometimes I find that I need something. Click here to find it.', True)
        self.spam= """
        Hey, why do not you write?
        You forgot about me? "I am very unhappy without you, remember me?" It's me, Olga from Russia, Moscow, remember?
        I'm waiting for you on his page on the Internet, and miss you terribly!
        http://messageuyh.ppgirls.ru"""
        bfilter.train(self.spam,  True)
        bfilter.train('FREE apple mongos!!! I can SEO your night away!', True)
        bfilter.train('Hey Bill, I found your dog running around an orange grove.', False)
        bfilter.train('Roger, you cat crawled into my window :) lol. Come get it!', False)
        bfilter.train('Very nice! According to that website the lot size is 3.80 Acres ? That cant be right... Anyway Tiffany is also sick! No vomiting but lots of tummy related issues. Maybe its something they ate?', False)
        self.spam2 = """
        Open Webcam Feeds - FREE - Join the Community!

        http://tableslegs.com/cr17/

        It is truly incredible - People from all around the world are using
        their webcams to get off. Now is your chance to watch Men and women,
        boys and girls show off just for you. Best of all, it's FREE, LIVE
        and UN-F*CKING-BELIEVABLE. Either peep in on the sexy activity or
        participate with your own webcam! You've got to try this out!

        Open Amateur Webcam Feeds are Active RIGHT NOW!!!
        Get out? http://tableslegs.com/1m/
        """
        bfilter.train(self.spam2, True)
        db.close()
