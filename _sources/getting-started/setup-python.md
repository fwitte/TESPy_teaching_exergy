(installation-label)=

# Setup your Python environment

In this section you learn how to prepare your python installation.

## Installation

Make sure you have installed your favorite python distribution as well as a code editor on your machine. A lightweight
python installation is, for example, [miniforge](https://github.com/conda-forge/miniforge). Then you can follow these
steps to create an environment and install the required dependencies:

1. Create a new folder on your machine.
2. Download the `environment.yml` file from the
   [github repository](https://github.com/fwitte/TESPy_teaching_exergy) and save it to the new folder OR create an
   `environment.yml` in your folder manually and copy the following contents into it:

   ```{literalinclude} /../environment.yml
   ```
3. Open the miniforge3 prompt and navigate into that folder with `cd /path/to/the/folder`
4. Create and prepare the environment mit `conda env create -f environment.yml`
5. Activate your environment using `conda activate exergy-env`

## Working with jupyter-notebooks

In the in person-workshop we will be working with Jupyter Notebooks. It is possible to edit the notebooks in code
editors (e.g. in VS Code) or in the browser.To learn more about how to use them, you can check out the respective
section in the [online documentation](https://jupyter.org/).

```{note}
If you installed all dependencies into your python environment as described in the steps above, you do NOT need to
install jupyter notebook separately.
```
