import streamlit as st
from azure.identity import ManagedIdentityCredential
from azure.storage.blob import BlobServiceClient

# Authenticate with system-managed identity
credential = ManagedIdentityCredential()

# Create BlobServiceClient
blob_service_client = BlobServiceClient(
    account_url="https://storagetrainingmay.blob.core.windows.net",
    credential=credential
)

# List containers
container_list = blob_service_client.list_containers()
st.title("List Storage Containers")

for container in container_list:
    st.write(container)

st.write("Listing Containers Done...")

