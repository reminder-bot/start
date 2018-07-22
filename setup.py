import os
import sqlite3
import configparser

try:
    os.mkdir('../DATA')
except FileExistsError:
    pass

files = ['todos']
contents = ['{}']

for fn, content in zip(files, contents):
    if fn + '.json' in os.listdir('../DATA/'):
        continue

    f = open('../DATA/' + fn + '.json', 'w')
    f.write(content)
    f.close()

if 'config.ini' not in os.listdir('..'):
    config = configparser.ConfigParser()
    config['DEFAULT'] = {
        'token' : 'token',
        'dbl_token' : 'discordbotslist token',
        'patreon_server' : 'serverid',
        'patreon_enabled' : 'yes',
        'strings_location' : './languages/'
    }

    config['WEB'] = {
        'DISCORD_OAUTH_CLIENT_ID' : 'id',
        'DISCORD_OAUTH_CLIENT_SECRET' : 'secretkey',
        'SECRET' : 'secretkey'
    }

    config['MYSQL'] = {
        'user' : 'username',
        'passwd' : 'password',
        'host' : 'localhost',
        'database' : 'reminders'
    }

    with open('../config.ini', 'w') as f:
        config.write(f)
