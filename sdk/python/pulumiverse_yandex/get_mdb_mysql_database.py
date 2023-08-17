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
    'GetMdbMysqlDatabaseResult',
    'AwaitableGetMdbMysqlDatabaseResult',
    'get_mdb_mysql_database',
    'get_mdb_mysql_database_output',
]

@pulumi.output_type
class GetMdbMysqlDatabaseResult:
    """
    A collection of values returned by getMdbMysqlDatabase.
    """
    def __init__(__self__, cluster_id=None, id=None, name=None):
        if cluster_id and not isinstance(cluster_id, str):
            raise TypeError("Expected argument 'cluster_id' to be a str")
        pulumi.set(__self__, "cluster_id", cluster_id)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter(name="clusterId")
    def cluster_id(self) -> str:
        return pulumi.get(self, "cluster_id")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> str:
        return pulumi.get(self, "name")


class AwaitableGetMdbMysqlDatabaseResult(GetMdbMysqlDatabaseResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetMdbMysqlDatabaseResult(
            cluster_id=self.cluster_id,
            id=self.id,
            name=self.name)


def get_mdb_mysql_database(cluster_id: Optional[str] = None,
                           name: Optional[str] = None,
                           opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetMdbMysqlDatabaseResult:
    """
    Use this data source to access information about an existing resource.
    """
    __args__ = dict()
    __args__['clusterId'] = cluster_id
    __args__['name'] = name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('yandex:index/getMdbMysqlDatabase:getMdbMysqlDatabase', __args__, opts=opts, typ=GetMdbMysqlDatabaseResult).value

    return AwaitableGetMdbMysqlDatabaseResult(
        cluster_id=__ret__.cluster_id,
        id=__ret__.id,
        name=__ret__.name)


@_utilities.lift_output_func(get_mdb_mysql_database)
def get_mdb_mysql_database_output(cluster_id: Optional[pulumi.Input[str]] = None,
                                  name: Optional[pulumi.Input[str]] = None,
                                  opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetMdbMysqlDatabaseResult]:
    """
    Use this data source to access information about an existing resource.
    """
    ...
