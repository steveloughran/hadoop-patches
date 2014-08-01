# !/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Licensed to the Apache Software Foundation (ASF) under one or more
# contributor license agreements.  See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.
# The ASF licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import sys
import subprocess




def read(pipe, line):
  """
  read a char, append to the listing if there is a char that is not \n
  :param pipe: pipe to read from 
  :param line: line being built up
  :return: (the potentially updated line, flag indicating newline reached)
  """

  c = pipe.read(1)
  if c != "":
    o = c.decode('utf-8')
    if o != '\n':
      line += o
      return line, False
    else:
      return line, True
  else:
    return line, False


def runProcess(commandline):
  """
  Run a process
  :param commandline: command line 
  :return:the return code
  """
  print "ready to exec : %s" % commandline
  exe = subprocess.Popen(commandline,
                         stdin=None,
                         stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE,
                         shell=False)
  stdout = exe.stdout
  stderr = exe.stderr
  outline = ""
  errline = ""
  while exe.poll() is None:
    # process is running; grab output and echo every line
    outline, done = read(stdout, outline)
    if done:
      print outline
      outline = ""
    errline, done = read(stderr, errline)
    if done:
      print errline
      errline = ""

  # get tail
  out, err = exe.communicate()
  print outline + out.decode()
  print errline + err.decode()
  return exe.returncode

def maven(args):
  cli = ["maven"]
  cli.extend(args)
  return runProcess(cli)


if __name__ == '__main__':
  """
  Entry point
  """
  try:
    returncode = maven(sys.argv)
  except Exception as e:
    print "Exception: %s " % e.message
    returncode = -1

  sys.exit(returncode)