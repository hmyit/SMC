# SMC
Self-modifying Code de-obfuscation

```
[1] decoder(8048e91,8048ea8,18)
[2] decoder(8048f0e,8048f25,21)
[3] decoder(8049774,804978b,9b)
[4] decoder(804a025,804a03c,8e)
[5] decoder(8049085,804909c,f3)
[6] decoder(8049981,8049998,8f)
[7] decoder(8048d97,8048dae,9c)
[8] decoder(8049d1e,8049d35,fd)
[9] decoder(80492dd,80492f4,81)
[10] decoder(804af48,804af5f,6a)
[11] decoder(804ac73,804ac8a,b)
[12] decoder(804a3c2,804a3d9,2d)
[13] decoder(804a59d,804a5b4,8)
[14] decoder(8049102,8049119,96)
[15] decoder(804a183,804a19a,4f)
[16] decoder(8048964,804897b,4d)
[17] decoder(804ac0f,804ac26,f7)
[18] decoder(804b010,804b027,9a)
[19] decoder(804ad86,804ad9d,67)
[20] decoder(80485c7,80485de,3f)
[21] decoder(804a840,804a857,63)
[22] decoder(804881f,8048836,3d)
[23] decoder(80495fd,8049614,cf)
[24] decoder(804a8bd,804a8d4,8b)
[25] decoder(80487ed,8048804,70)
[26] decoder(8049742,8049759,69)
[27] decoder(8048a2c,8048a43,60)
[28] decoder(80482f2,8048309,17)
[29] decoder(804a9b7,804a9ce,ab)
[30] decoder(80489c8,80489df,6f)
[31] decoder(80491fc,8049213,c9)
[32] decoder(804a520,804a537,fb)
[33] decoder(8049855,804986c,c7)
[34] decoder(804862b,8048642,6d)
[35] decoder(804adb8,804adcf,13)
[36] decoder(804830b,8048322,fc)
[37] decoder(804aa66,804aa7d,e8)
[38] decoder(804a4a3,804a4ba,6a)
[39] decoder(8048e14,8048e2b,98)
[40] decoder(804980a,8049821,13)
[41] decoder(8048531,8048548,78)
[42] decoder(80491e3,80491fa,5d)
[43] decoder(804914d,8049164,f4)
[44] decoder(804ad6d,804ad84,eb)
[45] decoder(80496c5,80496dc,6e)
[46] decoder(8049db4,8049dcb,2d)
[47] decoder(804a9d0,804a9e7,4e)
[48] decoder(8049a7b,8049a92,57)
[49] decoder(804a7dc,804a7f3,82)
[50] decoder(804909e,80490b5,91)
[51] decoder(80496de,80496f5,9e)
[52] decoder(8048aa9,8048ac0,ab)
[53] decoder(8049b5c,8049b73,98)
[54] decoder(804b2f0,804b307,42)
```


As you can see, there are some repetitive XoRs BBs in code:


![before unpack](https://raw.githubusercontent.com/pwnslinger/SMC/master/Before_unpack.PNG)


![before unpack Graph View](https://raw.githubusercontent.com/pwnslinger/SMC/master/GView_before_unpack.PNG)


![before unpack Graph View](https://raw.githubusercontent.com/pwnslinger/SMC/master/Gview_after-unpack.PNG)