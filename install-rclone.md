## Install rclone
- Download rclone: https://rclone.org/downloads/
- rclone config for Wasabi: https://rclone.org/s3/#wasabi

### Wasabi Config
S3 Provider = Wasabi
AWS Access Key ID = ****************
AWS Secret Access Key = LsDPz7zrjaaBqy2Ne7H16iwhasEUCR8nV1oQUp1s
Region = us-west-1
S3 Endpoint = s3.us-west-1.wasabisys.com
ACL = public-read

### Install Ubuntu
- need to upgrade to latest version of rclone by downloading (wget) and unpacking
1.) Configure rclone with wasabi config
2.) Create destination mapped folder
3.) rclone mount source folder to destination (note the case matters for rclone source name)

### Install RClone Docker Container
https://github.com/web2brain/docker-rclone-mount 
or forked from: https://github.com/Mumie-hub/docker-services/tree/master/rclone-mount

azVM-ND6 - Config file: /home/azureuser/.config/rclone/rclone.conf

sudo docker run -d --name rclone-mnt_wasabi-research \
    --restart=unless-stopped \
    --cap-add SYS_ADMIN \
    --device /dev/fuse \
    --security-opt apparmor:unconfined \
    -e RemotePath="wasabi:library-research-images" \
    -e MountCommands="--allow-other --allow-non-empty" \
    -v /root/.config/rclone/rclone.conf:/config/.rclone.conf \
    -v /datadrive/ext_mltooling/rclone_mnts/wasabi-research-archive:/mnt/data:shared \
    mumiehub/rclone-mount

- Not working correctly; can't seem to get rclone config to load properly into container
    - Issue help here: https://github.com/Mumie-hub/docker-services/issues/39

