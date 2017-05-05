import idaapi
from idc import *

class SMC:

    GlobalCounter = 0
    def decoder(self,from_loc,to_loc,key):
        self.GlobalCounter += 1
        for loc in range(from_loc, to_loc+1):
            temp = idc.Byte(loc) ^ key
            idc.PatchByte(loc,temp)
            SetColor(loc, CIC_ITEM, 0x208020)

        next_inst = from_loc
        ready = False

        while next_inst <= to_loc:
        
            if next_inst > to_loc:
                return
                
            idc.MakeCode(next_inst)
            idaapi.decode_insn(next_inst)
            inst = idc.GetDisasm(next_inst)
            #print "inst %s next_inst %x" % (inst, next_inst)
            opndValue = idc.GetOperandValue(next_inst,1)

            if ready:
                print 'decoder({0:x},{1:x},{2:x})'.format(from_loc,to_loc,key)
                if self.GlobalCounter >= 10:
                    print "5 rounds has been executed..."
                    return
                return self.decoder(from_loc,to_loc,key)
                
            if "xor" in inst:
                #key = hex(opndValue)
                #print idaapi.cmd.Operands[1].value
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
                
            #next_inst = idc.NextHead(next_inst)
            next_inst += idaapi.decode_insn(next_inst)

#decoder(0x8049774,0x804978B,0x18)
#decoder(0x8049774,0x804978B,0x21)
#decoder(0x804A025,0x804A03C,0x9b)
#decoder(0x804A025,0x804A03C,0x8e)

def main():
	smc = SMC()
	smc.decoder(0x8048A45,0x8048A5C,0x0BC)


if __name__ == "__main__":
    main()

'''
decoder(8048e91,8048ea8,18)
decoder(8048f0e,8048f25,21)
decoder(8049774,804978b,9b)
decoder(804a025,804978b,9b) --> ?? should be 0x8e
'''