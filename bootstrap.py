from colorama import init,Fore,Style
init()
import os
import sys
import typer

def info(msg):
    print(Fore.WHITE + msg)
    print(Style.RESET_ALL)


def yellow(msg):
    print(Fore.YELLOW + msg)
    print(Style.RESET_ALL)

def warn(msg):
    print(Fore.RED + msg)
    print(Style.RESET_ALL)

#System setup
if os.getuid() != 0:
    warn('Please be root first...')
    sys.exit()

def system_setup():
    yellow('System setups...')

    ## sudoers
    info('- copy sudoer to /etc')
    os.system("cp confs/sudoers /etc/")

    ## pacman.conf
    info('- copy pacman.conf')
    os.system("cp confs/pacman.conf /etc/")

    ## mirrorlist
    info('- copy mirrorlist')
    os.system("cp confs/mirrorlist /etc/pacman.d")

    ## enable sshd.service
    info('- enable ssh service')
    os.system("systemctl enable sshd.service")
    os.system("systemctl start sshd.service")

    ## system update
    info('- system update')
    os.system("pacman -Syu")



def install_pkgs():
    yellow("Installing packages...")
    PKGS = ["btop","htop","mc","byobu","xfce4-terminal","neovim","vim","yay"]
    FONTS = ["ttf-intone-nerd"]
    os.system("pacman -S " + " ".join(PKGS + FONTS))
    info("installing google-chrome")
    os.system("sudo -u niklas yay -S google-chrome") 



if __name__ == '__main__':
    system_setup()
    install_pkgs()



