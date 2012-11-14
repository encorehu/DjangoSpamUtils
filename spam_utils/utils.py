from django.conf import settings
from spam_utils.spambayes.storage import PickledClassifier, PG2Classifier

def get_bayes_db():

    bayes_db = None
    db_settings = settings.DATABASES['default']

    if db_settings['ENGINE'] == 'django.db.backends.postgresql_psycopg2' or db_settings['ENGINE']=='django.contrib.gis.db.backends.postgis':
        bayes_db = PG2Classifier(db_settings['NAME'], db_settings['USER'], db_settings['PASSWORD'], db_settings['HOST'], db_settings['PORT'])
    elif db_settings['ENGINE'] == 'django.db.backends.sqlite3':
        # when we use a sqlite db we're gonna use the PickledClassifier. I dont
        # suspect anyone would use sqlite in production but a lot of times I
        # use sqlite3 while dev'ing
        bayes_db = PickledClassifier('/tmp/' + db_settings['NAME'])

    return bayes_db
