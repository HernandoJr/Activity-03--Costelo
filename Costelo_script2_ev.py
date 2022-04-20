
class EffortValue():
    def compute_ev(stat, modifier, level, base, individual_value, effort_value):

        COMPUTE_D=(((2*base)+individual_value+(effort_value/4)) * ( level/100))
        statMODIFIER = stat/modifier    

        return ((((((statMODIFIER - COMPUTE_D) * 400 ) / level) / 4 ) * 4))    
