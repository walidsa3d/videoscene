import re

from operator import methodcaller
from scenedata import definitions


def parse(filename):
    """ parse a scene release string and return a dictionary of parsed values."""
    screensize = re.compile('720p|1080p', re.I)
    quality = re.compile(
        '\.(AHDTV|MBluRay|MDVDR|CAM|TS|TELESYNC|DVDSCR|DVD9|BDSCR|DDC|R5LINE|R5|DVDRip|HDRip|BRRip|BDRip|WEBRip|WEB-?HD|HDtv|PDTV|WEBDL|BluRay)', re.I)
    year = re.compile('(1|2)\d{3}')
    series = re.compile('s\d{1,3}e\d{1,3}', re.I)
    group = re.compile('[A-Za-z0-9]+$', re.I)
    video = re.compile('Xvid|MP4|NTSC|PAL|[xh][\.\s]?264', re.I)
    audio = re.compile('AAC2[\.\s]0|AAC|AC3|DTS|DD5', re.I)
    edition = re.compile(
        '\.(UNRATED|DC|(Directors|EXTENDED)[\.\s](CUT|EDITION)|EXTENDED|3D|2D|\bNF\b)',
        re.I)
    tags = re.compile(
        '\.(COMPLETE|LiMiTED|DL|DUAL|iNTERNAL|UNCUT|FS|FESTIVAL|DOKU|DOCU|DUBBED|SUBBED|WS)', re.I)
    release = re.compile(
        'REAL[\.\s]PROPER|REMASTERED|PROPER|REPACK|READNFO|READ[\.\s]NFO|DiRFiX|NFOFiX', re.I)
    subtitles = re.compile(
        '\.(MULTi(SUBS)?|FiNNiSH|NORDiC|DANiSH|SWEDiSH|NORWEGiAN|iTALiAN|SPANiSH|SWESUB)', re.I)
    language = re.compile('\.(German|ITALIAN|Chinese|CZECH|RUSSIAN|FRENCH|TRUEFRENCH)', re.I)

    title = filename
    attrs = {'screenSize': screensize,
             'quality': quality,
             'year': year,
             'series': series,
             'release_group': group,
             'video': video,
             'audio': audio,
             'edition': edition,
             'tags': tags,
             'release': release,
             'subtitles': subtitles,
             'language': language
             }
    data = {}
    for attr in attrs:
        match = methodcaller('search', filename)(attrs[attr])
        if match:
            matched = methodcaller('group')(match)
            data[attr] = matched.strip('.')
            title = re.sub(matched, '', title)
    if 'series' in data:
        s, e = re.split('e|E', data['series'])
        # use lstrip to remove leading zeros
        data['season'] = s[1:].lstrip('0')
        data['episode'] = e.lstrip('0')
        data['series'] = True
    temptitle = title.replace('.', ' ').strip('-').strip()
    data['title'] = re.sub('\s{2,}', ' ', temptitle)
    return data


def explain(tag):
    """explain scene release tags in plain english"""
    return definitions[tag.lower()]
