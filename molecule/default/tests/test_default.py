import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_docker_is_running(host):
    cmd = host.service('docker')
    assert cmd.is_running
    assert cmd.is_enabled


def test_docker_daemon_connection(host):
    c = host.run('docker ps')
    assert c.rc == 0


def test_docker_container_start(host):
    with host.sudo():
        c = host.run('docker run --rm alpine:3.12.0 cat /etc/alpine-release')
        assert c.rc == 0
        assert '3.12.0' in c.stdout


def test_diskover_running(host):
    c = host.run('docker ps')
    assert 'diskover' in c.stdout
    assert 'elasticsearch' in c.stdout
    assert 'redis' in c.stdout
    assert c.rc == 0


def test_sshfs_installed(host):
    c = host.run(
        'docker exec diskover_diskover_1 sshfs --version'
    )
    assert c.rc == 0
    assert 'SSHFS version' in c.stdout


def test_key_mount(host):
    f = host.file('/opt/docker/diskover/diskover.key')
    assert f.is_file
    assert f.user == 'root'
    assert oct(f.mode) == '0o600'
    assert f.contains('BEGIN OPENSSH PRIVATE KEY')
