import hashlib
import random

class RemoteServer:
    def __init__(self, stored_data):
        self.stored_data = stored_data

class DataOwner:
    def __init__(self, data):
        self.data = data

def generate_challenge():
    return random.randint(1, 1000)

def tag_generation(data_owner, Tp, Texp, Tmul):
    # RDPC Tag generation stage
    # Computational cost: 2Tp + Texp + Tmul
    tag = f"RDPC Tag generated for {data_owner.data} with computational cost {2*Tp + Texp + Tmul}"
    return tag

def proof_generation(tag, challenge, Texp, Tmul):
    # RDPC Proof generation stage
    # Computational cost: 2Texp + Tmul
    proof = f"RDPC Proof generated for tag {tag} and challenge {challenge} with computational cost {2*Texp + Tmul}"
    return proof

def verification(tag, challenge, stored_data, Tp, Texp, Tmul):
    # RDPC Verification stage
    # Computational cost: 3Tp + 3Texp + 2Tmul
    verification_result = f"RDPC Verification result for tag {tag}, challenge {challenge}, and computational cost {3*Tp + 3*Texp + 2*Tmul}"

    # Verify the stored data integrity using the tag, challenge, and stored data
    computed_tag = tag_generation(DataOwner(stored_data), Tp, Texp, Tmul)
    if computed_tag == tag:
        verification_result += "\nData integrity verified."
    else:
        verification_result += "\nData integrity not verified."

    return verification_result

if __name__ == "__main__":
    # User input for data details
    user_data = input("Enter your details: ")

    data_owner = DataOwner(user_data)
    remote_server = RemoteServer(data_owner.data)

    # User input for computational costs
    Tp_rdpc = float(input("Enter value for Tp (RDPC): "))  # Some value for Tp in RDPC
    Texp_rdpc = float(input("Enter value for Texp (RDPC): "))  # Some value for Texp in RDPC
    Tmul_rdpc = float(input("Enter value for Tmul (RDPC): "))  # Some value for Tmul in RDPC

    # RDPC Tag generation
    rdpc_tag = tag_generation(data_owner, Tp_rdpc, Texp_rdpc, Tmul_rdpc)
    print("\nRDPC Tag:", rdpc_tag)

    # User input for RDPC challenge
    rdpc_challenge = generate_challenge()

    # RDPC Proof generation
    rdpc_proof = proof_generation(rdpc_tag, rdpc_challenge, Texp_rdpc, Tmul_rdpc)
    print("RDPC Proof:", rdpc_proof)

    # User chooses whether to access and verify data details
    access_data = input("\nDo you want to access and verify data details? (yes/no): ").lower()

    if access_data == "yes":
        # RDPC Verification
        rdpc_verification_result = verification(rdpc_tag, rdpc_challenge, remote_server.stored_data, Tp_rdpc, Texp_rdpc, Tmul_rdpc)
        print("\nRDPC Verification Result:", rdpc_verification_result)
    else:
        print("Data details not accessed.")
