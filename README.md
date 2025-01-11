# addcifs
## About
Addcifs is a python tkinter project built to add CIFS shares to systems quickly. I have built/tested it on hyprland arch linux so I don't know compatibility with other systems.
## WARNING
The SMB credentials file that it is built to work with stores credentials in plain text. Use at your own risk.
## Images
![image](https://github.com/user-attachments/assets/40d720bb-39e6-4766-af82-f3787c9623cf)
![image](https://github.com/user-attachments/assets/cd3f46a9-2531-4166-b50f-095cb87114d5)

## Install
```bash
git clone https://github.com/ThreeTheOG/addcifs.git
cd addcifs
python3 -m venv ./venv
source ./venv/bin/activate
pip install -r requirnments.txt
deactivate
```
Edit the shabang at the top of the file to reflect your VENV python interpreter. (Ex: #!/home/mt/Desktop/addcifs/venv/bin/python3)
Run `./addcifs.py`

## Note
Everything has tooltips, everything is meant to be simple.
