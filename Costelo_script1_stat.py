
class health():

    def compute_hp(base, individual_value, effort_value, level):
        
        return (((2*base) + individual_value + (effort_value/4)*level))/100 + (level+10)


    def compute_otherstat(base, individual_value, effort_value, level, nature):
        
        return (((((2*base) + individual_value + (effort_value/4)*level))/100) + 5) * nature
