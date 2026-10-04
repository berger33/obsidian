---
id: software.seguranca.tranche14.001319
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-14.md"
fontes: ["https://raw.githubusercontent.com/kanidm/kanidm/master/README.md", "https://raw.githubusercontent.com/kanidm/kanidm/master/examples/server.toml"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Alta Disponibilidade e **Replicação Multi-Nó (`[replication]`)** no Kanidm: Sincronização via **mTLS** e Resolução de Conflitos por **CSN (*Change Sequence Number*)**

## Em uma frase
Como implantar o Kanidm em **Alta Disponibilidade (HA)** entre duas ou mais zonas de disponibilidade ou datacenters sem precisar gerenciar um cluster externo de banco de dados SQL?

## Por que importa
Inspirado na engenharia comprovada de servidores de diretório corporativos como o *389-ds*, o **Kanidm possui seu próprio protocolo nativo de replicação multi-nó (`[replication]` no `server.toml`)**!

## Como funciona
Cada nó `kanidmd` mantém sua cópia local completa do banco transacional `kanidm.db` (garantindo que leituras OIDC, WebAuthn, SSH e LDAPS sejam atendidas localmente em sub-milissegundos mesmo se o link WAN entre dois datacenters cair temporariamente!). Os nós sincronizam continuamente o estado entre si através de um canal dedicado autenticado por **Mutual TLS (mTLS) com certificados de nó pinados**, utilizando **Change Sequence Numbers (`CSN`)** e estados de atributo granulares (*Conflict-Free Replicated Data Types* — CRDTs em nível de atributo de entrada) para resolver automaticamente alterações concorrentes de forma determinística!

## Exemplo
```toml
# Exemplo de bloco [replication] no /etc/kanidm/server.toml para replicacao mTLS de alta disponibilidade entre dois nos Kanidm
[replication]
origin = "repl://idm-node1.interno.exemplo.br:8444"
bindaddress = "0.0.0.0:8444"

[replication."repl://idm-node2.interno.exemplo.br:8444"]
type = "mutual-pull"
partner_cert = "MII..."
automatic_refresh = false
```

## Limites e trade-offs
Veja como a configuração de confiança da replicação é blindada: cada nó gera seu próprio certificado de replicação (`kanidmd replication show-certificate`) e você fixa a chave pública exata do parceiro em **`partner_cert`** dentro do `server.toml` — garantindo que nenhum certificado emitido por CAs externas possa jamás se passar por um nó de replicação do seu diretório!

## Como verificar
Isole a porta de replicação (`:8444`) em uma VLAN privada ou malha **WireGuard** dedicada exclusivamente à comunicação entre os nós `kanidmd`.

## Conexões
- [[kanidm-ciclo-vida-identidades-valid-from-expire-recycle-bin-tombstones]] — Veja também: Governança de Ciclo de Vida de Contas no Kanidm: Janelas Temporais Automáticas (**`--valid-from` / `--expire`**), **Recycle Bin** e **Tombstones**.
- [[kanidm-operacao-cli-kanidmd-certificados-backups-migracoes-json]] — Veja também: Operação, Recuperação de Desastres e **Migrações Declarativas (`/etc/kanidm/migrations.d/`)** no Kanidm: `kanidmd database backup/restore` e `SIGHUP`.
- [[kanidm-arquitetura-idm-rust-banco-transacional-estrategia-zero-trust]] — Referência cruzada direta com kanidm-arquitetura-idm-rust-banco-transacional-estrategia-zero-trust.
- [[kanidm-configuracao-server-toml-domain-origin-zfs-backups-online]] — Referência cruzada direta com kanidm-configuracao-server-toml-domain-origin-zfs-backups-online.
- [[wireguard-arquitetura-protocolo-vpn-kernel-noise-ikpsk2-criptografia]] — Referência cruzada direta com wireguard-arquitetura-protocolo-vpn-kernel-noise-ikpsk2-criptografia.

## Fontes
- [Kanidm Official GitHub Repository (`kanidm/kanidm`)](https://raw.githubusercontent.com/kanidm/kanidm/master/README.md) — repositório oficial do servidor de gerenciamento de identidade Kanidm em Rust cobrindo WebAuthn/Passkeys, OAuth2/OIDC, LDAPS, RADIUS e clientes POSIX; consultado em 2026-10-03.
- [Kanidm Official Server Configuration Reference (`examples/server.toml`)](https://raw.githubusercontent.com/kanidm/kanidm/master/examples/server.toml) — especificação oficial de configuração do `kanidmd` (`server.toml`) cobrindo `bindaddress`, `ldapbindaddress`, TLS, `domain`, `origin`, `online_backup` e `trust_x_forward_for`; consultado em 2026-10-03.
