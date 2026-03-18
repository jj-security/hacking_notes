# Project Helix: CTF Scenario

<p>Three days ago, lead geneticist Dr. Owens sent a final frantic transmission claiming he had intercepted a "biological broadcast." He described it as a repeating signal he believed to be a synthetic RNA sequence manifesting as radio frequency interference.

In violation of Protocol 4, Owens began unauthorized testing on a high-risk specimen. All communications stopped soon after. A security sweep of Owens' laboratory confirmed he is missing. His local workstation was found powered on, but all of his research has been deleted. Internal sensors indicate the "broadcast" is still active on a localized frequency, but the specific coordinates were deleted along with Owens' research notes.

You have been provided a forensic triage image of Owens' workstation. Your objective is to recover the deleted notes and identify the RNA-based key required to unlock his encrypted specimen archive.</p>

I downloaded a file called: 2026-02-25T224057_Triage

It is a forensic backup of a Windows machine. I went through all the folders manually and found nothing.

Until I came across an $MFT file.

This is the master file table, which should show files which are deleted.

Now I am looking for tools to open it.

I found MFTECmd, which I can run on Linux using dotnet.

Found useful forensics tools:

https://ericzimmerman.github.io/ - Forensics tools

created an output to csv:

```bash
dotnet MFTECmd.dll -f ../../Downloads/2026-02-25T224057_Triage/C/\$MFT --csv out
```

It worked!!!

![alt text](images/Helix_writeup/image.png)

Filtering drowens desktop:
![alt text](images/Helix_writeup/image-1.png)

Found a file called: freq.txt on the desktop, with zoneidentifier, meaning that this file was downloaded from somewhere. Checking the file shows a link!:
https://ctf.tcmsecurity.com/3c7d7997c1a7/freq.txt
![alt text](images/Helix_writeup/image-2.png)

RNA-based Key:
![alt text](images/Helix_writeup/image-3.png)