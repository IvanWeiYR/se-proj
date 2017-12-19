### Fault Localization Process 
1. Generate Test cases files(.txt) 
2. Generate coverage information files(.xml)
3. Run Tarantula/BPNN

*Find example in run_xxxx.sh*

---

#### Sorting Algorithms
##### 1 . Generate testcases:
```text
python3 gen_tc_sorting.py

usage: gen_tc_sorting.py [-h] [--ntc NTC] [--len LEN] [--max MAX] [--dest DEST]

optional arguments:
--ntc NTC    number of testcases, default: 25  
--len LEN    length of list, default: 5  
--max MAX    maximum value for each element in list, default: 1001 
--dest DEST  destination folder to store the testcase .txt file, default: 'tc_sorting'
```

Output test cases format (.txt file): unsorted list separated elements by commas
```
x2,x3,x5,x1,x4
```
**Note** that files of re-generation will replace the testcases file, no deletion will be performed. Be careful when re-generate with smaller ntc

##### 2 . Run program with test cases and save coverage information:

```text
python3 cov_sorting.py treesort_v1 sort --src=tc_sorting

usage: cov_sorting.py [-h] [--src SRC] module func

positional arguments:
  module      name of the module
  func        name of entry function

optional arguments:
  -h, --help  show this help message and exit
  --src SRC   name of source folder containing testcase .txt files, default: 'tc_sorting'
```
Output one XML file for each test case, see section **Sample coverage.xml**


---
#### Symbol Counting problem

##### 1 . Generate testcases:
```text
python3 gen_tc_symbcount.py

usage: gen_tc_symbcount.py [-h] [--ntc NTC] [--dest DEST]

optional arguments:
--ntc NTC    number of testcases, default: 25  
--dest DEST  destination folder to store the testcase .txt file, default: 'tc_symbcount'
```

Output test cases format (.txt file): string followed by a *space* followed by the count of different type of symbols (in one line), the counts are test oracle that are predetermined before the test case generation.
```text
string c1,c2,c3,c4,c5,c6
```
**Note** that files of re-generation will replace the testcases file, no deletion will be performed. Be careful when re-generate with smaller ntc

##### 2 . Run program with test cases and save coverage information:

```text
python3 cov_symbcount.py count_v1 count --src=tc_symbcount

usage: cov_symbcount.py [-h] [--src SRC] module func

positional arguments:
  module      name of the module
  func        name of entry function

optional arguments:
  -h, --help  show this help message and exit
  --src SRC   name of source folder containing testcase .txt files, default: 'tc_symbcount'
```
Output one XML file for each test case, see section **Sample coverage.xml**

---

#### Sample coverage.xml
```xml
<?xml version='1.0' encoding='us-ascii'?>
<coverage branch-rate="0" branches-covered="0" branches-valid="0" complexity="0" line-rate="0.8889" lines-covered="8" lines-valid="9" timestamp="1513510670180" version="4.4.2">
	
	
	<sources>
		<source>/Users/user/Desktop/se</source>
	</sources>
	<packages>
		<package branch-rate="0" complexity="0" line-rate="0.8889" name=".">
			<classes>
				<class branch-rate="0" complexity="0" filename="insertionSort.py" line-rate="0.8889" name="insertionSort.py">
					<methods />
					<lines>
						<line hits="0" number="1" />
						<line hits="1" number="2" />
						<line hits="1" number="3" />
						<line hits="1" number="4" />
						<line hits="1" number="5" />
						<line hits="1" number="6" />
						<line hits="1" number="7" />
						<line hits="1" number="8" />
						<line hits="1" number="9" />
					</lines>
				</class>
			</classes>
		</package>
	</packages>
	<result pass="1" /> 
</coverage>
```
*Tag result - Attribute pass: 0 for passed, 1 for failed*

---

#### Run Tarantula 
e.g. python3 taran.py treesort_v1 treesort_v1
```text
usage: taran.py [-h] source prog_name

positional arguments:
  source      name of the folder containing coverage .xml file
  prog_name   name of program, i.e. 'sort' for sort.py
```

---

#### Run BPNN
e.g. python3 bpnn.py treesort_v1 treesort_v1
```text
usage: bpnn.py [-h] source prog_name

positional arguments:
  source      name of the folder containing coverage .xml file
  prog_name   name of program, i.e. 'sort' for sort.py
``` 

---

#### Programs:
| Program (Symbol counting) | # of bugs | Line # of bugs|
|---------|-----------|---------------|
| count.py.   | 0 | - |
| count_v1.py | 1 | 14 |
| count_v2.py | 2 | 14,16 |
| count_v3.py | 2 | 14,18 |
| count_v4.py | 2 | 14,20 |
| count_v5.py | 3 | 14,20,22 |
| count_v6.py | 4 | 14,20,22,24 |
| count_v7.py | 5 | 14,18,20,22,24 |
| count_v8.py | 6 | 14,16,18,20,22,24|

| Program (Tree Sort) | # of bugs | Line # of bugs|
|--------------------|-----------|---------------|
| treesort_origin.py | 0 | - |
| treesort_v1.py     | 1 | 10 |




