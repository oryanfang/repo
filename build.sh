#!/bin/sh
# 重新生成软件源索引：新的 .deb 放进 debs/ 后运行 ./build.sh，再提交推送
set -e
cd "$(dirname "$0")"
dpkg-scanpackages -m debs /dev/null > Packages 2>/dev/null
bzip2 -kf Packages
gzip -kf9 Packages
xz -kf Packages
zstd -qf -19 Packages -o Packages.zst
{
  cat Release.in
  echo "Date: $(LC_ALL=C date -u '+%a, %d %b %Y %H:%M:%S UTC')"
  for algo in MD5Sum:md5 SHA256:sha256; do
    echo "${algo%%:*}:"
    for f in Packages Packages.bz2 Packages.gz Packages.xz Packages.zst; do
      sum=$(openssl dgst -"${algo##*:}" -r "$f" | cut -d' ' -f1)
      echo " $sum $(wc -c < "$f" | tr -d ' ') $f"
    done
  done
} > Release
echo "索引已更新：$(grep -c '^Package:' Packages) 个包"
