#!/bin/bash

host_upgrade() {
    # Detect the package manager and update accordingly
    if command -v apt >/dev/null 2>&1; then
        echo "Detected Debian-based system. Updating with apt..."
        sudo apt update && sudo apt full-upgrade -y && sudo apt autoremove -y && sudo apt clean

    elif command -v dnf >/dev/null 2>&1; then
        echo "Detected RHEL-based system. Updating with dnf..."
        sudo dnf upgrade --refresh -y && sudo dnf autoremove -y && sudo dnf clean all

    elif command -v yum >/dev/null 2>&1; then
        echo "Detected older RHEL-based system. Updating with yum..."
        sudo yum update -y && sudo yum autoremove -y && sudo yum clean all

    elif command -v zypper >/dev/null 2>&1; then
        echo "Detected openSUSE-based system. Updating with zypper..."
        sudo zypper refresh && sudo zypper update -y && sudo zypper clean --all

    elif command -v pacman >/dev/null 2>&1; then
        echo "Detected Arch-based system. Updating with pacman..."
        sudo pacman -Syu --noconfirm && sudo pacman -Sc --noconfirm

    elif command -v apk >/dev/null 2>&1; then
        echo "Detected Alpine Linux. Updating with apk..."
        sudo apk update && sudo apk upgrade

    else
        echo "Unsupported OS or package manager not detected."
        return 1
    fi
}

# Uncomment the line below to execute the function when the script runs
host_upgrade
