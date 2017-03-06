# identifier2name
PoC that TTÜ-s unique student identifier ("matriklinumber") in not safe to be used to anonymize students grades.
Using it should be considered a violation of [95/46/EC](http://eur-lex.europa.eu/legal-content/EN/TXT/?uri=URISERV:l14012).
Instead, grades should only be presented to it's owner privately.

* Access to **TTÜ-s ÕIS** is required to use this software.
* A access token for ÕIS callsed **j_code** must be obtained from https://ois2.ttu.ee and inserted into token.txt
  * You can use any kind of request capturing tool (like DevTools on Chrome) to record a request and extract **j_code** parameter from it
* The script is written to use files formatted like input.txt.example as input, but can easily be modified to use any input format
  * The example input is taken from http://lambda.ee/wiki/J%C3%A4releksamite_tulemused_ITV0010_2016_s%C3%BCgissemester

_I am not responsible for what this software is used for. This PoC is for educational purposes only._
