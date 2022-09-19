#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#|
import os, discord, random
from ast                            import Expression
from discord.ext                    import commands #, tasks
from discord.ext.commands.errors    import MissingRequiredArgument, CommandNotFound, CommandInvokeError
from types                          import NoneType
from decouple                       import config
#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#|
class Character:
    def __init__ (self,name,hp,mp,str,dex,int,fth,cha,xp,lv,gold):
        self.name = name                        # nome
        self.hp  = f"{hp*10}/{hp*10}"           # 10/10          atual/total
        self.mp  = f"{mp*10}/{mp*10}"           # 10/10          atual/total
        self.str = str                          # 1              int
        self.dex = dex                          # 1              int
        self.int = int                          # 1              int
        self.fth = fth                          # 1              int
        self.cha = cha                          # 1              int
        self.lv  = lv                           # 1              int
        self.xp  = f"{xp}/{lv*10}"              # 0/10           atual/level up
        self.gold= gold                         # 0              int
#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#|
class Monster:
    def __init__ (self,name,damage,hp,agi,xp):
        self.name   = name               # string
        self.damage = damage             # int
        self.hp     = f"{int(hp)*10}/{int(hp)*10}" # atual/total
        self.agi    = agi                # int
        self.xp     = xp                 # int
#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#|
class Item_Skill:
    def __init__ (self,name,type,mod,tier,description,Item_Or_Skill):
        self.name        = name            # string
        self.type        = type            # int
        self.mod         = mod             # int
        self.tier        = tier            # int
        self.description = description     # string
        self.Item_Or_Skill = Item_Or_Skill # Boolean    ---> True: Item | False: Skill
#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#|
def new_file_C                      (name,authorName,hp=1,mp=1,str=1,dex=1,int=1,fth=1,cha=1,xp=0,lv=1,gold=0):
    c1 = Character (name,hp,mp,str,dex,int,fth,cha,xp,lv,gold)
    atributesList = [f"{c1.name}, por '{authorName}';", c1.hp,c1.mp,c1.str,c1.dex,c1.int,c1.fth,c1.cha,c1.xp,c1.lv,c1.gold]

    for cont in range (0, len(atributesList), 1):
        if cont == len(atributesList) -1:
            atributesList[cont] = f"{atributesList[cont]}"

        else: atributesList[cont] = f"{atributesList[cont]} \n"

    file = open(f"{c1.name}.txt","w")
    file.write("Tipo de arquivo: Personagem \n")
    file.writelines(atributesList)
    file.close()
    return
#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#|
def new_file_M                      (name,damage,hp,agi,xp):
    m1 = Monster (name,damage,hp,agi,xp)
    atributesList = [m1.name,m1.damage,m1.hp,m1.agi,m1.xp]

    for cont in range (0, len(atributesList), 1):
        if cont == len(atributesList) - 1:
            atributesList[cont] = f"{atributesList[cont]}"

        else: atributesList[cont] = f"{atributesList[cont]} \n"
    

    file = open(f"{m1.name}.txt","w")
    file.write("Tipo de arquivo: Monstro \n")
    file.writelines(atributesList)
    file.close()
    return
#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#|
def new_file_I                      (name,type,mod,tier,description):
    i1 = Item_Skill (name,type,mod,tier,description,True)
    atributesList = [i1.name,i1.type,i1.mod,i1.tier,i1.description];

    for cont in range (0, len(atributesList), 1):
        if cont == len(atributesList) - 1:
            atributesList[cont] = f"{atributesList[cont]}"

        else: atributesList[cont] = f"{atributesList[cont]} \n"

    file = open(f"{i1.name}.txt","w")
    file.write("Tipo de arquivo: Item \n")
    file.writelines(atributesList)
    file.close()
    return
#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#|
def new_file_S                      (name,type,mod,tier,description):
    s1 = Item_Skill (name,type,mod,tier,description,False)  #OBS: o tier da Skill representa o alcance
    atributesList = [s1.name,s1.type,s1.mod,s1.tier,s1.description];

    for cont in range (0, len(atributesList), 1):
        if cont == len(atributesList) - 1:
            atributesList[cont] = f"{atributesList[cont]}"

        else: atributesList[cont] = f"{atributesList[cont]} \n"

    file = open(f"{s1.name}.txt","w")
    file.write("Tipo de arquivo: Magia/Habilidade \n")
    file.writelines(atributesList)
    file.close()
    return
#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#|
def delete_file                     (name):
    if os.path.exists(f"{name}.txt"):
        os.remove(f"{name}.txt")
    else:
        return
#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#|
def modf_file                       (name,line,content = NoneType):
    if content == NoneType:                         #se quiser apenas retornar a linha
        file = open(f"{name}.txt", "r")
        AtributesList = file.readlines()

        if line < 1 or line > len(AtributesList):
            return ""

        else: return AtributesList[(line-1)]

    else:                                           #se quiser modificar de fato a linha
        file = open(f"{name}.txt", "r")
        AtributesList = file.readlines()
        file.close()

        if line < 1 or line > len(AtributesList):
            return ""

        else:
            file = open(f"{name}.txt", "w")
            AtributesList[(line-1)] = f"{content} \n"
            file.writelines(AtributesList)

            file.close()

            return AtributesList[(line-1)]
#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#|
def tupleString                     (tuple):
    stringT = ""

    list(tuple)

    for cont in range (0,len(tuple),1):
        stringT += tuple[cont]
        if cont != len(tuple) - 1:
            stringT += " "

    return stringT
#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#|
TOKEN       = config                ("TOKEN")
PLAYERSPATH = config                ("PLAYERSPATH")
intents     = discord.Intents.all   ()
bot         = commands.Bot          ("!", intents= intents, help_command=None)
#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#|
@bot.event
async def on_ready                  ():
    print (f"{bot.user}: Fui inicializado") #colocar as tasks aqui abaixo
#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#|
@bot.command                        (name= "help")
async def help                      (ctx):
    sinal1 = ":green_circle:"
    sinal2 = ":warning:"
    sinal3 = ":lock:"

    help1 = f"""
            Inicialmente, os jogadores são criados no **nível (LV) 1**, com todos seus atributos "humanos" e relevantes iniciando-se em 1.

            Cada atributo tem uma função e representação específica, sendo eles:
            **HP** :anatomical_heart:: saúde e resistência
            **MP** :scroll:: conhecimento, saúde mental e estratégia
            **STR** :muscle:: capacidade de levantar coisas pesadas, carregar pesos e causar dano físico
            **DEX** :leg:: habilidade de manejar objetos, reflexos e pontaria
            **INT** :brain:: afinidade mágica e QI
            **FTH** :pray:: devoção em determinada religião
            **CHA** :speaking_head:: capacidade de argumentar, gerar empatia e afinidade com a música
            **LV** :signal_strength:: nível de engajamento
            **XP** :up:: experiência em combate e em situações adversas

            Ao adquirir uma quantidade (LV*10) de XP, eles podem incrementar um de seus atributos (HP, MP, STR, DEX, INT, FTH ou CHA).
            """

    help2 = """
            **Monstros:** São inimigos dos jogadores que possuem status semelhantes. Ao serem derrotados provém XP e itens.

            **Itens:** São objetos ou artefatos que possuem propriedades físicas e possivelmente propriedades mágicas, bem como efeitos adicionais. Quando um jogador adquire um item, ele pode optar por coletá-lo, gastando espaços em seu **inventário**. Os espaços no inventário podem ser incrementados ao incrementar STR.

            **Magias:** Magias são habilidades ou ações místicas que o jogador desenvolveu ou aprendeu. Seus usos podem ser extremamente variados, tanto em combates, como em utilidades ou curas. Similarmente aos itens, magias são armazenadas e consomem espaços referentes à preparação do jogador. Para incrementar o número de espaços, deve-se incrementar MP.
            """

    help3 = f"""
            {sinal1}**!help**
            {sinal1}**!ficha** |nome|
            {sinal1}**!del_ficha** |nome|
            {sinal3}**!item** |nome|,|tipo|,|modificador|,|raridade|,|descrição|
            {sinal3}**!magia** |nome|,|tipo|,|modificador|,|tier|,|descrição|
            {sinal3}**!monstro** |nome|,|dano|,|hp|,|agi|,|xp|
            {sinal1}**!ver** |nome arquivo|
            {sinal1}**!levelUP** |nome|,|atributo| (hp e mp)
            {sinal1}**!dado** |número|
            {sinal3}**!modfStatus** |nome|,|atributo|,|quantidade|

            **Legenda:** 
            "||": representa um termo genérico descrito entre cada barra
            {sinal1}: funcionando
            {sinal2}: em desenvolvimento/com problema
            {sinal3}: exclusivo do adm
            """

    help4 = """
        As classes são profissões que os jogadores possuem que influenciam nas habilidades e no provável caminho que eles irão progredir.
            Exemplos delas:
            => Bárbaro
            => Cavaleiro
            => Espadachim
            => Arqueiro
            => Ladino
            => Assassino
            => Mago
            => Feiticeiro
            => Bruxo
            => Clérigo
            => Paladino
            => Bardo
            => Artesão
            => Alquimista
            """

    help5 = """
        O combate é definido em turnos. A prioridade de ataque é de quem possuir mais destreza (jogadores) ou agilidade (montros).
        Os jogadores podem se posicionar de modo que apenas os jogadores da vanguarda recebam dano.
        Danos físicos são calculados com a metade da soma de força com destreza.
        Danos à distância são calculados com a destreza.
        Danos mágicos são calculados com inteligência.
        Danos de milagres são calculados com fé.
        Essa regra também é equivalente bara buffs com carisma, fé e inteligência.
        Habilidades e magias possuem dano extra.
        Itens podem possuir efeitos adicionais e incrementam o ataque/defesa.


        
        Fórmula de ataque padrão: atributos + d6 + arma + magia/habilidade
    """


    embed_view = discord.Embed(
        title = f"Tutorial",
        description = f"(Um breve resumo manjado dos commandos e das regras do rpg)",
        color = 0x0000FF
    )

    embed_view.add_field(name= "Jogadores: "                ,value = help1)
    embed_view.add_field(name= "Monstros, Itens e Magias: " ,value = help2)
    embed_view.add_field(name= "Comandos: "                 ,value = help3)
    embed_view.add_field(name= "Classes: "                  ,value = help4)
    embed_view.add_field(name= "Combate: "                  ,value = help5)

    await ctx.author.send(embed=embed_view)

    await ctx.message.delete()
#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#|
@bot.command                        (name= "ficha")
async def addFicha                  (ctx, *expression):
    with open(f"{PLAYERSPATH}", "r") as file:
        playerList = file.readlines()
        playerStr = str(playerList)
        file.close()

    if f"{ctx.author}" in playerStr:
        await ctx.author.send(f"Apenas um personagem por vez")  #pega o nome do autor que enviou a mensagem e envia no canal privado
        await ctx.message.delete()  #apaga a mensagem enviada para limpar o chat

    else:
        try:
            name = tupleString (expression)

            new_file_C (name,f"{ctx.author}")

            await ctx.author.send(f"Ficha do seu personagem, '{name}' criada")  #pega o nome do autor que enviou a mensagem e envia no canal privado

            with open(f"{PLAYERSPATH}", "a") as file:
                file.write(f"{ctx.author}\n")

            await ctx.message.delete()  #apaga a mensagem enviada para limpar o chat
            
        except Exception as error:
            await ctx.send(f"Erro ao enviar mensagem no privado. **{ctx.author}** tente habilitar receber mensagens de qualquer pessoa do servidor (Opções > Privacidade)")
#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#|
@bot.command                        (name= "del_ficha")
async def delFicha                  (ctx, *expression):
    try: 
        name = tupleString (expression)
        author = f"{ctx.author}"

        with open(f"{name}.txt", "r") as file:
            lines = file.readlines()
            file.close()

        if author in lines[1]:
            delete_file(name)

            with open(f"{PLAYERSPATH}", "r") as file:
                lines = file.readlines()
                file.close()
            
            lines.remove(f"{author}\n")

            with open(f"{PLAYERSPATH}", "w") as file:
                file.writelines(lines)
                file.close()

            await ctx.author.send(f"Ficha do seu personagem '{name}' deletada")

        else:
            await ctx.author.send("Você não é o dono da ficha que tentou deletar")
        
        await ctx.message.delete()  #apaga a mensagem enviada para limpar o chat

    except Exception as error:
        await ctx.send(f"Erro ao enviar mensagem no privado. **{ctx.author}** tente habilitar receber mensagens de qualquer pessoa do servidor (Opções > Privacidade)")
#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#|
@bot.command                        (name= "item")
@commands.has_permissions           (administrator=True)
async def addItem                   (ctx, *expression):
    try:
        cmds= tupleString(expression)

        cmds = cmds.split(",")

        new_file_I(cmds[0],cmds[1],cmds[2],cmds[3],cmds[4])
        await ctx.message.delete()  #apaga a mensagem enviada para limpar o chat
        await ctx.author.send(f"Item '{cmds[0]}' criado")

    except Exception as error:
        await ctx.send(f"Erro ao enviar mensagem no privado. **{ctx.author}** tente habilitar receber mensagens de qualquer pessoa do servidor (Opções > Privacidade)")
        await ctx.message.delete()  #apaga a mensagem enviada para limpar o chat
#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#|
@bot.command                        (name= "magia")
@commands.has_permissions           (administrator= True)
async def addMagic                  (ctx, *expression):
    try:
        cmds= tupleString(expression)

        cmds = cmds.split(",")

        new_file_S(cmds[0],cmds[1],cmds[2],cmds[3],cmds[4])
        await ctx.message.delete()  #apaga a mensagem enviada para limpar o chat
        await ctx.author.send(f"Magia/Habilidade '{cmds[0]}' criadaa")

    except Exception as error:
        await ctx.send(f"Erro ao enviar mensagem no privado. **{ctx.author}** tente habilitar receber mensagens de qualquer pessoa do servidor (Opções > Privacidade)")
        await ctx.message.delete()  #apaga a mensagem enviada para limpar o chat
#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#|
@bot.command                        (name= "monstro")
@commands.has_permissions           (administrator= True)
async def addMob                    (ctx, *expression):
    try:
        cmds= tupleString(expression)
        cmds = cmds.split(",")

        new_file_M(cmds[0],cmds[1],cmds[2],cmds[3],cmds[4])
        await ctx.message.delete()  #apaga a mensagem enviada para limpar o chat
        await ctx.author.send(f"Monstro '{cmds[0]}' criado")

    except Exception as error:
        await ctx.send(f"Erro ao enviar mensagem no privado. **{ctx.author}** tente habilitar receber mensagens de qualquer pessoa do servidor (Opções > Privacidade)")
        await ctx.message.delete()  #apaga a mensagem enviada para limpar o chat
#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#|
@bot.command                        (name= "ver")
async def seeArq                    (ctx, *expression):
    fileName = tupleString(expression)

    tipo = ""
    lineList = [] #lista dos atributos (linhas)
    first_line = ""

    try:
        with open(f"{fileName}.txt", "r") as file:
            first_line = file.readline()
                
            for line in file:
                lines = line.rstrip("\n")
                lineList.append(lines)

            file.close()

    except Exception as error:
        await ctx.author.send(f"Arquivo inexistente.")
        await ctx.message.delete()  #apaga a mensagem enviada para limpar o chat

    atributos = "" ; legenda = ""

    if "Personagem"         in first_line:      # <=== personagem
        tipo = "Personagem"
        atributos += f":anatomical_heart:: {lineList[1]} \n"    ; legenda += "HP\n"
        atributos += f":scroll:: {lineList[2]} \n"              ; legenda += "MP\n"
        atributos += f":muscle:: {lineList[3]} \n"              ; legenda += "STR\n"
        atributos += f":leg:: {lineList[4]} \n"                 ; legenda += "DEX\n"
        atributos += f":brain:: {lineList[5]} \n"               ; legenda += "INT\n"
        atributos += f":pray:: {lineList[6]} \n"                ; legenda += "FTH\n"
        atributos += f":speaking_head:: {lineList[7]} \n"       ; legenda += "CHA\n"
        atributos += f":signal_strength:: {lineList[8]} \n"     ; legenda += "LV\n"
        atributos += f":up:: {lineList[9]} \n"                  ; legenda += "XP\n"
        atributos += f":coin:: {lineList[10]}"                  ; legenda += "Moedas\n"

    elif "Monstro"          in first_line:      # <=== monstro
        tipo = "Monstro"
        atributos += f":crossed_swords:: {lineList[1]} \n"      ; legenda += "Dano\n"
        atributos += f":anatomical_heart:: {lineList[2]} \n"    ; legenda += "HP\n"
        atributos += f":leg:: {lineList[3]} \n"                 ; legenda += "AGI\n"
        atributos += f":signal_strength:: {lineList[4]} \n"     ; legenda += "XP\n"

    elif "Item"             in first_line:      # <=== item
        tipo = "Item"
        if   lineList[1] == "1 " : atributos += f"Dano (:muscle:/:leg:): {lineList[2]}\n"           ; legenda += "Atributos influenciados: STR/DEX\n"
        elif lineList[1] == "2 " : atributos += f"Dano (:brain:): {lineList[2]}\n"                  ; legenda += "Atributos influenciados: INT\n"
        elif lineList[1] == "3 " : atributos += f"Dano (:muscle:): {lineList[2]}\n"                 ; legenda += "Atributos influenciados: STR\n"
        elif lineList[1] == "4 " : atributos += f"Dano (:leg:): {lineList[2]}\n"                    ; legenda += "Atributos influenciados: DEX\n"
        elif lineList[1] == "5 " : atributos += f"Dano (:pray:): {lineList[2]}\n"                   ; legenda += "Atributos influenciados: FTH\n"
        elif lineList[1] == "6 " : atributos += f"Dano (:speaking_head:): {lineList[2]}\n"          ; legenda += "Atributos influenciados: CHA\n"
        elif lineList[1] == "7 " : atributos += f"Defesa (:anatomical_heart:): {lineList[2]}\n"     ; legenda += "Atributos influenciados: HP\n"
        elif lineList[1] == "8 " : atributos += f"Diversos (:question:): {lineList[2]}\n"           ; legenda += "Atributos influenciados: ?\n"
        elif lineList[1] == "9 " : atributos += f"Poção (:question:): {lineList[2]}\n"              ; legenda += "Atributos influenciados: ?\n"
        atributos +="Raridade: " + (int(lineList[3]) * ":star:") + "\n"                             ; legenda += "Raridade\n"
        atributos += "\n :label:: " + lineList[4]                                                   ; legenda += "\nDescrição\n"

    elif "Magia/Habilidade" in first_line:      # <=== magia
        tipo = "Magia/Habilidade"
        if   lineList[1] == "1 " : atributos += f"Dano: {lineList[2]}\n"            ; legenda += "Causa dano ao alvo\n"
        elif lineList[1] == "2 " : atributos += f"Cura: {lineList[2]}\n"            ; legenda += "Cura o alvo\n"
        elif lineList[1] == "3 " : atributos += f"Atordoamento: {lineList[2]}\n"    ; legenda += "Atordoa o alvo\n"
        elif lineList[1] == "4 " : atributos += f"Buff/Debuff: {lineList[2]}\n"     ; legenda += "Modifica atributos do alvo\n"
        elif lineList[1] == "5 " : atributos += f"Diversos: {lineList[2]}\n"        ; legenda += "?\n"
        atributos +="Raridade: " + (int(lineList[3]) * ":star:") + "\n"             ; legenda += "Raridade\n"
        atributos += "\n :label:: " + lineList[4]                                   ; legenda += "\nDescrição\n"

    embed_view = discord.Embed(
        title = f"Arquivo: {fileName}.txt",
        description = f"Tipo: {tipo}",
        color = 0x0000FF
    )

    embed_view.add_field(name= "Atributos: ",value = atributos)
    embed_view.add_field(name= "Legenda: ",value = legenda)

    await ctx.author.send(embed=embed_view)
    await ctx.message.delete()  #apaga a mensagem enviada para limpar o chatait ctx.send(embed=embed_teste)
#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#|
@bot.command                        (name= "levelUP")
async def levelup                   (ctx, *expression):
    LevelList = tupleString(expression)

    LevelList = list(LevelList.split(","))

    name = LevelList[0]
    atribute = LevelList[1]

    first_line = modf_file(name,2)

    if f"{ctx.author}" in first_line:
        #verificar se há xp suficiente para subir de nível. se houver, subtrai-los logo após a modificação7

        listXP = list(modf_file(name,10)) #0/10
        strXP = ""

        for cont in range(0,len(listXP),1):
            if listXP[cont] == "/":
                break
            else: strXP += listXP[cont]

        strLV = modf_file(name,11)
        
        modf_file(name,11,f"{int(strLV) + 1}")

        if int(strXP) >= int(modf_file(name,11)):
            if   atribute == "hp" or atribute == "HP":                                      #hp
                total = modf_file(name,3)
                listAtributes = total.split("/")

                listAtributes[1] = int(listAtributes[0]) + 10

                modf_file(name,3,   f"{listAtributes[0]}/{listAtributes[1]}")

            if   atribute == "mp" or atribute == "MP":                                      #mp
                total = modf_file(name,4)
                listAtributes = total.split("/")

                listAtributes[1] = int(listAtributes[0]) + 10

                modf_file(name,4,   f"{listAtributes[0]}/{listAtributes[1]}")

            elif atribute == "str" or atribute == "STR":                                    #str
                strAtribute =  int(modf_file(name,5)) + 1
                modf_file(name,5,strAtribute)

            elif atribute == "dex" or atribute == "DEX":                                    #dex
                strAtribute =  int(modf_file(name,6)) + 1
                modf_file(name,6,strAtribute)

            elif atribute == "int" or atribute == "INT":                                    #int
                strAtribute =  int(modf_file(name,7)) + 1
                modf_file(name,7,strAtribute)

            elif atribute == "fth" or atribute == "FTH":                                    #fth
                strAtribute =  int(modf_file(name,8)) + 1
                modf_file(name,8,strAtribute)

            elif atribute == "cha" or atribute == "CHA":                                    #cha
                strAtribute =  int(modf_file(name,9)) + 1
                modf_file(name,9,strAtribute)

            strXP = f"{int(strXP) - (int (strLV)*10)}/{(int(strLV) + 1)* 10}"
            modf_file(name,10,strXP)
            
        else:
            await ctx.author.send("São necessários " + modf_file(name,9) + " pontos de xp para passar de nível.")
            await ctx.author.send("Seu personagem possui atualmente, " + strXP + " pontos de xp.")
            await ctx.message.delete()  #apaga a mensagem enviada para limpar o chat

        await ctx.author.send("1 ponto adicionado em " + atribute)
        await ctx.invoke(bot.get_command("ver"), name)

    else:
        await ctx.author.send("Você precisa ser autor do personagem para modificar seus atributos")
        await ctx.message.delete()  #apaga a mensagem enviada para limpar o chat
#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#|
@bot.command                        (name= "dado")
async def randomNumber              (ctx, *expression):
    try:
        number = int(tupleString(expression))
        if number <= 0 or number > 100:
            await ctx.message.delete()
            return

    except Exception as error:
        await ctx.message.delete()
        return
    
    numberrandom = random.randint(1,number)
    embed_view = discord.Embed(
        title = f"Rolando um d{number}",
        color = 0x0000FF
    )

    result = "?"

    if numberrandom == 1:
        result = "Falha crítica"

    elif numberrandom == number:
        result = "Acerto crítico"

    else: result = "Resultado: "

    embed_view.add_field(name= result,value = numberrandom)

    await ctx.send(embed=embed_view)
    await ctx.message.delete()
#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#|
@bot.command                        (name= "modfStatus", pass_context= True)
@commands.has_permissions           (administrator= True)
async def modfStatus                (ctx, *expression):
    listModf= tupleString(expression)
    listModf = list(listModf.split(","))
    name = listModf[0] ; atribute = listModf[1] ; quant = listModf[2]
    lineList = []

    try:
        with open(f"{name}.txt", "r") as file:
            first_line = file.readline()
                
            for line in file:
                lines = line.rstrip("\n")
                lineList.append(lines)  #todos as linhas do arquivo

            file.close()

    except Exception as error:
        await ctx.author.send(f"Arquivo inexistente.")
        await ctx.message.delete()  #apaga a mensagem enviada para limpar o chat
        return

    if   atribute == "hp" or atribute == "HP":                                      #hp
        line = 3 ; backupStatus = modf_file(name,line)
        final = backupStatus.split("/")

        final[1] = final[1].translate({ord('\n'): None})
        modf_file(name,line,f"{quant}/{final[1]}")

    elif atribute == "mp" or atribute == "MP":                                      #mp
        line = 4 ; backupStatus = modf_file(name,line)
        final = backupStatus.split("/")

        final[1] = final[1].translate({ord('\n'): None})
        modf_file(name,line,f"{quant}/{final[1]}")

    elif atribute == "str" or atribute == "STR":                                    #str
        line = 5 ; backupStatus = modf_file(name,line)
        list(modf_file(name,line,quant))

    elif atribute == "dex" or atribute == "DEX":                                    #dex
        line = 6 ; backupStatus = modf_file(name,line)
        list(modf_file(name,line,quant))

    elif atribute == "int" or atribute == "INT":                                    #int
        line = 7 ; backupStatus = modf_file(name,line)
        list(modf_file(name,line,quant))

    elif atribute == "fth" or atribute == "FTH":                                    #fth
        line = 8 ; backupStatus = modf_file(name,line)
        list(modf_file(name,line,quant))

    elif atribute == "cha" or atribute == "CHA":                                    #cha
        line = 9 ; backupStatus = modf_file(name,line)
        list(modf_file(name,line,quant))

    elif atribute == "xp" or atribute == "XP":                                      #xp
        line = 10; backupStatus = modf_file(name,line)
        final = backupStatus.split("/")

        final[1] = final[1].translate({ord('\n'): None})
        list(modf_file(name,line,f"{quant}/{final[1]}"))

    elif atribute == "gold" or atribute == "moedas":                                #xp
        line = 12; backupStatus = modf_file(name,line)
        list(modf_file(name,line,quant))

    embed_view = discord.Embed(
        title = f"Alteração na ficha de '{name}'",
        color = 0xFF0000
    )

    embed_view = discord.Embed(
        title = f"Alteração na ficha de '{name}'",
        color = 0xFF0000
    )

    embed_view.add_field(name= f"{atribute}", value= f"{backupStatus} para {modf_file(name,line)}")

    await ctx.send(embed=embed_view)
    await ctx.message.delete()

    await ctx.invoke(bot.get_command("ver"), name)
#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#|
@bot.event  #evento para caso aconteça erro nos comandos
async def on_command_error          (ctx, error):
    if isinstance(error,MissingRequiredArgument):
        await ctx.author.send("Erro: Faltam argumentos no comando. Digite !help para conferir os comandos.")

    if isinstance(error, CommandNotFound):
        await ctx.author.send("Erro: Comando não existe. Digite !help para conferir os comandos.")

    if isinstance(error, CommandInvokeError):
        await ctx.author.send("Erro: Erro de sintaxe do comando. Digite !help para conferir os comandos.")

    else: raise error

    await ctx.message.delete()
#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#|
bot.run(TOKEN)
#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#|
