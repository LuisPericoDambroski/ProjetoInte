from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from .models import CustomUser
from . import models
import bcrypt
import random
import string


def home(request):
    return render(request, "index.html")


def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        try:
            user = CustomUser.objects.get(username=username)
        except CustomUser.DoesNotExist:
            messages.error(request, "Usuário ou senha incorretos.")
            return redirect("/login/?modal=login")

        if bcrypt.checkpw(password.encode("utf-8"), user.password.encode("utf-8")):
            request.session["user_id"] = user.id
            messages.success(request, "Login realizado com sucesso!")
            return redirect("dashboard")
        else:
            messages.error(request, "Usuário ou senha incorretos.")
            return redirect("/login/?modal=login")

    return render(request, "login.html")


def register_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")

        if password != confirm_password:
            messages.error(request, "As senhas não coincidem.")
            return redirect("/login/?modal=register")

        if CustomUser.objects.filter(username=username).exists():
            messages.error(request, "Usuário já existe.")
            return redirect("/login/?modal=register")

        # 🔥 Melhorando a segurança da senha
        hashed_password = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")
        user = CustomUser(username=username, email=email, password=hashed_password)
        user.save()

        messages.success(request, "Cadastro realizado com sucesso!")
        return redirect("/login/?modal=register")

    return redirect("/login/")


def dashboard(request):
    if "user_id" not in request.session:
        messages.error(request, "Você precisa estar logado para acessar essa página.")
        return redirect("login")

    user = CustomUser.objects.get(id=request.session["user_id"])
    return render(request, "dashboard.html", {"user": user})


def logout_view(request):
    request.session.flush()
    messages.success(request, "Você saiu da conta.")
    return redirect("login")


def forgot_password(request):
    if request.method == "POST":
        email = request.POST.get("email")
        try:
            user = CustomUser.objects.get(email=email)
            reset_token = "".join(random.choices(string.ascii_letters + string.digits, k=32))
            user.reset_token = reset_token
            user.save()

            reset_link = f"http://127.0.0.1:8000/reset-password/{user.id}/{reset_token}/"
            send_mail(
                "Redefinição de Senha",
                f"Para redefinir sua senha, clique no link: {reset_link}",
                "noreply@seusite.com",
                [email],
                fail_silently=False,
            )
            messages.success(request, "E-mail de redefinição enviado!")
        except CustomUser.DoesNotExist:
            messages.error(request, "E-mail não encontrado.")

        return redirect("login")

    return render(request, "forgot_password.html")


def reset_password(request, uid, token):
    try:
        user = CustomUser.objects.get(id=uid, reset_token=token)
    except CustomUser.DoesNotExist:
        messages.error(request, "Token inválido ou expirado.")
        return redirect("login")

    if request.method == "POST":
        new_password = request.POST.get("new_password")
        confirm_password = request.POST.get("confirm_password")

        if new_password != confirm_password:
            messages.error(request, "As senhas não coincidem.")
            return redirect(f"/reset-password/{uid}/{token}/")

        user.password = bcrypt.hashpw(new_password.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")
        user.reset_token = None
        user.save()

        messages.success(request, "Senha redefinida com sucesso!")
        return redirect("login")

    return render(request, "reset_password.html", {"uid": uid, "token": token})

def teste(request):

    dados = [
    {
        "nome": "Acuidade com Arma",
        "desc": "Quando usa uma arma corpo a corpo leve ou uma arma de arremesso, você pode usar sua Destreza em vez de Força nos testes de ataque e rolagens de dano. Pré-requisito: Des 1.",
        "tipo": "combate"
    },
    {
        "nome": "Arma Secundária grande",
        "desc": "Você pode empunhar duas armas de uma mão com o poder Estilo de Duas Armas. Pré-requisito: Estilo de Duas Armas.",
        "tipo": "combate"
    },
    {
        "nome": "Arremesso Potente",
        "desc": "Quando usa uma arma de arremesso, você pode usar sua Força em vez de Destreza nos testes de ataque. Se você possuir o poder Ataque Poderoso, poderá usá-lo com armas de arremesso. Pré-requisitos: For 1, Estilo de Arremesso.",
        "tipo": "combate"
    },
    {
        "nome": "Arremesso Múltiplo",
        "desc": "Uma vez por rodada, quando faz um ataque com uma arma de arremesso, você pode gastar 1 PM para fazer um ataque adicional contra o mesmo alvo, arremessando outra arma de arremesso. Pré-requisitos: Des 1, Estilo de Arremesso.",
        "tipo": "combate"
    },
    {
        "nome": "Ataque com Escudo",
        "desc": "Uma vez por rodada, se estiver empunhando um escudo e fizer a ação agredir, você pode gastar 1 PM para fazer um ataque corpo a corpo extra com o escudo. Este ataque não faz você perder o bônus do escudo na Defesa. Pré-requisito: Estilo de Arma e Escudo.",
        "tipo": "combate"
    },
    {
        "nome": "Ataque Pesado",
        "desc": "Quando faz um ataque corpo a corpo com uma arma de duas mãos, você pode pagar 1 PM. Se fizer isso e acertar o ataque, além do dano você faz uma manobra derrubar ou empurrar contra o alvo como uma ação livre (use o resultado do ataque como o teste de manobra). Pré-requisito: Estilo de Duas Mãos.",
        "tipo": "combate"
    },
    {
        "nome": "Ataque Poderoso",
        "desc": "Sempre que faz um ataque corpo a corpo, você pode sofrer -2 no teste de ataque para receber +5 na rolagem de dano. Pré-requisito: For 1.",
        "tipo": "combate"
    },
    {
        "nome": "Ataque Preciso",
        "desc": "Se estiver empunhando uma arma corpo a corpo em uma das mãos e nada na outra, você recebe +2 na margem de ameaça e +1 no multiplicador de crítico. Pré-requisito: Estilo de Uma Arma.",
        "tipo": "combate"
    },
    {
        "nome": "Bloqueio com Escudo",
        "desc": "Quando sofre dano, você pode gastar 1 PM para receber redução de dano igual ao bônus na Defesa que seu escudo fornece contra este dano. Você só pode usar este poder se estiver usando um escudo. Pré-requisito: Estilo de Arma e Escudo.",
        "tipo": "combate"
    },
    {
        "nome": "Carga de Cavalaria",
        "desc": "Quando faz uma investida montada, você causa +2d8 pontos de dano. Além disso, pode continuar se movendo depois do ataque. Você deve se mover em linha reta e seu movimento máximo ainda é o dobro do seu deslocamento. Pré-requisito: Ginete.",
        "tipo": "combate"
    },
    {
        "nome": "Combate Defensivo",
        "desc": "Quando usa a ação agredir, você pode usar este poder. Se fizer isso, até seu próximo turno, sofre -2 em todos os testes de ataque, mas recebe +5 na Defesa. Pré-requisito: Int 1.",
        "tipo": "combate"
    },
    {
        "nome": "Derrubar Aprimorado",
        "desc": "Você recebe +2 em testes de ataque para derrubar. Quando derruba uma criatura com essa manobra,pode gastar 1 PM para fazer um ataque extracontra ela. Pré-requisito: Combate Defensivo.",
        "tipo": "combate"
    },
    {
        "nome": "Desarmar Aprimorado",
        "desc": "Você recebe +2 em testes de ataque para desarmar. Quando desarma uma criatura com essa manobra, a arma dela para longe. Para definir onde a arma cai, role 1d8 para a direção (sendo “1” diretamente à sua frente, “2” à frente e à direita e assim por diante) e 1d6 para a distância (medida em quadrados de 1,5m a partir da criatura desarmada). Pré-requisito: Combate Defensivo.",
        "tipo": "combate"
    },
    {
        "nome": "Disparo Preciso",
        "desc": "Você pode fazer ataques à distância contra oponentes envolvidos em combate corpo a corpo sem sofrer a penalidade de -5 no teste de ataque. Pré-requisito: Estilo de Disparo ou Estilo de Arremesso.",
        "tipo": "combate"
    },
    {
        "nome": "Disparo Rápido",
        "desc": "Se estiver empunhando uma arma de disparo que possa recarregar como ação livre e gastar umaação completa para agredir, pode fazer um ataque adicional com ela. Se fizer isso, sofre -2 em todos os testes de ataque até o seu próximo turno. Pré-requisitos: Des 1, Estilo de Disparo.",
        "tipo": "combate"
    },
    {
        "nome": "Empunhadura Poderosa",
        "desc": "Ao usar uma arma feita para uma categoria de tamanho maior que a sua, a penalidade que você sofre nos testes de ataque diminui para -2 (normalmente, usar uma arma de uma categoria de tamanho maior impõe -5 nos testes de ataque). Pré-requisito: For 3.",
        "tipo": "combate"
    },
    {
        "nome": "Encouraçado",
        "desc": "Se estiver usando uma armadura pesada, você recebe +2 na Defesa. Esse bônus aumenta em +2 para cada outro poder que você possua que tenha Encouraçado como pré-requisito. Pré-requisito: proficiência com armaduras pesadas.",
        "tipo": "combate"
    },
    {
        "nome": "Esquiva",
        "desc": "Você recebe +2 na Defesa e Reflexos. Pré-requisito: Des 1.",
        "tipo": "combate"
    },
    {
        "nome": "Estilo de Uma Arma e Escudo",
        "desc": "Se estiver usando um escudo, o bônus na Defesa que ele fornece aumenta em +2. Pré-requisitos: treinado em Luta, proficiência com escudos.",
        "tipo": "combate"
    },
    {
        "nome": "Estilo de Arma Longa",
        "desc": "Você recebe +2 em testes de ataque com armas alongadas e pode atacar alvos adjacentes com essas armas. Pré-requisitos: For 1, treinado em Luta.",
        "tipo": "combate"
    },
    {
        "nome": "Estilo de Arremesso",
        "desc": "Você pode sacar armas de arremesso como uma ação livre e recebe +2 nas rolagens de dano com elas. Se também possuir o poder Saque Rápido, também recebe +2 nos testes de ataque com essas armas. Pré-requisito: treinado em Pontaria.",
        "tipo": "combate"
    },
    {
        "nome": "Estilo de Disparo",
        "desc": "Se estiver usando uma arma de disparo, você soma sua Destreza nas rolagens de dano. Pré-requisito: treinado em Pontaria.",
        "tipo": "combate"
    },
    {
        "nome": "Estilo de Duas Armas",
        "desc": "Se estiver empunhando duas armas (e pelo menos uma delas for leve) e fizer a ação agredir, você pode fazer dois ataques, um com cada arma. Se fizer isso, sofre -2 em todos os testes de ataque até o seu próximo turno. Se possuir Ambidestria, em vez disso não sofre penalidade para usá-lo. Pré-requisitos: Des 2, treinado em Luta.",
        "tipo": "combate"
    },
    {
        "nome": "Estilo de Duas Mãos",
        "desc": "Se estiver usando uma arma corpo a corpo com as duas mãos, você recebe +5 nas rolagens de dano. Este poder não pode ser usado com armas leves. Pré-requisitos: For 2, Treinado em Luta.",
        "tipo": "combate"
    },
    {
        "nome": "Estilo de Uma Arma",
        "desc": "Se estiver usando uma arma corpo a corpo em uma das mãos e nada na outra, você recebe +2 na Defesa e nos testes de ataque com essa arma (exceto ataques desarmados). Pré-requisito: treinado em Luta.",
        "tipo": "combate"
    },
    {
        "nome": "Estilo Desarmado",
        "desc": "Seus ataques desarmados causam 1d6 pontos de dano e podem causar dano letal ou não letal (sem penalidades). Pré-requisito: treinado em Luta.",
        "tipo": "combate"
    },
    {
        "nome": "Fanático",
        "desc": "Seu deslocamento não é reduzido por usar armaduras pesadas. Pré-requisitos: 12º nível de personagem, Encouraçado.",
        "tipo": "combate"
    },
    {
        "nome": "Finta Aprimorada",
        "desc": "Você recebe +2 em testes de Enganação para fintar e pode fintar como uma ação de movimento. Pré-requisitos: treinado em Enganação.",
        "tipo": "combate"
    },
    {
        "nome": "Foco em Arma",
        "desc": "Escolha uma arma. Você recebe +2 em testes de ataque com essa arma. Você pode escolher este poder outras vezes para armas diferentes. Pré-requisito: proficiência com a arma.",
        "tipo": "combate"
    },
    {
        "nome": "Ginete",
        "desc": "Você passa automaticamente em testes de Cavalgar para não cair da montaria quando sofre dano. Além disso, não sofre penalidades para atacar à distância ou lançar magias quando montado. Pré-requisito: treinado em Cavalgar.",
        "tipo": "combate"
    },
    {
        "nome": "Inexpugnável",
        "desc": "Se estiver usando uma armadura pesada, você recebe +2 em todos os testes de resistência. Pré-requisitos: Encouraçado, 6º nível de personagem.",
        "tipo": "combate"
    },
    {
        "nome": "Mira Apurada",
        "desc": "Quando usa a ação mirar, você recebe +2 em testes de ataque e na margem de ameaça com ataques à distância até o fim do turno. Pré-requisitos: Sab 1, Disparo Preciso.",
        "tipo": "combate"
    },
    {
        "nome": "Piqueiro",
        "desc": "Uma vez por rodada, se estiver empunhando uma arma alongada e um inimigo entrar voluntariamente em seu alcance corpo a corpo, você pode gastar 1 PM para fazer um ataque corpo a corpo contra este oponente com esta arma. Se o oponente tiver se aproximado fazendo uma investida, seu ataque causa dois dados de dano extra do mesmo tipo. Pré-requisito: Estilo de Arma Longa.",
        "tipo": "combate"
    },
    {
        "nome": "Presença Aterradora",
        "desc": "Você pode gastar uma ação padrão e 1 PM para assustar todas as criaturas a sua escolha em alcance curto. Veja a perícia Intimidação para as regras de assustar. Pré-requisito: treinado em Intimidação.",
        "tipo": "combate"
    },
    {
        "nome": "Proficiência",
        "desc": "Escolha uma proficiência: armas marciais, armas de fogo, armaduras pesadas ou escudos (se for proficiente em armas marciais, você também pode escolher armas exóticas). Você recebe essa proficiência. Você pode escolher este poder outras vezes para proficiências diferentes.",
        "tipo": "combate"
    },
    {
        "nome": "Quebrar Aprimorado",
        "desc": "Você recebe +2 em testes de ataque para quebrar. Quando reduz os PV de uma arma para 0 ou menos, você pode gastar 1 PM para realizar um ataque extra contra o usuário dela. O ataque adicional usa os mesmos valores de ataque e dano, mas os dados devem ser rolados novamente. Pré-requisito: Ataque Poderoso.",
        "tipo": "combate"
    },
    {
        "nome": "Reflexos de Combate",
        "desc": "Você ganha uma ação de movimento extra no seu primeiro turno de cada combate. Pré-requisito: Des 1.",
        "tipo": "combate"
    },
    {
        "nome": "Saque Rápido",
        "desc": "Você recebe +2 em Iniciativa e pode sacar ou guardar itens como uma ação livre (em vez de ação de movimento). Além disso, a ação que você gasta para recarregar armas de disparo diminui em uma categoria (ação completa para padrão, padrão para movimento, movimento para livre). Pré-requisito: treinado em Iniciativa.",
        "tipo": "combate"
    },
    {
        "nome": "Trespassar",
        "desc": "Quando você faz um ataque corpo a corpo e reduz os pontos de vida do alvo para 0 ou menos, pode gastar 1 PM para fazer um ataque adicional contra outra criatura dentro do seu alcance. Pré-requisito: Ataque Poderoso.",
        "tipo": "combate"
    },
    {
        "nome": "Vitalidade",
        "desc": "Você recebe +1 PV por nível de personagem e +2 em Fortitude. Pré-requisito: Con 1.",
        "tipo": "combate"
    },
    {
        "nome": "Acrobático",
        "desc": "Você pode usar sua Destreza em vez de Força em testes de Atletismo. Além disso, terreno difícil não reduz seu deslocamento nem o impede de realizar investidas. Pré-requisito: Des 2.",
        "tipo": "destino"
    },
    {
        "nome": "Ao Sabor do Destino",
        "desc": "Confiando em suas próprias habilidades (ou em sua própria sorte), você abre mão de usar itens mágicos. Sua autoconfiança fornece diversos benefícios, de acordo com seu nível de personagem e a tabela da página seguinte.\nNível 6: +2 em uma perícia.\nNível 7: +1 na Defesa.\nNível 8: +1 nas rolagens de dano.\nNível 9: +1 em um atributo\nNível 11: +2 em uma perícia\nNível 12: +2 na Defesa\nNível 13: +2 nas rolagens de dano\nNível 14: +1 em um atributo\nNível 16: +2 em uma perícia\nNível 17: +3 na Defesa\nNível 18: +3 nas rolagens de dano\nNível 19: +1 em um atributo\nOs bônus não são cumulativos (os bônus em atributos e perícias devem ser aplicados num atributo ou perícia diferente a cada vez). Se você utilizar voluntariamente qualquer item mágico (exceto poções), perde o benefício deste poder até o fim da aventura. Você ainda pode lançar magias, receber magias benéficas ou beneficiar-se de itens usados por outros — por exemplo, pode “ir de carona” em um tapete voador, mas não pode você mesmo conduzi-lo. Pré-requisito: 6º nível de personagem.",
        "tipo": "destino"
    },
    {
        "nome": "Aparência Inofensiva",
        "desc": "A primeira criatura inteligente (Int -3 ou maior) que atacar você em uma cena deve fazer um teste de Vontade (CD Car). Se falhar, perderá sua ação. Este poder só funciona uma vez por cena; independentemente de a criatura falhar ou não no teste, poderá atacá-lo nas rodadas seguintes. Pré-requisito: Car 1.",
        "tipo": "destino"
    },
    {
        "nome": "Atlético",
        "desc": "Você recebe +2 em Atletismo e +3m em seu deslocamento. Pré-requisito: For 2.",
        "tipo": "destino"
    },
    {
        "nome": "Atraente",
        "desc": "Você recebe +2 em testes de perícias baseadas em Carisma contra criaturas que possam se sentir fisicamente atraídas por você. Pré-requisito: Car 1.",
        "tipo": "destino"
    },
    {
        "nome": "Comandar",
        "desc": "Você pode gastar uma ação de movimento e 1 PM para gritar ordens para seus aliados em alcance médio. Eles recebem +1 em testes de perícia até o fim da cena. Pré-requisito: Car 1.",
        "tipo": "destino"
    },
    {
        "nome": "Costas Largas",
        "desc": "Seu limite de carga aumenta em 5 espaços e você pode se beneficiar de um item vestido adicional. Pré-requisito: Con 1, For 1.",
        "tipo": "destino"
    },
    {
        "nome": "Foco em Perícia",
        "desc": "Escolha uma perícia. Quando faz um teste dessa perícia, você pode gastar 1 PM para rolar dois dados e usar o melhor resultado. Você pode escolher este poder outras vezes para perícias diferentes. Este poder não pode ser aplicado em Luta e Pontaria (mas veja Foco em Arma). Pré-requisito: treinado na perícia escolhida.",
        "tipo": "destino"
    },
    {
        "nome": "Inventário Organizado",
        "desc": "Você soma sua Inteligência no limite de espaços que pode carregar. Para você, itens muito leves ou pequenos, que normalmente ocupam meio espaço, em vez disso ocupam 1/4 de espaço. Pré-requisito: Int 1.",
        "tipo": "destino"
    },
    {
        "nome": "Investigador",
        "desc": "Você recebe +2 em Investigação e soma sua Inteligência em Intuição. Pré-requisito: Int 1.",
        "tipo": "destino"
    },
    {
        "nome": "Lobo Solitário",
        "desc": "Você recebe +1 em testes de perícia e Defesa se estiver sem nenhum aliado em alcance curto. Você não sofre penalidade por usar Cura em si mesmo.",
        "tipo": "destino"
    },
    {
        "nome": "Medicina",
        "desc": "Você pode gastar uma ação completa para fazer um teste de Cura (CD 15) em uma criatura. Se você passar, ela recupera 1d6 PV, mais 1d6 para cada 5 pontos pelos quais o resultado do teste exceder a CD (2d6 com um resultado 20, 3d6 com um resultado 25 e assim por diante). Você só pode usar este poder uma vez por dia numa mesma criatura. Pré-requisitos: Sab 1, treinado em Cura.",
        "tipo": "destino"
    },
    {
        "nome": "Parceiro",
        "desc": "Você possui um parceiro animal ou humanoide que o acompanha em aventuras. Escolha os detalhes dele, como nome, aparência e personalidade. Em termos de jogo, é um parceiro iniciante de um tipo a sua escolha (veja a página 260). O parceiro obedece às suas ordens e se arrisca para ajudá-lo, mas, se for maltratado, pode parar de segui-lo (de acordo com o mestre). Se perder seu parceiro, você recebe outro no início da próxima aventura. Pré-requisitos: treinado em Adestramento (parceiro animal) ou Diplomacia (parceiro humanoide), 5º nível de personagem.",
        "tipo": "destino"
    },
    {
        "nome": "Sortudo",
        "desc": "Você pode gastar 3 PM para rolar novamente um teste recém realizado (apenas uma vez por teste).",
        "tipo": "destino"
    },
    {
        "nome": "Surto Heroico",
        "desc": "Uma vez por rodada, você pode gastar 5 PM para realizar uma ação padrão ou de movimento adicional.",
        "tipo": "destino"
    },
    {
        "nome": "Torcida",
        "desc": "Você recebe +2 em testes de perícia e Defesa quando tem a torcida a seu favor. Entenda-se por “torcida” qualquer número de criaturas inteligentes em alcance médio que não esteja realizando nenhuma ação além de torcer por você. Pré-requisito: Car 1.",
        "tipo": "destino"
    },
    {
        "nome": "Treinamento em Perícia",
        "desc": "Você se torna treinado em uma perícia a sua escolha. Você pode escolher este poder outras vezes para perícias diferentes.",
        "tipo": "destino"
    },
    {
        "nome": "Venefício",
        "desc": "Quando usa um veneno, você não corre risco de se envenenar acidentalmente. Além disso, a CD para resistir aos seus venenos aumenta em +2. Pré-requisito: treinado em Ofício (alquimista).",
        "tipo": "destino"
    },
    {
        "nome": "Vontade de Ferro",
        "desc": "Você recebe +1 PM para cada dois níveis de personagem e +2 em Vontade. Pré-requisito: Sab 1.",
        "tipo": "destino"
    },
    {
        "nome": "Celebrar Ritual",
        "desc": "Você pode lançar magias como rituais. Isso dobra seu limite de PM, mas muda a execução para 1 hora (ou o dobro, o que for maior) e exige um gasto de T$ 10 por PM gasto (em incensos, oferendas...). Assim, um arcanista de 8º nível pode lançar uma magia de 16 PM gastando T$ 160. Pré-requisitos: treinado em Misticismo ou Religião, 8º nível de personagem. Magias lançadas como rituais não podem ser armazenadas em itens.",
        "tipo": "magia/aprimoramento"
    },
    {
        "nome": "Escrever Pergaminho",
        "desc": "Você pode usar a perícia Ofício (escriba) para fabricar pergaminhos com magias que conheça. Veja a página 121 para a regra de fabricar itens e as páginas 333 e 341 para as regras de pergaminhos. De acordo com o mestre, você pode usar objetos similares, como runas, tabuletas de argila etc. Pré-requisitos: habilidade de classe Magias, treinado em Ofício (escriba).",
        "tipo": "magia/aprimoramento"
    },
    {
        "nome": "Foco em Magia",
        "desc": "Escolha uma magia que possa lançar. Seu custo diminui em -1 PM (cumulativo com outras reduções de custo). Você pode escolher este poder outras vezes para magias diferentes.",
        "tipo": "magia/aprimoramento"
    },
    {
        "nome": "Magia Acelerada",
        "desc": "Muda a execução da magia para ação livre. Você só pode aplicar este aprimoramento em magias com execução de movimento, padrão ou completa e só pode lançar uma magia como ação livre por rodada. Custo: +4 PM. Pré-requisito: lançar magias de 2º círculo.",
        "tipo": "magia/aprimoramento"
    },
    {
        "nome": "Magia Ampliada",
        "desc": "Aumenta o alcance da magia em um passo (de curto para médio, de médio para longo) ou dobra a área de efeito da magia. Por exemplo, uma Bola de Fogo ampliada tem seu alcance aumentado para longo ou sua área aumentada para 12m de raio. Custo: +2 PM.",
        "tipo": "magia/aprimoramento"
    },
    {
        "nome": "Magia Discreta",
        "desc": "Você lança a magia sem gesticular e falar, usando apenas concentração. Isso permite lançar magias com as mãos presas, amordaçado etc. Também permite lançar magias arcanas usando armadura sem teste de Misticismo. Outros personagens só percebem que você lançou uma magia se passarem num teste de Misticismo (CD 20). Custo: +2 PM.",
        "tipo": "magia/aprimoramento"
    },
    {
        "nome": "Magia Ilimitada",
        "desc": "Você soma seu atributo-chave no limite de PM que pode gastar numa magia. Por exemplo, um arcanista de 5º nível com Int 4 e este poder pode gastar até 9 PM em cada magia.",
        "tipo": "magia"
    },
    {
        "nome": "Preparar Poção",
        "desc": "Você pode usar a perícia Ofício (alquimista) para fabricar poções com magias que conheça de 1º e 2º círculos. Veja a página 121 para a regra de fabricar itens e as páginas 333 e 341 para as regras de poções. Pré-requisitos: habilidade de classe Magias, treinado em Ofício (alquimista).",
        "tipo": "magia"
    },
    {
        "nome": "Afinidade com a Tormenta",
        "desc": "Você recebe +10 em testes de resistência contra efeitos da Tormenta, de suas criaturas e de devotos de Aharadak. Além disso, seu primeiro poder da Tormenta não conta para perda de Carisma.",
        "tipo": "concedido/Aharadak"
    },
    {
        "nome": "Almejar o Impossível",
        "desc": "Quando faz um teste de perícia, um resultado de 19 ou mais no dado sempre é um sucesso, não importando o valor a ser alcançado.",
        "tipo": "concedido/Thwor, Valkaria"
    },
    {
        "nome": "Anfíbio",
        "desc": "Você pode respirar embaixo d`água e adquire deslocamento de natação igual a seu deslocamento terrestre.",
        "tipo": "concedido/Oceano"
    },
    {
        "nome": "Apostar com o Trapaceiro",
        "desc": "Quando faz um teste de perícia, você pode gastar 1 PM para apostar com Hyninn. Você e o mestre rolam 1d20, mas o mestre mantém o resultado dele em segredo. Você então escolhe entre usar seu próprio resultado ou o resultado oculto do mestre (neste caso, ele revela o resultado). (Magia)",
        "tipo": "concedido/Hyninn"
    },
    {
        "nome": "Armas da ambição",
        "desc": "Você recebe +1 em testes de ataque e na margem de ameaça com armas nas quais é proficiente.",
        "tipo": "concedido/Valkaria"
    },
    {
        "nome": "Arsenal das profundezas",
        "desc": "Você recebe +2 nas rolagens de dano com azagaias, lanças e tridentes e seu multiplicador de crítico com essas armas aumenta em +1.",
        "tipo": "concedido/Oceano"
    },
    {
        "nome": "Astúcia da Serpente",
        "desc": "Você recebe +2 em Enganação, Furtividade e Intuição.",
        "tipo": "concedido/Sszzaas"
    },
    {
        "nome": "Ataque Piedoso",
        "desc": "Você pode usar armas corpo a corpo para causar dano não letal sem sofrer a penalidade de -5 no teste de ataque.",
        "tipo": "concedito/Lena,Thyatis"
    },
    {
        "nome": "Aura de Medo",
        "desc": "Você pode gastar 2 PM para gerar uma aura de medo de 9m de raio e duração até o fim da cena. Todos os inimigos que entrem na aura devem fazer um teste de Vontade (CD Car) ou ficam abalados até o fim da cena. Uma criatura que passe no teste de Vontade fica imune a esta habilidade por um dia. (magia)",
        "tipo": "concedido/Kally"
    },
    {
        "nome": "Aura de Paz",
        "desc": "Você pode gastar 2 PM para gerar uma aura de paz com alcance curto e duração de uma cena. Qualquer inimigo dentro da aura que tente fazer uma ação hostil contra você deve fazer um teste de Vontade (CD Car). Se falhar, perderá sua ação. Se passar, fica imune a esta habilidade por um dia. (magia)",
        "tipo": "concedido/Marah"
    },
    {
        "nome": "Aura Restauradora",
        "desc": "Efeitos de cura usados por você e seus aliados em alcance curto recuperam +1 PV por dado.",
        "tipo": "concedido/Lena"
    },
    {
        "nome": "Bênção do Mana",
        "desc": "Você recebe +1 PM a cada nível ímpar.",
        "tipo": "concedido/Wynna"
    },
    {
        "nome": "Carícia Sombria",
        "desc": "Você pode gastar 1 PM e uma ação padrão para cobrir sua mão com energia negativa e tocar uma criatura em alcance corpo a corpo. A criatura sofre 2d6 pontos de dano de trevas (Fortitude CD Sab reduz à metade) e você recupera PV iguais à metade do dano causado. Você pode aprender Toque Vampírico como uma magia divina. Se fizer isso, o custo dela diminui em -1 PM. (magia)",
        "tipo": "concedido/Tenebra"
    },
    {
        "nome": "Centelha Mágica",
        "desc": "Escolha uma magia arcana ou divina de 1º círculo. Você aprende e pode lançar essa magia.",
        "tipo": "concedido/Wynna"
    },
    {
        "nome": "Compreender os Ermos",
        "desc": "Você recebe +2 em Sobrevivência e pode usar Sabedoria para Adestramento (em vez de Carisma).",
        "tipo": "concedido/Allihanna"
    },
    {
        "nome": "Conhecimento Enciclopédico",
        "desc": "Você se torna treinado em duas perícias baseadas em Inteligência a sua escolha.",
        "tipo": "concedido/Tanna-Toh"
    },
    {
        "nome": "Conjurar Arma",
        "desc": "Você pode gastar 1 PM para invocar uma arma corpo a corpo ou de arremesso com a qual seja proficiente. A arma surge em sua mão, fornece +1 em testes de ataque e rolagens de dano, é considerada mágica e uma arma mágica e dura pela cena. Você não pode criar armas         de disparo, mas pode criar 20 munições. (magia)",
        "tipo": "concedido/Arsenal"
    },
    {
        "nome": "Coragem Total",
        "desc": "Você é imune a efeitos de medo, mágicos ou não. Este poder não elimina fobias raciais (como o medo de altura dos minotauros).",
        "tipo": "concedido/Arsenal, Khalmyr, Lin-Wu, Valkaria"
    },
    {
        "nome": "Cura Gentil",
        "desc": "Você soma seu Carisma aos PV restaurados por seus efeitos mágicos de cura.",
        "tipo": "concedido/Lena"
    },
    {
        "nome": "Curandeira Perfeita",
        "desc": "Você sempre pode escolher 10 em testes de Cura. Além disso, não sofre penalidade por usar essa perícia sem uma maleta de medicamentos. Se possuir o item, recebe +2 no teste de Cura (ou +5, se ele for aprimorado).",
        "tipo": "concedido/Lena"
    },
    {
        "nome": "Dedo Verde",
        "desc": "Você aprende e pode lançar Controlar Plantas. Caso aprenda novamente essa magia, seu custo diminui em -1 PM. (magia)",
        "tipo": "concedido/Allihanna"
    },
    {
        "nome": "Descanso Natural",
        "desc": "Para você, dormir ao relento conta como condição de descanso confortável.",
        "tipo": "concedido/Allihanna"
    },
    {
        "nome": "Dom da Esperança",
        "desc": "Você soma sua Sabedoria em seus PV em vez de Constituição, e se torna imune às condições alquebrado, esmorecido e frustrado.",
        "tipo": "concedido/Marah"
    },
    {
        "nome": "Dom da Imortalidade",
        "desc": "Você é imortal. Sempre que morre, não importando o motivo, volta à vida após 3d6 dias. Apenas paladinos podem escolher este poder. Um personagem pode ter Dom da Imortalidade ou Dom da Ressurreição, mas não ambos. (magia)",
        "tipo": "concedido/Thyatis"
    },
    {
        "nome": "Dom da Profecia",
        "desc": "Você pode lançar Augúrio. Caso aprenda novamente essa magia, seu custo diminui em -1 PM. Você também pode gastar 2 PM para receber +2 em um teste. (magia)",
        "tipo": "concedido/Thyatis"
    },
    {
        "nome": "Dom da Ressurreição",
        "desc": "Você pode gastar uma ação completa e todos os PM que possui (mínimo 1 PM) para tocar o corpo de uma criatura morta há menos de um ano e ressuscitá-la. A criatura volta à vida com 1 PV e 0 PM, e perde 1 ponto de Constituição permanentemente. Este poder só pode ser usado uma vez em cada criatura. Apenas clérigos podem escolher este poder. Um personagem pode ter Dom da Imortalidade ou Dom da Ressurreição, mas não ambos. (magia)",
        "tipo": "concedido/Thyatis"
    },
    {
        "nome": "Dom da Verdade",
        "desc": "Você pode pagar 2 PM para receber +5 em testes de Intuição, e em testes de Percepção contra Enganação e Furtividade, até o fim da cena.",
        "tipo": "concedido/Khalmyr"
    },
    {
        "nome": "Escamas Dracônicas",
        "desc": "Você recebe +2 na Defesa e em Fortitude.",
        "tipo": "concedido/Kally"
    },
    {
        "nome": "Escudo Mágico",
        "desc": "Quando lança uma magia, você recebe um bônus na Defesa igual ao círculo da magia lançada até o início do seu próximo turno. (magia)",
        "tipo": "concedido/Wynna"
    },
    {
        "nome": "Espada Justiceira",
        "desc": "Você pode gastar 1 PM para encantar sua espada (ou outra arma corpo a corpo de corte que esteja empunhando). Ela tem seu dano aumentado em um passo até o fim da cena. (magia)",
        "tipo": "concedido/Khalmyr"
    },
    {
        "nome": "Espada Solar",
        "desc": "Você pode gastar 1 PM para fazer uma arma corpo a corpo de corte que esteja empunhando causar +1d6 de dano por fogo até o fim da cena. (magia)",
        "tipo": "concedido/Azgher"
    },
    {
        "nome": "Êxtase da Loucura",
        "desc": "Toda vez que uma ou mais criaturas falham em um teste de Vontade contra uma de suas habilidades mágicas, você recebe 1 PM temporário cumulativo. Você pode ganhar um máximo de PM temporários por cena desta forma igual a sua Sabedoria.",
        "tipo": "concedido/Aharadak, Nimb"
    },
    {
        "nome": "Familiar Ofídico",
        "desc": "Você recebe um familiar cobra (veja a página 38) que não conta em seu limite de parceiros.",
        "tipo": "concedido/Sszzaas"
    },
    {
        "nome": "Farsa do Fingidor",
        "desc": "Você aprende e pode lançar Criar Ilusão. Caso aprenda novamente essa magia, seu custo diminui em -1 PM.",
        "tipo": "concedido/Hyninn"
    },
    {
        "nome": "Fé Guerreira",
        "desc": "Você pode usar Sabedoria para Guerra (em vez de Inteligência). Além disso, em combate, pode gastar 2 PM para substituir um teste de perícia (exceto testes de ataque) por um teste de Guerra.",
        "tipo": "concedido/Arsenal"
    },
    {
        "nome": "Forma de Macaco",
        "desc": "Você pode gastar uma ação completa e 2 PM para se transformar em um macaco. Você adquire tamanho Minúsculo (o que fornece +5 em Furtividade e -5 em testes de manobra) e recebe deslocamento de escalar 9m. Seu equipamento desaparece (e você perde seus benefícios) até você voltar ao normal, mas suas outras estatísticas não são alteradas. A transformação dura indefinidamente, mas termina caso você faça um ataque, lance uma magia ou sofra dano. (magia)",
        "tipo": "concedido/Hyninn"
    },
    {
        "nome": "Fulgor Solar",
        "desc": "Você recebe redução de frio e trevas 5. Além disso, quando é alvo de um ataque você pode gastar 1 PM para emitir um clarão solar que deixa o atacante ofuscado por uma rodada.",
        "tipo": "concedido/Azgher"
    },
    {
        "nome": "Fúria Divina",
        "desc": "Você pode gastar 2 PM para invocar uma fúria selvagem, tornando-se temível em combate. Até o fim da cena, você recebe +2 em testes de ataque e rolagens de dano corpo a corpo, mas não pode executar nenhuma ação que exija paciência ou concentração (como usar a perícia Furtividade ou lançar magias). Se usar este poder em conjunto com a habilidade Fúria, ela também dura uma cena (e não termina se você não atacar ou for alvo de uma ação hostil).",
        "tipo": "concedido/Thwor"
    },
    {
        "nome": "Golpista Divino",
        "desc": "Você recebe +2 em Enganação, Jogatina e Ladinagem.",
        "tipo": "concedido/Hyninn"
    },
    {
        "nome": "Habitante do Deserto",
        "desc": "Você recebe redução de fogo 10 e pode pagar 1 PM para criar água pura e potável suficiente para um odre (ou outro recipiente pequeno). (magia)",
        "tipo": "concedido/Azgher"
    },
    {
        "nome": "Inimigo de Tenebra",
        "desc": "Seus ataques e habilidades causam +1d6 pontos de dano contra mortos-vivos. Quando você usa um efeito que gera luz, o alcance da iluminação dobra.",
        "tipo": "concedido/Azgher"
    },
    {
        "nome": "Kiai Divino",
        "desc": "Uma vez por rodada, quando faz um ataque corpo a corpo, você pode pagar 3 PM. Se acertar o ataque, causa dano máximo, sem necessidade de rolar dados.",
        "tipo": "concedido/Lin-wu"
    },
    {
        "nome": "Liberdade Divina",
        "desc": "Você pode gastar 2 PM para receber imunidade a efeitos de movimento por uma rodada. (magia)",
        "tipo": "concedido/Valkaria"
    },
    {
        "nome": "Manto da Penumbra",
        "desc": "Você aprende e pode lançar Escuridão. Caso aprenda novamente essa magia, seu custo diminui em -1 PM. (magia)",
        "tipo": "concedido/Tenebra"
    },
    {
        "nome": "Mente Analítica",
        "desc": "Você recebe +2 em Intuição, Investigação e Vontade.",
        "tipo": "concedido/Tanna-Toh"
    },
    {
        "nome": "Mente Vazia",
        "desc": "Você recebe +2 em Iniciativa, Percepção e Vontade.",
        "tipo": "concedido/Lin-Wu"
    },
    {
        "nome": "Mestre dos Mares",
        "desc": "Você pode falar com animais aquáticos (como o efeito da magia Voz Divina) e aprende e pode lançar Acalmar Animal, mas só contra criaturas aquáticas. Caso aprenda novamente essa magia, seu custo diminui em -1 PM. (magia)",
        "tipo": "concedido/Oceano"
    },
    {
        "nome": "Olhar Amedrontador",
        "desc": "Você aprende e pode lançar Amedrontar. Caso aprenda novamente essa magia, seu custo diminui em -1 PM. (magia)",
        "tipo": "concedido/Megalokk, Thwor"
    },
    {
        "nome": "Palavras de Bondade",
        "desc": "Você aprende e pode lançar Enfeitiçar. Caso aprenda novamente essa magia, seu custo diminui em -1 PM. (magia)",
        "tipo": "concedido/Marah"
    },
    {
        "nome": "Percepção Temporal",
        "desc": "Você pode gastar 3 PM para somar sua Sabedoria (limitado por seu nível e não cumulativo com efeitos que somam este atributo) a seus ataques, Defesa e testes de Reflexos até o fim da cena.",
        "tipo": "concedido/Aharadak"
    },
    {
        "nome": "Pesquisa Abençoada",
        "desc": "Se passar uma hora pesquisando seus livros e anotações, você pode rolar novamente um teste de perícia baseada em Inteligência ou Sabedoria que tenha feito desde a última cena. Se tiver acesso a mais livros, você recebe um bônus no teste: +2 para uma coleção particular ou biblioteca pequena e +5 para a biblioteca de um templo ou universidade.",
        "tipo": "concedido/Tanna-Toh"
    },
    {
        "nome": "Poder Oculto",
        "desc": "Você pode gastar uma ação de movimento e 2 PM para invocar a força, a velocidade ou o vigor dos loucos. Role 1d6 para receber +2 em Força (1 ou 2), Destreza (3 ou 4) ou Constituição (5 ou 6) até o fim da cena. Você pode usar este poder várias vezes, mas bônus no mesmo atributo não são cumulativos. (magia)",
        "tipo": "concedido/Nimb"
    },
    {
        "nome": "Presas Primordiais",
        "desc": "Você pode gastar 1 PM para transformar seus dentes em presas afiadas até o fim da cena. Você recebe uma arma natural de mordida (dano 1d6, crítico x2, perfuração). Uma vez por rodada, quando usa a ação agredir com outra arma, você pode gastar 1 PM para fazer um ataque corpo a corpo extra com a mordida. Se já possuir outro ataque natural de mordida, em vez disso, o dano desse ataque aumenta em dois passos. (magia)",
        "tipo": "concedido/Kally, Megalokk"
    },
    {
        "nome": "Presas Venenosas",
        "desc": "Você pode gastar uma ação de movimento e 1 PM para envenenar uma arma corpo a corpo que esteja empunhando. Em caso de acerto, a arma causa perda de 1d12 pontos de vida. A arma permanece envenenada até atingir uma criatura ou até o fim da cena, o que acontecer primeiro. (magia)",
        "tipo": "concedido/Sszzaas"
    },
    {
        "nome": "Rejeição Divina",
        "desc": "Você recebe resistência a magia divina +5.",
        "tipo": "concedido/Aharadak"
    },
    {
        "nome": "Reparar Injustiça",
        "desc": "Uma vez por rodada, quando um oponente em alcance curto acerta um ataque em você ou em um de seus aliados, você pode gastar 2 PM para fazer este oponente repetir o ataque, escolhendo o pior entre os dois resultados.",
        "tipo": "concedido/Khalmyr"
    },
    {
        "nome": "Sangue de Ferro",
        "desc": "Você pode pagar 3 PM para receber +2 em rolagens de dano e redução de dano 5 até o fim da cena. (magia)",
        "tipo": "concedido/Arsenal"
    },
    {
        "nome": "Sangue Ofídico",
        "desc": "Você recebe resistência a veneno +5 e a CD para resistir aos seus venenos aumenta em +2.",
        "tipo": "concedido/Sszzaas"
    },
    {
        "nome": "Servos do Dragão",
        "desc": "Você pode gastar uma ação completa e 2 PM para invocar 2d4+1 kobolds capangas em espaços desocupados em alcance curto. Você pode gastar uma ação de movimento para fazer os kobolds andarem (eles têm deslocamento 9m) ou uma ação padrão para fazê-los causar dano a criaturas adjacentes (1d6-1 pontos de dano de perfuração cada). Os kobolds têm For -1, Des 1, Defesa 12, 1 PV e falham automaticamente em qualquer teste de resistência ou oposto. Eles desaparecem quando morrem ou no fim da cena. Os kobolds não agem sem receber uma ordem. Usos criativos para capangas fora de combate ficam a critério do mestre. (magia)",
        "tipo": "concedido/Kally"
    },
    {
        "nome": "Sopro do Mar",
        "desc": "Você pode gastar uma ação padrão e 1 PM para soprar vento marinho em um cone de 6m. Criaturas na área sofrem 2d6 pontos de dano de frio (Reflexos CD Sab reduz à metade). Você pode aprender Sopro das Uivantes como uma magia divina. Se fizer isso, o custo dela diminui em -1 PM. (magia)",
        "tipo": "concedido/Oceano"
    },
    {
        "nome": "Sorte dos Loucos",
        "desc": "Você pode pagar 1 PM para rolar novamente um teste recém realizado. Se ainda assim falhar no teste, você perde 1d6 PM.",
        "tipo": "concedido/Nimb"
    },
    {
        "nome": "Talento Artístico",
        "desc": "Você recebe +2 em Acrobacia, Atuação e Diplomacia.",
        "tipo": "concedido/Marah"
    },
    {
        "nome": "Teurgista Místico",
        "desc": "Até uma magia de cada círculo que você aprender poderá ser escolhida entre magias divinas (se você for um conjurador arcano) ou entre magias arcanas (se for um conjurador divino). Pré-requisito: habilidade de classe Magias.",
        "tipo": "concedido/Wynna"
    },
    {
        "nome": "Tradição de Lin-Wu",
        "desc": "Você considera a katana uma arma simples e, se for proficiente em armas marciais, recebe +1 na margem de ameaça com ela.",
        "tipo": "concedido/Lin-Wu"
    },
    {
        "nome": "Transmissão da Loucura",
        "desc": "Você pode lançar Sussurros Insanos (CD Car). Caso aprenda novamente essa magia, seu custo diminui em -1 PM. (magia)",
        "tipo": "concedido/Nimb"
    },
    {
        "nome": "Tropas Duyshidakk",
        "desc": "Você pode gastar uma ação completa e 2 PM para invocar 1d4+1 goblinoides capangas em espaços desocupados em alcance curto. Você pode gastar uma ação de movimento para fazer os goblinoides andarem (eles têm deslocamento 9m) ou uma ação padrão para fazê-los causar dano a criaturas adjacentes (1d6+1 pontos de dano de corte cada). Os goblinoides têm For 1, Des 1, Defesa 15, 1 PV e falham automaticamente em qualquer teste de resistência ou oposto. Eles desaparecem quando morrem ou no fim da cena. Os goblinoides não agem sem receber uma ordem. Usos criativos para capangas fora de combate ficam a critério do mestre. (magia)",
        "tipo": "concedido/Thwor"
    },
    {
        "nome": "Urro Divino",
        "desc": "Quando faz um ataque ou lança uma magia, você pode pagar 1 PM para somar sua Constituição (mínimo +1) à rolagem de dano desse ataque ou magia.",
        "tipo": "concedido/Megalokk"
    },
    {
        "nome": "Visão nas Trevas",
        "desc": "Você enxerga perfeitamente no escuro, incluindo em magias de escuridão.",
        "tipo": "concedido/Tenebra"
    },
    {
        "nome": "Voz da Civilização",
        "desc": "Você está sempre sob efeito de Compreensão. (magia)",
        "tipo": "concedido/Tanna-Toh"
    },
    {
        "nome": "Voz da Natureza",
        "desc": "Você pode falar com animais (como o efeito da magia Voz Divina) e aprende e pode lançar Acalmar Animal, mas só contra animais. Caso aprenda novamente essa magia, seu custo diminui em -1 PM. (magia)",
        "tipo": "concedido/Allihanna"
    },
    {
        "nome": "Voz dos Monstros",
        "desc": "Você conhece os idiomas de todos os monstros inteligentes e pode se comunicar livremente com monstros não inteligentes (Int -4 ou menor), como se estivesse sob efeito da magia Voz Divina. (magia)",
        "tipo": "concedido/Megalokk"
    },
    {
        "nome": "Zumbificar",
        "desc": "Você pode gastar uma ação completa e 3 PM para reanimar o cadáver de uma criatura Pequena ou Média adjacente por um dia. O cadáver funciona como um parceiro iniciante de um tipo a sua escolha entre combatente, fortão ou guardião. Além disso, quando sofre dano, você pode sacrificar esse parceiro; se fizer isso, você sofre apenas metade do dano, mas o cadáver é destruído. (magia)",
        "tipo": "concedido/Tenebra"
    },
    {
        "nome": "Anatomia Insana",
        "desc": "Você tem 25% de chance (resultado “1” em 1d4) de ignorar o dano adicional de um acerto crítico ou ataque furtivo. A chance aumenta em +25% para cada dois outros poderes da Tormenta que você possui.",
        "tipo": "tormenta"
    },
    {
        "nome": "Antenas",
        "desc": "Você recebe +1 em Iniciativa, Percepção e Vontade. Este bônus aumenta em +1 para cada dois outros poderes da Tormenta que você possui.",
        "tipo": "tormenta"
    },
    {
        "nome": "Armamento Aberrante",
        "desc": "Você pode gastar uma ação de movimento e 1 PM para produzir uma versão orgânica de qualquer arma corpo a corpo ou de arremesso com a qual seja proficiente — ela brota do seu braço, ombro ou costas como uma planta grotesca e então se desprende. O dano da arma aumenta em um passo para cada dois outros poderes da Tormenta que você possui. A arma dura pela cena, então se desfaz numa poça de gosma. Pré-requisito: outro poder da Tormenta.",
        "tipo": "tormenta"
    },
    {
        "nome": "Articulações Flexíveis",
        "desc": "Você recebe +1 em Acrobacia, Furtividade e Reflexos. Este bônus aumenta em +1 para cada dois outros poderes da Tormenta que você possui.",
        "tipo": "tormenta"
    },
    {
        "nome": "Asas Insetoides",
        "desc": "Você pode gastar 1 PM para receber deslocamento de voo 9m até o fim do seu turno. O deslocamento aumenta em +1,5m para cada outro poder da Tormenta que você possui. Pré-requisitos: quatro outros poderes da Tormenta.",
        "tipo": "tormenta"
    },
    {
        "nome": "Carapaça",
        "desc": "Sua pele é recoberta por placas quitinosas. Você recebe +1 na Defesa. Este bônus aumenta em +1 para cada dois outros poderes da Tormenta que você possui.",
        "tipo": "tormenta"
    },
    {
        "nome": "Corpo Aberrante",
        "desc": "Crostas vermelhas em várias partes de seu corpo tornam seus ataques mais perigosos. Seu dano desarmado aumenta em um passo, mais um passo para cada quatro outros poderes da Tormenta que você possui. Pré-requisito: outro poder da Tormenta.",
        "tipo": "tormenta"
    },
    {
        "nome": "Cuspir Enxame",
        "desc": "Você pode gastar uma ação completa e 2 PM para criar um enxame de insetos rubros em um ponto a sua escolha em alcance curto e com duração sustentada. O enxame tem tamanho Médio e pode passar pelo espaço de outras criaturas. Uma vez por rodada, você pode gastar uma ação de movimento para mover o enxame 9m. No final do seu turno, o enxame causa 2d6 pontos de dano de ácido a qualquer criatura no espaço que ele estiver ocupando. Para cada dois outros poderes da Tormenta que possui, você pode gastar +1 PM quando usa este poder para aumentar o dano do enxame em +1d6. (magia)",
        "tipo": "tormenta"
    },
    {
        "nome": "Dentes Afiados",
        "desc": "Você recebe uma arma natural de mordida (dano 1d4, crítico x2, corte). Uma vez por rodada, quando usa a ação agredir para atacar com outra arma, pode gastar 1 PM para fazer um ataque corpo a corpo extra com a mordida.",
        "tipo": "tormenta"
    },
    {
        "nome": "Desprezar a Realidade",
        "desc": "Você pode gastar 2 PM para ficar no limiar da realidade até o início de seu próximo turno. Nesse estado, você ignora terreno difícil e causa 20% de chance de falha em efeitos usados contra você (não apenas ataques). Para cada dois outros poderes de Tormenta que você possuir, essa chance aumenta em 5% (máximo de 50%). Pré-requisito: quatro outros poderes da Tormenta.",
        "tipo": "tormenta"
    },
    {
        "nome": "Empunhadura Rubra",
        "desc": "Você pode gastar 1 PM para cobrir suas mãos com uma carapaça rubra. Até o final da cena, você recebe +1 em Luta. Este bônus aumenta em +1 para cada dois outros poderes da Tormenta que você possui.",
        "tipo": "tormenta"
    },
    {
        "nome": "Fome de Mana",
        "desc": "Quando passa em um teste de resistência para resistir a uma habilidade mágica, você recebe 1 PM temporário cumulativo. Você pode ganhar um máximo de PM temporários por cena desta forma igual ao número de poderes da Tormenta que possui.",
        "tipo": "tormenta"
    },
    {
        "nome": "Larva Explosiva",
        "desc": "Se uma criatura que tenha sofrido dano de sua mordida nesta cena for reduzida a 0 ou menos PV, ela explode em chuva cáustica, morrendo e causando 4d4 pontos de dano de ácido em criaturas adjacentes. Para cada dois outros poderes da Tormenta que você possui, o dano aumenta em +2d4. Você é imune a esse dano. Pré-requisito: Dentes Afiados. e",
        "tipo": "tormenta"
    },
    {
        "nome": "Legião Aberrante",
        "desc": "Seu corpo se transforma em uma massa de insetos rubros. Você pode atravessar qualquer espaço por onde seja possível passar uma moeda (mas considera esses espaços como terreno difícil) e recebe +1 em testes contra manobras de combate e de resistência contra efeitos que tenham você como alvo (mas não efeitos de área). Este bônus aumenta em +1 para cada dois outros poderes da Tormenta que você possui. Pré-requisito: Anatomia Insana, três outros poderes da Tormenta.",
        "tipo": "tormenta"
    },
    {
        "nome": "Mãos Membranosas",
        "desc": "Você recebe +1 em Atletismo, Fortitude e testes de agarrar. Este bônus aumenta em +1 para cada dois outros poderes da Tormenta que você possui.",
        "tipo": "tormenta"
    },
    {
        "nome": "Membros Estendidos",
        "desc": "Seus braços e armas naturais são grotescamente mais longos que o normal, o que aumenta seu alcance natural para ataques corpo a corpo em +1,5m. Para cada quatro outros poderes da Tormenta que você possui, esse alcance aumenta em +1,5m.",
        "tipo": "tormenta"
    },
    {
        "nome": "Membros Extras",
        "desc": "Você possui duas armas naturais de patas insetoides que saem de suas costas, ombros ou flancos. Uma vez por rodada, quando usa a ação agredir para atacar com outra arma, pode gastar 2 PM para fazer um ataque corpo a corpo extra com cada uma (dano 1d4, crítico x2, corte). Se possuir Ambidestria ou Estilo de Duas Armas, pode empunhar armas leves em suas patas insetoides (mas ainda precisa pagar 2 PM para atacar com elas e sofre a penalidade de -2 em todos os ataques). Pré-requisitos: quatro outros poderes da Tormenta.",
        "tipo": "tormenta"
    },
    {
        "nome": "Mente Aberrante",
        "desc": "Você recebe resistência a efeitos mentais +1. Além disso, sempre que precisa fazer um teste de Vontade para resistir a uma habilidade, a criatura que usou essa habilidade sofre 1d6 pontos de dano psíquico. Para cada dois outros poderes da Tormenta que você possui o bônus em testes de resistência aumenta em +1 e o dano aumenta em +1d6. (magia)",
        "tipo": "tormenta"
    },
    {
        "nome": "Olhos Vermelhos",
        "desc": "Você recebe visão no escuro e +1 em Intimidação. Este bônus aumenta em +1 para cada dois outros poderes da Tormenta que você possui.",
        "tipo": "tormenta"
    },
    {
        "nome": "Pele Corrompida",
        "desc": "Sua carne foi mesclada à matéria vermelha. Você recebe redução de ácido, eletricidade, fogo, frio, luz e trevas 2. Esta RD aumenta em +2 para cada dois outros poderes da Tormenta que você possui.",
        "tipo": "tormenta"
    },
    {
        "nome": "Sangue Ácido",
        "desc": "Quando você sofre dano por um ataque corpo a corpo, o atacante sofre 1 ponto de dano de ácido por poder da Tormenta que você possui.",
        "tipo": "tormenta"
    },
    {
        "nome": "Visco Rubro",
        "desc": "Você pode gastar 1 PM para expelir um líquido grosso e corrosivo. Até o final da cena, você recebe +1 nas rolagens de dano corpo a corpo. Este bônus aumenta em +1 para cada dois outros poderes da Tormenta que você possui.",
        "tipo": "tormenta"
    }
]
    
    
    for item in dados:
        models.Poderes.objects.create(
            nome=item["nome"],
            descricao=item["desc"],
            tipo=3,
            concedente = 'Megalokk'
        )

    return redirect('login')