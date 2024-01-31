import random

class FogNode:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

def generate_blind_factor():
    return random.randint(1, 1000)

def tag_generation(data_owner_data, n, Texp, Tmul):
    # Tag generation stage - data owner runs TagGen algorithm
    # Computational cost: 2nTexp + nTmul
    tag = f"Tag generated for {data_owner_data} with computational cost {2*n*Texp + n*Tmul}"
    return tag

def proof_generation(tag, cb, Texp, Tmul):
    # Proof generation stage - computational cost: cbTexp + (cb - 1)Tmul
    proof = f"Proof generated for tag {tag} with cb={cb} and computational cost {cb*Texp + (cb-1)*Tmul}"
    return proof

def verification(tag, cb, Tp, Texp, Tmul):
    # Verification stage - computational cost: 3Tp + (cb + 1)Texp + cbTmul
    verification_result = f"Verification result for tag {tag}, cb={cb}, and computational cost {3*Tp + (cb+1)*Texp + cb*Tmul}"
    return verification_result

def ppdp_tag_generation(data_owner_data, n, Tp_ppdp, Texp_ppdp, Tmul_ppdp):
    # PPDP Tag generation stage
    # Computational cost: 2Tp_ppdp + Texp_ppdp + Tmul_ppdp
    tag = f"PPDP Tag generated for {data_owner_data} with computational cost {2*Tp_ppdp + Texp_ppdp + Tmul_ppdp}"
    return tag

def ppdp_proof_generation(tag, challenge, Texp_ppdp, Tmul_ppdp):
    # PPDP Proof generation stage
    # Computational cost: 2Texp_ppdp + Tmul_ppdp
    proof = f"PPDP Proof generated for tag {tag} and challenge {challenge} with computational cost {2*Texp_ppdp + Tmul_ppdp}"
    return proof

def ppdp_verification(tag, challenge, stored_data, Tp_ppdp, Texp_ppdp, Tmul_ppdp):
    # PPDP Verification stage
    # Computational cost: 3Tp_ppdp + 3Texp_ppdp + 2Tmul_ppdp
    verification_result = f"PPDP Verification result for tag {tag}, challenge {challenge}, and computational cost {3*Tp_ppdp + 3*Texp_ppdp + 2*Tmul_ppdp}"
    return verification_result

if __name__ == "__main__":
    fog_node1 = FogNode("FogNode1", 5)
    fog_node2 = FogNode("FogNode2", 3)
    fog_node3 = FogNode("FogNode3", 7)

    fog_nodes = [fog_node1, fog_node2, fog_node3]

    # User input for data
    original_data = input("Enter sensitive data: ")

    # User input for computational costs
    n = int(input("Enter value for n: "))  # Some value for n
    Tp = float(input("Enter value for Tp: "))  # Some value for Tp
    Texp = float(input("Enter value for Texp: "))  # Some value for Texp
    Tmul = float(input("Enter value for Tmul: "))  # Some value for Tmul

    # User selects options
    print("\nOptions:")
    print("1. Tag Generation")
    print("2. Proof Generation")
    print("3. Verification")
    print("4. PPDP Tag Generation")
    print("5. PPDP Proof Generation")
    print("6. PPDP Verification")

    option = int(input("Select an option (1/2/3/4/5/6): "))

    if option == 1:
        # Tag generation
        tag = tag_generation(original_data, n, Texp, Tmul)
        print("\nTag:", tag)
    elif option == 2:
        # Proof generation
        cb = int(input("Enter value for cb: "))  # Some value for cb
        proof = proof_generation(tag, cb, Texp, Tmul)
        print("Proof:", proof)
    elif option == 3:
        # Verification
        cb = int(input("Enter value for cb: "))  # Some value for cb
        verification_result = verification(tag, cb, Tp, Texp, Tmul)
        print("Verification Result:", verification_result)
    elif option == 4:
        # PPDP Tag generation
        ppdp_tag = ppdp_tag_generation(original_data, n, Tp, Texp, T
