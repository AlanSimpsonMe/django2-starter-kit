# Hands-On Django 2
## Alan Simpson


If you're new to Anaconda you can use Terminal in VS Code to enter the command:

`conda init`

Close and reopen terminal. If you see red error text in Windows 10, open PowerShell as Administrator and enter the commands:

`Get-ExecutionPolicy -List` 

`Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser`

Answer *y* when prompted, press ENTER. Close and reopen Terminal and you should see the current environment name (base) at the left side of the command prompt.
Refer to https:/go.microsoft.com/fwlink/?LinkID=135170

## Create Anaconda Environment

1. In Anaconda, click **Environments**, then **Create**.
2. Enter **django2** as the Name, and MAKE SURE to pick **Python** and **3.7**.
3. Click **Create**.
4. Once created django2 should be selected with 11 packages showing and a triangle next to the name django2.
5. Click **Home** and make sure the name django2 shows in the Applications on dropdown.
6. Launch **VS Code**.
7. Choose **Terminal** > **New Terminal** from the menu bar.
8. At the command pompt type **conda activate django2** and press ENTER. Make sure (django2) shows at the left side of the command prompt, indicating that you're in that evironment.
9. Type or copy/paste this command and press ENTER:

`conda install -c conda-forge autopep8 django django-crispy-forms django-bootstrap4 furl pillow pylint sqlparse `

10. Wait for the Proceed? prompt and type **y** and press ENTER to answer Yes.

It could take a few minutes to download and install everything. When it's done, you'll be returned to the command prompt. You can follow these steps tp verify that everything went well:

1. Close VS Code
2. In Anaconda Navigate click **Environments**.
3. Click the **base (root)** environment.
4. Click the **django2** environment.

It might take a few seconds, but eventually you'll see all the packages in that django2 environment, about 41 packages in all. If you look at the django package name, you'll see its version number to the right. It should be version 2.2 or higher.
