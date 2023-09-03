import os

# Renk kodları
reset_color = "\033[0m"
black_color = "\033[0;30m"
red_color = "\033[0;31m"
green_color = "\033[0;32m"
yellow_color = "\033[0;33m"
blue_color = "\033[0;34m"
purple_color = "\033[0;35m"
cyan_color = "\033[0;36m"
white_color = "\033[0;37m"
bold_black_color = "\033[1;30m"
bold_red_color = "\033[1;31m"
bold_green_color = "\033[1;32m"
bold_yellow_color = "\033[1;33m"
bold_blue_color = "\033[1;34m"
bold_purple_color = "\033[1;35m"
bold_cyan_color = "\033[1;36m"
bold_white_color = "\033[1;37m"

def generate_custom_banner(username):
    custom_banner = f"""
{bold_blue_color}
         _nnnn_
        dGGGGMMb     ,.......................
       @p~qp~~qMb    | Hoşgeldin {username} |
       M|@||@) M|   _;.......................
       @,----.JM| -'
      JS^\__/  qKL
     dZP        qKRb
    dZP          qKKb
   fZP            SMMb
   HZM            MMMM
   FqM            MMMM
 __| ".        |\dS"qML
 |    `.       | `' \Zq
_)      \.___.,|     .'
\____   )MMMMMM|   .'
     `-'       `--'
{reset_color}
"""
    return custom_banner

def termux_banner():
    termux_banner = f"""
{bold_red_color}
{bold_red_color} ⠀⠀⣰⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⣆⠀  {reset_color}
{bold_red_color}⠀⠀⣼⣿⣿⣿⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣿⣿⣿⣧  {reset_color}
{bold_red_color}⠀⢰⣿⣿⡟⠈⣿⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⠁⢻⣿⣿⡆ {reset_color}{bold_purple_color}Tool Name:{reset_color}{bold_cyan_color}TermuxBanner{reset_color}
{bold_red_color}⠀⠘⣿⣿⡇⠀⠸⡟⢿⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡿⢻⠇⠀⢸⣿⣿⠃ {reset_color}{bold_purple_color}Producer:{reset_color}{bold_cyan_color}Coderfenrir{reset_color}
{bold_red_color}⠀⠀⠈⠙⠻⠦⢤⣄⣀⣙⣷⣤⡀⠀⠀⠀⠀⢀⣤⣾⣋⣀⣠⡤⠴⠟⠋⠁⠀ {reset_color}{bold_purple_color}Version:{reset_color}{bold_cyan_color}1.0{reset_color}⠀
{bold_green_color}
████████╗   ██████╗  █████╗ ███╗   ██╗███╗   ██╗███████╗██████╗
╚══██╔══╝   ██╔══██╗██╔══██╗████╗  ██║████╗  ██║██╔════╝██╔══██╗
   ██║█████╗██████╔╝███████║██╔██╗ ██║██╔██╗ ██║█████╗  ██████╔╝
   ██║╚════╝██╔══██╗██╔══██║██║╚██╗██║██║╚██╗██║██╔══╝  ██╔══██╗
   ██║      ██████╔╝██║  ██║██║ ╚████║██║ ╚████║███████╗██║  ██║
   ╚═╝      ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝
{reset_color}{bold_purple_color}Insta / Github: coderfenrir{reset_color}
"""
    return termux_banner

def clear_screen():
    os.system('clear')

def customize_termux_motd(username):
    try:
        clear_screen()
        custom_banner = generate_custom_banner(username)
        with open('/data/data/com.termux/files/usr/etc/motd', 'w') as motd_file:
            motd_file.write(custom_banner)

        print("Termux motd başarıyla özelleştirildi!")

    except Exception as e:
        print(f"Bir hata oluştu: {e}")
        print("Termux motd özelleştirmekte başarısız oldu.")

def customize_termux_interface(username):
    try:
        custom_prompt = f'\\n\\[$(tput setaf 1)\\]┌─[\\[$(tput sgr0)\\] root@{username} \\[$(tput setaf 3)\\]]─[\\[$(tput setaf 2)\\] {username} \\[$(tput setaf 1)\\]] \\n\\[$(tput setaf 3)\\]└─>\\[$(tput setaf 3)\\]'

        os.system(f'echo "PS1=\'{custom_prompt}\'" > ~/.bashrc')

        print("Termux arayüzü başarıyla renklendirilmiş ve kişiselleştirilmiştir!")

    except Exception as e:
        print(f"Bir hata oluştu: {e}")
print("Termux arayüzünü özelleştirmekte başarısız oldu.") 

if __name__ == "__main__":
    while True:
        clear_screen()
        print(termux_banner())
        print(f"{bold_green_color}[{bold_white_color}01{green_color}] {bold_cyan_color}Arayüz Özelleştir")
        print(f"{bold_green_color}[{bold_white_color}X{green_color}] {bold_cyan_color}Exit")
        choice = input("Seçiminizi yapın: ")

        if choice == "01":
            username = input("Kullanıcı adınızı girin: ")
            customize_termux_interface(username)
            customize_termux_motd(username)
        elif choice == "X":
            print("Çıkılıyor...")
            break
        else:
            print("Geçersiz seçenek, tekrar deneyin.")
