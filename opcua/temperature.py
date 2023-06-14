class TemperatureEngine:
    def __init__(self, scratchpad):
        self.scratchpad = scratchpad
        self.resolution = self.define_resolution(scratchpad[4])
        self.decimal_step = self.decimal_step()


    def define_resolution(self, config_reg):
        binary_string = "{0:08b}".format(int(config_reg, 16))
        resolution_binary = binary_string[1] + binary_string[2]
        if resolution_binary == '00':
            return 9
        if resolution_binary == '01':
            return 10
        if resolution_binary == '10':
            return 11
        if resolution_binary == '11':
            return 12


    def decimal_step(self):
        if self.resolution == 9:
            return 0.5
        if self.resolution == 10:
            return 0.25
        if self.resolution == 11:
            return 0.125
        if self.resolution == 12:
            return 0.0625


    def read_temperature(self):
        lsb = "{0:08b}".format(int(self.scratchpad[0], 16))
        msb = "{0:08b}".format(int(self.scratchpad[1], 16))
        temp_int_binary = msb[5] + msb[6] + msb[7] + lsb[0] + lsb[1] + lsb[2] + lsb[3]
        temp_int = int('0b' + temp_int_binary, 2)
        temp_int = float(temp_int)
        temp_decimal_binary = ''
        if self.resolution == 9:
            temp_decimal_binary = lsb[4]
        if self.resolution == 10:
            temp_decimal_binary = lsb[4] + lsb[5]
        if self.resolution == 11:
            temp_decimal_binary = lsb[4] + lsb[5] + lsb[6]
        if self.resolution == 12:
            temp_decimal_binary = lsb[4] + lsb[5] + lsb[6] + lsb[7]
        temp_decimal = int('0b' + temp_decimal_binary, 2)
        temp_decimal = float(temp_decimal) * self.decimal_step
        temperature = temp_int + temp_decimal
        if msb[0] == 1:
            temperature = 0 - temperature
        return temperature


    def watermark_integer(self, watermark):
        lsb = "{0:08b}".format(int(self.scratchpad[0], 16))
        lsb = lsb[0] + lsb[1] + lsb[2] + watermark + lsb[4] + lsb[5] + lsb[6] + lsb[7]
        lsb = hex(int(lsb, 2))
        self.scratchpad[0] = lsb[2] + lsb[3]
        return


    def verify_watermark_integer(self, watermark):
        lsb = "{0:08b}".format(int(self.scratchpad[0], 16))
        if lsb[3] == watermark:
            return True
        else:
            return False


    def watermark_decimal(self, bit):
        lsb = "{0:08b}".format(int(self.scratchpad[0], 16))
        lsb = lsb[0] + lsb[1] + lsb[2] + lsb[3] + lsb[4] + lsb[5] + lsb[6] + bit
        lsb = hex(int(lsb, 2))
        self.scratchpad[0] = lsb[2] + lsb[3]
        return


    def watermark_config_reg(self):
        return


    def watermark_sign(self):
        return