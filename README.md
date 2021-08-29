#        Youtube Downloader        

---------------------------------------------
 ### What is Youtube Downloader?
---------------------------------------------

<p>Youtube Downloader uses pytube API to download and view vidoes/medias from Youtube. I have implemented the search with
keyword and with url functions but in the future I may have implement the additional functions such as playlists. If I do, this
README will be updated to reflect the changes I made.<p>

---------------------------------------------
 ### How to install pip3
---------------------------------------------
<p>This project utilises some non-standard python 3.8 packages which need to be installed using pip3.
In the instance where you're unsure if your device has pip3 installed, please continue following this section.
Alternatively, if your device does have pip3 installed but simply lacks the required libraries, please install them by refering to "3. How to install the required libraries".</p>

<pre>You can check to see if pip3 is installed on your device via:
Windows:            py -m pip --version
Unix/macOS:         python -m pip --version
Linux:              pip3 --version</pre>

<pre>If pip3 is not found, then please install it by refering to the respective link:

For Windows and Unix/macOS:     https://pip.pypa.io/en/stable/installing/
For Linux Package Manager:      https://packaging.python.org/guides/installing-using-linux-tools/</pre>


---------------------------------------------
 ### How to install the required libraries
---------------------------------------------
<p>For your convenience, I have provided a requirement.txt file which details the necessary libraries and their versions.
In you terminal within the root directory of the application (the one with main.py), please enter the following to install the required libraries: 
<br><br>
pip install -r ./requirements.txt</p>
<br>
OR
<br><br>
just
pip install pytube

---------------------------------------------
 ### NOTE: MAC USERS
---------------------------------------------
<p>If you are using mac and getting an error such as below visit https://stackoverflow.com/questions/50236117/scraping-ssl-certificate-verify-failed-error-for-http-en-wikipedia-org to solve the problem. If
the issue below did not occur in your machine, just ignore this part. </p>

<pre>
File "/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/urllib/request.py", line 1319, in do_open
    raise URLError(err)
urllib.error.URLError: <urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.c:1049)
</pre>






