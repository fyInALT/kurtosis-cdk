import os
import subprocess
import argparse
import zipfile

def download_file(enclave, file_name, destination_path):
    """
    Download a file from Kurtosis enclave to the specified destination path.
    
    :param enclave: The name of the Kurtosis enclave.
    :param file_name: The name of the file.
    :param destination_path: The destination path where the file will be downloaded.
    """
    # Ensure the destination directory exists
    os.makedirs(destination_path, exist_ok=True)
    
    # Construct the command to download the file
    command = f"kurtosis files download {enclave} {file_name} {destination_path}"
    
    # Execute the command
    try:
        subprocess.run(command, shell=True, check=True)
        print(f"Successfully downloaded {file_name} to {destination_path}")
    except subprocess.CalledProcessError as e:
        print(f"Failed to download {file_name}: {e}")

def zip_directory(folder_path, output_path):
    """
    Compresses the contents of a directory into a ZIP file.

    :param folder_path: Path to the directory to be compressed.
    :param output_path: Path where the ZIP file will be saved.
    """
    # Ensure the provided folder path exists
    if not os.path.exists(folder_path):
        raise FileNotFoundError(f"The directory {folder_path} does not exist.")

    # Create a ZipFile object in write mode
    with zipfile.ZipFile(output_path, 'w', compression=zipfile.ZIP_DEFLATED, compresslevel=9) as zipf:
        # Walk through the directory
        for root, dirs, files in os.walk(folder_path):
            # Loop over all the files in the current directory
            for file in files:
                # Construct the full file path
                file_path = os.path.join(root, file)
                # Construct the relative path (this will be the path inside the ZIP file)
                relative_path = os.path.relpath(file_path, folder_path)
                # Add the file to the ZIP file
                zipf.write(file_path, arcname=relative_path)

def main():
    # Parse command line arguments
    parser = argparse.ArgumentParser(description="Download files from Kurtosis enclave and organize them into a directory.")
    parser.add_argument("enclave", type=str, help="The name of the Kurtosis enclave")
    parser.add_argument("destination_root_path", type=str, help="The root directory where the files will be downloaded")
    args = parser.parse_args()

    # List of files to download, format: (file_name, destination_sub_path)
    files_to_download = [
        ("agglayer-config-artifact", "agglayer"),
        ("agglayer-keystore", "keystore"),
        ("agglayer-prover-config-artifact", "agglayer-prover"),
        ("aggoracle-keystore", "keystore"),
        ("bridge-config-artifact", "bridge"),
        ("cdk-aggoracle-config-artifact", "agglayer-kit"),
        ("combined.json", "config"),
        ("deploy_output.json", "config"),
        ("genesis.json", "config"),
        ("create_rollup_parameters.json", "config"),
        ("create_new_rollup.json", "config"),
        ("deploy_parameters.json", "config"),
        ("sequencer-keystore", "keystore"),
        ("sovereignadmin-keystore", "keystore"),
        ("claimtxmanager-keystore", "keystore"),
        ("op-deployer-configs", "op"),
        ("init.sql-030", "sql"),
        # Add more files as needed
    ]

    # Download each file
    for file_name, destination_sub_path in files_to_download:
        destination_path = os.path.join(args.destination_root_path, destination_sub_path)
        download_file(args.enclave, file_name, destination_path)

    # Zip all files
    parent_dir = os.path.dirname(args.destination_root_path)
    root_name = os.path.basename(args.destination_root_path)
    zip_destination_path = os.path.join(parent_dir, f"{root_name}.zip")
    zip_directory(args.destination_root_path, zip_destination_path)


if __name__ == "__main__":
    main()