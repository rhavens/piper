import cPickle
from django.core.cache import cache

a = {'Movie', 'Hello', 'Worked?'}
cache.set('key', a)
fileObject = open('redis-cache.txt','w')
cPickle.dump(cache.get('key'), fileObject)
fileObject.close()