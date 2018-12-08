import requests
from bs4 import BeautifulSoup
import directorycontrol
import re


def archive_spider(maxpages):
    # start the "url" and depending on the maxpages parameter given by user it will get ALL links found in the
    # source code of "url"

    page = 0

    # the page portion is brittle code, "url" contains "offset" and "limit" so these values have to tuned to the
    # incrementation of the program as well as the input maximum pages desired.
    # as is, the program provides information on 30 posts per page.
    # so if maxpages is 4, the program should process 120 posts, for example.

    while page <= maxpages:

        url = "https://www.securityfocus.com/cgi-bin/index.cgi?offset=" + str(page) + \
              "&limit=30&c=11&op=display_thread" \
              "s&ListID=1&mode=threaded&expand_all=false"

        srccode = requests.get(url)

        plaintxt = srccode.text

        souptxt = BeautifulSoup(plaintxt, "html.parser")

        # create a text file
        txtfile = open("Archive Links", "w")

        # do a loop for each of the results(messages) found on the archive page
        for link in souptxt.find_all("a", href=re.compile("30/30")):
            href = "https://www.securityfocus.com/" + link.get('href')
            subject = link.string
            srccode = requests.get(href).text
            processedtxt = BeautifulSoup(srccode, "html.parser")

            # grab the date, sender, and the message body
            postdate = processedtxt.find("span","commentDate").text
            postauthor = processedtxt.find("span", "commentAuthor").text
            postbody = processedtxt.find("div", "comments_reply").text

            # this is a list type, contains all words in the message
            # separated by all spaces found in the message, and removing the space character
            bodyprocessed = postbody.split(" ")

            # stores the message list without spaces
            bodypro_string = ' '.join(bodyprocessed)

            # sometimes, CVE ID comes as CVE-???-????, last 4 slot is at least 4, but has no limit of digits
            # looks for CVE-(any number of numeric digits)-(any number of numeric digits)
            cvesearch = re.findall(r"CVE-\d+-\d+", bodypro_string)
            cveid = cvesearch

            # for monitoring on the terminal, terminal may be more readable/useful than the text files
            print(href)
            print(subject)
            print(postdate)
            print(postauthor)
            print(cveid)
            for x in cveid:
                print("https://cve.mitre.org/cgi-bin/cvekey.cgi?keyword=" + x)
            print("\n\n\n")

            # for debugging
            # print("bodyprocessed: ")
            # print(bodyprocessed)

            # takes care of storing information about each individual post in their respective text files
            directorycontrol.fill_list(txtfile, href, subject)
            directorycontrol.compile_postinfo(subject, href, postdate, postauthor, cveid, postbody)

        page += 30

# "https://cve.mitre.org/cgi-bin/cvekey.cgi?keyword=" + (cve id found in the post)


archive_spider(30)

