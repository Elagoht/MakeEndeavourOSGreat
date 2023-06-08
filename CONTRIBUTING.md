# About Contributing

You should note that this project was developed under the **GNU GPLv3**. Your contributions to the code will also be evaluated and made available under the same license.

This project, which will be shared via https://aur.archlinux.org/, will use binaries obtained directly from github releases.

If the external changes you have made in the project are merged with this project, your profile information will automatically appear under the contributors heading in the README.md file thanks to the github workflow.

## Code Edits

### Python Files

You should prepare your code in a modular way. Each window should be in a different file. Python codes must be formatted **with autopep8**.

### JSON Files

If you are going to modify JSON files to install a package, you should also pay attention to the **JSON formatting**. The JSON format used does not support comment lines. Consider this.

### Image Files

All images that will appear in the application must be **64x64** in size. If you want to get an application, icon pack or mouse cursor image, automatically create the images using the shell files in the relevant directories under the Assets directory. Otherwise, your image will be reviewed privately. Images **must be in png format**. Svg, gif, jpg files are not required in the project.

**Do not PR until you try your changes.**
