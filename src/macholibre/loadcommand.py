#!/usr/bin/python

'''
Copyright 2016 Aaron Stephens <aaron@icebrg.io>, ICEBRG

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
'''


class LoadCommand(object):

    # Constructor
    def __init__(self, cmd=None, size=None):
        # Fields
        self.cmd = cmd
        self.size = size
        self.data = {}

    # Generators
    def gen_data(self):
        for i in self.data.iteritems():
            yield i

    # Functions
    def add_data(self, key, value): self.data[key] = value

    def is_segment(self):
        return self.cmd == 'SEGMENT' or self.cmd == 'SEGMENT_64'

