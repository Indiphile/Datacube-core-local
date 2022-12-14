# This file is part of the Open Data Cube, see https://opendatacube.org for more information
#
# Copyright (c) 2015-2020 ODC Contributors
# SPDX-License-Identifier: Apache-2.0


class DuplicateRecordError(Exception):
    pass


class MissingRecordError(Exception):
    pass


class IndexSetupError(Exception):
    pass
