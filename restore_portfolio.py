from pathlib import Path
import base64,hashlib,json,zipfile,io
root=Path(__file__).resolve().parent
source=root/'.portfolio-payload'
manifest=json.loads((source/'ready.json').read_text())
archive=io.BytesIO()
for p in manifest['parts']:
    data=base64.b64decode((source/p['name']).read_text(),validate=True)
    assert len(data)==p['bytes'] and hashlib.sha256(data).hexdigest()==p['sha256']
    archive.write(data)
assert hashlib.sha256(archive.getvalue()).hexdigest()==manifest['sha256']
dest=root/'restored-portfolio'
with zipfile.ZipFile(archive) as z: z.extractall(dest)
mobile=root/'.portfolio-mobile-v2.b64'
if mobile.exists():
    with zipfile.ZipFile(io.BytesIO(base64.b64decode(mobile.read_text(),validate=True))) as z: z.extractall(dest)
print('Verified and restored:',dest)
