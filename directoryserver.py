import web
import shelve
import os
import sys

urls = (
    '/(.*)/', 'redirect',
    '/(.*)', 'example'
)

class example:
    def GET(self,filename):
        s = shelve.open('dir_db')
        try:
            f_dir = s[filename]
        finally:
            s.close()
        fullpath = os.path.join(f_dir, filename)
        f = open(fullpath,"r")
        return f.read()
class redirect:
    def GET(self, path):
        web.seeother('/' + path)

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
