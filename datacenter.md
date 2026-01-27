# Measuring Business Value and Productivity Data Center

## I. Adding a new dataset

The site loads data from CSV files and dynamically builds nested list representations for the site interface..

### 1. Format the CSV

The JavaScript function used to load data assumes the following CSV structure:

* **All variable names must appear in the first column.**
* Variables may be **nested hierarchically** by indenting them with leading whitespace.
  * A variable nested under another variable **must appear below it** and have a **greater indent**.
  * Only the **relative amount of indentation** matters (e.g., 2 spaces vs. 4 spaces), not the absolute number.
* For example, a CSV containing GDP data may look like:
```
"Gross Domestic Product", ...
"  Consumption", ...
"    Goods", ...
"    Services", ...
"  Investment", ...
```
* Each remaining column corresponds to a year.
  * The **first row of each column** must contain the year label (e.g., `1997`, `1998`, etc.).

Once the CSV is properly formatted, place it in the `DATA/` subdirectory.

---

### 2. Update `datacenter.html`

1. Download [datacenter.html](datacenter.html) and open it in a code editor.
2. Use `Ctrl + F` (`Cmd + F` on macOS) to locate the following line:
```
<!-- Add new datasets here -->
```

3. Add a new dataset button using the following template:
```
<button id="idname" class="selection-entry" onclick=
    "buildTables(
      'csvName',
      'startRow', 
      'endRow',
      headers = ['H1', 'H2'],
      'source'
    ); highlightDataset(this);"
  ><p> DatasetName </p></button>
```

#### Parameter definitions

* **idname**  
  A short, unique identifier for the dataset (used internally).

* **csvName**  
  The name of the CSV file **without** the `.csv` extension.

* **startRow**  
  The exact text (after trimming whitespace) of the first variable you want included from the CSV’s first column.

* **endRow**  
  The exact text (after trimming whitespace) of the final variable you want included from the CSV’s first column.

  * Both `startRow` and `endRow` must match the CSV exactly **after leading and trailing whitespace is removed**.

* **H1**, **H2**  
  Variables that will be used as the top-level headers for the two data selection tables.

* **source**  
  A string describing the data source (displayed in the UI).  
  Example: _Statistics of Income_. Internal Revenue Service.

* **DatasetName**  
  The human-readable dataset name shown in the dataset selection menu.

---

#### _Example_

Suppose you want to add data from a CSV file called `pinkfloyd.csv`.

* The first variable to include is `"The Wall"`.
* The final variable to include is `"   Pigs on the Wing (Part Two)"`.
* The header variables are `"The Wall"` and `"Animals"`.
* The source is `"Britannia Row"`.
* The dataset name shown in the dataset selection menu should be `"Pink Floyd"`.

The correct button definition is:
```
<button id="PinkFloyd" class="selection-entry" onclick=
    "buildTables(
      'pinkfloyd',
      'The Wall', 
      'Pigs on the Wing (Part Two)',
      headers = ['The Wall', 'Animals'],
      'Britannia Row'
    ); highlightDataset(this);"
  ><p> Pink Floyd </p></button>
```
Once finished, upload the updated `datacenter.html` back to the repository.

---

## II. Editing the site

To modify the site beyond simply adding a dataset (e.g., editing styles, JavaScript behavior, or layout), follow the steps below.

---

### 1. Download the site ZIP

1. Go to the main repository page.
2. Click the green **`<> Code`** button near the top.
3. Select **“Download ZIP”**.
4. Once downloaded, extract the ZIP to a directory on your computer.
   * The remaining steps assume this directory is named **`LiveSite/`**.

---

### 2. Serve the site locally

Because the site loads CSV files using JavaScript, it **must be served from a local web server**. Opening the HTML file directly will not work.

There are several ways to serve a file locally. One simple method uses Python:

1. Ensure python is installed by entering:
```
python --version
```
into a terminal. 
* If the output appears similar to `python 3.X.X`, then Python is already installed and you may proceed.
* Otherwise, [download Python](https://www.python.org/downloads/) first.
3. Open a terminal or command prompt.
4. Navigate to the `LiveSite` directory:
```
cd path/to/LiveSite
```
5. Start a local server:
```
python -m http.server 8000
```
6. Open a web browser and go to:
```
http://localhost:8000
```

You should now see the site running locally.

---

### 3. Edit files

While the server is running, you may edit any of the HTML or CSS files contained in this repository.

After saving changes:
* Reload the page in your browser to see updates.
* If changes do not appear, try a **hard refresh** (`Ctrl + Shift + R` / `Cmd + Shift + R`).

---

### 4. Debugging

* Open your browser’s developer tools:
  * `F12` or `Ctrl + Shift + I` (`Cmd + Option + I` on macOS)
* Use:
  * **Console** tab to view JavaScript errors
  * **Network** tab to verify CSV files are loading correctly

---

### 5. Upload changes

Once you are satisfied with your edits, upload any updated files to this repository.
