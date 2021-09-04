echo "Building project"
docker build -t project_name:latest .

echo "Saving image to project.tar"
docker save project_name:latest | gzip > tar_name.tar