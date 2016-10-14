# -*- coding:utf-8 -*-
#
# Gerador de index.html com molde nos exemplos de template do Bootstrap.
# Por Sabrina Andrade | 12.10.2016 | sdw@hotmail.com.br | github.com/sabrinandra
#
# Python 3.5.0

import os
import shutil
import urllib.request
import zipfile

# cria os diretorios
if "site" not in os.listdir(os.getcwd()):
    os.mkdir("site")
    os.mkdir("site/css")

# apaga arquivos utilizados anteriormente por outro modelo de template
if "bootstrap" in os.listdir("site"):
    shutil.rmtree("site/bootstrap/")

# cria os arquivos
html = open("site/index.html", "w")
css = open("site/css/index.css", "w")

# baixa e extrai o bootstrap
bootzip = "http://globocom.github.io/bootstrap/assets/bootstrap.zip"
urllib.request.urlretrieve(bootzip, "site/bootstrap.zip")
with zipfile.ZipFile("site/bootstrap.zip", "r") as b:
    b.extractall("site/")
os.remove("site/bootstrap.zip")


def main():
    print("-----------------")
    print("GERADOR DE INDEX")
    print("-----------------")

    tipos_site = ["simples", "marketing", "portifolio"]

    tipo = input("\nTipo de site(simples/marketing/portifolio): ").lower()
    while tipo not in tipos_site:
        print("\nTipo inválido.")
        tipo = input("Tipo de site(simples/marketing/portifolio): ").lower()

    if tipo == "simples":
        criar_html_simples()
        criar_css_simples()
    elif tipo == "portifolio":
        criar_html_port()
        criar_css_port()
    elif tipo == "marketing":
        criar_html_marketing()
        criar_css_marketing()

    print("\nSite gerado!")

# ---------------------------- variáveis base ----------------------------
# (insira aqui variaveis com conteudos que serao comuns a todos os modelos)

htmlinitial = ("<!DOCTYPE html>\n"
               "<html lang=\"en\">\n")

footer = ("      <hr>\n"
          "      <footer>\n"
          "        <p>&copy; Projeto 2016</p>\n"
          "      </footer>\n")


htmlfinal = ("    </body>\n"
             "</html>\n")
# ---------------------------- modelo simples ----------------------------
def criar_html_simples():
    head = ("\n"
            "  <head>\n"
            "    <meta charset=\"utf-8\">\n"
            "    <title>Pagina Simples</title>\n"
            "    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">\n"
            "    <meta name=\"description\" content=\"\">\n"
            "    <meta name=\"author\" content=\"\">\n"
            "    <!-- Estilos -->\n"
            "\n"
            "    <!-- CSS customizado -->\n"
            "    <link href=\"css/index.css\" rel=\"stylesheet\">"
            "\n"
            "    <link href=\"bootstrap/css/bootstrap.css\" rel=\"stylesheet\">\n"
            "    <style>\n"
            "      body {\n"
            "        padding-top: 60px; /* 60px to make the container go all the way to the bottom of the topbar */\n"
            "      }\n"
            "    </style>\n"
            "    <link href=\"bootstrap/css/bootstrap-responsive.css\" rel=\"stylesheet\">\n"
            "\n"
            "    <!-- Suporte de elementos do HTML5 para IE6-8 -->\n"
            "    <!--[if lt IE 9]>\n"
            "      <script src=\"http://html5shim.googlecode.com/svn/trunk/html5.js\"></script>\n"
            "    <![endif]-->\n"
            "\n"
            "    <!-- Favicon -->\n"
            "    <link rel=\"shortcut icon\" href=\"#\">\n"
            "  </head>\n")

    body = ("\n"
            "    <body>\n"
            "        <div class=\"navbar navbar-inverse navbar-fixed-top\">\n"
            "          <div class=\"navbar-inner\">\n"
            "            <div class=\"container\">\n"
            "              <a class=\"btn btn-navbar\" data-toggle=\"collapse\" data-target=\".nav-collapse\">\n"
            "                <span class=\"icon-bar\"></span>\n"
            "                <span class=\"icon-bar\"></span>\n"
            "                <span class=\"icon-bar\"></span>\n"
            "              </a>\n"
            "              <a class=\"brand\" href=\"#\">Pagina Simples</a>\n"
            "              <div class=\"nav-collapse collapse\">\n"
            "                <ul class=\"nav\">\n"
            "                  <li class=\"active\"><a href=\"#\">Inicio</a></li>\n"
            "                  <li><a href=\"#about\">Sobre</a></li>\n"
            "                  <li><a href=\"#contact\">Contato</a></li>\n"
            "                </ul>\n"
            "              </div><!--/.nav-collapse -->\n"
            "            </div>\n"
            "          </div>\n"
            "        </div>\n"
            "        <div class=\"container\">\n"
            "          <h1>Modelo Inicial - Bootstrap</h1>\n"
            "          <p>Utilize este documento para iniciar rapidamente qualquer novo projeto."
            "          <br> Index simples, com caminhos de arquivo predefinidos.</p>\n"
            "        </div>")

    html.write(htmlinitial +
               head + body +
               footer + htmlfinal)
    html.close()

def criar_css_simples():
    css.write("/* Insira seu CSS personalizado aqui! */")
    css.close()


# ---------------------------- modelo marketing ----------------------------
def criar_html_marketing():

    # baixa os js necessarios para o dropdown
    elementos = ["dropdown", "typeahead", "button", "carousel", "transition", "alert",
                 "modal", "scrollspy", "tab", "tooltip", "popover", "collapse"]

    for e in elementos:
        url = "http://globocom.github.io/bootstrap/assets/js/bootstrap-" + e + ".js"
        urllib.request.urlretrieve(url, "site/bootstrap/js/bootstrap-" + e +".js")

    jquery = "http://globocom.github.io/bootstrap/assets/js/jquery.js"
    urllib.request.urlretrieve(jquery,"site/bootstrap/js/jquery.js")

    head = ("  <head>\n"
            "    <meta charset=\"utf-8\">\n"
            "    <title>Marketing</title>\n"
            "    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">\n"
            "    <meta name=\"description\" content=\"\">\n"
            "    <meta name=\"author\" content=\"\">\n"
            "\n"
            "    <!-- Estilos -->\n"
            "    <link href=\"bootstrap/css/bootstrap.css\" rel=\"stylesheet\">\n"
            "\n"
            "    <!-- CSS customizado -->\n"
            "    <link href=\"css/index.css\" rel=\"stylesheet\">"
            "\n"
            "    <style type=\"text/css\">\n"
            "      body {\n"
            "        padding-top: 60px;\n"
            "        padding-bottom: 40px;\n"
            "      }\n"
            "    </style>\n"
            "    <link href=\"bootstrap/css/bootstrap-responsive.css\" rel=\"stylesheet\">\n"
            "\n"
            "    <!-- Suporte de elementos do HTML5 para IE6-8 -->\n"
            "    <!--[if lt IE 9]>\n"
            "      <script src=\"http://html5shim.googlecode.com/svn/trunk/html5.js\"></script>\n"
            "    <![endif]-->\n"
            "\n"
            "    <!-- Favicon -->\n"
            "    <link rel=\"shortcut icon\" href=\"#\">\n"
            "  </head>\n")

    body = ("\n"
            "   <body>\n"
            "    <div class=\"navbar navbar-inverse navbar-fixed-top\">\n"
            "      <div class=\"navbar-inner\">\n"
            "        <div class=\"container\">\n"
            "          <a class=\"btn btn-navbar\" data-toggle=\"collapse\" data-target=\".nav-collapse\">\n"
            "            <span class=\"icon-bar\"></span>\n"
            "            <span class=\"icon-bar\"></span>\n"
            "            <span class=\"icon-bar\"></span>\n"
            "          </a>\n"
            "          <a class=\"brand\" href=\"#\">Marketing</a>\n"
            "          <div class=\"nav-collapse collapse\">\n"
            "            <ul class=\"nav\">\n"
            "              <li class=\"active\"><a href=\"#\">Inicio</a></li>\n"
            "              <li><a href=\"#about\">Sobre</a></li>\n"
            "              <li><a href=\"#contact\">Contato</a></li>\n"
            "              <li class=\"dropdown\">\n"
            "                <a href=\"#\" class=\"dropdown-toggle\" data-toggle=\"dropdown\">Dropdown <b class=\"caret\"></b></a>\n"
            "                <ul class=\"dropdown-menu\">\n"
            "                  <li><a href=\"#\">Acao</a></li>\n"
            "                  <li><a href=\"#\">Outra acao</a></li>\n"
            "                  <li><a href=\"#\">Mais alguma coisa</a></li>\n"
            "                  <li class=\"divider\"></li>\n"
            "                  <li class=\"nav-header\">Nav inicial</li>\n"
            "                  <li><a href=\"#\">Link para separar</a></li>\n"
            "                  <li><a href=\"#\">Mais um link para separar</a></li>\n"
            "                </ul>\n"
            "              </li>\n"
            "            </ul>\n"
            "            <form class=\"navbar-form pull-right\">\n"
            "              <input class=\"span2\" type=\"text\" placeholder=\"E-mail\">\n"
            "              <input class=\"span2\" type=\"password\" placeholder=\"Senha\">\n"
            "              <button type=\"submit\" class=\"btn\">Entrar</button>\n"
            "            </form>\n"
            "          </div><!--/.nav-collapse -->\n"
            "        </div>\n"
            "      </div>\n"
            "    </div>\n"
            "\n"
            "    <div class=\"container\">\n"
            "\n"
            "      <!-- Unidade principal de uma mensagem de marketing primaria ou chamada a acao -->\n"
            "      <div class=\"hero-unit\">\n"
            "        <h1>Ola, mundo!</h1>\n"
            "        <p>Modelo para um marketing simples ou site informativo.\n"
            "        Ele inclui uma grande chamada e tres pecas de suporte de conteudo.\n"
            "        Use-o como um ponto de partida para criar algo mais original.</p>\n"
            "        <p><a class=\"btn btn-primary btn-large\">Leia mais &raquo;</a></p>\n"
            "      </div>\n"
            "\n"
            "      <!-- Example row of columns -->\n"
            "      <div class=\"row\">\n"
            "        <div class=\"span4\">\n"
            "          <h2>Titulo</h2>\n"
            "          <p>Donec id elit non mi porta gravida at eget metus. Fusce dapibus, tellus ac cursus commodo, tortor mauris condimentum nibh, ut fermentum massa justo sit amet risus. Etiam porta sem malesuada magna mollis euismod. Donec sed odio dui. </p>\n"
            "          <p><a class=\"btn\" href=\"#\">Ver detalhes &raquo;</a></p>\n"
            "        </div>\n"
            "        <div class=\"span4\">\n"
            "          <h2>Titulo</h2>\n"
            "          <p>Donec id elit non mi porta gravida at eget metus. Fusce dapibus, tellus ac cursus commodo, tortor mauris condimentum nibh, ut fermentum massa justo sit amet risus. Etiam porta sem malesuada magna mollis euismod. Donec sed odio dui. </p>\n"
            "          <p><a class=\"btn\" href=\"#\">Ver detalhes &raquo;</a></p>\n"
            "       </div>\n"
            "        <div class=\"span4\">\n"
            "          <h2>Titulo</h2>\n"
            "          <p>Donec sed odio dui. Cras justo odio, dapibus ac facilisis in, egestas eget quam. Vestibulum id ligula porta felis euismod semper. Fusce dapibus, tellus ac cursus commodo, tortor mauris condimentum nibh, ut fermentum massa justo sit amet risus.</p>\n"
            "          <p><a class=\"btn\" href=\"#\">Ver detalhes &raquo;</a></p>\n"
            "        </div>\n"
            "      </div>\n"
            "     </div>")

    js_marketing = ("     <!-- Colocado ao final do documento para que as paginas carreguem mais rapido -->\n"
                    "     <script src=\"../site/bootstrap/js/bootstrap-dropdown.js\"></script>\n"
                    "     <script src=\"../site/bootstrap/js/bootstrap-typeahead.js\"></script>\n"
                    "     <script src=\"../site/bootstrap/js/bootstrap-button.js\"></script>\n"
                    "     <script src=\"../site/bootstrap/js/bootstrap-transition.js\"></script>\n"
                    "     <script src=\"../site/bootstrap/js/bootstrap-alert.js\"></script>\n"
                    "     <script src=\"../site/bootstrap/js/bootstrap-modal.js\"></script>\n"
                    "     <script src=\"../site/bootstrap/js/bootstrap-scrollspy.js\"></script>\n"
                    "     <script src=\"../site/bootstrap/js/bootstrap-tab.js\"></script>\n"
                    "     <script src=\"../site/bootstrap/js/bootstrap-tooltip.js\"></script>\n"
                    "     <script src=\"../site/bootstrap/js/bootstrap-popover.js\"></script>\n"
                    "     <script src=\"../site/bootstrap/js/bootstrap-collapse.js\"></script>\n"
                    "     <script src=\"../site/bootstrap/js/jquery.js\"></script>\n"
                    "     <script src=\"../site/bootstrap/js/bootstrap-carousel.js\"></script>\n")

    html.write(htmlinitial +
               head + body +
               footer + js_marketing
               + htmlfinal)
    html.close()

def criar_css_marketing():
    css.write("/* Insira seu CSS personalizado aqui! */"
              "\nfooter {text-align: center;}")
    css.close()


# ---------------------------- modelo portifolio ----------------------------
def criar_html_port():

    # baixa bootstrap.min
    bootmin = "http://getbootstrap.com.br/dist/css/bootstrap.min.css"
    urllib.request.urlretrieve(bootmin, "site/bootstrap/css/bootstrap.min.css")

    #baixa o hack do IE
    viewport = "http://getbootstrap.com.br/assets/js/ie10-viewport-bug-workaround.js"
    urllib.request.urlretrieve(viewport, "site/bootstrap/css/viewport-bug-workaround.js")


    head = ("\n"
            " <head>\n"
            "    <meta charset=\"utf-8\">\n"
            "    <meta http-equiv=\"X-UA-Compatible\" content=\"IE=edge\">\n"
            "    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">\n"
            "    <meta name=\"description\" content=\"\">\n"
            "    <meta name=\"author\" content=\"\">\n"
            "    <link rel=\"icon\" href=\"#\">\n"
            "\n"
            "    <title>Portifolio</title>\n"
            "\n"
            "    <!-- Nucleo Bootstrap CSS -->\n"
            "    <link href=\"bootstrap/css/bootstrap.min.css\" rel=\"stylesheet\">\n"
            "\n"
            "    <!-- IE10 hack de exibicao para bug de superficie/desktop do Windows 8-->\n"
            "    <link href=\"bootstrap/css/ie10-viewport-bug-workaround.css\" rel=\"stylesheet\">\n"
            "\n"
            "    <!-- CSS customizado -->\n"
            "    <link href=\"css/index.css\" rel=\"stylesheet\">\n"
            "\n"
            "\n"
            "    <!-- Suporte de elementos do HTML5 para IE6-8 -->\n"
            "    <!--[if lt IE 9]>\n"
            "      <script src=\"http://html5shim.googlecode.com/svn/trunk/html5.js\"></script>\n"
            "    <![endif]-->\n"
            "  </head>\n"
            "    "
    )
    body = ("\n"
            "  <body>\n"
            "    <div class=\"site-wrapper\">\n"
            "      <div class=\"site-wrapper-inner\">\n"
            "        <div class=\"cover-container\">\n"
            "          <div class=\"masthead clearfix\">\n"
            "            <div class=\"inner\">\n"
            "              <h3 class=\"masthead-brand\">Portifolio</h3>\n"
            "              <nav>\n"
            "                <ul class=\"nav masthead-nav\">\n"
            "                  <li class=\"active\"><a href=\"#\">Inicio</a></li>\n"
            "                  <li><a href=\"#\">Trabalhos</a></li>\n"
            "                  <li><a href=\"#\">Contato</a></li>\n"
            "                </ul>\n"
            "              </nav>\n"
            "            </div>\n"
            "          </div>\n"
            "\n"
            "          <div class=\"inner cover\">\n"
            "            <h1 class=\"cover-heading\">Personalize sua pagina.</h1>\n"
            "            <p class=\"lead\">Cover e um modelo de pagina para a construcao de home pages simples e bonita. Baixe, edite o texto e adicione seu proprio fundo de tela cheio de fotos para torna-la unica.</p>\n"
            "            <p class=\"lead\">\n"
            "              <a href=\"#\" class=\"btn btn-lg btn-default\">Leia mais</a>\n"
            "            </p>\n"
            "          </div>\n"
            "        </div>\n"
            "      </div>\n"
            "    </div>\n")

    js_portifolio = ("    <script src=\"https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js\"></script>\n"
                     "    <script>window.jQuery || document.write('<script src=\"bootstrap/js/vendor/jquery.min.js\"><\\/script>')</script>\n"
                     "    <script src=\"site/bootstrap/bootstrap.min.js\"></script>\n"
                     "    <script src=\"site/bootstrap/ie10-viewport-bug-workaround.js\"></script>\n"
                     "    <script src=\"https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js\"></script>\n")

    html.write(htmlinitial +
               head + body +
               footer + js_portifolio
               + htmlfinal)
    html.close()

def criar_css_port():
    css.write("/* Globals */\n"
               "\n"
               "/* Links */\n"
               "a,\n"
               "a:focus,\n"
               "a:hover {\n"
               "  color: #fff;\n"
               "}\n"
               "\n"
               "/* Custom default button */\n"
               ".btn-default,\n"
               ".btn-default:hover,\n"
               ".btn-default:focus {\n"
               "  color: #333;\n"
               "  text-shadow: none; /* Prevent inheritance from `body` */\n"
               "  background-color: #fff;\n"
               "  border: 1px solid #fff;\n"
               "}\n"
               "\n"
               "/*\n"
               " * Base structure\n"
               " */\n"
               "\n"
               "html,\n"
               "body {\n"
               "  height: 100%;\n"
               "  background-color: #333;\n"
               "}\n"
               "body {\n"
               "  color: #fff;\n"
               "  text-align: center;\n"
               "  text-shadow: 0 1px 3px rgba(0,0,0,.5);\n"
               "}\n"
               "\n"
               "/* Extra markup and styles for table-esque vertical and horizontal centering */\n"
               ".site-wrapper {\n"
               "  display: table;\n"
               "  width: 100%;\n"
               "  height: 100%; /* For at least Firefox */\n"
               "  min-height: 100%;\n"
               "  -webkit-box-shadow: inset 0 0 100px rgba(0,0,0,.5);\n"
               "          box-shadow: inset 0 0 100px rgba(0,0,0,.5);\n"
               "}\n"
               ".site-wrapper-inner {\n"
               "  display: table-cell;\n"
               "  vertical-align: top;\n"
               "}\n"
               ".cover-container {\n"
               "  margin-right: auto;\n"
               "  margin-left: auto;\n"
               "}\n"
               "\n"
               "/* Padding for spacing */\n"
               ".inner {\n"
               "  padding: 30px;\n"
               "}\n"
               "\n"
               "\n"
               "/*\n"
               " * Header\n"
               " */\n"
               ".masthead-brand {\n"
               "  margin-top: 10px;\n"
               "  margin-bottom: 10px;\n"
               "}\n"
               "\n"
               ".masthead-nav > li {\n"
               "  display: inline-block;\n"
               "}\n"
               ".masthead-nav > li + li {\n"
               "  margin-left: 20px;\n"
               "}\n"
               ".masthead-nav > li > a {\n"
               "  padding-right: 0;\n"
               "  padding-left: 0;\n"
               "  font-size: 16px;\n"
               "  font-weight: bold;\n"
               "  color: #fff; /* IE8 proofing */\n"
               "  color: rgba(255,255,255,.75);\n"
               "  border-bottom: 2px solid transparent;\n"
               "}\n"
               ".masthead-nav > li > a:hover,\n"
               ".masthead-nav > li > a:focus {\n"
               "  background-color: transparent;\n"
               "  border-bottom-color: #a9a9a9;\n"
               "  border-bottom-color: rgba(255,255,255,.25);\n"
               "}\n"
               ".masthead-nav > .active > a,\n"
               ".masthead-nav > .active > a:hover,\n"
               ".masthead-nav > .active > a:focus {\n"
               "  color: #fff;\n"
               "  border-bottom-color: #fff;\n"
               "}\n"
               "\n"
               "@media (min-width: 768px) {\n"
               "  .masthead-brand {\n"
               "    float: left;\n"
               "  }\n"
               "  .masthead-nav {\n"
               "    float: right;\n"
               "  }\n"
               "}\n"
               "\n"
               "/*\n"
               " * Cover\n"
               " */\n"
               "\n"
               ".cover {\n"
               "  padding: 0 20px;\n"
               "}\n"
               ".cover .btn-lg {\n"
               "  padding: 10px 20px;\n"
               "  font-weight: bold;\n"
               "}\n"
               "\n"
               "/*\n"
               " * Footer\n"
               " */\n"
               "\n"
               ".mastfoot {\n"
               "  color: #999; /* IE8 proofing */\n"
               "  color: rgba(255,255,255,.5);\n"
               "}\n"
               "\n"
               "\n"
               "/*\n"
               " * Affix and center\n"
               " */\n"
               "\n"
               "@media (min-width: 768px) {\n"
               "  /* Pull out the header and footer */\n"
               "  .masthead {\n"
               "    position: fixed;\n"
               "    top: 0;\n"
               "  }\n"
               "  .mastfoot {\n"
               "    position: fixed;\n"
               "    bottom: 0;\n"
               "  }\n"
               "  /* Start the vertical centering */\n"
               "  .site-wrapper-inner {\n"
               "    vertical-align: middle;\n"
               "  }\n"
               "  /* Handle the widths */\n"
               "  .masthead,\n"
               "  .mastfoot,\n"
               "  .cover-container {\n"
               "    width: 100%; /* Must be percentage or pixels for horizontal alignment */\n"
               "  }\n"
               "}\n"
               "\n"
               "@media (min-width: 992px) {\n"
               "  .masthead,\n"
               "  .mastfoot,\n"
               "  .cover-container {\n"
               "    width: 700px;\n"
               "  }\n"
               "}\n")
    css.close()


if __name__ == "__main__":
    main()