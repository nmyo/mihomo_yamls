import os
import yaml
import re
from urllib.parse import quote

SOURCE_BASE = "THEYAMLS"
OUTPUT_BASE = "Overwrite/THEOPENCLASH"
INI_BASE = "Overwrite/THEINI"
REPO_RAW = f"https://raw.githubusercontent.com/{os.getenv('GITHUB_REPOSITORY')}/main"

yaml.add_multi_constructor("!", lambda loader, suffix, node: None, Loader=yaml.SafeLoader)

def gen_openclash():
    os.makedirs(OUTPUT_BASE, exist_ok=True)
    count = 0
    for root, dirs, files in os.walk(SOURCE_BASE):
        dirs[:] = [d for d in dirs if not d.startswith('.')]
        for file in files:
            if not file.endswith(('.yaml', '.yml')): continue
            
            full_path = os.path.join(root, file)
            try:
                with open(full_path, 'r', encoding='utf-8') as f:
                    data = yaml.safe_load(f)
                
                providers = data.get('proxy-providers', {}) if isinstance(data, dict) else {}
                if not providers: continue
                
                rel_dir = os.path.relpath(root, SOURCE_BASE)
                out_dir = os.path.join(OUTPUT_BASE, rel_dir)
                os.makedirs(out_dir, exist_ok=True)
                
                raw_url = f"{REPO_RAW}/{quote(f'{SOURCE_BASE}/{rel_dir}/{file}'.replace(os.sep, '/'))}"
                out_file = os.path.join(out_dir, os.path.splitext(file)[0] + ".conf")
                
                lines = [
                    "# OpenClash Overwrite Config", f"# Source: {file}", "", "[General]",
                    "DISABLE_UDP_QUIC = 1",
                    f"DOWNLOAD_FILE = url={raw_url}, path=/etc/openclash/config/{file}, cron=0 6 * * *, force=false",
                    f"CONFIG_FILE = /etc/openclash/config/{file}", "SUB_INFO_URL = $EN_KEY1", "", "[Overwrite]"
                ]
                for idx, name in enumerate(providers.keys(), 1):
                    lines.append(f'ruby_map_edit "$CONFIG_FILE" "[\'proxy-providers\']" "{name}" "[\'url\']" "$EN_KEY{idx}"')
                
                with open(out_file, 'w', encoding='utf-8') as f:
                    f.write("\n".join(lines))
                count += 1
            except Exception as e:
                print(f"⚠️ Error {file}: {e}")
    
    # Generate READMEs for OpenClash
    for cat in os.listdir(OUTPUT_BASE):
        cat_path = os.path.join(OUTPUT_BASE, cat)
        if os.path.isdir(cat_path):
            confs = [f for f in os.listdir(cat_path) if f.endswith('.conf')]
            if confs:
                lines = [f"# 📁 {cat}", "", "| 配置文件 | 说明 |", "| :--- | :--- |"]
                for c in sorted(confs): lines.append(f"| `{c}` | OpenClash 覆写配置 |")
                lines.extend(["", "[🔙 返回总览](../README.md)"])
                with open(os.path.join(cat_path, "README.md"), "w", encoding="utf-8") as f:
                    f.write("\n".join(lines))
    
    # OpenClash Main README
    lines = ["# 📦 OpenClash 覆写配置总览", "", "## 📂 分类目录", ""]
    for cat in sorted(os.listdir(OUTPUT_BASE)):
        if os.path.isdir(os.path.join(OUTPUT_BASE, cat)):
            lines.append(f"- 📁 **[{cat}](./{cat}/README.md)**")
    lines.extend(["", "## 🚀 使用方法", "请查看各分类下的详细说明。", "", "[🏠 返回项目主页](../../README.md)"])
    with open(os.path.join(OUTPUT_BASE, "README.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    print(f"✅ Generated {count} OpenClash configs")

def gen_ini_docs():
    script_path = ".github/scripts/download-ini.sh"
    if not os.path.exists(script_path): return
    
    with open(script_path, 'r', encoding='utf-8') as f: content = f.read()
    urls = re.findall(r'https?://[^\s"\']+', content)
    cats = {"ACL4SSR": [], "Airport": [], "General": []}
    
    for url in urls:
        cat = "ACL4SSR" if 'ACL4SSR' in url else ("Airport" if any(x in url for x in ['jklolixxs', 'customized', 'airports']) else "General")
        author = url.split('/')[3] if 'github' in url else url.split('/')[2].split('.')[0]
        cats[cat].append({'author': author, 'file': url.split('/')[-1], 'url': url})
    
    os.makedirs(INI_BASE, exist_ok=True)
    lines = ["# 📂 INI 覆写配置集合", "", "| 分类 | 数量 |", "| :--- | :--- |"]
    names = {"ACL4SSR": "ACL4SSR 系列", "Airport": "机场定制", "General": "通用配置"}
    
    for k, v in cats.items():
        if v: lines.append(f"| **{names.get(k, k)}** | {len(v)} 个 |")
    
    lines.append("")
    for k, items in cats.items():
        if items:
            lines.extend([f"## {names.get(k, k)}", "", "| 作者 | 文件 | 链接 |", "| :--- | :--- | :--- |"])
            for item in items: lines.append(f"| **{item['author']}** | `{item['file']}` | [Source]({item['url']}) |")
            lines.append("")
            
    with open(os.path.join(INI_BASE, "README.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    print("✅ Generated INI docs")

if __name__ == "__main__":
    gen_openclash()
    gen_ini_docs()
