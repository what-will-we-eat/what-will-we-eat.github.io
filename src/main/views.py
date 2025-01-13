from bs4 import BeautifulSoup as bs
from django.shortcuts import render, redirect
from glob import glob
from lxml import etree
import io
import json
import markdown
import os
import re
#import six
#import pybtex
#import pybtex.database.input.bibtex
#import pybtex.plugin


####################
# Helper functions #
####################
def mk_html(_file):
    with open(_file, "r") as inf:
        return markdown.markdown(inf.read(), extensions=["sane_lists", "tables"])


def fix_ni(ni):
    meta = {}
    md = []
    meta_block = None
    title_found = False
    with open(ni, "r") as inf:
        lines = inf.readlines()
    for line in lines:
        if line.startswith("---"):
            if meta_block is None:
                meta_block = True
            elif meta_block == True:
                meta_block = False
        elif line.startswith("+ ") and meta_block == True:
            k = re.search(r'\+\s(\S*):', line).group(1)
            v = re.search(f':(.*)', line).group(1)
            meta[k] = v
        else:
            md.append(line)
    md2 = []
    for line in md:
        if line.startswith("# ") and title_found == False:
            title_found = True
            line = f"#{line}"
            md2.append(line)
            md2.append(f"<small>{meta['date']} {meta['place']} &mdash;{meta['author'].strip()}</small><br>")
        elif line.startswith("#"):
            md2.append(f"#{line}")
        else:
            md2.append(line)
    return markdown.markdown(''.join(md2), extensions=["sane_lists", "tables"])


def get_bios(team):
    for k, v in team.items():
        v['bio'] = mk_html(f"main/markdown/team-bios/{k}-bio.md")
    return team


def get_publications(team):
    for k, v in team.items():
        if os.path.exists(f"main/bibtex/{k}/references.html"):
            p = []
            with open(f"main/bibtex/{k}/references.html", 'r') as html:
                soup = bs(html, "html.parser")
            bib_data = soup.find_all("li")
            for ref in bib_data:
                ref = str(ref).replace("<li>", '<li><p class="pubP">').replace("</li>", "</p></li>")
                p.append(ref)
                print(ref)
            if len(p) > 0:
                team[k]["recent_publications"] = p
    return team



##################
# View functions #
##################
def landing(request):
    context = {
            "md": mk_html(f"main/markdown/landing.md")
        }
    return render(request, 'main/landing.html', context)


def program(request):
    context = {
            "title": "What will we eat? Research Program",
            "md": mk_html("main/markdown/research-program.md")
        }
    return render(request, 'main/research-program.html', context)


def team(request):
    with open("main/json/team.json", "r") as inf:
        team = json.load(inf)
    team = get_bios(team)
    team = get_publications(team)
    context = {
        "title": "What will we eat? Team",
        "team": team
    }
    return render(request, 'main/team.html', context)




def news(request):
    context = {
        "title": "What will we eat? News and Info",
        "nis": []
    }
    news_items = glob("main/markdown/news-n-info/*.md")
    news_items = [ni for ni in news_items if ni != "main/markdown/news-n-info/_template.md"]
    news_items.sort(reverse=True)
    for ni in news_items:
        context["nis"].append(fix_ni(ni))
    return render(request, "main/news-info.html", context)





def output(request):
    context = {
        "title": "What will we eat? Research output",
        "publications": None,
        "talks": None
    }
    if os.path.exists("main/bibtex/project/publications.html"):
        p = []
        with open("main/bibtex/project/publications.html", "r") as html:
            soup = bs(html, "html.parser")
        bib_data = soup.find_all("li")
        for ref in bib_data:
            ref = str(ref).replace("<li>", '<li><p class="pubP">').replace("</li>", "</p></li>")
            p.append(ref)
        if len(p) > 0:
            context["publications"] = p
    if os.path.exists("main/bibtex/project/talks.html"):
        p = []
        with open("main/bibtex/project/talks.html", "r") as html:
            soup = bs(html, "html.parser")
        bib_data = soup.find_all("li")
        for ref in bib_data:
            ref = str(ref).replace("<li>", '<li><p class="pubP">').replace("</li>", "</p></li>")
            p.append(ref)
        if len(p) > 0:
            context["talks"] = p
    return render(request, "main/output.html", context)
