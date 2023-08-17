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
    'GetMdbGreenplumClusterResult',
    'AwaitableGetMdbGreenplumClusterResult',
    'get_mdb_greenplum_cluster',
    'get_mdb_greenplum_cluster_output',
]

@pulumi.output_type
class GetMdbGreenplumClusterResult:
    """
    A collection of values returned by getMdbGreenplumCluster.
    """
    def __init__(__self__, accesses=None, assign_public_ip=None, backup_window_starts=None, cluster_id=None, created_at=None, deletion_protection=None, description=None, environment=None, folder_id=None, greenplum_config=None, health=None, id=None, labels=None, maintenance_windows=None, master_host_count=None, master_hosts=None, master_subclusters=None, name=None, network_id=None, pooler_config=None, security_group_ids=None, segment_host_count=None, segment_hosts=None, segment_in_host=None, segment_subclusters=None, status=None, subnet_id=None, user_name=None, version=None, zone=None):
        if accesses and not isinstance(accesses, list):
            raise TypeError("Expected argument 'accesses' to be a list")
        pulumi.set(__self__, "accesses", accesses)
        if assign_public_ip and not isinstance(assign_public_ip, bool):
            raise TypeError("Expected argument 'assign_public_ip' to be a bool")
        pulumi.set(__self__, "assign_public_ip", assign_public_ip)
        if backup_window_starts and not isinstance(backup_window_starts, list):
            raise TypeError("Expected argument 'backup_window_starts' to be a list")
        pulumi.set(__self__, "backup_window_starts", backup_window_starts)
        if cluster_id and not isinstance(cluster_id, str):
            raise TypeError("Expected argument 'cluster_id' to be a str")
        pulumi.set(__self__, "cluster_id", cluster_id)
        if created_at and not isinstance(created_at, str):
            raise TypeError("Expected argument 'created_at' to be a str")
        pulumi.set(__self__, "created_at", created_at)
        if deletion_protection and not isinstance(deletion_protection, bool):
            raise TypeError("Expected argument 'deletion_protection' to be a bool")
        pulumi.set(__self__, "deletion_protection", deletion_protection)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if environment and not isinstance(environment, str):
            raise TypeError("Expected argument 'environment' to be a str")
        pulumi.set(__self__, "environment", environment)
        if folder_id and not isinstance(folder_id, str):
            raise TypeError("Expected argument 'folder_id' to be a str")
        pulumi.set(__self__, "folder_id", folder_id)
        if greenplum_config and not isinstance(greenplum_config, dict):
            raise TypeError("Expected argument 'greenplum_config' to be a dict")
        pulumi.set(__self__, "greenplum_config", greenplum_config)
        if health and not isinstance(health, str):
            raise TypeError("Expected argument 'health' to be a str")
        pulumi.set(__self__, "health", health)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if labels and not isinstance(labels, dict):
            raise TypeError("Expected argument 'labels' to be a dict")
        pulumi.set(__self__, "labels", labels)
        if maintenance_windows and not isinstance(maintenance_windows, list):
            raise TypeError("Expected argument 'maintenance_windows' to be a list")
        pulumi.set(__self__, "maintenance_windows", maintenance_windows)
        if master_host_count and not isinstance(master_host_count, int):
            raise TypeError("Expected argument 'master_host_count' to be a int")
        pulumi.set(__self__, "master_host_count", master_host_count)
        if master_hosts and not isinstance(master_hosts, list):
            raise TypeError("Expected argument 'master_hosts' to be a list")
        pulumi.set(__self__, "master_hosts", master_hosts)
        if master_subclusters and not isinstance(master_subclusters, list):
            raise TypeError("Expected argument 'master_subclusters' to be a list")
        pulumi.set(__self__, "master_subclusters", master_subclusters)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if network_id and not isinstance(network_id, str):
            raise TypeError("Expected argument 'network_id' to be a str")
        pulumi.set(__self__, "network_id", network_id)
        if pooler_config and not isinstance(pooler_config, dict):
            raise TypeError("Expected argument 'pooler_config' to be a dict")
        pulumi.set(__self__, "pooler_config", pooler_config)
        if security_group_ids and not isinstance(security_group_ids, list):
            raise TypeError("Expected argument 'security_group_ids' to be a list")
        pulumi.set(__self__, "security_group_ids", security_group_ids)
        if segment_host_count and not isinstance(segment_host_count, int):
            raise TypeError("Expected argument 'segment_host_count' to be a int")
        pulumi.set(__self__, "segment_host_count", segment_host_count)
        if segment_hosts and not isinstance(segment_hosts, list):
            raise TypeError("Expected argument 'segment_hosts' to be a list")
        pulumi.set(__self__, "segment_hosts", segment_hosts)
        if segment_in_host and not isinstance(segment_in_host, int):
            raise TypeError("Expected argument 'segment_in_host' to be a int")
        pulumi.set(__self__, "segment_in_host", segment_in_host)
        if segment_subclusters and not isinstance(segment_subclusters, list):
            raise TypeError("Expected argument 'segment_subclusters' to be a list")
        pulumi.set(__self__, "segment_subclusters", segment_subclusters)
        if status and not isinstance(status, str):
            raise TypeError("Expected argument 'status' to be a str")
        pulumi.set(__self__, "status", status)
        if subnet_id and not isinstance(subnet_id, str):
            raise TypeError("Expected argument 'subnet_id' to be a str")
        pulumi.set(__self__, "subnet_id", subnet_id)
        if user_name and not isinstance(user_name, str):
            raise TypeError("Expected argument 'user_name' to be a str")
        pulumi.set(__self__, "user_name", user_name)
        if version and not isinstance(version, str):
            raise TypeError("Expected argument 'version' to be a str")
        pulumi.set(__self__, "version", version)
        if zone and not isinstance(zone, str):
            raise TypeError("Expected argument 'zone' to be a str")
        pulumi.set(__self__, "zone", zone)

    @property
    @pulumi.getter
    def accesses(self) -> Sequence['outputs.GetMdbGreenplumClusterAccessResult']:
        return pulumi.get(self, "accesses")

    @property
    @pulumi.getter(name="assignPublicIp")
    def assign_public_ip(self) -> bool:
        return pulumi.get(self, "assign_public_ip")

    @property
    @pulumi.getter(name="backupWindowStarts")
    def backup_window_starts(self) -> Sequence['outputs.GetMdbGreenplumClusterBackupWindowStartResult']:
        return pulumi.get(self, "backup_window_starts")

    @property
    @pulumi.getter(name="clusterId")
    def cluster_id(self) -> str:
        return pulumi.get(self, "cluster_id")

    @property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> str:
        return pulumi.get(self, "created_at")

    @property
    @pulumi.getter(name="deletionProtection")
    def deletion_protection(self) -> bool:
        return pulumi.get(self, "deletion_protection")

    @property
    @pulumi.getter
    def description(self) -> str:
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def environment(self) -> str:
        return pulumi.get(self, "environment")

    @property
    @pulumi.getter(name="folderId")
    def folder_id(self) -> str:
        return pulumi.get(self, "folder_id")

    @property
    @pulumi.getter(name="greenplumConfig")
    def greenplum_config(self) -> Mapping[str, str]:
        return pulumi.get(self, "greenplum_config")

    @property
    @pulumi.getter
    def health(self) -> str:
        return pulumi.get(self, "health")

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
        return pulumi.get(self, "labels")

    @property
    @pulumi.getter(name="maintenanceWindows")
    def maintenance_windows(self) -> Sequence['outputs.GetMdbGreenplumClusterMaintenanceWindowResult']:
        return pulumi.get(self, "maintenance_windows")

    @property
    @pulumi.getter(name="masterHostCount")
    def master_host_count(self) -> int:
        return pulumi.get(self, "master_host_count")

    @property
    @pulumi.getter(name="masterHosts")
    def master_hosts(self) -> Sequence['outputs.GetMdbGreenplumClusterMasterHostResult']:
        return pulumi.get(self, "master_hosts")

    @property
    @pulumi.getter(name="masterSubclusters")
    def master_subclusters(self) -> Sequence['outputs.GetMdbGreenplumClusterMasterSubclusterResult']:
        return pulumi.get(self, "master_subclusters")

    @property
    @pulumi.getter
    def name(self) -> str:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="networkId")
    def network_id(self) -> str:
        return pulumi.get(self, "network_id")

    @property
    @pulumi.getter(name="poolerConfig")
    def pooler_config(self) -> Optional['outputs.GetMdbGreenplumClusterPoolerConfigResult']:
        return pulumi.get(self, "pooler_config")

    @property
    @pulumi.getter(name="securityGroupIds")
    def security_group_ids(self) -> Sequence[str]:
        return pulumi.get(self, "security_group_ids")

    @property
    @pulumi.getter(name="segmentHostCount")
    def segment_host_count(self) -> int:
        return pulumi.get(self, "segment_host_count")

    @property
    @pulumi.getter(name="segmentHosts")
    def segment_hosts(self) -> Sequence['outputs.GetMdbGreenplumClusterSegmentHostResult']:
        return pulumi.get(self, "segment_hosts")

    @property
    @pulumi.getter(name="segmentInHost")
    def segment_in_host(self) -> int:
        return pulumi.get(self, "segment_in_host")

    @property
    @pulumi.getter(name="segmentSubclusters")
    def segment_subclusters(self) -> Sequence['outputs.GetMdbGreenplumClusterSegmentSubclusterResult']:
        return pulumi.get(self, "segment_subclusters")

    @property
    @pulumi.getter
    def status(self) -> str:
        return pulumi.get(self, "status")

    @property
    @pulumi.getter(name="subnetId")
    def subnet_id(self) -> str:
        return pulumi.get(self, "subnet_id")

    @property
    @pulumi.getter(name="userName")
    def user_name(self) -> str:
        return pulumi.get(self, "user_name")

    @property
    @pulumi.getter
    def version(self) -> str:
        return pulumi.get(self, "version")

    @property
    @pulumi.getter
    def zone(self) -> str:
        return pulumi.get(self, "zone")


class AwaitableGetMdbGreenplumClusterResult(GetMdbGreenplumClusterResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetMdbGreenplumClusterResult(
            accesses=self.accesses,
            assign_public_ip=self.assign_public_ip,
            backup_window_starts=self.backup_window_starts,
            cluster_id=self.cluster_id,
            created_at=self.created_at,
            deletion_protection=self.deletion_protection,
            description=self.description,
            environment=self.environment,
            folder_id=self.folder_id,
            greenplum_config=self.greenplum_config,
            health=self.health,
            id=self.id,
            labels=self.labels,
            maintenance_windows=self.maintenance_windows,
            master_host_count=self.master_host_count,
            master_hosts=self.master_hosts,
            master_subclusters=self.master_subclusters,
            name=self.name,
            network_id=self.network_id,
            pooler_config=self.pooler_config,
            security_group_ids=self.security_group_ids,
            segment_host_count=self.segment_host_count,
            segment_hosts=self.segment_hosts,
            segment_in_host=self.segment_in_host,
            segment_subclusters=self.segment_subclusters,
            status=self.status,
            subnet_id=self.subnet_id,
            user_name=self.user_name,
            version=self.version,
            zone=self.zone)


def get_mdb_greenplum_cluster(cluster_id: Optional[str] = None,
                              folder_id: Optional[str] = None,
                              greenplum_config: Optional[Mapping[str, str]] = None,
                              name: Optional[str] = None,
                              pooler_config: Optional[pulumi.InputType['GetMdbGreenplumClusterPoolerConfigArgs']] = None,
                              opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetMdbGreenplumClusterResult:
    """
    Use this data source to access information about an existing resource.
    """
    __args__ = dict()
    __args__['clusterId'] = cluster_id
    __args__['folderId'] = folder_id
    __args__['greenplumConfig'] = greenplum_config
    __args__['name'] = name
    __args__['poolerConfig'] = pooler_config
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('yandex:index/getMdbGreenplumCluster:getMdbGreenplumCluster', __args__, opts=opts, typ=GetMdbGreenplumClusterResult).value

    return AwaitableGetMdbGreenplumClusterResult(
        accesses=__ret__.accesses,
        assign_public_ip=__ret__.assign_public_ip,
        backup_window_starts=__ret__.backup_window_starts,
        cluster_id=__ret__.cluster_id,
        created_at=__ret__.created_at,
        deletion_protection=__ret__.deletion_protection,
        description=__ret__.description,
        environment=__ret__.environment,
        folder_id=__ret__.folder_id,
        greenplum_config=__ret__.greenplum_config,
        health=__ret__.health,
        id=__ret__.id,
        labels=__ret__.labels,
        maintenance_windows=__ret__.maintenance_windows,
        master_host_count=__ret__.master_host_count,
        master_hosts=__ret__.master_hosts,
        master_subclusters=__ret__.master_subclusters,
        name=__ret__.name,
        network_id=__ret__.network_id,
        pooler_config=__ret__.pooler_config,
        security_group_ids=__ret__.security_group_ids,
        segment_host_count=__ret__.segment_host_count,
        segment_hosts=__ret__.segment_hosts,
        segment_in_host=__ret__.segment_in_host,
        segment_subclusters=__ret__.segment_subclusters,
        status=__ret__.status,
        subnet_id=__ret__.subnet_id,
        user_name=__ret__.user_name,
        version=__ret__.version,
        zone=__ret__.zone)


@_utilities.lift_output_func(get_mdb_greenplum_cluster)
def get_mdb_greenplum_cluster_output(cluster_id: Optional[pulumi.Input[Optional[str]]] = None,
                                     folder_id: Optional[pulumi.Input[Optional[str]]] = None,
                                     greenplum_config: Optional[pulumi.Input[Optional[Mapping[str, str]]]] = None,
                                     name: Optional[pulumi.Input[Optional[str]]] = None,
                                     pooler_config: Optional[pulumi.Input[Optional[pulumi.InputType['GetMdbGreenplumClusterPoolerConfigArgs']]]] = None,
                                     opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetMdbGreenplumClusterResult]:
    """
    Use this data source to access information about an existing resource.
    """
    ...
