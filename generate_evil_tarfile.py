import io
import os
import tarfile


OUTPUT_DIR = './test'


# tarファイルを作成する関数
def create_tar(filename, arcname, link_target=None, content=b'hacked!!'):
    with tarfile.open(filename, 'w') as tar:
        info = tarfile.TarInfo(name=arcname)

        # シンボリックリンクの場合
        if link_target:
            info.type = tarfile.SYMTYPE
            info.linkname = link_target
            tar.addfile(info)

        else:
            content_bytes = io.BytesIO(content)
            info.size = len(content)
            tar.addfile(info, fileobj=content_bytes)


if not os.path.isdir(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)

# AbsolutePathErrorを引き起こすtarファイルを作成
# 先頭のスラッシュがfilter='tar' or 'data'だと削除されるため、
# このエラーが発生するのはWindowsのみ
create_tar(os.path.join(OUTPUT_DIR, 'absolute_path_test.tar'), '/etc/passwd')

# OutsideDestinationErrorを引き起こすtarファイルを作成
create_tar(os.path.join(OUTPUT_DIR, 'outside_destination_test.tar'), '../../../../etc/passwd')

# AbsoluteLinkErrorを引き起こすtarファイルを作成
create_tar(os.path.join(OUTPUT_DIR, 'absolute_link_test.tar'), 'absolute_link', link_target='/etc/passwd')

# LinkOutsideDestinationErrorを引き起こすtarファイルを作成
create_tar(os.path.join(OUTPUT_DIR, 'link_outside_destination_test.tar'), 'link_outside_destination', link_target='../../../../etc/passwd')
