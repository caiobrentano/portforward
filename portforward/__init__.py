"""
Kubernetes Port-Forward Go-Edition For Python
"""

from . import _internal


def forward_by_home(namespace: str, pod: str, from_port: int, to_port: int) -> None:
    """
    Connects to a Pod and tunnels traffic from a local port to this pod.
    It uses the kubectl kube config from the home dir.

    :param namespace: Target namespace
    :param pod: Name of target Pod
    :param from_port: Local port
    :param to_port: Port inside the pod
    :return: None
    """

    _validate_str("namespace", namespace)
    _validate_str("pod", pod)

    _validate_port("from_port", from_port)
    _validate_port("to_port", to_port)

    _internal.forward_by_home(namespace, pod, from_port, to_port)


# ===== PRIVATE =====


def _validate_str(arg_name, arg):
    if arg is None or not isinstance(arg, str):
        raise ValueError(f"{arg_name}={arg} is not a valid str")
    if len(arg) == 0:
        raise ValueError(f"{arg_name} cannot be an empty str")


def _validate_port(arg_name, arg):
    in_range = 80 < arg < 65536
    if arg is None or not isinstance(arg, int) or not in_range:
        raise ValueError(f"{arg_name}={arg} is not a valid port")
