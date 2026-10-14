#%%Import the Path object
from pathlib import Path

#%% Get the current working directory
the_cwd = Path.cwd()
print("Current working directory:", the_cwd)

#%% Navigate to the parent folder
the_parent = the_cwd.parent
print("Parent directory:", the_parent)

#%% Navigate up one folder and into the data folder
data_folder = the_parent / "data"
print("Data folder path:", data_folder)

#%% List all files in the current directory
print("\nAll items in current directory:")
for item in the_cwd.iterdir():
    print(" -", item)

#%% List only python files in the current directory
print("\nPython files in current directory:")
for py_file in the_cwd.glob("*.py"):
    print(" -", py_file)
# %%
