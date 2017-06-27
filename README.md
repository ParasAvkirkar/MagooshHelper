# MagooshHelper
A simple application based on words published by Magoosh Vocabulary Flash Cards.
I made this tool for my friends and for students who needed to improve their Vocabulary, for Competitive exams like GRE, CAT, etc can use this application.

A Python3 user can fork and use the tool from master branch.

A Python2 user can fork and use the tool from python2_support branch.

Users can run check_accents_available.py to check some of the voices/accents available on their platforms.
For example, users using Windows will have different accents available than users at OS X and Ubuntu.
Same applies for any combination. This is because of the driver support for pyttsx library use in this tool is different at this platforms.
Windows have different speech synthesiser driver, OS X have different and Ubuntu have different.

You can refer https://github.com/RapidWareTech/pyttsx repository where the respective drivers are listed.

For Windows it is sapi5, for Ubuntu it is espeak and for OS X it is NSSS.

Kindly download the respective drivers for your platforms.

Then you can check the available accents.
Based on your preference, you can change the line voice = get_voice_property() inside speech_utilities.py

The default is a British Accent, but it is tested for Ubuntu.


Terms:
MagooshHelper is being secured by GitHub's default Copyright terms.

You can fork and modify locally as per GitHub's policy.

You cannot redistribute the tool without my permission as per policy regarding original owner under Github.

I am ready to accept some Pull Request after some amount of reviewing.

I strictly do not permit the use of this tool for any commercial purposes.

The sole purpose of the MagooshHelper (which is built on freely published pdf of Vocabulary Flashcards by Magoosh),
is to help out young students
