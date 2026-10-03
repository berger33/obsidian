---
id: software.seguranca.tranche11.001041
tipo: tecnica
dominio: software
subdominio: seguranca
nivel: intermediario
confianca: media
ultima_verificacao: 2026-10-03
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-03
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-11.md"
fontes: ["https://raw.githubusercontent.com/sensepost/objection/master/README.md", "https://github.com/sensepost/objection/wiki/Patching-Android-Applications"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# **SensePost Objection (`sensepost/objection`)**: Arquitetura de Exploração Mobile em Runtime sobre **Frida** para **Android e iOS Sem Root/Jailbreak**

## Em uma frase
Criado por Leon Jacobs na **SensePost** (`sensepost/objection`, licença GPL-3.0, escrito em Python + agentes TypeScript/Frida), o **`objection`** é um toolkit interativo de **Exploração Mobile em Tempo de Execução (*Runtime Mobile Exploration*)** construído sobre o **Frida (`frida.re`)** para avaliar a postura de segurança de aplicativos **Android e iOS sem exigir um aparelho com Root ou Jailbreak**!

## Por que importa
Qual é a vantagem operacional do `objection` sobre escrever scripts Frida do zero em cada pentest? Enquanto o Frida puro exige que você escreva código JavaScript/TypeScript para cada tarefa (`Java.perform(...)` ou `ObjC.classes...`), o `objection` compila um **Agente Frida rico em comandos prontos** e entrega um shell REPL interativo com autocompletar (`tab`), gerenciamento de tarefas assíncronas (`jobs list` / `jobs kill`), navegação no sistema de arquivos do sandbox do aplicativo (`env`, `ls`, `cd`, `file download`) e cliente SQLite integrado (`sqlite connect`)!

## Como funciona
Ele funciona tanto contra dispositivos com `frida-server` (root/jailbreak) quanto contra **dispositivos comuns bloqueados de fábrica** embutindo o `frida-gadget` no pacote via **`objection patchapk`** e **`objection patchipa`**!

## Exemplo
```bash
# Instalar o objection e iniciar uma sessao de exploracao interativa conectando ao aplicativo alvo (ou Frida Gadget) via USB/Rede
pip3 install --upgrade objection
objection --gadget "com.empresa.mobileapp" explore
```

## Limites e trade-offs
Para executar comandos de inicialização automaticamente no milissegundo em que o aplicativo abre (*Early Instrumentation* — essencial quando o app verifica Root ou SSL Pinning logo no método `Application.onCreate`!), passe a flag **`-s` / `--startup-command`**: por exemplo, `objection -g "com.empresa.mobileapp" explore -s "android sslpinning disable"`!

## Como verificar
Use o comando `env` assim que entrar no REPL do `objection` para listar todos os diretórios de dados privados (`files`, `cache`, `code_cache` no Android, ou `DocumentDirectory`, `LibraryDirectory` no iOS) do aplicativo.

## Conexões
- [[objection-patchapk-patchipa-instrumentacao-sem-root-jailbreak]] — Veja também: Instrumentação Sem Root/Jailbreak com **`objection patchapk`** e **`objection patchipa`**: Automação do `frida-gadget` e Configurações de Script.
- [[objection-bypass-ssl-pinning-android-ios-network-security-trustkit]] — Referência cruzada direta com objection-bypass-ssl-pinning-android-ios-network-security-trustkit.
- [[frida-arquitetura-instrumentacao-dinamica-gum-v8-quickjs-modos]] — Referência cruzada direta com frida-arquitetura-instrumentacao-dinamica-gum-v8-quickjs-modos.

## Fontes
- [SensePost Objection Official GitHub — Runtime Mobile Exploration Toolkit Powered by Frida](https://raw.githubusercontent.com/sensepost/objection/master/README.md) — repositório oficial do `objection` cobrindo exploração em tempo de execução para Android e iOS sem necessidade de root/jailbreak; consultado em 2026-10-03.
- [SensePost Objection Official Wiki — Patching Android & iOS Applications (`patchapk` / `frida-gadget`)](https://github.com/sensepost/objection/wiki/Patching-Android-Applications) — documentação oficial detalhando o processo automatizado de injeção do `frida-gadget.so`, reempacotamento e assinatura; consultado em 2026-10-03.
