---
id: software.seguranca.tranche12.001160
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

# Engenharia de Deception na **Rede Interna (Intranet)** com Cowrie: Transformando Tentativas de Movimentação Lateral SSH em Alertas de Alta Fidelidade

## Em uma frase
Existe uma diferença gigantesca entre posicionar o **Cowrie na Internet pública** (onde ele receberá milhares de scans de botnets por dia para pesquisa de Threat Intelligence) e posicionar o **Cowrie dentro das VLANs internas de servidores corporativos** (onde **nenhum tráfego legítimo deveria jamais tentar fazer login SSH naquele IP**)!

## Por que importa
Na **Engenharia de Deception interna**, você implanta sensores leves do Cowrie em sub-redes críticas (VLAN de bancos de dados, VLAN de servidores de produção, sub-rede de gerenciamento) e planta referências ao IP do Cowrie dentro de arquivos **`~/.ssh/config`**, **`~/.ssh/known_hosts`** (sem `HashKnownHosts` nas iscas!) e variáveis de ambiente nas estações de desenvolvedores ou servidores de aplicação!

## Como funciona
Se um invasor comprometer a estação de um desenvolvedor ou um pod de aplicação e tentar usar o `~/.ssh/config` para pivotar via SSH para o host listado (`Host prod-vault-master`), ele conecta diretamente no seu Cowrie interno: **um único evento `cowrie.session.connect` ou `cowrie.login.*` em um Cowrie interno tem 0% de falso positivo e denuncia uma intrusão ativa em segundos**!

## Exemplo
```bash
# Monitorar em tempo real conexoes e logins em um sensor Cowrie interno e disparar alerta critico para qualquer interacao fora da allowlist de scanners
tail -F ./var/log/cowrie/cowrie.json | \
  jq --unbuffered 'select(.eventid == "cowrie.session.connect" or .eventid == "cowrie.login.success" or .eventid == "cowrie.login.failed") | {time: .timestamp, event: .eventid, attacker_ip: .src_ip, user: .username, pass: .password}'
```

## Limites e trade-offs
Lembre-se de excluir os IPs do seu próprio scanner interno de vulnerabilidades (Qualys, Nessus, OpenVAS, Nuclei) na regra de alerta do SIEM para que varreduras agendadas de conformidade não acionem o alarme de intrusão do honeypot.

## Como verificar
Combine o **Cowrie** (para interações profundas de shell SSH/Telnet e captura de payloads) com o **OpenCanary** (para emular dezenas de outros protocolos de rede como SMB, RDP, MySQL, Redis e HTTP no mesmo nó de Deception)!

## Conexões
- [[cowrie-modo-llm-inteligencia-artificial-emulacao-dinamica-comandos]] — Veja também: Emulação Dinâmica de Comandos com **IA Generativa (`backend = llm`)** no Cowrie: Como Responder a Qualquer Comando Inédito do Atacante.
- [[cowrie-arquitetura-honeypot-ssh-telnet-shell-proxy-llm]] — Referência cruzada direta com cowrie-arquitetura-honeypot-ssh-telnet-shell-proxy-llm.
- [[opencanary-arquitetura-honeypot-multiprotocolo-rede-interna-thinkst]] — Referência cruzada direta com opencanary-arquitetura-honeypot-multiprotocolo-rede-interna-thinkst.
- [[pacu-deteccao-honeytokens-canarytokens-aws-iam-detect-honeytokens]] — Referência cruzada direta com pacu-deteccao-honeytokens-canarytokens-aws-iam-detect-honeytokens.

## Fontes
- [Cowrie Official GitHub (`README.rst`) — Medium to High Interaction SSH and Telnet Honeypot](https://raw.githubusercontent.com/cowrie/cowrie/main/README.rst) — documentação oficial do Cowrie cobrindo os modos `shell`, `proxy` e `llm`, sistema de arquivos falso `fs.pickle`, utilitários `fsctl`/`createfs`/`playlog` e logs JSON; consultado em 2026-10-03.
- [Cowrie Official Configuration Reference (`src/cowrie/data/etc/cowrie.cfg.dist`)](https://raw.githubusercontent.com/cowrie/cowrie/main/src/cowrie/data/etc/cowrie.cfg.dist) — especificação completa dos parâmetros de configuração do Cowrie (`[honeypot]`, `auth_class`, `UserDB`, `AuthRandom`, `ttylog`, `download_limit_size`, `[backend_pool]`); consultado em 2026-10-03.
