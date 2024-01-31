import random

class RDPC:
    def __init__(self, fog_nodes):
        self.fog_nodes = fog_nodes
        self.Z = 100  # Example value for transmitted data size
        self.q = 10   # Example value for transmission delay factor
        self.n = 5    # Example value for the number of data blocks
        self.cb = 2   # Example value for the number of challenge blocks

    def allocate_optimal_path(self):
        # Simulating dynamic allocation of optimal path
        return random.choice(self.fog_nodes)

    def data_upload_stage(self):
        # Data Upload Communication Overhead Analysis
        optimal_fog_node = self.allocate_optimal_path()
        data_upload_overhead = self.n + self.n * self.q
        print(f"Data Upload Communication Overhead: {data_upload_overhead}")
        print(f"Data sent to fog node: {optimal_fog_node}")
        # Perform other processing steps in data upload stage

    def tpa_challenge_stage(self):
        # TPA Challenge Communication Overhead Analysis
        tpa_challenge_overhead = 3 * self.Z * self.q
        print(f"TPA Challenge Communication Overhead: {tpa_challenge_overhead}")
        # Perform other processing steps in TPA Challenge stage

    def csp_response_stage(self):
        # CSP Response Communication Overhead Analysis
        csp_response_overhead = self.n + self.Z * self.q
        print(f"CSP Response Communication Overhead: {csp_response_overhead}")
        # Perform other processing steps in CSP Response stage

class CommunicationOverheadAnalysis:
    def __init__(self):
        self.Z = 100  # Example value for transmitted data size
        self.q = 10   # Example value for transmission delay factor
        self.n = 5    # Example value for the number of data blocks
        self.cb = 2   # Example value for the number of challenge blocks

    def communication_overhead_analysis(self):
        # Data Upload stage
        data_upload_overhead = self.calculate_data_upload_overhead()
        print(f"Data Upload Communication Overhead: {data_upload_overhead}")

        # TPA Challenge stage
        tpa_challenge_overhead = self.calculate_tpa_challenge_overhead()
        print(f"TPA Challenge Communication Overhead: {tpa_challenge_overhead}")

        # CSP Response stage
        csp_response_overhead = self.calculate_csp_response_overhead()
        print(f"CSP Response Communication Overhead: {csp_response_overhead}")

    def calculate_data_upload_overhead(self):
        # Calculate the communication overhead for Data Upload stage
        data_upload_overhead = self.n + self.n * self.q - self.calculate_tau(self.n + self.n * self.q)
        return data_upload_overhead

    def calculate_tpa_challenge_overhead(self):
        # Calculate the communication overhead for TPA Challenge stage
        tpa_challenge_overhead = 3 * self.Z * self.q - self.calculate_tau(3 * self.Z * self.q)
        return tpa_challenge_overhead

    def calculate_csp_response_overhead(self):
        # Calculate the communication overhead for CSP Response stage
        csp_response_overhead = self.n + self.Z * self.q - self.calculate_tau(self.n + self.Z * self.q)
        return csp_response_overhead

    def calculate_tau(self, value):
        # Placeholder function for calculating tau
        return value  # Replace with the actual tau calculation

# User input for fog nodes
fog_nodes_rdpc = input("Enter fog nodes (comma-separated): ").split(", ")
rdpc_scheme = RDPC(fog_nodes_rdpc)

# User input for data size and other parameters
user_Z = int(input("Enter transmitted data size (Z): "))
user_q = int(input("Enter transmission delay factor (q): "))
user_n = int(input("Enter the number of data blocks (n): "))
user_cb = int(input("Enter the number of challenge blocks (cb): "))

communication_analysis = CommunicationOverheadAnalysis()

# User menu for options
while True:
    print("\nOptions:")
    print("1. Perform RDPC Scheme Communication Overhead Analysis")
    print("2. Perform Generic Communication Overhead Analysis")
    print("3. Exit")

    choice = input("Enter your choice (1/2/3): ")

    if choice == "1":
        # Set user-provided values
        rdpc_scheme.Z = user_Z
        rdpc_scheme.q = user_q
        rdpc_scheme.n = user_n
        rdpc_scheme.cb = user_cb

        print("\nRDPC Scheme Communication Overhead Analysis:")
        rdpc_scheme.data_upload_stage()
        rdpc_scheme.tpa_challenge_stage()
        rdpc_scheme.csp_response_stage()

    elif choice == "2":
        # Set user-provided values
        communication_analysis.Z = user_Z
        communication_analysis.q = user_q
        communication_analysis.n = user_n
        communication_analysis.cb = user_cb

        print("\nGeneric Communication Overhead Analysis:")
        communication_analysis.communication_overhead_analysis()

    elif choice == "3":
        print("Exiting program. Goodbye!")
        break

    else:
        print("Invalid choice. Please enter a valid option.")
