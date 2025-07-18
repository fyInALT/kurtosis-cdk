# Download All Configs For Deployed Rollup

```bash
 python3 ./download.py cdk3 ./d6
INFO[2025-07-18T11:34:39+08:00] File package with identifier 'agglayer-config-artifact' extracted to '/home/fy/kurtosis-cdk/download/d6/agglayer' 
Successfully downloaded agglayer-config-artifact to ./d6/agglayer
INFO[2025-07-18T11:34:39+08:00] File package with identifier 'agglayer-keystore' extracted to '/home/fy/kurtosis-cdk/download/d6/keystore' 
Successfully downloaded agglayer-keystore to ./d6/keystore
INFO[2025-07-18T11:34:39+08:00] File package with identifier 'agglayer-prover-config-artifact' extracted to '/home/fy/kurtosis-cdk/download/d6/agglayer-prover' 
Successfully downloaded agglayer-prover-config-artifact to ./d6/agglayer-prover
INFO[2025-07-18T11:34:39+08:00] File package with identifier 'aggoracle-keystore' extracted to '/home/fy/kurtosis-cdk/download/d6/keystore' 
Successfully downloaded aggoracle-keystore to ./d6/keystore
INFO[2025-07-18T11:34:39+08:00] File package with identifier 'bridge-config-artifact' extracted to '/home/fy/kurtosis-cdk/download/d6/bridge' 
Successfully downloaded bridge-config-artifact to ./d6/bridge
INFO[2025-07-18T11:34:39+08:00] File package with identifier 'cdk-aggoracle-config-artifact' extracted to '/home/fy/kurtosis-cdk/download/d6/agglayer-kit' 
Successfully downloaded cdk-aggoracle-config-artifact to ./d6/agglayer-kit
INFO[2025-07-18T11:34:39+08:00] File package with identifier 'combined.json' extracted to '/home/fy/kurtosis-cdk/download/d6/config' 
Successfully downloaded combined.json to ./d6/config
INFO[2025-07-18T11:34:39+08:00] File package with identifier 'deploy_output.json' extracted to '/home/fy/kurtosis-cdk/download/d6/config' 
Successfully downloaded deploy_output.json to ./d6/config
INFO[2025-07-18T11:34:39+08:00] File package with identifier 'genesis.json' extracted to '/home/fy/kurtosis-cdk/download/d6/config' 
Successfully downloaded genesis.json to ./d6/config
INFO[2025-07-18T11:34:39+08:00] File package with identifier 'create_rollup_parameters.json' extracted to '/home/fy/kurtosis-cdk/download/d6/config' 
Successfully downloaded create_rollup_parameters.json to ./d6/config
INFO[2025-07-18T11:34:39+08:00] File package with identifier 'create_new_rollup.json' extracted to '/home/fy/kurtosis-cdk/download/d6/config' 
Successfully downloaded create_new_rollup.json to ./d6/config
INFO[2025-07-18T11:34:39+08:00] File package with identifier 'deploy_parameters.json' extracted to '/home/fy/kurtosis-cdk/download/d6/config' 
Successfully downloaded deploy_parameters.json to ./d6/config
INFO[2025-07-18T11:34:39+08:00] File package with identifier 'sequencer-keystore' extracted to '/home/fy/kurtosis-cdk/download/d6/keystore' 
Successfully downloaded sequencer-keystore to ./d6/keystore
INFO[2025-07-18T11:34:40+08:00] File package with identifier 'sovereignadmin-keystore' extracted to '/home/fy/kurtosis-cdk/download/d6/keystore' 
Successfully downloaded sovereignadmin-keystore to ./d6/keystore
INFO[2025-07-18T11:34:40+08:00] File package with identifier 'claimtxmanager-keystore' extracted to '/home/fy/kurtosis-cdk/download/d6/keystore' 
Successfully downloaded claimtxmanager-keystore to ./d6/keystore
INFO[2025-07-18T11:34:40+08:00] File package with identifier 'op-deployer-configs' extracted to '/home/fy/kurtosis-cdk/download/d6/op' 
Successfully downloaded op-deployer-configs to ./d6/op
INFO[2025-07-18T11:34:40+08:00] File package with identifier 'init.sql-030' extracted to '/home/fy/kurtosis-cdk/download/d6/sql' 
Successfully downloaded init.sql-030 to ./d6/sql
```

```bash
python3 ./download.py -h       
usage: download.py [-h] enclave destination_root_path

Download files from Kurtosis enclave and organize them into a directory.

positional arguments:
  enclave               The name of the Kurtosis enclave
  destination_root_path
                        The root directory where the files will be downloaded

options:
  -h, --help            show this help message and exit
```