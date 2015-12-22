#!/usr/bin/python

# Experimetal


from mininet.net import Mininet
from mininet.node import Node, Switch, RemoteController
from mininet.link import Link, Intf
from mininet.log import setLogLevel, info
from mininet.cli import CLI

def main():

    net = Mininet()
    net.addController('c0', controller=RemoteController, ip="127.0.0.1", port=6633)

    spine0 = net.addRouter('spine0', bgpdConfFilei="./configs/spine0/bgpd.conf", zebraConfFile="./configs/spine0/zebra.conf")
    #spine1 = net.addRouter('spine1', bgpdConfFilei="./configs/spine1/bgpd.conf", zebraConfFile="./configs/spine1/zebra.conf")
    leaf0 = net.addRouter('leaf0', bgpdConfFilei="./configs/leaf0/bgpd.conf", zebraConfFile="./configs/leaf0/zebra.conf")
    #leaf1 = net.addRouter('leaf1', bgpdConfFilei="./configs/leaf1/bgpd.conf", zebraConfFile="./configs/leaf1/zebra.conf")

    net.addLink(spine0, leaf0)

    net.start()

    net.stop()


if __name__ == '__main__':
    setLogLevel('info')
    main()
