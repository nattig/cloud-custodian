# Copyright 2017-2018 Capital One Services, LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
from c7n_gcp.query import QueryResourceManager

from c7n.provider import gcp


@gcp.register('instance')
class Instance(QueryResourceManager):

    class resource_type(object):
        service = 'compute'
        version = 'v1'
        component = 'instance'


@gcp.register('image')
class Image(QueryResourceManager):

    class resource_type(object):
        service = 'compute'
        version = 'v1'
        component = 'images'


@gcp.register('disk')
class Disk(QueryResourceManager):

    class resource_type(object):
        service = 'compute'
        version = 'v1'
        component = 'disks'
