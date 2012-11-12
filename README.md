#Spam fitering for Django based on spambayes
Spam training and filter via a modified version of http://spambayes.sourceforge.net/
I've really only modified it to work with psycopg2 and also to use the PickledClassifier if you are using ```sqlite3```. 
That being said, I've really only implemented enough of it to be usefull to me. I think there is alot that could be done.

## Usage Example

```
from spam_utils.utils import *
from spam_utils.spambayes.hammie import Hammie

db = get_bayes_db() # helper method that will choose an appropriate classifier for spambayes based on your django config.
# create a filter
bfilter = Hammie(db,'w') # 'w' is spambayes convention.
# train it
bfilter.train('FREE rolex enlargement pills! Click here', True) # True means you want to train this as spam
bfilter.train('Roger, you cat crawled into my window :) lol. Come get it!', False)# False means you want to train this as ham

# run it through the filter
spammy_mssg=""" Hey, why do not you write? You forgot about me? "I am very unhappy without you, remember me?" It's me, Olga from Russia, Moscow, remember? I'm waiting for you on his page on the Internet, and miss you terribly! http://somelinkyoushouldvisit.ru"""


prob, result = bfilter.score_and_filter(msg=spammy_mssg) # returns probability as 0.0 -> 1 and the spambayes message with all sorts of goodies.

```

## You should...
Train it quite a bit. See the tests included to see it actually do something meaningful.



