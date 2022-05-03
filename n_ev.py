class otep():
    def evneed(stat,bas,iv,ev,lvl):
        D = (2*bas+iv+(ev/4))*(lvl/100)
        return ((((stat/1.0-D)*400)/lvl)/4)*4