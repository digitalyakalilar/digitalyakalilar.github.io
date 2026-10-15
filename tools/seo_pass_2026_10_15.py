import re,sys
B="/workspace/blog/posts/"
def edit(path, fm, first_add, renames, before_first_h2, links, faq, extra=None):
    s=open(B+path).read()
    _,f,body=s.split("---",2)
    lines=[l for l in f.strip().splitlines() if not l.split(":")[0] in fm]
    for k,v in fm.items(): lines.append(f"{k}: {v}")
    body=body.lstrip("\n")
    i=body.index("\n\n"); body=body[:i]+" "+first_add+body[i:]
    for a,b in renames:
        assert a in body,(path,a); body=body.replace(a,b,1)
    if before_first_h2:
        j=body.index("\n## "); body=body[:j]+"\n\n"+before_first_h2.strip()+"\n"+body[j:]
    if extra:
        anchor,txt=extra; assert anchor in body,(path,anchor); body=body.replace(anchor,txt.strip()+"\n\n"+anchor,1)
    m=re.search(r"\n## (Bu ne anlama geliyor|What it means)[^\n]*\n",body); assert m,path
    k=body.index("\n## ",m.end()); body=body[:k]+"\n\n"+links.strip()+"\n"+body[k:]
    ref="\n## Kaynaklar" if not path.startswith("en/") else "\n## References"
    k=body.index(ref); body=body[:k]+"\n\n"+faq.strip()+"\n"+body[k:]
    body=re.sub(r"\n{3,}","\n\n",body)
    open(B+path,"w").write("---\n"+"\n".join(lines)+"\n---\n"+body)
exec(open(sys.argv[1]).read())
