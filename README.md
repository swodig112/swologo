# swologo
##### Swodig's logo generator

## What does this do?
This little script generates my logo with custom resolution and offset.

## Background
When I was studying at elementary school, I always wanted to have a logo for
myself. I designed a beautiful logo and drew it on my books, notes etc.
On my birthday, I asked for a cake with my logo on it. I told my mother how
the logo should exactly look like. She told me the bakers don't use a ruler when
they work. My heart broke and I asked for a blue cake with a big yellow star on
it.

After years, I remembered about my logo and decided to use it as my profile
picture. At first I decided to use gimp but apparently designing stuff isn't
one of my talents. So I wrote this little script which generates my logo in png
format (with transparent background and custom resolution).

## Installation and Usage
This is a simple script so there's no installation. Just clone the repo, install
dependencies and enjoy.

Clone the repo:

`git clone --depth=1 https://github.com/swodig112/swologo.git`

I suggest you to use a virtual environment but it's your choice after all. You
can skip this step:

```
python3 -m venv swologo
cd swologo
source bin/activate
python3 -m pip install -r requirements.txt
```

Now run the script this way:

`./main.py`

(`python main.py` should work on Windows)

It should look like this:

```
$ ./main.py
insert image size(in pixels): 1000
insert offset size(in pixels): 30
```

Logo is saved to `logo.png`
