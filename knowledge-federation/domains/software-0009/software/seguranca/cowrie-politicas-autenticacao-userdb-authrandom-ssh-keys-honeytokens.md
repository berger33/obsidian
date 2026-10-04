---
id: software.seguranca.tranche12.001153
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

# Estratégias de Autenticação no Cowrie: **`UserDB` (`etc/userdb.txt`)** vs. **`AuthRandom`** e Captura de Credenciais de Força Bruta

## Em uma frase
Quando um atacante tenta fazer login via SSH ou Telnet no Cowrie, qual combinação de usuário e senha deve ser aceita para deixá-lo entrar no shell emulado? O Cowrie oferece duas classes de autenticação configuráveis em **`auth_class`** dentro do `etc/cowrie.cfg`!

## Por que importa
A primeira é **`auth_class = UserDB` (padrão)**, que lê o arquivo **`etc/userdb.txt`** — onde cada linha possui o formato `<usuario>:<uid>:<padrao_senha>` suportando curingas `*` e negações `!` (por exemplo, `root:x:!root` rejeita a senha óbvia `root`, `root:x:!123456` rejeita `123456`, e `root:x:*` no final aceita qualquer outra senha)!

## Como funciona
A segunda estratégia — extremamente eficaz contra atacantes humanos que desconfiam quando acertam a senha na primeira tentativa — é **`auth_class = AuthRandom`** com **`auth_class_parameters = 2, 5, 10`**: o Cowrie rejeita as primeiras tentativas do atacante e **só permite o login após um número aleatório entre 2 e 5 tentativas**, memorizando em cache (`maxcache = 10`) aquela combinação exata de usuário/senha para que o invasor possa reconectar depois usando a mesma senha que "descobriu"!

## Exemplo
```ini
# Configurar em etc/cowrie.cfg o modo AuthRandom para simular resistencia realista a forca bruta antes de permitir o login
[honeypot]
hostname = prd-bastion-02
auth_class = AuthRandom
auth_class_parameters = 2, 5, 10
```

## Limites e trade-offs
Se você estiver posicionando o Cowrie na **rede interna corporativa** (como armadilha de movimentação lateral), o modo **`UserDB`** configurado com senhas específicas que você plantou em *honeytokens* (ou aceitando qualquer senha após a 1ª tentativa) garante que mesmo um atacante que teste apenas uma única credencial roubada entre na sessão monitorada e gere telemetria completa.

## Como verificar
Toda tentativa de login (bem-sucedida `cowrie.login.success` ou falha `cowrie.login.failed`), incluindo chaves públicas SSH apresentadas pelo cliente (`cowrie.client.fingerprint`), é gravada com timestamp UTC em `var/log/cowrie/cowrie.json`.

## Conexões
- [[cowrie-sistema-arquivos-falso-fs-pickle-fsctl-createfs-honeyfs]] — Veja também: Customização do Sistema de Arquivos Falso do Cowrie: **`fs.pickle`**, **`createfs`**, **`fsctl`**, **`honeyfs` (`contents_path`)** e **`txtcmds`**.
- [[cowrie-captura-malware-downloads-ttylog-playlog-asciinema]] — Veja também: Coleta Automática de Malware (**`var/lib/cowrie/downloads/`**) e Replay Visual de Sessões TTY com **`playlog`** e **`asciinema`**.
- [[cowrie-arquitetura-honeypot-ssh-telnet-shell-proxy-llm]] — Referência cruzada direta com cowrie-arquitetura-honeypot-ssh-telnet-shell-proxy-llm.
- [[cowrie-telemetria-json-siem-splunk-elastic-misp-threat-intel]] — Referência cruzada direta com cowrie-telemetria-json-siem-splunk-elastic-misp-threat-intel.

## Fontes
- [Cowrie Official GitHub (`README.rst`) — Medium to High Interaction SSH and Telnet Honeypot](https://raw.githubusercontent.com/cowrie/cowrie/main/README.rst) — documentação oficial do Cowrie cobrindo os modos `shell`, `proxy` e `llm`, sistema de arquivos falso `fs.pickle`, utilitários `fsctl`/`createfs`/`playlog` e logs JSON; consultado em 2026-10-03.
- [Cowrie Official Configuration Reference (`src/cowrie/data/etc/cowrie.cfg.dist`)](https://raw.githubusercontent.com/cowrie/cowrie/main/src/cowrie/data/etc/cowrie.cfg.dist) — especificação completa dos parâmetros de configuração do Cowrie (`[honeypot]`, `auth_class`, `UserDB`, `AuthRandom`, `ttylog`, `download_limit_size`, `[backend_pool]`); consultado em 2026-10-03.
