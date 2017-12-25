#!/usr/bin/python
# coding: utf-8

from hdfs.util.exceptions.illegalArgumentException \
    import IllegalArgumentException

class BlockConstructionStage(object):
    PIPELINE_SETUP_APPEND = 1
    PIPELINE_SETUP_APPEND_RECOVERY = 2
    DATA_STREAMING = 3
    PIPELINE_SETUP_STREAMING_RECOVERY = 4
    PIPELINE_CLOSE = 5
    PIPELINE_CLOSE_RECOVERY = 6
    PIPELINE_SETUP_CREATE = 7
    PIPELINE_RBW = 8
    TRANSFER_FINALIZED = 9

    RECOVERY_BIT = bytes.fromhex("1")

    def __init__(self, stage):
        self.stage = stage

    def get_recovery_stage(self):
        if self.stage == BlockConstructionStage.PIPELINE_SETUP_CREATE:
            raise IllegalArgumentException("Unexcepted blockStage" + self.stage)
        else:
            self.stage | BlockConstructionStage.RECOVERY_BIT


