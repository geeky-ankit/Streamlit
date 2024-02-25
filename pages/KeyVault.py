import streamlit as st
from azure.identity import ManagedIdentityCredential
from azure.keyvault.secrets import SecretClient

# Authenticate with system-managed identity
credential = ManagedIdentityCredential()

# Create BlobServiceClient
secret_client = SecretClient(
    vault_url="https://may2023kv.vault.azure.net",
    credential=credential
)

# List containers
secret_list = secret_client.list_properties_of_secrets()
st.title("List Storage Containers")

for secret in secret_list:
    st.write(secret)

st.write("Listing Containers Done...")