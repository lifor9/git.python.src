#!/usr/bin/python
# -*- coding: utf-8 -*-

import paramiko
import os
import platform

# sample code
# paramiko를 이용하여 python으로 ssh command line 실행 및 file, directory upload 하기
# 출처: https://greenfishblog.tistory.com/258
ssh = get_ssh("xxx.xxx.xxx.xxx", 22, "root", "root")  # ssh context를 생성

exitcode=ssh_execute(ssh, "ls /root -laR")              # ssh 명령 실행, 해당 명령의 stdout, stderr를 함께 출력
print("result : %d" % exitcode)                         # command-line을 실행하기 위한 과정에서 에러가 발생하면 exception이 발생합니다.

sftp = get_sftp(ssh)                                    # sftp context를 생성
file_upload(sftp, "aaa.txt", "/home/admin/bbb")         # File Upload 명령을 실행

close_ssh(ssh)
close_sftp(sftp)

# sftp 상에 경로를 생성한다.
# remote 경로가 directory 이면, is_dir 에 True 를 전달한다.
def get_ssh(hostip, port, id, pw):
    try:
        # ssh client 생성
        ssh = paramiko.SSHClient()

        # ssh 정책 설정
        # set_missing_host_key_policy(policy)를 이용하여 host keys를 받아 저장할 것인지 아닌지를 판단하게 되는데.
        # 기본값은 RejectPolicy로 되어있으며, yes를 받아와야한다면 AutoAddPolicy를 사용하도록 한다.
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        # connect
        ssh.connect(hostname=hostip, port=port, username=id, password=pw)
    except Exception e:
        print(e)
        raise e
    return ssh

# ssh 명령을 수행
def ssh_execute(ssh):
    # ssh 명령의 결과로 exit status를 구하는게 쉽지 않다.
    # 따라서, 명령의 끝에 "mark=$?"를 출력하여,
    # 최종 exit statud를 구할 수 있도록 한다.
    exit_status=0
    mark="ssh_helper_result_mark!!@@="
    command=command+";echo " + mark + "$?"

    # exec_command를 실행하게되면, 값을 3개를 tuple로 받아온다.
    # stdin, stdout, stderr이다.
    try:
        stdin, stdout, stderr = ssh.exec_command(command, get_pty=True)
    except Exception as e:
        print(e)
        raise  e
    # stdin, stdout, stderr = ssh.exec_command()
    # stdout.readlines()
    # for line in stdout.read().splitlines():
    #     print(line)
    for line in stdout:
        msg=line.strip('\n')
        if (msg.startswith(mark)):
            exit_status=msg[len(mark):]
        else:
            if(True==is_print):
                print(line.strip('\n'))

    # 만약 sudo명령어가 필요한 경우,
    # stdin, stdout, stderr = ssh.exec_command('sudo')
    # stdin.write('lol\n')
    # stdin.flush()
    # data = stdout.read()

    return int(exit_status)

def get_sftp(ssh):
    try:
        sftp = paramiko.SFTPClient.from_transport(ssh.get_transport())
    except Exception as e:
        print(e)
        raise e
    return sftp

# sftp 상에 경로를 생성한다.
# remote 경로가 directory이면, is_dir에 True를 전달한다.
def mkdir_p(sftp, remote, is_dir=False):
    dirs_ = []
    if is_dir:
        dir_ = remote
    else:
        dir_, basename = os.path.split(remote)
    while len(dir_) > 1:
        dirs_.append(dir_)
        dir_, _  = os.path.split(dir_)

    if len(dir_) == 1 and not dir_.startswith("/"):
        dirs_.append(dir_) # For a remote path like y/x.txt

    while len(dirs_):
        dir_ = dirs_.pop()
        try:
            sftp.stat(dir_)
        except:
            print("making ... dir",  dir_)
            sftp.mkdir(dir_)

# 파일을 업로드 합니다.
# src_path 에서 dest_path 로 업로드 (모두 file full path 사용)
def file_upload(sftp, src_path, dest_path):
    # open_sftp()후
    # 파일을 가져올때는 get('localfile.py', 'remotefile.py')를 이용하고,
    # 올려둘때는 put('localfile.py', 'remotefile.py')를 사용하면된다.
    mkdir_p(sftp, dest_path)
    try:
        sftp.put(src_path, dest_path)
    except Exception as e:
        print("fail to upload " + src_path + " ==> " + dest_path)
        raise e
    print("success to upload " + src_path + " ==> " + dest_path)

# sftp 상에 directory를 업로드한다.
# src_directory, dest_directory 모두 directory 경로여야 한다.
# dest_directory에 src_directory가 포함되어 복사된다.
# 즉, src_directory에 CTRL+C, dest_directory에 CTRL+V한 효과가 있다.
def directory_upload(sftp, src_directory, dest_directory):
        mkdir_p(sftp, dest_directory, True)
        cwd = os.getcwd()
        os.chdir(os.path.split(src_directory)[0])
        parent = os.path.split(src_directory)[1]
        is_window = (platform.system() == "Windows")
        for walker in os.walk(parent):
            try:
                for file in walker[2]:
                    pathname = os.path.join(dest_directory, walker[0], file)
                    if (True == is_window):
                        pathname = pathname.replace('\\', '/')
                        file_upload(sftp, os.path.join(walker[0], file), pathname)
            except Exception as e:
                print(e)
                raise e

def close_ssh(ssh):
    ssh.close()                                         # ssh context 를 제거

def close_sftp(sftp):
    sftp.close()                                        # sftp context 를 제거




