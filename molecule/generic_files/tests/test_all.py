import pytest
from testinfra.utils.ansible_runner import AnsibleRunner

testinfra_hosts = ["ansible://all"]


def test_borg_package(host):
    ans_dict = host.ansible.get_variables()
    package = ans_dict['borgbackup_install_from_pkg']
    if package is True:
      borg = host.package("borgbackup")
      assert borg.is_installed
    else:
      borg = host.file("/usr/local/bin/borg")
      assert borg.exists
      assert borg.user == "root"
      assert borg.group == "root"
      assert borg.mode == 0o755
