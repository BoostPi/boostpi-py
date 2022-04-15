# coding=utf-8

EULA_WARNING = """
⚠️⚠️⚠️ By using this tool, you are agreeing to the following: ⚠️⚠️⚠️
- You are responsible for any damage caused by this tool.
- You will hold the author(s) of this tool harmless for any damage or loss of data caused.
- You will not use this tool to cause damage to any other person.
- Use of this tool may void your warranty.
- Use of this tool may make permanent changes to your raspberry pi.
- Use of this tool may increase performance of your raspberry pi. 🎉

A copy of the EULA will be saved in your boot directory.
"""


EULA_ACCEPT_WARNING = (
    """
This file exists as a record that I have accepted the EULA for the use of boostpi.
The following is a copy of the EULA:
"""
    + EULA_WARNING
)


WARRANTY_VOID_WARNING = """
APPLYING THIS CONFIGURATION WILL VOID YOUR PI's WARRANTY.
This configuration will set a permanent bit on your pi that can detect if you have overclocked your pi.
"""


BOOT_WARNING = """
VERY IMPORTANT INSTRUCTIONS:

In the event your pi is unable to boot, or is unstable, disconnect power from the pi.
While holding the left shift key down, plug in power and wait until the OS has booted.
This will cause the pi to ignore overclock settings during startup.
Once the pi has booted, you can release the shift key and run `python -m boostpi --reset` to reset the pi's overclocking settings to factory defaults.
"""
