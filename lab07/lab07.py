import random
from unittest import TestCase

################################################################################
# EXTENSIBLE HASHTABLE
################################################################################
class ExtensibleHashTable:

    def __init__(self, n_buckets=1000, fillfactor=0.5):
        self.n_buckets = n_buckets
        self.fillfactor = fillfactor
        self.buckets = [None] * n_buckets
        self.nitems = 0

    def find_bucket(self, key):
        # BEGIN_SOLUTION
        test = hash(key)%self.n_buckets
        while True:
          if self.buckets[test]==None or self.buckets[test][0]==key:
            return test
          test = (test+1)%self.n_buckets
        # END_SOLUTION

    def __getitem__(self,  key):
        # BEGIN_SOLUTION
       test = self.find_bucket(key)
       if self.buckets[test]!=None:
         return self.buckets[test][1]
       else:
         raise KeyError("Key does not exist in the hash table")
       
       
         
        # END_SOLUTION

    def __setitem__(self, key, value):
        # BEGIN_SOLUTION
         test = key%self.n_buckets
         while self.buckets[test]!=None and self.buckets[test][0]!=key:
           test = (test+1)%self.n_buckets
         self.buckets[test] = [key, value]
         self.nitems+=1
         if self.nitems==self.n_buckets*self.fillfactor:
           self.n_buckets = self.n_buckets*2
           newtable = self.n_buckets*[None]
           for i in range(self.n_buckets//2):
             if self.buckets[i]:
               test = self.buckets[i][0]%self.n_buckets
               while newtable[test]!=None:
                 test = (test+1)%self.n_buckets
               newtable[test] = self.buckets[i]
           self.buckets = newtable
        # END_SOLUTION

    def __delitem__(self, key):
        # BEGIN SOLUTION
        test = key%self.n_buckets
        while self.buckets[test]!=None and self.buckets[test][0]!=key:
          test = (test+1)%self.n_buckets
        if self.buckets[test][0]==key:
          self.nitems = self.nitems-1
          aboveAdjust = test+1
          while self.buckets[aboveAdjust]!= None and self.buckets[aboveAdjust][0] % self.n_buckets==test:
            self.buckets[aboveAdjust-1] = self.buckets[aboveAdjust]
            aboveAdjust =  aboveAdjust+1
          self.buckets[aboveAdjust-1]=None
        else:
          raise KeyError()
        # END SOLUTION

    def __contains__(self, key):
        try:
            _ = self[key]
            return True
        except:
            return False

    def __len__(self):
        return self.nitems

    def __bool__(self):
        return self.__len__() != 0

    def __iter__(self):
        ### BEGIN SOLUTION
        for i in self.buckets:
          if i: 
            yield i[0]
        ### END SOLUTION

    def keys(self):
        return iter(self)

    def values(self):
        ### BEGIN SOLUTION
        for i in self.buckets:
          if i:
            yield i[1]
        ### END SOLUTION

    def items(self):
        ### BEGIN SOLUTION
        for i in self.buckets:
          if i:
            yield tuple(i)
        ### END SOLUTION

    def __str__(self):
        return '{ ' + ', '.join(str(k) + ': ' + str(v) for k, v in self.items()) + ' }'

    def __repr__(self):
        return str(self)

################################################################################
# TEST CASES
################################################################################
# points: 20
def test_insert():
    tc = TestCase()
    h = ExtensibleHashTable(n_buckets=100000)

    for i in range(1,10000):
        h[i] = i
        tc.assertEqual(h[i], i)
        tc.assertEqual(len(h), i)

    random.seed(1234)
    for i in range(1000):
        k = random.randint(0,1000000)
        h[k] = k
        tc.assertEqual(h[k], k)

    for i in range(1000):
        k = random.randint(0,1000000)
        h[k] = "testing"
        tc.assertEqual(h[k], "testing")

# points: 10
def test_getitem():
    tc = TestCase()
    h = ExtensibleHashTable()

    for i in range(0,100):
        h[i] = i * 2

    with tc.assertRaises(KeyError):
        h[200]


# points: 10
def test_iteration():
    tc = TestCase()
    h = ExtensibleHashTable(n_buckets=100)
    entries = [ (random.randint(0,10000), i) for i in range(100) ]
    keys = [ k for k, v in entries ]
    values = [ v for k, v in entries ]

    for k, v in entries:
        h[k] = v

    for k, v in entries:
        tc.assertEqual(h[k], v)

    tc.assertEqual(set(keys), set(h.keys()))
    tc.assertEqual(set(values), set(h.values()))
    tc.assertEqual(set(entries), set(h.items()))

# points: 20
def test_modification():
    tc = TestCase()
    h = ExtensibleHashTable()
    random.seed(1234)
    keys = [ random.randint(0,10000000) for i in range(100) ]

    for i in keys:
        h[i] = 0

    for i in range(10):
        for i in keys:
            h[i] = h[i] + 1

    for k in keys:
        tc.assertEqual(h[k], 10)

# points: 20
def test_extension():
    tc = TestCase()
    h = ExtensibleHashTable(n_buckets=100,fillfactor=0.5)
    nitems = 10000
    for i in range(nitems):
        h[i] = i

    tc.assertEqual(len(h), nitems)
    tc.assertEqual(h.n_buckets, 25600)

    for i in range(nitems):
        tc.assertEqual(h[i], i)


# points: 20
def test_deletion():
    tc = TestCase()
    h = ExtensibleHashTable(n_buckets=100000)
    random.seed(1234)
    keys = [ random.randint(0,1000000) for i in range(10) ]
    for k in keys:
        h[k] = 1

    for k in keys:
        del h[k]

    tc.assertEqual(len(h), 0)
    with tc.assertRaises(KeyError):
        h[keys[0]]

    with tc.assertRaises(KeyError):
        h[keys[3]]

    with tc.assertRaises(KeyError):
        h[keys[5]]

################################################################################
# TEST HELPERS
################################################################################
def say_test(f):
    print(80 * "*" + "\n" + f.__name__)

def say_success():
    print("SUCCESS")

################################################################################
# MAIN
################################################################################
def main():
    for t in [test_insert,
              test_iteration,
              test_getitem,
              test_modification,
              test_deletion,
              test_extension]:
        say_test(t)
        t()
        say_success()

if __name__ == '__main__':
    main()
