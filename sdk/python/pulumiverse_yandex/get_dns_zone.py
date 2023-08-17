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
    'GetDnsZoneResult',
    'AwaitableGetDnsZoneResult',
    'get_dns_zone',
    'get_dns_zone_output',
]

@pulumi.output_type
class GetDnsZoneResult:
    """
    A collection of values returned by getDnsZone.
    """
    def __init__(__self__, created_at=None, description=None, dns_zone_id=None, folder_id=None, id=None, labels=None, name=None, private_networks=None, public=None, zone=None):
        if created_at and not isinstance(created_at, str):
            raise TypeError("Expected argument 'created_at' to be a str")
        pulumi.set(__self__, "created_at", created_at)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if dns_zone_id and not isinstance(dns_zone_id, str):
            raise TypeError("Expected argument 'dns_zone_id' to be a str")
        pulumi.set(__self__, "dns_zone_id", dns_zone_id)
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
        if private_networks and not isinstance(private_networks, list):
            raise TypeError("Expected argument 'private_networks' to be a list")
        pulumi.set(__self__, "private_networks", private_networks)
        if public and not isinstance(public, bool):
            raise TypeError("Expected argument 'public' to be a bool")
        pulumi.set(__self__, "public", public)
        if zone and not isinstance(zone, str):
            raise TypeError("Expected argument 'zone' to be a str")
        pulumi.set(__self__, "zone", zone)

    @property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> str:
        """
        (Computed) The DNS zone creation timestamp.
        """
        return pulumi.get(self, "created_at")

    @property
    @pulumi.getter
    def description(self) -> str:
        """
        (Computed) Description of the DNS zone.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="dnsZoneId")
    def dns_zone_id(self) -> str:
        return pulumi.get(self, "dns_zone_id")

    @property
    @pulumi.getter(name="folderId")
    def folder_id(self) -> str:
        """
        (Computed) The ID of the folder that the resource belongs to. If it is not provided, the default provider folder is used.
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
        (Computed) A set of key/value label pairs to assign to the DNS zone.
        """
        return pulumi.get(self, "labels")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        (Computed) User assigned name of a specific resource. Must be unique within the folder.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="privateNetworks")
    def private_networks(self) -> Sequence[str]:
        """
        (Computed) For privately visible zones, the set of Virtual Private Cloud resources that the zone is visible from.
        """
        return pulumi.get(self, "private_networks")

    @property
    @pulumi.getter
    def public(self) -> bool:
        """
        (Computed) The zone's visibility: public zones are exposed to the Internet, while private zones are visible only to Virtual Private Cloud resources.
        """
        return pulumi.get(self, "public")

    @property
    @pulumi.getter
    def zone(self) -> str:
        """
        (Computed) The DNS name of this zone, e.g. "example.com.". Must ends with dot.
        """
        return pulumi.get(self, "zone")


class AwaitableGetDnsZoneResult(GetDnsZoneResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetDnsZoneResult(
            created_at=self.created_at,
            description=self.description,
            dns_zone_id=self.dns_zone_id,
            folder_id=self.folder_id,
            id=self.id,
            labels=self.labels,
            name=self.name,
            private_networks=self.private_networks,
            public=self.public,
            zone=self.zone)


def get_dns_zone(dns_zone_id: Optional[str] = None,
                 folder_id: Optional[str] = None,
                 name: Optional[str] = None,
                 opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetDnsZoneResult:
    """
    Get information about a DNS Zone.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_yandex as yandex

    foo = yandex.get_dns_zone(dns_zone_id=%!v(PANIC=Format method: runtime error: invalid memory address or nil pointer dereference))
    pulumi.export("zone", foo.zone)
    ```


    :param str dns_zone_id: The ID of the DNS Zone.
    :param str folder_id: Folder that the resource belongs to. If value is omitted, the default provider folder is used.
    :param str name: Name of the DNS Zone.
           
           > **NOTE:** One of `dns_zone_id` or `name` should be specified.
    """
    __args__ = dict()
    __args__['dnsZoneId'] = dns_zone_id
    __args__['folderId'] = folder_id
    __args__['name'] = name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('yandex:index/getDnsZone:getDnsZone', __args__, opts=opts, typ=GetDnsZoneResult).value

    return AwaitableGetDnsZoneResult(
        created_at=__ret__.created_at,
        description=__ret__.description,
        dns_zone_id=__ret__.dns_zone_id,
        folder_id=__ret__.folder_id,
        id=__ret__.id,
        labels=__ret__.labels,
        name=__ret__.name,
        private_networks=__ret__.private_networks,
        public=__ret__.public,
        zone=__ret__.zone)


@_utilities.lift_output_func(get_dns_zone)
def get_dns_zone_output(dns_zone_id: Optional[pulumi.Input[Optional[str]]] = None,
                        folder_id: Optional[pulumi.Input[Optional[str]]] = None,
                        name: Optional[pulumi.Input[Optional[str]]] = None,
                        opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetDnsZoneResult]:
    """
    Get information about a DNS Zone.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_yandex as yandex

    foo = yandex.get_dns_zone(dns_zone_id=%!v(PANIC=Format method: runtime error: invalid memory address or nil pointer dereference))
    pulumi.export("zone", foo.zone)
    ```


    :param str dns_zone_id: The ID of the DNS Zone.
    :param str folder_id: Folder that the resource belongs to. If value is omitted, the default provider folder is used.
    :param str name: Name of the DNS Zone.
           
           > **NOTE:** One of `dns_zone_id` or `name` should be specified.
    """
    ...