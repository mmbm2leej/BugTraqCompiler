import requests
from bs4 import BeautifulSoup


# this is for the text file that spider.py will name "Archive Links"
def fill_list(txtfile, link, text):
    txtfile.write(link + "\n" + text + "\n\n\n")


def compile_postinfo(subj, href, postdate, postauthor, cveid, postbody):
    postfile = open(subj, "w")  # create a text file for the post
    postfile.write(subj + "\n"  # take the parameters and write them line by line
                   + postauthor + "\n"
                   + postdate + "\n"
                   + href + "\n")
    if cveid is not None:
        for x in cveid:
            postfile.write(x + "\n")
        postfile.write("\n\n\n")
        postfile.write("More about this/these CVE ID(s): + \n")
        for x in cveid:
            cveurl = requests.get("https://cve.mitre.org/cgi-bin/cvekey.cgi?keyword="+x)  # access the database over web
            cveurlplain = cveurl.text
            cveurlprocessed = BeautifulSoup(cveurlplain, "html.parser")

            # this portion below finds the description of the CVE in the list from the website's search engine
            cveinfo0 = cveurlprocessed.find("div", id="TableWithRules")
            cveinfo1 = cveinfo0.findAll("td")
            cveinfofinal = cveinfo1[1].text

            # for testing and debugging
            # print(cveinfo1[1].text)

            # writes the CVE ID followed by retrieved description
            postfile.write(x + "  :  ")
            postfile.write(cveinfofinal + "\n\n")
    postfile.write("\n\n\n")

    # spacing and message body
    soup = str(postbody).replace('<br/>', '\n\n\n')
    postfile.write(soup)

    postfile.close()

