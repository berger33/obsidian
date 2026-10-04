---
id: software.seguranca.tranche12.001151
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

# Arquitetura do **Cowrie (`cowrie/cowrie`)**: Honeypot SSH e Telnet de Média e Alta Interação (`backend = shell`, `proxy` e `llm`)

## Em uma frase
Como capturar em tempo real as credenciais testadas por botnets, todos os comandos digitados pelo invasor após o login e uma cópia intacta de cada malware baixado via `wget`, `curl`, `scp` ou `sftp` — sem jamais colocar um servidor Linux real em risco de comprometimento?

## Por que importa
Mantido por Michel Oosterhof em Python 3.11+ (baseado na arquitetura Twisted/Conch e sucessor direto do histórico Kippo), o **Cowrie** é o **Honeypot SSH e Telnet de média a alta interação** mais utilizado no mundo por centros de pesquisa de ameaças, CERTs e equipes corporativas de Deception Engineering!

## Como funciona
O Cowrie opera em três modos de backend configuráveis em `etc/cowrie.cfg` (`backend = ...`): **(1) Modo `shell` (padrão — Média Interação)**: emula inteiramente em Python um sistema de arquivos UNIX completo (`fs.pickle` modelado sobre uma instalação Debian) e dezenas de comandos de terminal; **(2) Modo `proxy` (Alta Interação)**: atua como um proxy SSH/Telnet transparente que encaminha a sessão do atacante para um pool de máquinas virtuais reais gerenciadas via QEMU (`backend_pool`) enquanto grava 100% do tráfego e TTY; e **(3) Modo `llm` (Experimental)**: usa Large Language Models para sintetizar respostas realistas para qualquer comando inédito digitado pelo invasor!

## Exemplo
```bash
# Instalar o Cowrie em um ambiente virtual Python isolado, inicializar o diretorio de configuracao (etc/cowrie.cfg) e iniciar o honeypot
mkdir -p ~/meu-honeypot-cowrie && cd ~/meu-honeypot-cowrie
python3 -m venv cowrie-env && source cowrie-env/bin/activate
pip install cowrie
cowrie init
cowrie start
cowrie status
```

## Limites e trade-offs
Por segurança operacional fundamental, o daemon do Cowrie **nunca deve rodar como `root`**: ele escuta por padrão na porta não-privilegiada **`2222`** (para SSH) e **`2223`** (para Telnet), e você utiliza uma regra de redirecionamento de porta (`PREROUTING` no `nftables` ou `iptables`) para encaminhar o tráfego externo da porta `22` para a porta `2222`!

## Como verificar
Nunca edite o arquivo distribuído `src/cowrie/data/etc/cowrie.cfg.dist`: faça todas as suas customizações exclusivamente em `etc/cowrie.cfg` (criado por `cowrie init`).

## Conexões
- [[cowrie-sistema-arquivos-falso-fs-pickle-fsctl-createfs-honeyfs]] — Veja também: Customização do Sistema de Arquivos Falso do Cowrie: **`fs.pickle`**, **`createfs`**, **`fsctl`**, **`honeyfs` (`contents_path`)** e **`txtcmds`**.
- [[cowrie-captura-malware-downloads-ttylog-playlog-asciinema]] — Referência cruzada direta com cowrie-captura-malware-downloads-ttylog-playlog-asciinema.
- [[opencanary-arquitetura-honeypot-multiprotocolo-rede-interna-thinkst]] — Referência cruzada direta com opencanary-arquitetura-honeypot-multiprotocolo-rede-interna-thinkst.

## Fontes
- [Cowrie Official GitHub (`README.rst`) — Medium to High Interaction SSH and Telnet Honeypot](https://raw.githubusercontent.com/cowrie/cowrie/main/README.rst) — documentação oficial do Cowrie cobrindo os modos `shell`, `proxy` e `llm`, sistema de arquivos falso `fs.pickle`, utilitários `fsctl`/`createfs`/`playlog` e logs JSON; consultado em 2026-10-03.
- [Cowrie Official Configuration Reference (`src/cowrie/data/etc/cowrie.cfg.dist`)](https://raw.githubusercontent.com/cowrie/cowrie/main/src/cowrie/data/etc/cowrie.cfg.dist) — especificação completa dos parâmetros de configuração do Cowrie (`[honeypot]`, `auth_class`, `UserDB`, `AuthRandom`, `ttylog`, `download_limit_size`, `[backend_pool]`); consultado em 2026-10-03.
