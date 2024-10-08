#!/usr/bin/python3
# Copyright 2016 Red Hat, Inc.
# Copyright 2024 Ericsson Software Technology
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

import base64
import io

from fake_ipa import base


class LogExtension(base.BaseAgentExtension):

    @base.sync_command('collect_system_logs')
    def collect_system_logs(self):
        """Collect system logs.

        Collect and package diagnostic and support data from the ramdisk.

        :raises: CommandExecutionError if failed to collect the system logs.
        :returns: A dictionary with the key `system_logs` and the value
                  of a gzipped and base64 encoded string of the file with
                  the logs.
        """
        logs = collect_system_logs()
        return {'system_logs': logs}


def _encode_as_text(s):
    if isinstance(s, str):
        s = s.encode('utf-8')
    s = base64.b64encode(s)
    return s.decode('ascii')


def collect_system_logs(journald_max_lines=None):
    """Collect system logs.

    :param journald_max_lines: Maximum number of lines to retrieve from
                               the journald. if None, return everything.
    :returns: A tar, gzip base64 encoded string with the logs.
    """

    with io.BytesIO() as fp:
        return _encode_as_text(fp.getvalue())
