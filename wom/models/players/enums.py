# wom.py - An asynchronous wrapper for the Wise Old Man API.
# Copyright (c) 2023-present Jonxslays
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from __future__ import annotations

from wom.enums import BaseEnum

__all__ = (
    "AchievementMeasure",
    "Country",
    "PlayerBuild",
    "PlayerType",
)


class PlayerType(BaseEnum):
    """Different types of players."""

    Unknown = "unknown"
    Regular = "regular"
    Ironman = "ironman"
    Hardcore = "hardcore"
    Ultimate = "ultimate"
    FreshStart = "fresh_start"


class PlayerBuild(BaseEnum):
    """Potential account builds."""

    Main = "main"
    F2p = "f2p"
    Lvl3 = "lvl3"
    Zerker = "zerker"
    Def1 = "def1"
    Hp10 = "hp10"


class AchievementMeasure(BaseEnum):
    """Measures used to categorize achievements."""

    Levels = "levels"
    Experience = "experience"
    Kills = "kills"
    Score = "score"
    Value = "value"


class Country(BaseEnum):
    """Countries in the world."""

    Ad = "AD"
    Ae = "AE"
    Af = "AF"
    Ag = "AG"
    Ai = "AI"
    Al = "AL"
    Am = "AM"
    Ao = "AO"
    Aq = "AQ"
    Ar = "AR"
    As = "AS"
    At = "AT"
    Au = "AU"
    Aw = "AW"
    Ax = "AX"
    Az = "AZ"
    Ba = "BA"
    Bb = "BB"
    Bd = "BD"
    Be = "BE"
    Bf = "BF"
    Bg = "BG"
    Bh = "BH"
    Bi = "BI"
    Bj = "BJ"
    Bl = "BL"
    Bm = "BM"
    Bn = "BN"
    Bo = "BO"
    Bq = "BQ"
    Br = "BR"
    Bs = "BS"
    Bt = "BT"
    Bv = "BV"
    Bw = "BW"
    By = "BY"
    Bz = "BZ"
    Ca = "CA"
    Cc = "CC"
    Cd = "CD"
    Cf = "CF"
    Cg = "CG"
    Ch = "CH"
    Ci = "CI"
    Ck = "CK"
    Cl = "CL"
    Cm = "CM"
    Cn = "CN"
    Co = "CO"
    Cr = "CR"
    Cu = "CU"
    Cv = "CV"
    Cw = "CW"
    Cx = "CX"
    Cy = "CY"
    Cz = "CZ"
    De = "DE"
    Dj = "DJ"
    Dk = "DK"
    Dm = "DM"
    Do = "DO"
    Dz = "DZ"
    Ec = "EC"
    Ee = "EE"
    Eg = "EG"
    Eh = "EH"
    Er = "ER"
    Es = "ES"
    Et = "ET"
    Fi = "FI"
    Fj = "FJ"
    Fk = "FK"
    Fm = "FM"
    Fo = "FO"
    Fr = "FR"
    Ga = "GA"
    Gb = "GB"
    Gd = "GD"
    Ge = "GE"
    Gf = "GF"
    Gg = "GG"
    Gh = "GH"
    Gi = "GI"
    Gl = "GL"
    Gm = "GM"
    Gn = "GN"
    Gp = "GP"
    Gq = "GQ"
    Gr = "GR"
    Gs = "GS"
    Gt = "GT"
    Gu = "GU"
    Gw = "GW"
    Gy = "GY"
    Hk = "HK"
    Hm = "HM"
    Hn = "HN"
    Hr = "HR"
    Ht = "HT"
    Hu = "HU"
    Id = "ID"
    Ie = "IE"
    Il = "IL"
    Im = "IM"
    In = "IN"
    Io = "IO"
    Iq = "IQ"
    Ir = "IR"
    Is = "IS"
    It = "IT"
    Je = "JE"
    Jm = "JM"
    Jo = "JO"
    Jp = "JP"
    Ke = "KE"
    Kg = "KG"
    Kh = "KH"
    Ki = "KI"
    Km = "KM"
    Kn = "KN"
    Kp = "KP"
    Kr = "KR"
    Kw = "KW"
    Ky = "KY"
    Kz = "KZ"
    La = "LA"
    Lb = "LB"
    Lc = "LC"
    Li = "LI"
    Lk = "LK"
    Lr = "LR"
    Ls = "LS"
    Lt = "LT"
    Lu = "LU"
    Lv = "LV"
    Ly = "LY"
    Ma = "MA"
    Mc = "MC"
    Md = "MD"
    Me = "ME"
    Mf = "MF"
    Mg = "MG"
    Mh = "MH"
    Mk = "MK"
    Ml = "ML"
    Mm = "MM"
    Mn = "MN"
    Mo = "MO"
    Mp = "MP"
    Mq = "MQ"
    Mr = "MR"
    Ms = "MS"
    Mt = "MT"
    Mu = "MU"
    Mv = "MV"
    Mw = "MW"
    Mx = "MX"
    My = "MY"
    Mz = "MZ"
    Na = "NA"
    Nc = "NC"
    Ne = "NE"
    Nf = "NF"
    Ng = "NG"
    Ni = "NI"
    Nl = "NL"
    No = "NO"
    Np = "NP"
    Nr = "NR"
    Nu = "NU"
    Nz = "NZ"
    Om = "OM"
    Pa = "PA"
    Pe = "PE"
    Pf = "PF"
    Pg = "PG"
    Ph = "PH"
    Pk = "PK"
    Pl = "PL"
    Pm = "PM"
    Pn = "PN"
    Pr = "PR"
    Ps = "PS"
    Pt = "PT"
    Pw = "PW"
    Py = "PY"
    Qa = "QA"
    Re = "RE"
    Ro = "RO"
    Rs = "RS"
    Ru = "RU"
    Rw = "RW"
    Sa = "SA"
    Sb = "SB"
    Sc = "SC"
    Sd = "SD"
    Se = "SE"
    Sg = "SG"
    Sh = "SH"
    Si = "SI"
    Sj = "SJ"
    Sk = "SK"
    Sl = "SL"
    Sm = "SM"
    Sn = "SN"
    So = "SO"
    Sr = "SR"
    Ss = "SS"
    St = "ST"
    Sv = "SV"
    Sx = "SX"
    Sy = "SY"
    Sz = "SZ"
    Tc = "TC"
    Td = "TD"
    Tf = "TF"
    Tg = "TG"
    Th = "TH"
    Tj = "TJ"
    Tk = "TK"
    Tl = "TL"
    Tm = "TM"
    Tn = "TN"
    To = "TO"
    Tr = "TR"
    Tt = "TT"
    Tv = "TV"
    Tw = "TW"
    Tz = "TZ"
    Ua = "UA"
    Ug = "UG"
    Um = "UM"
    Us = "US"
    Uy = "UY"
    Uz = "UZ"
    Va = "VA"
    Vc = "VC"
    Ve = "VE"
    Vg = "VG"
    Vi = "VI"
    Vn = "VN"
    Vu = "VU"
    Wf = "WF"
    Ws = "WS"
    Ye = "YE"
    Yt = "YT"
    Za = "ZA"
    Zm = "ZM"
    Zw = "ZW"
