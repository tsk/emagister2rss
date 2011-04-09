# -*- coding: utf-8 -*-

import sys
from xml.etree.ElementTree import ElementTree
from lxml import etree
from datetime import datetime as dt
import PyRSS2Gen as PyRSS2

def rss_wall(page, opener):
    data = []
    parsedPage = etree.HTML(page)
    divs = parsedPage.xpath("//div")
    for div in divs:
        try:
            if div.attrib['class'] == "app_wall_item_container":
                l = len(div)
                if l == 3:
                    idata = []
                    for element in div:
                        if element.attrib['class'] == "app_wall_item_content":
                            bs = element.xpath(".//b")
                            for b in bs:
                                if b.attrib['class']=="wallTit":
                                    linkdeb = b.xpath(".//a")[0]
                                    idata.append(`linkdeb.text`)
                                    idata.append(linkdeb.attrib['href'])
                            spans = element.xpath(".//span")
                            for span in spans:
                                if span.attrib['class'] == "wallFecha":
                                    idata.append(`span.text`)
                                if span.attrib['class'] == "wallDescr":
                                    idata.append(`span.text`)
                    data.append(idata)
        except:
            pass
    items = [PyRSS2.RSSItem(title=d[0],link=d[1],description=d[2]+": "+d[3]) for d in data]

    rss = PyRSS2.RSS2(
        title = "Wall Emagister",
        link = ("http://localhost:8080/statics/feeds/wall.rss"),
        description = "",
        lastBuildDate = dt.utcnow(),
        items = items,)
    rss.write_xml(open("static/feeds/wall.rss","w"))

def rss_group(page, group_name, group_link):
    data = []
    parsedPage = etree.HTML(page)
    divs = parsedPage.xpath("//div")
    for div in divs:
        try:
            if div.attrib['class'] == "app_wall_item_container":
                l = len(div)
                if l == 3:
                    idata = []
                    for element in div:
                        if element.attrib['class'] == "app_wall_item_content":
                            bs = element.xpath(".//b")
                            for b in bs:
                                if b.attrib['class']=="wallTit":
                                    linkdeb = b.xpath(".//a")[0]
                                    idata.append(`linkdeb.text`)
                                    idata.append(linkdeb.attrib['href'])
                            spans = element.xpath(".//span")
                            for span in spans:
                                if span.attrib['class'] == "wallFecha":
                                    idata.append(`span.text`)
                                if span.attrib['class'] == "wallDescr":
                                    idata.append(`span.text`)
                    data.append(idata)
        except:
            pass
    items = [PyRSS2.RSSItem(title=d[0],link=d[1],description=d[2]+": "+d[3]) for d in data]
    rssdst = group_link.split('/')[3]
    rss = PyRSS2.RSS2(
        title = str(group_name),
        link = ("http://localhost:8080/statics/feeds/"),
        description = "",
        lastBuildDate = dt.utcnow(),
        items = items,)
    rss.write_xml(open("static/feeds/"+rssdst+".rss","w"))


def rss_groups(page,opener):
    groups = {}
    parsedPage = etree.HTML(page)
    links = parsedPage.xpath("//a")
    for link in links:
        try:
            if link.attrib['class'] == "titulo":
                group_name = link.text
                group_link = link.attrib['href']
                print "parsing "+group_name
                rss_group(opener.open(group_link).read(),group_name,group_link)
        except:
            pass
    #search for more groups pages
    for link in links:
        if link.text == ' siguiente >':
            rss_groups(opener.open("http://grupos.emagister.com"+link.attrib['href']).read(),opener)
