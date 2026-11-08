from pathlib import Path
import base64, hashlib, json, zipfile, io
root=Path(__file__).resolve().parent
source=root/'.portfolio-payload'
manifest=json.loads((source/'ready.json').read_text())
archive=io.BytesIO()
for p in manifest['parts']:
    data=base64.b64decode((source/p['name']).read_text(),validate=True)
    assert len(data)==p['bytes'] and hashlib.sha256(data).hexdigest()==p['sha256'],p['name']
    archive.write(data)
assert archive.tell()==manifest['bytes']
assert hashlib.sha256(archive.getvalue()).hexdigest()==manifest['sha256']
dest=root/'restored-portfolio'
with zipfile.ZipFile(archive) as z:
    for name in z.namelist():
        p=Path(name)
        assert not p.is_absolute() and '..' not in p.parts
    z.extractall(dest)
print('Verified and restored:',dest)
