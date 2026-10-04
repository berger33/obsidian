---
id: software.seguranca.tranche12.001152
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-12.md"
fontes: ["https://raw.githubusercontent.com/cowrie/cowrie/main/README.rst", "https://raw.githubusercontent.com/cowrie/cowrie/main/src/cowrie/data/etc/cowrie.cfg.dist"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Customização do Sistema de Arquivos Falso do Cowrie: **`fs.pickle`**, **`createfs`**, **`fsctl`**, **`honeyfs` (`contents_path`)** e **`txtcmds`**

## Em uma frase
A primeira coisa que um atacante humano (ou um script automatizado de reconhecimento) faz ao entrar em um servidor SSH é verificar se caiu em um honeypot padrão — checando o hostname (`svr04`), lendo `/etc/passwd`, `/proc/cpuinfo`, `/proc/version` ou listando diretórios!

## Por que importa
No modo `shell`, o Cowrie representa o sistema de arquivos em duas camadas: **(1) Metadados e estrutura de diretórios (`src/cowrie/data/fs.pickle`)**, que armazena caminhos, permissões, UID, GID, tamanho e timestamps de cada arquivo e pode ser modificado interativamente com o utilitário **`fsctl`** ou gerado a partir de um servidor real da sua empresa com **`createfs`**; e **(2) Conteúdo real dos arquivos (`contents_path = honeyfs`)**, de onde comandos como `cat`, `head`, `grep` e `less` leem os bytes quando o atacante abre um arquivo cujos metadados existem no `fs.pickle`!

## Como funciona
Além disso, para criar rapidamente a saída de um comando simples que só imprime texto (como `nvidia-smi`, `kubectl version` ou `aws sts get-caller-identity`), basta criar um arquivo de texto com a saída desejada dentro do diretório **`txtcmds/`** (ex.: `txtcmds/usr/bin/nvidia-smi`) e garantir que o caminho exista no `fs.pickle`!

## Exemplo
```bash
# Clonar a arvore de metadados de /etc e /home de um servidor de referencia com createfs e inspecionar o fs.pickle com fsctl
createfs -l /etc -o ./custom_etc_fs.pickle
fsctl ./src/cowrie/data/fs.pickle -c "ls -la /root"
```

## Limites e trade-offs
Para tornar seu honeypot Cowrie indistinguível dos servidores reais da sua organização, altere obrigatoriamente no `etc/cowrie.cfg` o **`hostname`** (padrão `svr04` é conhecido por todas as botnets!), a versão do banner SSH (`version = SSH-2.0-OpenSSH_9.6p1 Ubuntu-3ubuntu13.5`), o `boot_offset` e plante arquivos "isca" (*breadcrumbs* / *honeytokens*) dentro de `honeyfs/root/.aws/credentials` ou `honeyfs/home/deploy/.env`!

## Como verificar
Lembre-se da regra documentada no `cowrie.cfg.dist`: adicionar um arquivo em `contents_path` (`honeyfs`) só surte efeito para o comando `cat` se o mesmo caminho também existir registrado dentro do `fs.pickle`!

## Conexões
- [[cowrie-arquitetura-honeypot-ssh-telnet-shell-proxy-llm]] — Veja também: Arquitetura do **Cowrie (`cowrie/cowrie`)**: Honeypot SSH e Telnet de Média e Alta Interação (`backend = shell`, `proxy` e `llm`).
- [[cowrie-politicas-autenticacao-userdb-authrandom-ssh-keys-honeytokens]] — Veja também: Estratégias de Autenticação no Cowrie: **`UserDB` (`etc/userdb.txt`)** vs. **`AuthRandom`** e Captura de Credenciais de Força Bruta.
- [[pacu-deteccao-honeytokens-canarytokens-aws-iam-detect-honeytokens]] — Referência cruzada direta com pacu-deteccao-honeytokens-canarytokens-aws-iam-detect-honeytokens.

## Fontes
- [Cowrie Official GitHub (`README.rst`) — Medium to High Interaction SSH and Telnet Honeypot](https://raw.githubusercontent.com/cowrie/cowrie/main/README.rst) — documentação oficial do Cowrie cobrindo os modos `shell`, `proxy` e `llm`, sistema de arquivos falso `fs.pickle`, utilitários `fsctl`/`createfs`/`playlog` e logs JSON; consultado em 2026-10-03.
- [Cowrie Official Configuration Reference (`src/cowrie/data/etc/cowrie.cfg.dist`)](https://raw.githubusercontent.com/cowrie/cowrie/main/src/cowrie/data/etc/cowrie.cfg.dist) — especificação completa dos parâmetros de configuração do Cowrie (`[honeypot]`, `auth_class`, `UserDB`, `AuthRandom`, `ttylog`, `download_limit_size`, `[backend_pool]`); consultado em 2026-10-03.
