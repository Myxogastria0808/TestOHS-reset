export LANG=ja_JP.UTF-8
export LC_CTYPE=ja_JP.UTF-8
cd ..
squoosh-cli --webp auto *.jpg -d post-processed-files
squoosh-cli --webp auto *.png -d post-processed-files
squoosh-cli --webp auto *.PNG -d post-processed-files
squoosh-cli --webp auto *.JPG -d post-processed-files
squoosh-cli --webp auto *.jpeg -d post-processed-files
squoosh-cli --webp auto *.JPEG -d post-processed-files