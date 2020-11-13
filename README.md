# OpenCV

## Face & Eye Detection

- Face & eye detection using OpenCV [Haarcascades XML](https://github.com/opencv/opencv/tree/master/data/haarcascades) data

## Installation

### Python Version

- Python == 3.8 (Any version of Python3 will work fine)

### Library Installation

#### Windows

- Virtual Environment
  - `python -m venv venv`
  - `.\venv\Scripts\activate`
  - If any problem for scripts activation
    - Execute following command in administration mode
      - `Set-ExecutionPolicy Unrestricted -Force`
    - Later you can revert the change
      - `Set-ExecutionPolicy restricted -Force`
- Library Install
  - `python .\installation\get-pip.py`
  - `pip install --upgrade pip`
  - `pip install --upgrade setuptools`
  - `pip install -r requirements.txt`

#### Linux

- Virtual Environment
  - `python -m venv venv`
  - `source venv/bin/activate`
- Library Install
  - `pip install --upgrade pip`
  - `pip install --upgrade setuptools`
  - `pip install -r requirements.txt`

## Face & Eye Detect

### Sample

<table>
<tr align='center'>
<td><img src="sample_box/male.jpg" alt="Male.jpg" width="460" height="500"/></td>
<td><img src="sample_box/female.jpg" alt="Male.jpg" width="460" height="500"/></td>
</tr>
<table>

### Detection from Image

- For only face detection
  - `python facebox.py --image sample/female.jpg --face True`
- For only eye detection
  - `python facebox.py --image sample/female.jpg --eye True`
- For both face & eye detection
  - `python facebox.py --image sample/male.jpg --face True --eye True`

### Detection from Realtime Video

- For only face detection
  - `python facebox.py --video True --face True`
- For only eye detection
  - `python facebox.py --video True --eye True`
- For both face & eye detection
  - `python facebox.py --video True --face True --eye True`

## Referecne

- OpenCV [Haarcascade](https://github.com/opencv/opencv/tree/master/data/haarcascades)
- Sample Female photo by <span><a href="https://unsplash.com/@michaeldam?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText">Michael Dam</a> on <a href="https://unsplash.com/?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText">Unsplash</a></span>
- Sample Male photo by <span> <a href="https://unsplash.com/@erik_lucatero?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText">Erik Lucatero</a> on <a href="https://unsplash.com/?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText">Unsplash</a></span>
