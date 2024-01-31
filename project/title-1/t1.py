from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import hashes
import random

class DBCFModel:
    def __init__(self):
        self.cloud_storage = {}
        self.fog_nodes = []
        self.data_owner_keys = self.setup()
        self.file_data = None
        self.tag_set = None
        self.challenge_info = None
        self.proofs = None

    def setup(self):
        # Algorithm 1: Setup
        private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048,
        )
        public_key = private_key.public_key()
        return public_key, private_key

    def tag_gen(self, file_data):
        # Algorithm 2: TagGen
        tag_set = []
        for block in file_data:
            tag = hashes.Hash(hashes.SHA256())
            tag.update(block.encode())
            tag_set.append(tag.finalize().hex())
        return tag_set

    def challenge(self, num_blocks):
        # Algorithm 3: Challenge
        return random.sample(range(1, num_blocks + 1), num_blocks)

    def proof_gen(self, file_data, tag_set, challenge_info):
        # Algorithm 4: ProofGen
        proofs = []
        for block_num in challenge_info:
            block_data = file_data[block_num - 1]
            tag = tag_set[block_num - 1]

            # Simulating proof generation using SHA256 hash
            proof_data = hashes.Hash(hashes.SHA256())
            proof_data.update((block_data + tag).encode())
            proofs.append(proof_data.finalize().hex())

        return proofs

    def verify(self, file_data, tag_set, challenge_info, proofs):
        # Algorithm 5: Verify
        for i, block_num in enumerate(challenge_info):
            block_data = file_data[block_num - 1]
            tag = tag_set[block_num - 1]
            proof_data = proofs[i]

            # Simulating verification using SHA256 hash
            expected_proof = hashes.Hash(hashes.SHA256())
            expected_proof.update((block_data + tag).encode())
            expected_proof = expected_proof.finalize().hex()

            if proof_data != expected_proof:
                return 0  # Verification failed

        return 1  # Verification successful

    def input_data(self):
        # Allow the user to input data
        num_blocks = int(input("Enter the number of data blocks: "))
        self.file_data = [input(f"Enter data for Block {i + 1}: ") for i in range(num_blocks)]
        print("Data input successful.")

    def audit_data(self):
        if not self.file_data:
            print("Error: Data not available. Please input data first.")
            return

        # Simulating the data integrity audit process
        self.tag_set = self.tag_gen(self.file_data)
        self.challenge_info = self.challenge(len(self.file_data))
        self.proofs = self.proof_gen(self.file_data, self.tag_set, self.challenge_info)
        verification_result = self.verify(self.file_data, self.tag_set, self.challenge_info, self.proofs)

        if verification_result:
            print("Data integrity verified successfully.")
        else:
            print("Data integrity verification failed.")

# Sample usage
data_owner = DBCFModel()

while True:
    print("\nOptions:")
    print("1. Input Data")
    print("2. Audit Data")
    print("3. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        data_owner.input_data()

    elif choice == '2':
        data_owner.audit_data()

    elif choice == '3':
        print("Exiting the program.")
        break

    else:
        print("Invalid choice. Please try again.")
