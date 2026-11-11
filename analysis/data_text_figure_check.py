import json, re, pandas as pd, sys
from pathlib import Path
R=Path("/home/ubuntu/repos/wip/pricing-the-rain"); sys.path.insert(0,str(R))
from manuscript.build_manuscript import replacements
v=replacements(); s=pd.read_csv(R/"results/general_summary.csv")
t2=pd.read_csv(R/"tables/table2_general_regimes.csv")
g=lambda reg,rule,m: float(s[(s.regime==reg)&(s.obs_rule==rule)&(s.metric==m)]["mean"].iloc[0])
checks=[]
def chk(name,ok): checks.append((name,ok))
# table2 vs summary
for _,row in t2.iterrows():
    for col in t2.columns:
        if col in ("Regime","Observation rule") or col.endswith("share_D_reputation"): continue
        chk(f"T2 {row['Regime']} {row['Observation rule']} {col}", abs(row[col]-g(row["Regime"],row["Observation rule"],col))<1e-9)
# text tokens vs summary
pairs={"D_REL_D_ENDO_COMMON":("common","endogenous","D_rel_D_reputation",2),"D_REL_D_ENDO_VRARE":("very_rare","endogenous","D_rel_D_reputation",2),
"REP_HAZARD_CORR_ENDO_RARE":("rare","endogenous","reputation_hazard_corr",3),"PRICE_DIFF_D_ENDO_RARE":("rare","endogenous","price_success_diff_D_reputation",3),
"B_SUBJ_SELECTIVE_ENDO_RARE":("rare","endogenous","B_subj_selective",3),"D_REL_B_ENDO_VRARE":("very_rare","endogenous","D_rel_B_experienced",2),"D_REL_C_ENDO_VRARE":("very_rare","endogenous","D_rel_C_weighted",2)}
for k,(a,b,c,d) in pairs.items(): chk(f"text {k}", v[k]==f"{g(a,b,c):.{d}f}")
md=(R/"manuscript/manuscript.md").read_text()
for k in pairs: chk(f"rendered {k}", v[k] in md)
# table 3 (equivalence) vs csv
eq=pd.read_csv(R/"results/general_observational_equivalence.csv"); t3=pd.read_csv(R/"tables/table4_observational_equivalence.csv")
chk("T3 rows", len(t3)==eq.groupby(["regime","obs_rule"]).ngroups)
# captions
cap=json.loads((R/"results/manuscript_values.json").read_text())["figure_captions"]["Figure 5"]
chk("Fig5 caption ratio", f"{s[(s.metric=='selection_ratio')&(s.obs_rule=='endogenous')]['mean'].mean():.2f}" in cap)
chk("no bounded frequency wording", "bounded frequency" not in md and "bounded frequency" not in cap)
# figure source: figures built from same summary file -> mtime order
import os
chk("figure4 newer than summary", os.path.getmtime(R/"figures/figure4_four_probabilities.png")>os.path.getmtime(R/"results/general_summary.csv"))
chk("figure5 newer than summary", os.path.getmtime(R/"figures/figure5_distortion_decomposition.png")>os.path.getmtime(R/"results/general_summary.csv"))
bad=[c for c in checks if not c[1]]
print(len(checks),"checks;",len(bad),"failed"); [print("FAIL",b[0]) for b in bad]
