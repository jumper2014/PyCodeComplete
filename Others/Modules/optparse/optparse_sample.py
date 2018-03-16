# coding=utf-8
#

import optparse

if __name__ == '__main__':
    parser = optparse.OptionParser(
        usage="%prog [optons] [<arg1> <arg2> ...]",
        version="1.0"
    )
    parser.add_option('-p', '--peer', dest='peer_num',
                      type='int', default=10, help='how many peer to start')
    parser.add_option('-l', '--lf', dest='lf_num',
                      type='int', default=20, help='how many lf to start')
    (options, args) = parser.parse_args()
    peer_num = options.peer_num
    lf_num = options.lf_num
    print "peer num is:", peer_num
    print "lf num is:", lf_num
