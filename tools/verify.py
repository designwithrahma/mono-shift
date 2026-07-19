#!/usr/bin/env python3
from pathlib import Path
import hashlib, json, re, subprocess, sys, tempfile
from html.parser import HTMLParser

ROOT = Path(__file__).resolve().parents[1]
RUNTIME_HTML = [ROOT/'index.html', ROOT/'game.html', ROOT/'game-design.html']
FORBIDDEN_FILES = [
    re.compile(r'(^|/)\.env($|\.)'), re.compile(r'\.(pem|key|p12|pfx)$', re.I),
    re.compile(r'(^|/)(id_rsa|id_ed25519|credentials\.json|secrets\.json)$', re.I)
]
FORBIDDEN_RUNTIME = {
    'remote URL': re.compile(r'https?://', re.I),
    'network request': re.compile(r'\b(fetch|XMLHttpRequest|WebSocket|EventSource|sendBeacon|axios)\b'),
    'dynamic code': re.compile(r'\beval\s*\(|\bnew\s+Function\s*\('),
    'wildcard postMessage': re.compile(r'postMessage\s*\([^;]+,[ ]*[\'\"]\*[\'\"]\s*\)', re.S),
}

class RefParser(HTMLParser):
    def __init__(self):
        super().__init__(); self.refs=[]; self.scripts=[]; self._in_script=False; self._buf=[]
    def handle_starttag(self, tag, attrs):
        data=dict(attrs)
        for key in ('src','href'):
            value=data.get(key)
            if value: self.refs.append(value)
        if tag=='script' and not data.get('src'):
            self._in_script=True; self._buf=[]
    def handle_endtag(self, tag):
        if tag=='script' and self._in_script:
            self.scripts.append(''.join(self._buf)); self._in_script=False
    def handle_data(self, data):
        if self._in_script: self._buf.append(data)

def fail(message):
    print(f'FAIL: {message}')
    return False

def main():
    ok=True
    expected=['index.html','game.html','game-design.html','README.md','SECURITY.md','ATTRIBUTION.md','COPYRIGHT.md','LICENSE','assets/audio/background-calm-loop.wav']
    for item in expected:
        if not (ROOT/item).is_file(): ok=fail(f'missing required file: {item}') and ok

    for path in ROOT.rglob('*'):
        if path.is_file():
            rel=path.relative_to(ROOT).as_posix()
            if any(p.search(rel) for p in FORBIDDEN_FILES): ok=fail(f'forbidden secret-like file: {rel}') and ok

    for html in RUNTIME_HTML:
        text=html.read_text(encoding='utf-8')
        for label, pattern in FORBIDDEN_RUNTIME.items():
            if pattern.search(text): ok=fail(f'{label} found in {html.name}') and ok
        parser=RefParser(); parser.feed(text)
        for ref in parser.refs:
            if ref.startswith(('#','data:','mailto:','tel:','javascript:','about:')): continue
            if '://' in ref: continue
            clean=ref.split('#',1)[0].split('?',1)[0]
            if not clean: continue
            target=(html.parent/clean).resolve()
            if not target.exists(): ok=fail(f'broken local reference in {html.name}: {ref}') and ok
        node=shutil_which('node')
        if node:
            for i, script in enumerate(parser.scripts, 1):
                if not script.strip(): continue
                with tempfile.NamedTemporaryFile('w',suffix='.js',delete=False,encoding='utf-8') as f:
                    f.write(script); temp=f.name
                result=subprocess.run([node,'--check',temp],capture_output=True,text=True)
                Path(temp).unlink(missing_ok=True)
                if result.returncode:
                    ok=fail(f'JavaScript syntax error in {html.name} script {i}: {result.stderr.strip()}') and ok

    manifest_path=ROOT/'PROVENANCE-MANIFEST.json'
    manifest=json.loads(manifest_path.read_text(encoding='utf-8'))
    for rel, expected_hash in manifest['files'].items():
        path=ROOT/rel
        if not path.is_file(): ok=fail(f'manifest file missing: {rel}') and ok; continue
        actual=hashlib.sha256(path.read_bytes()).hexdigest()
        if actual != expected_hash: ok=fail(f'hash mismatch: {rel}') and ok

    if ok:
        print('PASS: MONO//SHIFT static security and integrity checks completed.')
        return 0
    return 1

def shutil_which(cmd):
    from shutil import which
    return which(cmd)

if __name__=='__main__':
    sys.exit(main())
