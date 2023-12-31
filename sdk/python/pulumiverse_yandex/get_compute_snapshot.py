# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = [
    'GetComputeSnapshotResult',
    'AwaitableGetComputeSnapshotResult',
    'get_compute_snapshot',
    'get_compute_snapshot_output',
]

@pulumi.output_type
class GetComputeSnapshotResult:
    """
    A collection of values returned by getComputeSnapshot.
    """
    def __init__(__self__, created_at=None, description=None, disk_size=None, folder_id=None, id=None, labels=None, name=None, product_ids=None, snapshot_id=None, source_disk_id=None, status=None, storage_size=None):
        if created_at and not isinstance(created_at, str):
            raise TypeError("Expected argument 'created_at' to be a str")
        pulumi.set(__self__, "created_at", created_at)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if disk_size and not isinstance(disk_size, int):
            raise TypeError("Expected argument 'disk_size' to be a int")
        pulumi.set(__self__, "disk_size", disk_size)
        if folder_id and not isinstance(folder_id, str):
            raise TypeError("Expected argument 'folder_id' to be a str")
        pulumi.set(__self__, "folder_id", folder_id)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if labels and not isinstance(labels, dict):
            raise TypeError("Expected argument 'labels' to be a dict")
        pulumi.set(__self__, "labels", labels)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if product_ids and not isinstance(product_ids, list):
            raise TypeError("Expected argument 'product_ids' to be a list")
        pulumi.set(__self__, "product_ids", product_ids)
        if snapshot_id and not isinstance(snapshot_id, str):
            raise TypeError("Expected argument 'snapshot_id' to be a str")
        pulumi.set(__self__, "snapshot_id", snapshot_id)
        if source_disk_id and not isinstance(source_disk_id, str):
            raise TypeError("Expected argument 'source_disk_id' to be a str")
        pulumi.set(__self__, "source_disk_id", source_disk_id)
        if status and not isinstance(status, str):
            raise TypeError("Expected argument 'status' to be a str")
        pulumi.set(__self__, "status", status)
        if storage_size and not isinstance(storage_size, int):
            raise TypeError("Expected argument 'storage_size' to be a int")
        pulumi.set(__self__, "storage_size", storage_size)

    @property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> str:
        """
        Snapshot creation timestamp.
        """
        return pulumi.get(self, "created_at")

    @property
    @pulumi.getter
    def description(self) -> str:
        """
        An optional description of this snapshot.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="diskSize")
    def disk_size(self) -> int:
        """
        Minimum required size of the disk which is created from this snapshot.
        """
        return pulumi.get(self, "disk_size")

    @property
    @pulumi.getter(name="folderId")
    def folder_id(self) -> str:
        """
        ID of the folder that the snapshot belongs to.
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
    @pulumi.getter
    def labels(self) -> Mapping[str, str]:
        """
        A map of labels applied to this snapshot.
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
        License IDs that indicate which licenses are attached to this snapshot.
        """
        return pulumi.get(self, "product_ids")

    @property
    @pulumi.getter(name="snapshotId")
    def snapshot_id(self) -> str:
        return pulumi.get(self, "snapshot_id")

    @property
    @pulumi.getter(name="sourceDiskId")
    def source_disk_id(self) -> str:
        """
        ID of the source disk.
        """
        return pulumi.get(self, "source_disk_id")

    @property
    @pulumi.getter
    def status(self) -> str:
        """
        The status of the snapshot.
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter(name="storageSize")
    def storage_size(self) -> int:
        """
        The size of the snapshot, specified in Gb.
        """
        return pulumi.get(self, "storage_size")


class AwaitableGetComputeSnapshotResult(GetComputeSnapshotResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetComputeSnapshotResult(
            created_at=self.created_at,
            description=self.description,
            disk_size=self.disk_size,
            folder_id=self.folder_id,
            id=self.id,
            labels=self.labels,
            name=self.name,
            product_ids=self.product_ids,
            snapshot_id=self.snapshot_id,
            source_disk_id=self.source_disk_id,
            status=self.status,
            storage_size=self.storage_size)


def get_compute_snapshot(folder_id: Optional[str] = None,
                         name: Optional[str] = None,
                         snapshot_id: Optional[str] = None,
                         opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetComputeSnapshotResult:
    """
    Get information about a Yandex Compute snapshot. For more information, see
    [the official documentation](https://cloud.yandex.com/docs/compute/concepts/snapshot).


    :param str folder_id: ID of the folder that the snapshot belongs to.
    :param str name: The name of the snapshot.
           
           > **NOTE:** One of `snapshot_id` or `name` should be specified.
    :param str snapshot_id: The ID of a specific snapshot.
    """
    __args__ = dict()
    __args__['folderId'] = folder_id
    __args__['name'] = name
    __args__['snapshotId'] = snapshot_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('yandex:index/getComputeSnapshot:getComputeSnapshot', __args__, opts=opts, typ=GetComputeSnapshotResult).value

    return AwaitableGetComputeSnapshotResult(
        created_at=__ret__.created_at,
        description=__ret__.description,
        disk_size=__ret__.disk_size,
        folder_id=__ret__.folder_id,
        id=__ret__.id,
        labels=__ret__.labels,
        name=__ret__.name,
        product_ids=__ret__.product_ids,
        snapshot_id=__ret__.snapshot_id,
        source_disk_id=__ret__.source_disk_id,
        status=__ret__.status,
        storage_size=__ret__.storage_size)


@_utilities.lift_output_func(get_compute_snapshot)
def get_compute_snapshot_output(folder_id: Optional[pulumi.Input[Optional[str]]] = None,
                                name: Optional[pulumi.Input[Optional[str]]] = None,
                                snapshot_id: Optional[pulumi.Input[Optional[str]]] = None,
                                opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetComputeSnapshotResult]:
    """
    Get information about a Yandex Compute snapshot. For more information, see
    [the official documentation](https://cloud.yandex.com/docs/compute/concepts/snapshot).


    :param str folder_id: ID of the folder that the snapshot belongs to.
    :param str name: The name of the snapshot.
           
           > **NOTE:** One of `snapshot_id` or `name` should be specified.
    :param str snapshot_id: The ID of a specific snapshot.
    """
    ...
