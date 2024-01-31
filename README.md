# FHGR Text Analytics

## Setup
Please run the following command to install all necessary packages

```bash
cd code
python -m venv ./venv
pip install -r ./requirements.txt
ipython kernel install --user --name=venv
```

## Documentation
Make sure pandoc and the necessary latex packages are installed:
```bash
sudo pacman -S pandoc texlive ttf-jetbrains 
```
> :warning: Please make sure you have at least Pandoc Version > 3.1.8 installed because of this issue [here](https://github.com/Wandmalfarbe/pandoc-latex-template/issues/361) For example you can download Pandoc from [here](https://github.com/jgm/pandoc/releases/)

### :pencil: Build Documentation
As a base template the awesome pandoc-latex-template from [Wandmalfarbe](https://github.com/Wandmalfarbe/pandoc-latex-template) was used. In order to generate the Documentation simply the `doc.sh` file executable and run it:

```bash
cd doc
chmod +x doc.sh
./doc.sh
```
## Jupyer Notebooks
In order to run the Jupyter Notebooks execute the following command:
```bash
cd code
jupyter notebook ./
```

