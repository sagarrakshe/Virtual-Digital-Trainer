## Virtual Digital Trainer (VDT)

`Virtual Digital Trainer` is a simple application made in Python. It provides the dashboard to simulate the simple logic circuits and to verify them. It is similar to [Electronics workbench](http://sine.ni.com/nips/cds/view/p/lang/en/nid/202311), though it is not that advanced.

## Requirement

For this application to work you need install the `Python 2.7`. In windows the "Tkinter" module (library file for GUI in Python) is installed along with the python2.7 but in `Ubuntu` you have to install it separately. Along with it you will need another module called `Easygui`.

To install in ubuntu execute the following command-

    $ sudo apt-get install python-tk


## Working

Run the file `project.py`. 
    
    $ ./project.py

It will take sometime to initialized. Now you will have the main window. Click on the gate-buttons below the menu bar and Double-click on the work-area, the gate will appear. Now using the middle button dragging it you can create connections between the gates. Right click on the gate will pop a window for inputs to the gate. At least one seven segment is required for the circuit to simulate. After all connections check click on *final connections* button and verify the connections. At last click on the simulate button to activate the circuit. I have used some images in the project so comment them before running it.

## Downside

You cannot simulate circuits which has more number of gates. 

## Suggestions, Comments

Feel free to raise errors, views, suggestions @ sagarrakshe2@gmail.com         
