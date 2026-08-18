from pathlib import Path
import re

p=Path('index.html')
s=p.read_text(encoding='utf-8')
if 'id="retro-gatts"' in s:
    raise SystemExit(0)

css=r'''*{box-sizing:border-box}html{scroll-behavior:smooth}body{margin:0;background:#d7dbd6;color:#222;font-family:Arial,"Hiragino Kaku Gothic ProN","Yu Gothic","Meiryo",sans-serif;font-size:14px;line-height:1.75}a{color:#275e8f}.topbar{background:#fff;border-bottom:1px solid #aeb3ad}.topbar-inner{width:min(980px,100%);margin:auto;padding:7px 11px;display:flex;justify-content:space-between;align-items:center;gap:12px}.brand{font-size:18px;font-weight:bold;color:#333}.brand em{font-style:normal;color:#4f7b56}.toplinks{font-size:11px;color:#777}#retro-gatts{width:min(980px,100%);margin:0 auto;background:#fff;box-shadow:0 0 0 1px #bfc4be}.bloghead{background:linear-gradient(#315c39,#173c23);color:#fff;padding:20px 25px 17px;border-bottom:5px solid #b2c281}.bloghead h1{font-size:25px;line-height:1.3;margin:0;text-shadow:0 1px #000}.bloghead p{font-size:12px;color:#edf3e8;margin:9px 0 0}.site-nav{background:#eef1e8;border-bottom:1px solid #b9beb4}.nav{max-width:none;margin:0;padding:6px 11px;display:flex;gap:0;overflow:auto}.tab{border:0;background:transparent;padding:3px 9px;border-right:1px solid #b8bdb5;border-radius:0;font-size:12px;font-weight:bold;color:#285832;white-space:nowrap;cursor:pointer}.tab.on{background:#d9e5d7}.layout{display:grid;grid-template-columns:220px minmax(0,1fr)}.sidebar{background:#f1f3ee;border-right:1px solid #c5c9c2;padding:13px}.sidebox{background:#fff;border:1px solid #bac0b6;margin-bottom:14px}.sidebox h3{margin:0;padding:5px 8px;background:#365f3d;color:#fff;font-size:13px}.sidebox .in{padding:9px;font-size:12px;white-space:pre-line}.sidebox a{font-size:12px}.main{max-width:none;margin:0;padding:14px 18px 30px;min-width:0}.panel{display:none}.panel.on{display:block}.card{background:#fff;border:0;border-bottom:1px dotted #999;border-radius:0;padding:0 0 23px;margin:0 0 23px;box-shadow:none}.card h2{margin:3px 0 12px;padding:4px 8px;background:#edf2eb;border-left:6px solid #385e3f;color:#193b22;font-size:18px;line-height:1.45}.date{font-size:12px;font-weight:bold;color:#666}.meta{font-size:11px;color:#777}.note{background:#fffbe7;border:1px solid #d6ca84;padding:10px 12px;margin-bottom:20px}.stats{display:flex;gap:8px;flex-wrap:wrap}.stat{border:1px solid #bbb;background:#f4f5f1;border-radius:0;padding:6px 10px;text-align:center}.stat b{font-size:20px;color:#315c39}.controls{display:grid;grid-template-columns:1fr 110px;gap:7px;position:sticky;top:31px;background:#fff;padding:8px 0;z-index:5}.controls input,.controls select{padding:8px;border:1px solid #aaa;border-radius:0;background:#fff;font-size:13px}.open{border:1px solid #315739;background:#496f4e;color:#fff;padding:6px 10px;border-radius:0;font-weight:bold;cursor:pointer}.body pre,.entry_body pre{white-space:pre-wrap;font-family:inherit}.body img,.entry_body img{max-width:100%;height:auto;display:block;margin:12px auto;border:1px solid #aaa;border-radius:0}.missing{padding:9px;border:1px dashed #999;background:#f5f5f5;color:#777;margin:9px 0}.comment{background:#f7f7f4;border:0;border-top:1px dotted #aaa;border-left:4px solid #aeb9ad;border-radius:0;padding:9px;margin:0}.gallery{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:11px}.photo{background:#fafafa;border:1px solid #bbb;border-radius:0;padding:7px}.photo img{width:100%;height:220px;object-fit:contain;background:#eee;border-radius:0}.fc_violet{color:#7a2685}.fc_red{color:#c00}.fc_green{color:#087108}.fs_1{font-size:12px}.fs_2{font-size:14px}.fs_3{font-size:16px}@media(max-width:720px){body{background:#fff;font-size:15px}.toplinks{display:none}#retro-gatts{box-shadow:none}.bloghead{padding:16px 14px}.bloghead h1{font-size:20px}.bloghead p{font-size:11px}.site-nav{position:sticky;top:0;z-index:20}.nav{padding:5px}.tab{font-size:13px;padding:6px 9px}.layout{display:block}.sidebar{display:none}.main{padding:12px}.controls{top:37px;grid-template-columns:1fr}.card h2{font-size:19px}.gallery{grid-template-columns:1fr}.photo img{height:auto}.fs_1{font-size:13px}}'''

s=re.sub(r'<style>.*?</style>', '<style>'+css+'</style>', s, count=1, flags=re.S)
header='''<div class="topbar"><div class="topbar-inner"><div class="brand">スポーツナビ<em>＋</em> <span style="font-size:11px;color:#777">archive reconstruction</span></div><div class="toplinks">トップ ｜ ログイン ｜ お知らせ ／ スポーツナビ</div></div></div><div id="retro-gatts"><header class="bloghead"><h1>【ガッツイーストRFCの挑戦！】<br>神奈川県川崎市で活動するラグビークラブチーム</h1><p>※部員随時募集中！詳しくは左バー・プロフィールをご覧下さい。ガッツイーストに名称変更して幹部陣も一新！新生・ガッツで挑む６シーズン目の挑戦記！</p></header>'''
s=re.sub(r'<header>.*?</header>', header, s, count=1, flags=re.S)
nav='''<nav class="site-nav"><div class="nav"><button class="tab on" data-t="home">TOP</button><button class="tab" data-t="articles">記事一覧</button><button class="tab" data-t="photos">写真</button><button class="tab" data-t="about">この復元版について</button></div></nav>'''
s=re.sub(r'<nav>.*?</nav>', nav, s, count=1, flags=re.S)
side='''<div class="layout"><aside class="sidebar"><div class="sidebox"><h3>プロフィール</h3><div class="in">ずっと所属出来るラグビークラブを目指して発足。
「助っ人を呼ばない」で活動するクラブチーム。

社会人での限られた生活の中で
「激しく！楽しく！」挑戦。

関東社会人リーグ
神奈川県社会人会長杯
オイルメンリーグ ほか</div></div><div class="sidebox"><h3>旧HPアーカイブ</h3><div class="in">Wayback Machineに残っていた公開ページから復元。

本文・コメントは回収できた内容を掲載し、消失部分は推測で補っていません。</div></div><div class="sidebox"><h3>検索のヒント</h3><div class="in">小室
オイルメン
三田倶楽部
キヤノン
2部昇格</div></div></aside><main class="main">'''
s=s.replace('<main>',side,1)
s=re.sub(r'</main>\s*<script>', '</main></div></div><script>', s, count=1)
p.write_text(s,encoding='utf-8')
