import random

class PPDP:
    def __init__(self, fog_nodes):
        self.fog_nodes = fog_nodes
        self.Z = 100  # Example value for transmitted data size
        self.q = 10   # Example value for transmission delay factor
        self.n = 5    # Example value for the number of data blocks
        self.cb = 2   # Example value for the number of challenge blocks

    def allocate_optimal_path(self):
        # Simulating dynamic allocation of optimal path
        return random.choice(self.fog_nodes)

    def do_to_csp_stage(self):
        # DOtoCSP Communication Overhead Analysis
        optimal_fog_node = self.allocate_optimal_path()
        DOtoCSP_overhead = self.n + self.n * self.q
        print(f"DOtoCSP Communication Overhead: {DOtoCSP_overhead}")
        print(f"Data sent to fog node: {optimal_fog_node}")
        # Perform other processing steps in DOtoCSP stage

    def tpa_to_csp_stage(self):
        # TPAtoCSP Communication Overhead Analysis
        TPAtoCSP_overhead = 3 * self.Z * self.q
        print(f"TPAtoCSP Communication Overhead: {TPAtoCSP_overhead}")
        # Perform other processing steps in TPAtoCSP stage

    def csp_to_tpa_stage(self):
        # CSPtoTPA Communication Overhead Analysis
        CSPtoTPA_overhead = self.n + self.Z * self.q
        print(f"CSPtoTPA Communication Overhead: {CSPtoTPA_overhead}")
        # Perform other processing steps in CSPtoTPA stage

class CommunicationOverheadAnalysis:
    def __init__(self):
        self.Z = 100  # Example value for transmitted data size
        self.q = 10   # Example value for transmission delay factor
        self.n = 5    # Example value for the number of data blocks
        self.cb = 2   # Example value for the number of challenge blocks

    def communication_overhead_analysis(self):
        # DOtoCSP stage
        DOtoCSP_overhead = self.calculate_DOtoCSP_overhead()
        print(f"DOtoCSP Communication Overhead: {DOtoCSP_overhead}")

        # TPAtoCSP stage
        TPAtoCSP_overhead = self.calculate_TPAtoCSP_overhead()
        print(f"TPAtoCSP Communication Overhead: {TPAtoCSP_overhead}")

        # CSPtoTPA stage
        CSPtoTPA_overhead = self.calculate_CSPtoTPA_overhead()
        print(f"CSPtoTPA Communication Overhead: {CSPtoTPA_overhead}")

    def calculate_DOtoCSP_overhead(self):
        # Calculate the communication overhead for DOtoCSP stage
        DOtoCSP_overhead = self.n + self.n * self.q - self.calculate_tau(self.n + self.n * self.q)
        return DOtoCSP_overhead

    def calculate_TPAtoCSP_overhead(self):
        # Calculate the communication overhead for TPAtoCSP stage
        TPAtoCSP_overhead = 3 * self.Z * self.q - self.calculate_tau(3 * self.Z * self.q)
        return TPAtoCSP_overhead

    def calculate_CSPtoTPA_overhead(self):
        # Calculate the communication overhead for CSPtoTPA stage
        CSPtoTPA_overhead = self.n + self.Z * self.q - self.calculate_tau(self.n + self.Z * self.q)
        return CSPtoTPA_overhead

    def calculate_tau(self, value):
        # Placeholder function for calculating tau
        return value  # Replace with the actual tau calculation

# User input for fog nodes
fog_nodes_ppdp = input("Enter fog nodes (comma-separated): ").split(", ")
ppdp_scheme = PPDP(fog_nodes_ppdp)

# User input for data size and other parameters
user_Z = int(input("Enter transmitted data size (Z): "))
user_q = int(input("Enter transmission delay factor (q): "))
user_n = int(input("Enter the number of data blocks (n): "))
user_cb = int(input("Enter the number of challenge blocks (cb): "))

communication_analysis = CommunicationOverheadAnalysis()

# User menu for options
while True:
    print("\nOptions:")
    print("1. Perform PPDP Scheme Communication Overhead Analysis")
    print("2. Perform Generic Communication Overhead Analysis")
    print("3. Exit")

    choice = input("Enter your choice (1/2/3): ")

    if choice == "1":
        # Set user-provided values
        ppdp_scheme.Z = user_Z
        ppdp_scheme.q = user_q
        ppdp_scheme.n = user_n
        ppdp_scheme.cb = user_cb

        print("\nPPDP Scheme Communication Overhead Analysis:")
        ppdp_scheme.do_to_csp_stage()
        ppdp_scheme.tpa_to_csp_stage()
        ppdp_scheme.csp_to_tpa_stage()

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
