import idaapi
from idc import *
import binascii

class SMC:

    GlobalCounter = 0
    flag = []
	
    def make_unknown(self):
        for seg in Segments():
	   if idc.SegName(seg) == '.text':
	       start = idc.SegStart(seg)
	       end = idc.SegEnd(seg)
	       
	       while start < end:
	           i=idautils.DecodeInstruction(start)
	           if i.Op1.dtyp == FF_DWRD:
	               print "Found an dword_XXX shit!"
	               idc.MakeUnkn(start,DOUNK_SIMPLE)
	           start = NextHead(start)
    
    def decoder(self,from_loc,to_loc,key):
        self.GlobalCounter += 1
        for loc in range(from_loc, to_loc+1):
            temp = idc.Byte(loc) ^ key
            idc.PatchByte(loc,temp)
            SetColor(loc, CIC_ITEM, 0x208020)

        next_inst = from_loc
        ready = False
        xor_check = False
        jmp_dword = False
        
        #self.make_unknown()        
        #print "---> %s" % to_loc
        
        while True:
 
            #idc.MakeUnkn(next_inst,DOUNK_SIMPLE)
            idc.MakeCode(next_inst)
            idaapi.decode_insn(next_inst)
            inst = idc.GetDisasm(next_inst)
            #print "inst %s next_inst %x" % (inst, next_inst)
            opndValue = idc.GetOperandValue(next_inst,1)

            if ready and xor_check and jmp_dword:
                self.flag.append(format(key,'x'))
                print '[{0:d}] decoder(0x{1:x},0x{2:x},0x{3:x})'.format(self.GlobalCounter,from_loc,to_loc,key)
                
                '''
                if self.GlobalCounter >= 54:
                    print ''.join([chr(int(i,16)) for i in self.flag]).strip()
                    return
                '''
                
                return self.decoder(from_loc,to_loc,key)
            
            elif "jnz" in inst and jmp_dword is False:
                next_inst = GetOperandValue(next_inst,0)
                
            elif "xor" in inst:
                #key = hex(opndValue)
                #print idaapi.cmd.Operands[1].value
                xor_check = True
                key = idaapi.cmd.Operands[1].value
                
            elif "mov" in inst:
                #to_loc = hex(opndValue)
                #print idaapi.cmd.Operands[1].value
                to_loc = idaapi.cmd.Operands[1].value
               
            #elif "cmp" in inst:
            elif format(idaapi.get_byte(next_inst),'x') == "81":
                #print idaapi.cmd.Operands[1].value
                from_loc = idaapi.cmd.Operands[1].value
                ready = True
                
            #elif "jmp" in inst:
            elif format(idaapi.get_byte(next_inst),'x') == "e9" or "jmp" in inst:
                jmp_dword = True
                
                if ready is False and xor_check is False:
                    next_inst = GetOperandValue(next_inst,0)
                    
                elif idaapi.cmd.Operands[0].type == o_near and "dword" in GetOpnd(next_inst,0): 
                    offset = int(idaapi.tag_remove(idaapi.ua_outop2(next_inst, 0))[24:-1],16)
                    address = GetOperandValue(next_inst,0)
                    dword_adr = address - offset
                    idc.MakeUnkn(dword_adr,DOUNK_SIMPLE)
                    idc.MakeCode(address)
                
                
            #next_inst = idc.NextHead(next_inst)
            #print idaapi.decode_insn(next_inst)
            next_inst += idaapi.decode_insn(next_inst)
            
        print "out of loop"

#decoder(0x8049774,0x804978B,0x18)
#decoder(0x8049774,0x804978B,0x21)
#decoder(0x804A025,0x804A03C,0x9b)
#decoder(0x804A025,0x804A03C,0x8e)

def main():
	smc = SMC()
	
	#smc.make_unknown()
	smc.decoder(0x8048A45,0x8048A5C,0x0BC)


if __name__ == "__main__":
    main()

'''
[1] decoder(0x8048e91,0x8048ea8,0x18)
[2] decoder(0x8048f0e,0x8048f25,0x21)
[3] decoder(0x8049774,0x804978b,0x9b)
[4] decoder(0x804a025,0x804a03c,0x8e)
[5] decoder(0x8049085,0x804909c,0xf3)
[6] decoder(0x8049981,0x8049998,0x8f)
[7] decoder(0x8048d97,0x8048dae,0x9c)
[8] decoder(0x8049d1e,0x8049d35,0xfd)
[9] decoder(0x80492dd,0x80492f4,0x81)
[10] decoder(0x804af48,0x804af5f,0x6a)
[11] decoder(0x804ac73,0x804ac8a,0xb)
[12] decoder(0x804a3c2,0x804a3d9,0x2d)
[13] decoder(0x804a59d,0x804a5b4,0x8)
[14] decoder(0x8049102,0x8049119,0x96)
[15] decoder(0x804a183,0x804a19a,0x4f)
[16] decoder(0x8048964,0x804897b,0x4d)
[17] decoder(0x804ac0f,0x804ac26,0xf7)
[18] decoder(0x804b010,0x804b027,0x9a)
[19] decoder(0x804ad86,0x804ad9d,0x67)
[20] decoder(0x80485c7,0x80485de,0x3f)
[21] decoder(0x804a840,0x804a857,0x63)
[22] decoder(0x804881f,0x8048836,0x3d)
[23] decoder(0x80495fd,0x8049614,0xcf)
[24] decoder(0x804a8bd,0x804a8d4,0x8b)
[25] decoder(0x80487ed,0x8048804,0x70)
[26] decoder(0x8049742,0x8049759,0x69)
[27] decoder(0x8048a2c,0x8048a43,0x60)
[28] decoder(0x80482f2,0x8048309,0x17)
[29] decoder(0x804a9b7,0x804a9ce,0xab)
[30] decoder(0x80489c8,0x80489df,0x6f)
[31] decoder(0x80491fc,0x8049213,0xc9)
[32] decoder(0x804a520,0x804a537,0xfb)
[33] decoder(0x8049855,0x804986c,0xc7)
[34] decoder(0x804862b,0x8048642,0x6d)
[35] decoder(0x804adb8,0x804adcf,0x13)
[36] decoder(0x804830b,0x8048322,0xfc)
[37] decoder(0x804aa66,0x804aa7d,0xe8)
[38] decoder(0x804a4a3,0x804a4ba,0x6a)
[39] decoder(0x8048e14,0x8048e2b,0x98)
[40] decoder(0x804980a,0x8049821,0x13)
[41] decoder(0x8048531,0x8048548,0x78)
[42] decoder(0x80491e3,0x80491fa,0x5d)
[43] decoder(0x804914d,0x8049164,0xf4)
[44] decoder(0x804ad6d,0x804ad84,0xeb)
[45] decoder(0x80496c5,0x80496dc,0x6e)
[46] decoder(0x8049db4,0x8049dcb,0x2d)
[47] decoder(0x804a9d0,0x804a9e7,0x4e)
[48] decoder(0x8049a7b,0x8049a92,0x57)
[49] decoder(0x804a7dc,0x804a7f3,0x82)
[50] decoder(0x804909e,0x80490b5,0x91)
[51] decoder(0x80496de,0x80496f5,0x9e)
[52] decoder(0x8048aa9,0x8048ac0,0xab)
[53] decoder(0x8049b5c,0x8049b73,0x98)
[54] decoder(0x804b2f0,0x804b307,0x42)
[55] decoder(0x8049215,0x804922c,0x15)
[56] decoder(0x804894b,0x8048962,0x15)
[57] decoder(0x804a539,0x804a550,0x57)
[58] decoder(0x8048b58,0x8048b6f,0x85)
[59] decoder(0x8049c88,0x8049c9f,0xaa)
[60] decoder(0x80480b3,0x80480ca,0x4c)
[61] decoder(0x80499b3,0x80499ca,0xc7)
[62] decoder(0x8048612,0x8048629,0xc5)
[63] decoder(0x804b074,0x804b08b,0x6d)
[64] decoder(0x804b0bf,0x804b0d6,0x88)
[65] decoder(0x804ab47,0x804ab5e,0x1d)
[66] decoder(0x804b110,0x804b11d,0xd6)
[67] decoder(0x8049ff3,0x804a00a,0xac)
[68] decoder(0x804b029,0x804b040,0x10)
[69] decoder(0x8048900,0x8048917,0xd)
[70] decoder(0x80486a8,0x80486bf,0x90)
[71] decoder(0x80499fe,0x8049a15,0x96)
[72] decoder(0x8048211,0x8048228,0x65)
[73] decoder(0x80492ab,0x80492c2,0x50)
[74] decoder(0x8048f59,0x8048f70,0xc)
[75] decoder(0x804a151,0x804a168,0x65)
[76] decoder(0x8048c6b,0x8048c82,0xf5)
[77] decoder(0x804ad09,0x804ad20,0x59)
[78] decoder(0x804817b,0x8048192,0x7d)
[79] decoder(0x8048e5f,0x8048e76,0xec)
[80] decoder(0x8048c39,0x8048c50,0x83)
[81] decoder(0x804994f,0x8049966,0xd4)
[82] decoder(0x804b1f0,0x804b1fa,0x84)
[83] decoder(0x804a7f5,0x804a80c,0x31)
[84] decoder(0x804a1ce,0x804a1e5,0x4e)
[85] decoder(0x80493f0,0x8049407,0xc2)
[86] decoder(0x804a200,0x804a217,0xa3)
[87] decoder(0x804a633,0x804a64a,0xed)
[88] decoder(0x804849b,0x80484b2,0x2e)
[89] decoder(0x804a32c,0x804a343,0x83)
[90] decoder(0x80494ea,0x8049501,0x64)
[91] decoder(0x8049f5d,0x8049f74,0x55)
[92] decoder(0x804873e,0x8048755,0xf2)
[93] decoder(0x804a1e7,0x804a1fe,0x8c)
[94] decoder(0x80497bf,0x80497d6,0x69)
[95] decoder(0x804b270,0x804b27a,0xcb)
'''