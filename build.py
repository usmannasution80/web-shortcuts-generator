from sites import sites
import os
from shutil import copytree, rmtree, copy2

dirname = 'htmls'
icondirname = dirname + '/icons'
redirectScript = 'redirect.js'

def createHtmlFile(name, url):
  htmlFile = dirname + '/' + name + '.html'

  htmlContent = '''<html>
  <head>
    <title>{title}</title>
    <link rel="icon" href="{icon}"/>
    <script src="redirect.js"></script>
    <script>
      redirect('{url}');
    </script>
  </head>
  </html>'''.format(
    title = name,
    url = url,
    icon = icondirname.replace(dirname + '/', '') + '/' + name + '.png'
  )

  file = open(htmlFile, 'w')
  file.write(htmlContent)
  file.close()

if os.path.isdir(icondirname):
  rmtree(icondirname)

if not os.path.isdir(dirname + '/' + redirectScript):
  copy2(
    redirectScript,
    dirname + '/' + redirectScript
  )

copytree(
  icondirname.replace(dirname + '/', ''),
  icondirname
)

if not os.path.isdir(dirname):
  os.makedirs(dirname)

for key in sites.keys():

  createHtmlFile(
    key,
    sites[key]
  )
