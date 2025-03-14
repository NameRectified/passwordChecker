import hashlib
import requests
import sys


class PassChecker():
    def __init__(self,password):
        self.password = password

    def hashConvert(self):
        hash = hashlib.sha1(self.password.encode('utf-8')).hexdigest().upper()
        return hash

    def headAndTail(self):
        splitHash = self.hashConvert()
        # we need only first 5 characters for the api
        head, tail = splitHash[:5],splitHash[5:]
        return head,tail
    def haveIbeenPwned(self):
        head, tail = self.headAndTail()
        url = 'https://api.pwnedpasswords.com/range/' + head
        result = requests.get(url)
        if result.status_code!=200:
            raise RuntimeError(f"Trouble fetching. {result.status_code}")
        else:
            return self.leakCount(result,tail)
    def leakCount(self,hashes,hashToCheck):
        hashes = (line.split(':') for line in hashes.text.splitlines())
        for hash, count in hashes:
            if hash==hashToCheck:
                return count
        return 0
    def isValidPassword(self):
        count = self.haveIbeenPwned()
        if count:
            return f"Password was found in a data breach {count} times, please change it."
        else:
            return f"{self.password} is a good password. You can use it."



if __name__ == "__main__":
    for arg in sys.argv[1:]:
        checker = PassChecker(arg)
        print(checker.isValidPassword())
