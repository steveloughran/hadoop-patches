#!/usr/bin/env python
import os
import re
import subprocess
import logging
import optparse

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(levelname)s %(message)s')

def main():

#print sys.argv 

echo maven install with none of the tests

mvn -o -DskipTests install