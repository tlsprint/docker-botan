def get_supported_tls(version):
    """Return a list of all TLS versions supported by the specified version."""
    # Default to returning the versions supported by tlsprint
    return ["TLS10", "TLS11", "TLS12"]


def extract_versions(tags):
    # Do not include any pre-releases, as those often don't work properly.
    tags = [tag for tag in tags if "rc" not in tag]

    # For botan, the tags and the versions are actually the same.
    version_info = [{
        "tag": tag,
        "version": tag,
    } for tag in tags]

    # Add info about supported TLS versions
    for info in version_info:
        info["supported_tls"] = get_supported_tls(info["version"])

    return version_info
