# plugs/topic.py
#
#

__copyright__ = 'this file is in the public domain'
__gendocfirst__ = ['topic-set', ]

from gozerbot.commands import cmnds
from gozerbot.examples import examples
from gozerbot.plughelp import plughelp
import time

plughelp.add('topic', 'manage the topic of a channel')

def checktopicmode(bot, ievent):
    """ callback for change in channel topic mode """
    chan = ievent.channel
    mode = bot.channels.get(chan, 'mode')
    if mode and 't' in mode:
        if chan not in bot.state['opchan']:
            ievent.reply("i'm not op on %s" % chan)
            return 0
    return 1

def handle_gettopic(bot, ievent):
    """ topic [<channel>] .. get topic """
    try:
        channel = ievent.args[0]
    except IndexError:
        channel = ievent.channel
    result = bot.gettopic(channel)
    if not result:
        ievent.reply("can't get topic data of channel %s" % channel)
    else:
        (what, who, when) = result
        ievent.reply('topic on %s is %s made by %s on %s' % \
(channel, what, who, time.ctime(when)))

cmnds.add('topic', handle_gettopic, 'USER', threaded=True)
examples.add('topic', 'topic [<channel>] .. get topic', '1) topic 2) topic \
#dunkbots')

def handle_topicset(bot, ievent):
    """ topic-set .. set the topic """
    if not bot.jabber and not checktopicmode(bot, ievent):
        return
    if not ievent.rest:
        ievent.missing('<what>')
        return
    bot.settopic(ievent.channel, ievent.rest)

cmnds.add('topic-set', handle_topicset, 'USER', allowqueue=False)
examples.add('topic-set', 'set channel topic', 'topic-set Yooo')

def handle_topicadd(bot, ievent):
    """ topic-add <txt> .. add topic item """
    if not bot.jabber and not checktopicmode(bot, ievent):
        return
    if not ievent.rest:
        ievent.missing("<what>")
        return
    result = bot.gettopic(ievent.channel)
    if not result:
        ievent.reply("can't get topic data")
        return
    what = result[0]
    what += " | %s" % ievent.rest
    bot.settopic(ievent.channel, what)

cmnds.add('topic-add', handle_topicadd, 'USER', threaded=True)
examples.add('topic-add', 'topic-add <txt> .. add a topic item', \
'topic-add mekker')

def handle_topicdel(bot, ievent):
    """ topic-del <topicnr> .. delete topic item """
    if not bot.jabber and not checktopicmode(bot, ievent):
        return
    try:
        topicnr = int(ievent.args[0])
    except (IndexError, ValueError):
        ievent.reply('i need a integer as argument')
        return
    if topicnr < 1:
        ievent.reply('topic items start at 1')
        return
    result = bot.gettopic(ievent.channel)
    if not result:
        ievent.reply("can't get topic data")
        return
    what = result[0].split(' | ')
    if topicnr > len(what):
        ievent.reply('there are only %s topic items' % len(what))
        return
    del what[topicnr-1]
    newtopic = ' | '.join(what)
    bot.settopic(ievent.channel, newtopic)

cmnds.add('topic-del', handle_topicdel, 'USER', threaded=True)
examples.add('topic-del', 'topic-del <topicnr> .. delete topic item', \
'topic-del 1')

def handle_topicmove(bot, ievent):
    """ topic-move <nrfrom> <nrto> .. move topic item """
    if not bot.jabber and not checktopicmode(bot, ievent):
        return
    try:
        (topicfrom, topicto) = ievent.args
    except ValueError:
        ievent.missing('<from> <to>')
        return
    try:
        topicfrom = int(topicfrom)
        topicto = int(topicto)
    except ValueError:
        ievent.reply('i need two integers as arguments')
        return
    if topicfrom < 1 or topicto < 1:
        ievent.reply('topic items start at 1')
        return
    topicdata = bot.gettopic(ievent.channel)
    if not topicdata:
        ievent.reply("can't get topic data")
        return
    splitted = topicdata[0].split(' | ')
    if topicfrom > len(splitted) or topicto > len(splitted):
        ievent.reply('max item is %s' % len(splitted))
        return
    tmp = splitted[topicfrom-1]
    del splitted[topicfrom-1]
    splitted.insert(topicto-1, tmp)
    newtopic = ' | '.join(splitted)
    bot.settopic(ievent.channel, newtopic)

cmnds.add('topic-move', handle_topicmove, 'USER', threaded=True)
examples.add('topic-move', 'topic-move <nrfrom> <nrto> .. move topic \
items', 'topic-move 3 1')

def handle_topiclistadd(bot, ievent):
    """ topic-listadd <topicnr> <person> .. add a person to a topic list """
    if not bot.jabber and not checktopicmode(bot, ievent):
        return
    try:
        (topicnr, person) = ievent.args
    except ValueError:
        ievent.missing('<topicnr> <person>')
        return
    try:
        topicnr = int(topicnr)
    except ValueError:
        ievent.reply('i need an integer as topicnr')
        return
    if topicnr < 1:
        ievent.reply('topic items start at 1')
        return
    topicdata = bot.gettopic(ievent.channel)
    if not topicdata:
        ievent.reply("can't get topic data")
        return
    splitted = topicdata[0].split(' | ')
    if topicnr > len(splitted):
        ievent.reply('max item is %s' % len(splitted))
        return
    try:
        topic = splitted[topicnr-1]
    except IndexError:
        ievent.reply('no %s topic found' % str(topicnr))
        return
    if topic.strip().endswith(':'):
        topic += " %s" % person
    else:
        topic += ",%s" % person
    splitted[topicnr-1] = topic
    newtopic = ' | '.join(splitted)
    bot.settopic(ievent.channel, newtopic)

cmnds.add('topic-listadd', handle_topiclistadd, 'USER', threaded=True)
examples.add('topic-listadd', 'topic-listadd <toicnr> <person> .. add user to \
topiclist', 'topic-listadd 1 bart')

def handle_topiclistdel(bot, ievent):
    """ topic-listdel <topicnr> <person> .. remove person from topic list """
    if not bot.jabber and not checktopicmode(bot, ievent):
        return
    try:
        (topicnr, person) = ievent.args
    except ValueError:
        ievent.missing('<topicnr> <person>')
        return
    try:
        topicnr = int(topicnr)
    except ValueError:
        ievent.reply('i need an integer as topicnr')
        return
    if topicnr < 1:
        ievent.reply('topic items start at 1')
        return
    topicdata = bot.gettopic(ievent.channel)
    if not topicdata:
        ievent.reply("can't get topic data")
        return
    splitted = topicdata[0].split(' | ')
    if topicnr > len(splitted):
        ievent.reply('max item is %s' % len(splitted))
        return
    try:
        topic = splitted[topicnr-1]
    except IndexError:
        ievent.reply('no %s topic found' % str(topicnr))
        return
    if not person in topic:
        ievent.reply('%s is not on the list' % person)
        return
    l = topic.rsplit(':', 1)
    try:
        persons = l[-1].split(',')
        persons = [i.strip() for i in persons]
        persons.remove(person)
    except ValueError:
        ievent.reply('no %s in list' % person)
        return
    except IndexError:
        ievent.reply('i need a : in the topic to work properly')
        return
    splitted[topicnr-1] = "%s: %s" % (l[0], ','.join(persons))
    newtopic = ' | '.join(splitted)
    bot.settopic(ievent.channel, newtopic)

cmnds.add('topic-listdel', handle_topiclistdel, 'USER', threaded=True)
examples.add('topic-listdel', 'topic-listdel <topicnr> <person> .. delete \
 user from topiclist', 'topic-listdel 1 bart')
