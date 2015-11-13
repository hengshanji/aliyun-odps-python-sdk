#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

import zlib

import six


class Crc32(object):
    def __init__(self):
        self.crc = None

    def update(self, buf, off, length):
        assert isinstance(buf, (six.binary_type, bytearray))

        to_crc = str(buf[off: off+length])
        if self.crc:
            self.crc = zlib.crc32(to_crc, self.crc)
        else:
            self.crc = zlib.crc32(to_crc)

    def reset(self):
        self.crc = None

    def getvalue(self):
        return self.crc


_CRC_TABLE = (
    0x00000000L, 0xf26b8303L, 0xe13b70f7L, 0x1350f3f4L,
    0xc79a971fL, 0x35f1141cL, 0x26a1e7e8L, 0xd4ca64ebL,
    0x8ad958cfL, 0x78b2dbccL, 0x6be22838L, 0x9989ab3bL,
    0x4d43cfd0L, 0xbf284cd3L, 0xac78bf27L, 0x5e133c24L,
    0x105ec76fL, 0xe235446cL, 0xf165b798L, 0x030e349bL,
    0xd7c45070L, 0x25afd373L, 0x36ff2087L, 0xc494a384L,
    0x9a879fa0L, 0x68ec1ca3L, 0x7bbcef57L, 0x89d76c54L,
    0x5d1d08bfL, 0xaf768bbcL, 0xbc267848L, 0x4e4dfb4bL,
    0x20bd8edeL, 0xd2d60dddL, 0xc186fe29L, 0x33ed7d2aL,
    0xe72719c1L, 0x154c9ac2L, 0x061c6936L, 0xf477ea35L,
    0xaa64d611L, 0x580f5512L, 0x4b5fa6e6L, 0xb93425e5L,
    0x6dfe410eL, 0x9f95c20dL, 0x8cc531f9L, 0x7eaeb2faL,
    0x30e349b1L, 0xc288cab2L, 0xd1d83946L, 0x23b3ba45L,
    0xf779deaeL, 0x05125dadL, 0x1642ae59L, 0xe4292d5aL,
    0xba3a117eL, 0x4851927dL, 0x5b016189L, 0xa96ae28aL,
    0x7da08661L, 0x8fcb0562L, 0x9c9bf696L, 0x6ef07595L,
    0x417b1dbcL, 0xb3109ebfL, 0xa0406d4bL, 0x522bee48L,
    0x86e18aa3L, 0x748a09a0L, 0x67dafa54L, 0x95b17957L,
    0xcba24573L, 0x39c9c670L, 0x2a993584L, 0xd8f2b687L,
    0x0c38d26cL, 0xfe53516fL, 0xed03a29bL, 0x1f682198L,
    0x5125dad3L, 0xa34e59d0L, 0xb01eaa24L, 0x42752927L,
    0x96bf4dccL, 0x64d4cecfL, 0x77843d3bL, 0x85efbe38L,
    0xdbfc821cL, 0x2997011fL, 0x3ac7f2ebL, 0xc8ac71e8L,
    0x1c661503L, 0xee0d9600L, 0xfd5d65f4L, 0x0f36e6f7L,
    0x61c69362L, 0x93ad1061L, 0x80fde395L, 0x72966096L,
    0xa65c047dL, 0x5437877eL, 0x4767748aL, 0xb50cf789L,
    0xeb1fcbadL, 0x197448aeL, 0x0a24bb5aL, 0xf84f3859L,
    0x2c855cb2L, 0xdeeedfb1L, 0xcdbe2c45L, 0x3fd5af46L,
    0x7198540dL, 0x83f3d70eL, 0x90a324faL, 0x62c8a7f9L,
    0xb602c312L, 0x44694011L, 0x5739b3e5L, 0xa55230e6L,
    0xfb410cc2L, 0x092a8fc1L, 0x1a7a7c35L, 0xe811ff36L,
    0x3cdb9bddL, 0xceb018deL, 0xdde0eb2aL, 0x2f8b6829L,
    0x82f63b78L, 0x709db87bL, 0x63cd4b8fL, 0x91a6c88cL,
    0x456cac67L, 0xb7072f64L, 0xa457dc90L, 0x563c5f93L,
    0x082f63b7L, 0xfa44e0b4L, 0xe9141340L, 0x1b7f9043L,
    0xcfb5f4a8L, 0x3dde77abL, 0x2e8e845fL, 0xdce5075cL,
    0x92a8fc17L, 0x60c37f14L, 0x73938ce0L, 0x81f80fe3L,
    0x55326b08L, 0xa759e80bL, 0xb4091bffL, 0x466298fcL,
    0x1871a4d8L, 0xea1a27dbL, 0xf94ad42fL, 0x0b21572cL,
    0xdfeb33c7L, 0x2d80b0c4L, 0x3ed04330L, 0xccbbc033L,
    0xa24bb5a6L, 0x502036a5L, 0x4370c551L, 0xb11b4652L,
    0x65d122b9L, 0x97baa1baL, 0x84ea524eL, 0x7681d14dL,
    0x2892ed69L, 0xdaf96e6aL, 0xc9a99d9eL, 0x3bc21e9dL,
    0xef087a76L, 0x1d63f975L, 0x0e330a81L, 0xfc588982L,
    0xb21572c9L, 0x407ef1caL, 0x532e023eL, 0xa145813dL,
    0x758fe5d6L, 0x87e466d5L, 0x94b49521L, 0x66df1622L,
    0x38cc2a06L, 0xcaa7a905L, 0xd9f75af1L, 0x2b9cd9f2L,
    0xff56bd19L, 0x0d3d3e1aL, 0x1e6dcdeeL, 0xec064eedL,
    0xc38d26c4L, 0x31e6a5c7L, 0x22b65633L, 0xd0ddd530L,
    0x0417b1dbL, 0xf67c32d8L, 0xe52cc12cL, 0x1747422fL,
    0x49547e0bL, 0xbb3ffd08L, 0xa86f0efcL, 0x5a048dffL,
    0x8ecee914L, 0x7ca56a17L, 0x6ff599e3L, 0x9d9e1ae0L,
    0xd3d3e1abL, 0x21b862a8L, 0x32e8915cL, 0xc083125fL,
    0x144976b4L, 0xe622f5b7L, 0xf5720643L, 0x07198540L,
    0x590ab964L, 0xab613a67L, 0xb831c993L, 0x4a5a4a90L,
    0x9e902e7bL, 0x6cfbad78L, 0x7fab5e8cL, 0x8dc0dd8fL,
    0xe330a81aL, 0x115b2b19L, 0x020bd8edL, 0xf0605beeL,
    0x24aa3f05L, 0xd6c1bc06L, 0xc5914ff2L, 0x37faccf1L,
    0x69e9f0d5L, 0x9b8273d6L, 0x88d28022L, 0x7ab90321L,
    0xae7367caL, 0x5c18e4c9L, 0x4f48173dL, 0xbd23943eL,
    0xf36e6f75L, 0x0105ec76L, 0x12551f82L, 0xe03e9c81L,
    0x34f4f86aL, 0xc69f7b69L, 0xd5cf889dL, 0x27a40b9eL,
    0x79b737baL, 0x8bdcb4b9L, 0x988c474dL, 0x6ae7c44eL,
    0xbe2da0a5L, 0x4c4623a6L, 0x5f16d052L, 0xad7d5351L,
    )

_CRC_INIT = 0xffffffffL


class Crc32c(object):

    def __init__(self):
        self.crc = _CRC_INIT

    def update(self, buf, off, length):
        assert isinstance(buf, (six.binary_type, bytearray))
        if isinstance(buf, six.binary_type):
            buf = bytearray(buf)

        to_crc = buf[off: off+length]

        crc = self.crc
        for b in to_crc:
            table_index = (crc ^ b) & 0xff
            crc = (_CRC_TABLE[table_index] ^ (crc >> 8)) & 0xffffffffL
        self.crc = crc & 0xffffffffL

    def reset(self):
        self.crc = _CRC_INIT

    @classmethod
    def _crc_finalize(cls, crc):
        return crc ^ 0xffffffffL

    def getvalue(self):
        return Crc32c._crc_finalize(self.crc)
