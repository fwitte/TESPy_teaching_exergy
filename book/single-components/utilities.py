from CoolProp.CoolProp import PropsSI as PSI


def calc_physical_exergy(p, h, p0, T0, fluid):
    r"""Calculate specific physical exergy."""
    s = PSI("S", "P", p, "H", h, fluid)
    h0 = PSI("H", "P", p0, "T", T0, fluid)
    s0 = PSI("S", "P", p0, "T", T0, fluid)

    ex = (h - h0) - T0 * (s - s0)
    return ex


def calc_splitted_physical_exergy(p, h, p0, T0, fluid):
    r"""Calculate specific physical exergy according to splitting rule."""
    s = PSI("S", "P", p, "H", h, fluid)

    h_T0_p = PSI("H", "P", p, "T", T0, fluid)
    s_T0_p = PSI("S", "P", p, "T", T0, fluid)

    ex_therm = (h - h_T0_p) - T0 * (s - s_T0_p)

    h0 = PSI("H", "P", p0, "T", T0, fluid)
    s0 = PSI("S", "P", p0, "T", T0, fluid)

    ex_mech = (h_T0_p - h0) - T0 * (s_T0_p - s0)
    return ex_therm, ex_mech