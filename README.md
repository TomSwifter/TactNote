# TactNote

TactNote is a project made for MakeHarvard Hackathon

Currently only offered as a web interface (Mobile + Siri/google voice support to follow).

The web interface allows anyone who can use a computer to send a greeting card and a picture to someone who is blind/visually impaired.

The building blocks:

Web interface (HTML/CSS)
AWS
- A python program to translate text into arrays of 0's and 1's representing braille
- A Python program which takes a picture as input queries Microsoft vision API and returns a textual description of what's in the image
- A python script that takes an array of arrays of 0's and 1's (representing braille) and converts it into a 3D braille model.
We use blender to mock the 3D model and Blender API to generate the 3D file
We then send the file to a 3D printer to print a greeting card: - One side of the card is the description of the picture in braille - The other side is the actual greeting in braille
