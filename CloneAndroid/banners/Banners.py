class Banner(object):

	def Banner(self, port, user, password):
		pic = "\n"
		pic += "\n"
		pic += "\033[1;31m                \\     /                            \033[1;32m  \\     / \033[1;31m\n"
		pic += "            .oOOOOOOOOOOo                        \033[1;32m oOOOOOOOOOOo\033[1;31m \n"
		pic += "           .OOOOOOOOOOOOOOo     \033[1;36m--=======--\033[0m   \033[1;32m  OOOOOOOOOOOOOOo \033[1;31m\n"
		pic += "          oOOOOOOOOOOOOOOOOo             \033[1;32m      oOOOOOOOOOOOOOOOOo \033[1;31m\n"
		pic += "         .OO<  >OOOOOOO<  >O.    \033[1;36m ------- \033[0m \033[1;32m   .OO<  >OOOOOOO<  >O. \033[1;31m\n"
		pic += "         BOOOZZOOOOOOOOOZZOOH          \033[1;32m       BOOOZZOOOOOOOOOZZOOH \033[1;31m\n"
		pic += "     AO. ____________________ .OA      \033[1;32m   AO. ____________________ .OA \033[1;31m\n"
		pic += "    AOOA BOOOOOOOOOOOOOOOOOOH BOOH    \033[1;32m   AOOA BOOOOOOOOOOOOOOOOOOH BOOH \033[1;31m\n"
		pic += "    BOOH BOOOOOOOOOOOOOOOOOOH BOOH  \033[1;32m     BOOH BOOOOOOOOOOOOOOOOOOH BOOH\033[1;31m\n"
		pic += "    BOOH BOOOOOOOOOOOOOOOOOOH BOOH  \033[1;36m---\033[1;32m  BOOH BOOOOOOOOOOOOOOOOOOH BOOH\033[1;31m\n"
		pic += "    VOOV BOOOOOOOOOOOOOOOOOOH VOOV  \033[1;32m     VOOV BOOOOOOOOOOOOOOOOOOH VOOV\033[1;31m\n"
		pic += "     VO^ BOOOOOOOOOOOOOOOOOOH ^OV   \033[1;32m      VO^ BOOOOOOOOOOOOOOOOOOH ^OV\033[1;31m\n"
		pic += "         \\OOOOOOOOOOOOOOOOOO/       \033[1;36m --  \033[1;32m     \\OOOOOOOOOOOOOOOOOO/\033[1;31m\n"
		pic += "          \\OOOOOOOOOOOOOOOO/         \033[1;32m          \\OOOOOOOOOOOOOOOO/\033[1;31m\n"
		pic += "             BOOH     BOOH             \033[1;32m           OOOO     OOOO \033[1;31m\n"
		pic += "             BOOH     BOOH      \033[1;36m--======-- \033[0m  \033[1;32m     OOOO     BOOH \033[1;31m\n"
		pic += "             \\OO/     \\OO/\033[0m                        \\OO/     \\OO/\033[0m\n"
		pic += "\n"
		pic += "         /* ---===========================================--- *\\ \n"
		pic += "        -=***-            \033[1;36mCA - Clone Android\033[0m           \n"
		pic += "       --=**         Application running port {port}           \n".format(port=port)
		pic += "      --==*    Open in your browser \033[4;33mhttp://127.0.0.1:{port}\033[0m    \n".format(port=port)
		pic += "     --===*              User:     \033[6;37m{user}\033[0m            \n".format(user=user)
		pic += "      --==*              Password: \033[5;37m{password}\033[0m            \n".format(password=password)
		pic += "       --=**           Version 1.0 - Dario Sotelo            \n"
		pic += "        -=***-         	 \033[4;33mdario-s-c@outlook.com\033[0m            \n"
		pic += "         \\* ---===========================================--- */ \n"
		pic += ""
		
		return pic

	def BannerInvalid(self):
		pic = "\n"
		pic += " \033[1;33m [*] Sorry, you must specify a valid port, ej: python run.py [80, 8080, 8081 ...]\033[0m\n"
		pic += "\n"

		return pic

	def BannerError(self, port):
		pic = "\n"
		pic += " \033[1;31m [*] error running through port {port}\033[0m\n".format(port=port)
		pic += "\n"

		return pic
		
Banner = Banner()