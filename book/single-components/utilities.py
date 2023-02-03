from CoolProp.CoolProp import PropsSI as PSI


def calc_physical_exergy(p, h, p0, T0, fluid):
    r"""
    Calculate specific physical exergy.

    Physical exergy is allocated to a thermal and a mechanical share.

    Parameters
    ----------
    p : float
        Pressure of fluid p / Pa.

    h : float
        Spec. enthalpy of fluid T / K.

    p0 : float
        Ambient pressure p0 / Pa.

    T0 : float
        Ambient temperature T0 / K.

    Returns
    -------
    e_ph : tuple
        Specific thermal and mechanical exergy
        (:math:`e^\mathrm{T}`, :math:`e^\mathrm{M}`) in J / kg.
    """
    s = PSI("S", "P", p, "H", h, fluid)

    h_T0_p = PSI("H", "P", p, "T", T0, fluid)
    s_T0_p = PSI("S", "P", p, "T", T0, fluid)

    ex_therm = (h - h_T0_p) - T0 * (s - s_T0_p)

    h0 = PSI("H", "P", p0, "T", T0, fluid)
    s0 = PSI("S", "P", p0, "T", T0, fluid)

    ex_mech = (h_T0_p - h0) - T0 * (s_T0_p - s0)
    return ex_therm, ex_mech
