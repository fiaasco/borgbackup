testinfra_hosts = ["ansible://folders"]


def test_include_exclude(host):
    script = host.file("/usr/local/bin/borg-backup")
    assert script.contains("/var/cache")
    assert script.contains("--exclude '/var/cache/apt'")
    assert script.user == "root"
    assert script.group == "root"
