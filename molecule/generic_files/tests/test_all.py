def test_borg_binary(host):
    borg = host.file("/usr/local/bin/borg")
    assert borg.exists
    assert borg.user == "root"
    assert borg.group == "root"
    assert borg.mode == 0o755
