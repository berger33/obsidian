---
id: software.seguranca.tranche14.001312
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

# Configuração Segura do **`server.toml`** no Kanidm: Consistência Estrita **`domain` / `origin` (WebAuthn)**, `http_client_address_info` (`proxy-v2`) e `[online_backup]`

## Em uma frase
Quais são as regras de segurança estruturais impostas pelo arquivo de configuração **`/etc/kanidm/server.toml`** (`version = "2"`) do Kanidm logo na inicialização do servidor?

## Por que importa
Primeiro, o Kanidm exige consistência criptográfica absoluta entre as diretivas **`domain = "idm.exemplo.br"`** e **`origin = "https://idm.exemplo.br"`**: o `domain` é usado para formar os *Security Principal Names (`spn`, ex.: `ana@idm.exemplo.br`)* e o `origin` é o Relying Party ID (RP ID) vinculado criptograficamente às chaves **WebAuthn / Passkeys**! Se `origin` não coincidir com `domain` (ou não for um subdomínio válido dele), **o `kanidmd` recusa-se a iniciar (*Fail-Closed*)**!

## Como funciona
Segundo, ao colocar um Load Balancer ou Proxy Reverso na frente do Kanidm (HTTPS `:443` ou LDAPS `:636`), o Kanidm recusa cabeçalhos de IP de cliente por padrão (`none`) até que você declare explicitamente os IPs confiáveis do proxy em **`[http_client_address_info]`** e **`[ldap_client_address_info]`**, recomendando fortemente o protocolo binário **`proxy-v2` (HAProxy PROXY protocol v2)** por ter muito menos sobrecarga e risco de parsing que cabeçalhos de texto!

## Exemplo
```toml
# Exemplo de /etc/kanidm/server.toml com TLS nativo, validacao estrita de origin WebAuthn, PROXY protocol v2 e backup online diario
version = "2"
bindaddress = "[::]:443"
ldapbindaddress = "[::]:636"
db_path = "/var/lib/private/kanidm/kanidm.db"
tls_chain = "/var/lib/private/kanidm/chain.pem"
tls_key = "/var/lib/private/kanidm/key.pem"
domain = "idm.exemplo.br"
origin = "https://idm.exemplo.br"

[http_client_address_info]
proxy-v2 = ["10.10.0.10/32"]

[online_backup]
path = "/var/lib/private/kanidm/backups/"
schedule = "00 22 * * *"
versions = 7
compression = "gzip"
```

## Limites e trade-offs
Atenção ao aviso oficial no `server.toml`: se um dia você precisar alterar o valor de **`domain`** após o servidor já estar em uso, **você deve executar imediatamente `kanidmd domain rename -c /etc/kanidm/server.toml`** (e estar ciente de que credenciais WebAuthn registradas sob o RP ID antigo precisarão ser recadastradas, pois o protocolo FIDO2 vincula cada Passkey ao domínio exato para impedir phishing!).

## Como verificar
Quando o arquivo `kanidm.db` residir em um dataset **ZFS**, configure `recordsize=64k` no ZFS e defina **`db_fs_type = "zfs"`** no `server.toml` (seguido de `kanidmd database vacuum`) para alinhar perfeitamente as páginas de 64 KB do banco com os blocos do sistema de arquivos!

## Conexões
- [[kanidm-arquitetura-idm-rust-banco-transacional-estrategia-zero-trust]] — Veja também: Arquitetura do **Kanidm (`kanidm/kanidm`)**: Plataforma Completa de Gerenciamento de Identidade (IDM) em **Rust** com Banco Transacional Próprio e Padrões Estritos.
- [[kanidm-autenticacao-passkeys-webauthn-attested-passkeys-politicas]] — Veja também: Autenticação Criptográfica no Kanidm: **Passkeys (WebAuthn)**, **Attested Passkeys (Verificação de Fabricante FIDO)** e Políticas de Credenciais por Grupo.
- [[kanidm-operacao-cli-kanidmd-certificados-backups-migracoes-json]] — Referência cruzada direta com kanidm-operacao-cli-kanidmd-certificados-backups-migracoes-json.
- [[rustls-arquitetura-tls-memory-safe-rust-cryptoprovider-aws-lc-ring]] — Referência cruzada direta com rustls-arquitetura-tls-memory-safe-rust-cryptoprovider-aws-lc-ring.

## Fontes
- [Kanidm Official GitHub Repository (`kanidm/kanidm`)](https://raw.githubusercontent.com/kanidm/kanidm/master/README.md) — repositório oficial do servidor de gerenciamento de identidade Kanidm em Rust cobrindo WebAuthn/Passkeys, OAuth2/OIDC, LDAPS, RADIUS e clientes POSIX; consultado em 2026-10-03.
- [Kanidm Official Server Configuration Reference (`examples/server.toml`)](https://raw.githubusercontent.com/kanidm/kanidm/master/examples/server.toml) — especificação oficial de configuração do `kanidmd` (`server.toml`) cobrindo `bindaddress`, `ldapbindaddress`, TLS, `domain`, `origin`, `online_backup` e `trust_x_forward_for`; consultado em 2026-10-03.
