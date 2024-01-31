import random

class FogNode:
    def __init__(self, node_id, weight):
        self.node_id = node_id
        self.weight = weight

    def process_data(self, data):
        print(f"Fog Node {self.node_id} processing data: {data}")
        return f"Processed data by Fog Node {self.node_id}"

class FogComputingLayer:
    def __init__(self, fog_nodes):
        self.fog_nodes = fog_nodes

    def allocate_optimal_path(self, data):
        chosen_node = random.choice(self.fog_nodes)
        return chosen_node.process_data(data)

class CloudService:
    def transmit_data(self, data):
        print(f"Transmitting data to cloud: {data}")
        return "Data transmitted to cloud"

class DataOwner:
    def __init__(self):
        self.data_store = {}

    def store_sensitive_data(self, user_id, data):
        self.data_store[user_id] = data
        print(f"Sensitive data stored for User ID {user_id}")

    def generate_evidence(self, user_id):
        data = self.data_store.get(user_id)
        if data:
            blind_factor = random.randint(1, 10)
            evidence = f"Blind factor: {blind_factor}, Original data: {data}"
            print(f"Evidence generated: {evidence}")
            return evidence
        else:
            print(f"No data found for User ID {user_id}")
            return None

    def generate_tag(self, data):
        # Simulate TagGen algorithm
        computational_cost = 2 * len(data)  # Placeholder, replace with actual cost calculation
        print(f"Tag generation complete. Computational cost: {computational_cost}")
        return "Generated Tag"

class DataIntegrityAuditScheme:
    def __init__(self, fog_layer, cloud_service, data_owner):
        self.fog_layer = fog_layer
        self.cloud_service = cloud_service
        self.data_owner = data_owner

    def upload_data_to_csp(self, data):
        processed_data = self.fog_layer.allocate_optimal_path(data)
        communication_overhead = self.optimize_communication_overhead(processed_data)
        self.cloud_service.transmit_data(processed_data)
        print("Data upload to CSP complete.")
        return communication_overhead

    def submit_challenge_to_csp(self, challenge_info):
        communication_overhead = self.optimize_communication_overhead(challenge_info)
        self.cloud_service.transmit_data(challenge_info)
        print("Challenge submission to CSP complete.")
        return communication_overhead

    def generate_proof_by_csp(self, proof_info):
        communication_overhead = self.optimize_communication_overhead(proof_info)
        print("Proof generation by CSP complete.")
        return communication_overhead

    def optimize_communication_overhead(self, data):
        optimized_overhead = len(data)  # Placeholder, replace with actual optimization logic
        print(f"Optimized communication overhead: {optimized_overhead}")
        return optimized_overhead

# Sample usage with user interaction
fog_node1 = FogNode(1, 0.8)
fog_node2 = FogNode(2, 0.6)
fog_nodes = [fog_node1, fog_node2]

fog_layer = FogComputingLayer(fog_nodes)
cloud_service = CloudService()
data_owner = DataOwner()

audit_scheme = DataIntegrityAuditScheme(fog_layer, cloud_service, data_owner)

while True:
    print("\n1. Store sensitive data")
    print("2. Audit data integrity")
    print("3. Generate Tag")
    print("4. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        try:
            user_id = input("Enter your User ID: ")
            sensitive_data = input("Enter sensitive data: ")
            data_owner.store_sensitive_data(user_id, sensitive_data)
        except Exception as e:
            print(f"Error: {e}")

    elif choice == '2':
        try:
            user_id = input("Enter your User ID to audit data integrity: ")
            data_to_audit = data_owner.generate_evidence(user_id)

            if data_to_audit:
                # Simulate DOtoCSP stage
                upload_communication_overhead = audit_scheme.upload_data_to_csp(data_to_audit)
                
                # Simulate TPAtoCSP stage
                challenge_info = "Challenge information"
                challenge_communication_overhead = audit_scheme.submit_challenge_to_csp(challenge_info)

                # Simulate CSPtoTPA stage
                proof_info = "Proof information"
                proof_communication_overhead = audit_scheme.generate_proof_by_csp(proof_info)

        except Exception as e:
            print(f"Error: {e}")

    elif choice == '3':
        data_to_tag = "Data to tag"
        data_owner.generate_tag(data_to_tag)

    elif choice == '4':
        print("Exiting the program.")
        break

    else:
        print("Invalid choice. Please try again.")
