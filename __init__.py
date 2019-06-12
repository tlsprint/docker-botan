def extract_versions(tags):
    # Do not include any pre-releases, as those often don't work properly.
    tags = [tag for tag in tags if "rc" not in tag]

    # For botan, the tags and the versions are actually the same.
    version_info = [{
        "tag": tag,
        "version": tag,
    } for tag in tags]

    return version_info
