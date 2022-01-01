#!/usr/bin/python3

import bs4
# https://docs.python.org/3/library/configparser.html
import configparser
import os
import sys

def check_first_run():
    print('os.path.join(os.getcwd(), \'bookmarks.ini\'): ')
    print (os.path.join(os.getcwd(), 'bookmarks.ini'))
    config = configparser.ConfigParser()
    config.read('bookmarks.ini')
    print('config.sections(): ' + str(config.sections()))
    w3m_directory = config['DEFAULT']['w3m_directory']
    print('w3m_directory: ' + str(w3m_directory))
    is_dir = os.path.isdir(w3m_directory)    
    if w3m_directory == '':
        print('*** CONFIG BLANK: ***\n\'w3m_directory\' config variable is blank. Fix this in the \'bookmarks.ini\' file and re-run program.')
        sys.exit()
    elif is_dir == False:
        print('*** CONFIG INCORRECT: ***\n\'w3m_directory\' config variable does not. Fix this in the \'bookmarks.ini\' file and re-run program.')
        sys.exit()
    else:
        return w3m_directory

def sort_links(w3m_directory):
    # NOTE :Adjust the directory with whatever your user is on your system:
    # bookmarks_file = open('/home/sam/.w3m/bookmark.html')

    try:
        # print('\nEntering try block...')
        bookmarks_file = str(w3m_directory + '/bookmark.html')
        # print('bookmarks_file = ' + str(bookmarks_file))
        soup = bs4.BeautifulSoup(open(bookmarks_file, encoding="utf8"), 'html.parser')
        h2_list = soup.find_all("h2")
        ul_list = soup.find_all("ul")
        # print('h2_list: ' + str(h2_list))
        # print('ul_list: ' + str(ul_list))

        h2_string_list = []

        for item in h2_list:
            # print('\nCycling through h2_list...')
            # print('item: ' + str(item))
            h2_string = item.string
            # print('h2_string: ' + str(h2_string))
            h2_string_list.append(h2_string)

        # print('h2_string_list: ' + str(h2_string_list))
        sorted_h2_list = sorted(h2_string_list)
        # print('sorted_h2_list: ' + str(sorted_h2_list))

        index_list = []

        for item in sorted_h2_list:
            # print('\nCycling through sorted_h2_list')
            # print('item: ' + str(item))
            index_list.append(h2_string_list.index(item))

        # print('index_list: ' + str(index_list))
        # print('h2_list: ' + str(h2_list))
        # print('ul_list: ' + str(ul_list))
        
        return index_list, h2_list, ul_list

    except:
        raise Exception('***CONFIG ERROR: ***\n\'w3m_directory\' is not a valid: Correct this and re-run \'main.py\'')


def output_file(w3m_directory, index_list, h2_list, ul_list):
    # with open('/home/sam/.w3m/bookmark.html', 'w') as f:
    with open(str(w3m_directory) + '/bookmark.html', 'w') as f:
        f.write('<html><head><title>Bookmarks</title></head>')
        f.write('\n')
        f.write('<body>')
        f.write('\n')
        f.write('<h1>Bookmarks</h1>')
        f.write('\n')
        for item in index_list:
            f.write(str(h2_list[item]))
            f.write('\n')
            f.write(str(ul_list[item]))
            f.write('\n')
        f.write('</body>')
        f.write('\n')
        f.write('</html>')
    f.close()


def main():
    w3m_directory = check_first_run()
    index_list, h2_list, ul_list = sort_links(w3m_directory)
    output_file(w3m_directory, index_list, h2_list, ul_list)


if __name__ == "__main__":
    main()
