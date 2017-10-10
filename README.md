# create-learning-data
## use

- centos 7.4
- pyenv
  - python 3.6.3

# initial settings(in linux)

https://qiita.com/mogom625/items/b1b673f530a05ec6b423

## install ffmpeg

https://trac.ffmpeg.org/wiki/CompilationGuide/Centos
https://qiita.com/snoguchi/items/d12f0407075d7978925c

### 実際にやった手順
pyenv でpython3.6インストール
```bash
pip install pydub
rpm -Uvh http://li.nux.ro/download/nux/dextop/el7/x86_64/nux-dextop-release-0-1.el7.nux.noarch.rpm
yum install ffmpeg ffmpeg-devel

python main.py
```

# sample data
http://www.sousound.com/music_sample.html
