# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities
from . import outputs
from ._inputs import *

__all__ = [
    'GetComputeDiskResult',
    'AwaitableGetComputeDiskResult',
    'get_compute_disk',
    'get_compute_disk_output',
]

@pulumi.output_type
class GetComputeDiskResult:
    """
    A collection of values returned by getComputeDisk.
    """
    def __init__(__self__, block_size=None, created_at=None, description=None, disk_id=None, disk_placement_policy=None, folder_id=None, id=None, image_id=None, instance_ids=None, labels=None, name=None, product_ids=None, size=None, snapshot_id=None, status=None, type=None, zone=None):
        if block_size and not isinstance(block_size, int):
            raise TypeError("Expected argument 'block_size' to be a int")
        pulumi.set(__self__, "block_size", block_size)
        if created_at and not isinstance(created_at, str):
            raise TypeError("Expected argument 'created_at' to be a str")
        pulumi.set(__self__, "created_at", created_at)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if disk_id and not isinstance(disk_id, str):
            raise TypeError("Expected argument 'disk_id' to be a str")
        pulumi.set(__self__, "disk_id", disk_id)
        if disk_placement_policy and not isinstance(disk_placement_policy, dict):
            raise TypeError("Expected argument 'disk_placement_policy' to be a dict")
        pulumi.set(__self__, "disk_placement_policy", disk_placement_policy)
        if folder_id and not isinstance(folder_id, str):
            raise TypeError("Expected argument 'folder_id' to be a str")
        pulumi.set(__self__, "folder_id", folder_id)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if image_id and not isinstance(image_id, str):
            raise TypeError("Expected argument 'image_id' to be a str")
        pulumi.set(__self__, "image_id", image_id)
        if instance_ids and not isinstance(instance_ids, list):
            raise TypeError("Expected argument 'instance_ids' to be a list")
        pulumi.set(__self__, "instance_ids", instance_ids)
        if labels and not isinstance(labels, dict):
            raise TypeError("Expected argument 'labels' to be a dict")
        pulumi.set(__self__, "labels", labels)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if product_ids and not isinstance(product_ids, list):
            raise TypeError("Expected argument 'product_ids' to be a list")
        pulumi.set(__self__, "product_ids", product_ids)
        if size and not isinstance(size, int):
            raise TypeError("Expected argument 'size' to be a int")
        pulumi.set(__self__, "size", size)
        if snapshot_id and not isinstance(snapshot_id, str):
            raise TypeError("Expected argument 'snapshot_id' to be a str")
        pulumi.set(__self__, "snapshot_id", snapshot_id)
        if status and not isinstance(status, str):
            raise TypeError("Expected argument 'status' to be a str")
        pulumi.set(__self__, "status", status)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)
        if zone and not isinstance(zone, str):
            raise TypeError("Expected argument 'zone' to be a str")
        pulumi.set(__self__, "zone", zone)

    @property
    @pulumi.getter(name="blockSize")
    def block_size(self) -> int:
        """
        The block size of the disk in bytes.
        """
        return pulumi.get(self, "block_size")

    @property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> str:
        """
        Disk creation timestamp.
        """
        return pulumi.get(self, "created_at")

    @property
    @pulumi.getter
    def description(self) -> str:
        """
        Optional description of this disk.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="diskId")
    def disk_id(self) -> str:
        return pulumi.get(self, "disk_id")

    @property
    @pulumi.getter(name="diskPlacementPolicy")
    def disk_placement_policy(self) -> Optional['outputs.GetComputeDiskDiskPlacementPolicyResult']:
        return pulumi.get(self, "disk_placement_policy")

    @property
    @pulumi.getter(name="folderId")
    def folder_id(self) -> str:
        """
        ID of the folder that the disk belongs to.
        """
        return pulumi.get(self, "folder_id")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="imageId")
    def image_id(self) -> str:
        """
        ID of the source image that was used to create this disk.
        """
        return pulumi.get(self, "image_id")

    @property
    @pulumi.getter(name="instanceIds")
    def instance_ids(self) -> Sequence[str]:
        """
        IDs of instances to which this disk is attached.
        """
        return pulumi.get(self, "instance_ids")

    @property
    @pulumi.getter
    def labels(self) -> Mapping[str, str]:
        """
        Map of labels applied to this disk.
        """
        return pulumi.get(self, "labels")

    @property
    @pulumi.getter
    def name(self) -> str:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="productIds")
    def product_ids(self) -> Sequence[str]:
        """
        License IDs that indicate which licenses are attached to this disk.
        """
        return pulumi.get(self, "product_ids")

    @property
    @pulumi.getter
    def size(self) -> int:
        """
        Size of the disk, specified in Gb.
        """
        return pulumi.get(self, "size")

    @property
    @pulumi.getter(name="snapshotId")
    def snapshot_id(self) -> str:
        """
        Source snapshot that was used to create this disk.
        """
        return pulumi.get(self, "snapshot_id")

    @property
    @pulumi.getter
    def status(self) -> str:
        """
        Status of the disk.
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Type of the disk.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter
    def zone(self) -> str:
        """
        ID of the zone where the disk resides.
        """
        return pulumi.get(self, "zone")


class AwaitableGetComputeDiskResult(GetComputeDiskResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetComputeDiskResult(
            block_size=self.block_size,
            created_at=self.created_at,
            description=self.description,
            disk_id=self.disk_id,
            disk_placement_policy=self.disk_placement_policy,
            folder_id=self.folder_id,
            id=self.id,
            image_id=self.image_id,
            instance_ids=self.instance_ids,
            labels=self.labels,
            name=self.name,
            product_ids=self.product_ids,
            size=self.size,
            snapshot_id=self.snapshot_id,
            status=self.status,
            type=self.type,
            zone=self.zone)


def get_compute_disk(disk_id: Optional[str] = None,
                     disk_placement_policy: Optional[pulumi.InputType['GetComputeDiskDiskPlacementPolicyArgs']] = None,
                     folder_id: Optional[str] = None,
                     name: Optional[str] = None,
                     opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetComputeDiskResult:
    """
    Get information about a Yandex Compute disk. For more information, see
    [the official documentation](https://cloud.yandex.com/docs/compute/concepts/disk).


    :param str disk_id: The ID of a specific disk.
    :param str folder_id: ID of the folder that the disk belongs to.
    :param str name: Name of the disk.
           
           > **NOTE:** One of `disk_id` or `name` should be specified.
    """
    __args__ = dict()
    __args__['diskId'] = disk_id
    __args__['diskPlacementPolicy'] = disk_placement_policy
    __args__['folderId'] = folder_id
    __args__['name'] = name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('yandex:index/getComputeDisk:getComputeDisk', __args__, opts=opts, typ=GetComputeDiskResult).value

    return AwaitableGetComputeDiskResult(
        block_size=__ret__.block_size,
        created_at=__ret__.created_at,
        description=__ret__.description,
        disk_id=__ret__.disk_id,
        disk_placement_policy=__ret__.disk_placement_policy,
        folder_id=__ret__.folder_id,
        id=__ret__.id,
        image_id=__ret__.image_id,
        instance_ids=__ret__.instance_ids,
        labels=__ret__.labels,
        name=__ret__.name,
        product_ids=__ret__.product_ids,
        size=__ret__.size,
        snapshot_id=__ret__.snapshot_id,
        status=__ret__.status,
        type=__ret__.type,
        zone=__ret__.zone)


@_utilities.lift_output_func(get_compute_disk)
def get_compute_disk_output(disk_id: Optional[pulumi.Input[Optional[str]]] = None,
                            disk_placement_policy: Optional[pulumi.Input[Optional[pulumi.InputType['GetComputeDiskDiskPlacementPolicyArgs']]]] = None,
                            folder_id: Optional[pulumi.Input[Optional[str]]] = None,
                            name: Optional[pulumi.Input[Optional[str]]] = None,
                            opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetComputeDiskResult]:
    """
    Get information about a Yandex Compute disk. For more information, see
    [the official documentation](https://cloud.yandex.com/docs/compute/concepts/disk).


    :param str disk_id: The ID of a specific disk.
    :param str folder_id: ID of the folder that the disk belongs to.
    :param str name: Name of the disk.
           
           > **NOTE:** One of `disk_id` or `name` should be specified.
    """
    ...
