def solution(pb):
    
    for p in pb:
        for b in pb:
            if p.startswith(b):
                if p!=b:
                    return False
    
    return True
