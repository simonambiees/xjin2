import subprocess


def main():
    subprocess.run(["apt-get", "update"])
    subprocess.run(["apt-get", "install", "-y", "binwalk"])
    subprocess.run(["tar", "-xzvf", "latest_scandal.tar.gz"])
    subprocess.run(["binwalk", "--extract", "the_building_photo.jpg"])
    subprocess.run(["tar", "-xzvf", "_the_building_photo.jpg.extracted/8EA9.gz"])
    with open('./flag.txt', 'r') as r:
        flag = r.read().strip()
        with open('./flag', 'w') as w:
            w.write(flag)


if __name__ == "__main__":
    main()