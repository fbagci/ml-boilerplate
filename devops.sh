echo "Build Project and Generate .tar file"
./install/build_project.sh

echo "Copy files to server and start project"
./install/copy_and_run_on_server.sh

# echo "Remove tar file"
# sudo rm project.tar