# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['ServerlessContainerIamBindingArgs', 'ServerlessContainerIamBinding']

@pulumi.input_type
class ServerlessContainerIamBindingArgs:
    def __init__(__self__, *,
                 container_id: pulumi.Input[str],
                 members: pulumi.Input[Sequence[pulumi.Input[str]]],
                 role: pulumi.Input[str],
                 sleep_after: Optional[pulumi.Input[int]] = None):
        """
        The set of arguments for constructing a ServerlessContainerIamBinding resource.
        :param pulumi.Input[str] container_id: The [Yandex Serverless Container](https://cloud.yandex.com/docs/serverless-containers/) ID to apply a binding to.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] members: Identities that will be granted the privilege in `role`.
               Each entry can have one of the following values:
               * **userAccount:{user_id}**: A unique user ID that represents a specific Yandex account.
               * **serviceAccount:{service_account_id}**: A unique service account ID.
               * **system:{allUsers|allAuthenticatedUsers}**: see [system groups](https://cloud.yandex.com/docs/iam/concepts/access-control/system-group)
        :param pulumi.Input[str] role: The role that should be applied.
        """
        pulumi.set(__self__, "container_id", container_id)
        pulumi.set(__self__, "members", members)
        pulumi.set(__self__, "role", role)
        if sleep_after is not None:
            pulumi.set(__self__, "sleep_after", sleep_after)

    @property
    @pulumi.getter(name="containerId")
    def container_id(self) -> pulumi.Input[str]:
        """
        The [Yandex Serverless Container](https://cloud.yandex.com/docs/serverless-containers/) ID to apply a binding to.
        """
        return pulumi.get(self, "container_id")

    @container_id.setter
    def container_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "container_id", value)

    @property
    @pulumi.getter
    def members(self) -> pulumi.Input[Sequence[pulumi.Input[str]]]:
        """
        Identities that will be granted the privilege in `role`.
        Each entry can have one of the following values:
        * **userAccount:{user_id}**: A unique user ID that represents a specific Yandex account.
        * **serviceAccount:{service_account_id}**: A unique service account ID.
        * **system:{allUsers|allAuthenticatedUsers}**: see [system groups](https://cloud.yandex.com/docs/iam/concepts/access-control/system-group)
        """
        return pulumi.get(self, "members")

    @members.setter
    def members(self, value: pulumi.Input[Sequence[pulumi.Input[str]]]):
        pulumi.set(self, "members", value)

    @property
    @pulumi.getter
    def role(self) -> pulumi.Input[str]:
        """
        The role that should be applied.
        """
        return pulumi.get(self, "role")

    @role.setter
    def role(self, value: pulumi.Input[str]):
        pulumi.set(self, "role", value)

    @property
    @pulumi.getter(name="sleepAfter")
    def sleep_after(self) -> Optional[pulumi.Input[int]]:
        return pulumi.get(self, "sleep_after")

    @sleep_after.setter
    def sleep_after(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "sleep_after", value)


@pulumi.input_type
class _ServerlessContainerIamBindingState:
    def __init__(__self__, *,
                 container_id: Optional[pulumi.Input[str]] = None,
                 members: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 role: Optional[pulumi.Input[str]] = None,
                 sleep_after: Optional[pulumi.Input[int]] = None):
        """
        Input properties used for looking up and filtering ServerlessContainerIamBinding resources.
        :param pulumi.Input[str] container_id: The [Yandex Serverless Container](https://cloud.yandex.com/docs/serverless-containers/) ID to apply a binding to.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] members: Identities that will be granted the privilege in `role`.
               Each entry can have one of the following values:
               * **userAccount:{user_id}**: A unique user ID that represents a specific Yandex account.
               * **serviceAccount:{service_account_id}**: A unique service account ID.
               * **system:{allUsers|allAuthenticatedUsers}**: see [system groups](https://cloud.yandex.com/docs/iam/concepts/access-control/system-group)
        :param pulumi.Input[str] role: The role that should be applied.
        """
        if container_id is not None:
            pulumi.set(__self__, "container_id", container_id)
        if members is not None:
            pulumi.set(__self__, "members", members)
        if role is not None:
            pulumi.set(__self__, "role", role)
        if sleep_after is not None:
            pulumi.set(__self__, "sleep_after", sleep_after)

    @property
    @pulumi.getter(name="containerId")
    def container_id(self) -> Optional[pulumi.Input[str]]:
        """
        The [Yandex Serverless Container](https://cloud.yandex.com/docs/serverless-containers/) ID to apply a binding to.
        """
        return pulumi.get(self, "container_id")

    @container_id.setter
    def container_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "container_id", value)

    @property
    @pulumi.getter
    def members(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        Identities that will be granted the privilege in `role`.
        Each entry can have one of the following values:
        * **userAccount:{user_id}**: A unique user ID that represents a specific Yandex account.
        * **serviceAccount:{service_account_id}**: A unique service account ID.
        * **system:{allUsers|allAuthenticatedUsers}**: see [system groups](https://cloud.yandex.com/docs/iam/concepts/access-control/system-group)
        """
        return pulumi.get(self, "members")

    @members.setter
    def members(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "members", value)

    @property
    @pulumi.getter
    def role(self) -> Optional[pulumi.Input[str]]:
        """
        The role that should be applied.
        """
        return pulumi.get(self, "role")

    @role.setter
    def role(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "role", value)

    @property
    @pulumi.getter(name="sleepAfter")
    def sleep_after(self) -> Optional[pulumi.Input[int]]:
        return pulumi.get(self, "sleep_after")

    @sleep_after.setter
    def sleep_after(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "sleep_after", value)


class ServerlessContainerIamBinding(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 container_id: Optional[pulumi.Input[str]] = None,
                 members: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 role: Optional[pulumi.Input[str]] = None,
                 sleep_after: Optional[pulumi.Input[int]] = None,
                 __props__=None):
        """
        ## yandex\\_serverless\\_container\\_iam\\_binding

        ```python
        import pulumi
        import pulumiverse_yandex as yandex

        container_iam = yandex.ServerlessContainerIamBinding("container-iam",
            container_id="your-container-id",
            members=["system:allUsers"],
            role="serverless.containers.invoker")
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] container_id: The [Yandex Serverless Container](https://cloud.yandex.com/docs/serverless-containers/) ID to apply a binding to.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] members: Identities that will be granted the privilege in `role`.
               Each entry can have one of the following values:
               * **userAccount:{user_id}**: A unique user ID that represents a specific Yandex account.
               * **serviceAccount:{service_account_id}**: A unique service account ID.
               * **system:{allUsers|allAuthenticatedUsers}**: see [system groups](https://cloud.yandex.com/docs/iam/concepts/access-control/system-group)
        :param pulumi.Input[str] role: The role that should be applied.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ServerlessContainerIamBindingArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        ## yandex\\_serverless\\_container\\_iam\\_binding

        ```python
        import pulumi
        import pulumiverse_yandex as yandex

        container_iam = yandex.ServerlessContainerIamBinding("container-iam",
            container_id="your-container-id",
            members=["system:allUsers"],
            role="serverless.containers.invoker")
        ```

        :param str resource_name: The name of the resource.
        :param ServerlessContainerIamBindingArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ServerlessContainerIamBindingArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 container_id: Optional[pulumi.Input[str]] = None,
                 members: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 role: Optional[pulumi.Input[str]] = None,
                 sleep_after: Optional[pulumi.Input[int]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ServerlessContainerIamBindingArgs.__new__(ServerlessContainerIamBindingArgs)

            if container_id is None and not opts.urn:
                raise TypeError("Missing required property 'container_id'")
            __props__.__dict__["container_id"] = container_id
            if members is None and not opts.urn:
                raise TypeError("Missing required property 'members'")
            __props__.__dict__["members"] = members
            if role is None and not opts.urn:
                raise TypeError("Missing required property 'role'")
            __props__.__dict__["role"] = role
            __props__.__dict__["sleep_after"] = sleep_after
        super(ServerlessContainerIamBinding, __self__).__init__(
            'yandex:index/serverlessContainerIamBinding:serverlessContainerIamBinding',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            container_id: Optional[pulumi.Input[str]] = None,
            members: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            role: Optional[pulumi.Input[str]] = None,
            sleep_after: Optional[pulumi.Input[int]] = None) -> 'ServerlessContainerIamBinding':
        """
        Get an existing ServerlessContainerIamBinding resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] container_id: The [Yandex Serverless Container](https://cloud.yandex.com/docs/serverless-containers/) ID to apply a binding to.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] members: Identities that will be granted the privilege in `role`.
               Each entry can have one of the following values:
               * **userAccount:{user_id}**: A unique user ID that represents a specific Yandex account.
               * **serviceAccount:{service_account_id}**: A unique service account ID.
               * **system:{allUsers|allAuthenticatedUsers}**: see [system groups](https://cloud.yandex.com/docs/iam/concepts/access-control/system-group)
        :param pulumi.Input[str] role: The role that should be applied.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _ServerlessContainerIamBindingState.__new__(_ServerlessContainerIamBindingState)

        __props__.__dict__["container_id"] = container_id
        __props__.__dict__["members"] = members
        __props__.__dict__["role"] = role
        __props__.__dict__["sleep_after"] = sleep_after
        return ServerlessContainerIamBinding(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="containerId")
    def container_id(self) -> pulumi.Output[str]:
        """
        The [Yandex Serverless Container](https://cloud.yandex.com/docs/serverless-containers/) ID to apply a binding to.
        """
        return pulumi.get(self, "container_id")

    @property
    @pulumi.getter
    def members(self) -> pulumi.Output[Sequence[str]]:
        """
        Identities that will be granted the privilege in `role`.
        Each entry can have one of the following values:
        * **userAccount:{user_id}**: A unique user ID that represents a specific Yandex account.
        * **serviceAccount:{service_account_id}**: A unique service account ID.
        * **system:{allUsers|allAuthenticatedUsers}**: see [system groups](https://cloud.yandex.com/docs/iam/concepts/access-control/system-group)
        """
        return pulumi.get(self, "members")

    @property
    @pulumi.getter
    def role(self) -> pulumi.Output[str]:
        """
        The role that should be applied.
        """
        return pulumi.get(self, "role")

    @property
    @pulumi.getter(name="sleepAfter")
    def sleep_after(self) -> pulumi.Output[Optional[int]]:
        return pulumi.get(self, "sleep_after")

