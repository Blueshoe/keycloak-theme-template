import errno
import os
import shutil
import urllib.request
import tempfile
import zipfile


tag = "{{ cookiecutter.keycloak_tag }}"
url = f"https://api.github.com/repos/keycloak/keycloak/zipball/{tag}"
zipball = f"{tag}.zip"
source_dir = "themes/src/main/resources/theme/keycloak"
cwd = os.getcwd()
destination_dir = os.path.join(cwd, "{{ cookiecutter.theme_title }}")

with tempfile.TemporaryDirectory() as tmpdirname:
    target = os.path.join(tmpdirname, zipball)
    urllib.request.urlretrieve(url, target)
    with zipfile.ZipFile(target, 'r') as zip_ref:
        zip_ref.extractall(tmpdirname)
    os.remove(target)
    root = os.path.join(tmpdirname, os.listdir(tmpdirname)[0])
    src = os.path.join(root, source_dir)
    try:
        shutil.copytree(src, destination_dir)
    except OSError as exc:  # python >2.5
        if exc.errno in (errno.ENOTDIR, errno.EINVAL):
            shutil.copy(src, destination_dir)
        else:
            raise
