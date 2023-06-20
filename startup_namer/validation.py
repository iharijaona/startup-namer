import whois 
from tqdm import tqdm
import multiprocessing as mp

def is_domain_available(candidate: dict, tldr=["fr", "com"]) -> bool:
    """
    A function that returns a boolean indicating 
    whether a `domain_name` is registered
    """
    is_available = True
    for root in tldr:
        try:
            domain_name = f'{candidate["name"]}.{root}'.lower()
            w = whois.whois(domain_name)
            is_available = not bool(w.domain_name)
            # print(f'{domain_name} => ', "Available" if is_available else "Exists")
            if not is_available:
                break
        except Exception:
            is_available = True
    return is_available, candidate["name"]
    
def vilidate_availabilty(candidates: list[dict]) -> list[dict]:
    pool = mp.Pool(mp.cpu_count())
    for idx,(is_available, name)  in enumerate(tqdm(pool.imap(is_domain_available, candidates), total=len(candidates))):
        assert candidates[idx]['name'] == name
        candidates[idx]['available'] = is_available
    pool.close()
    return candidates