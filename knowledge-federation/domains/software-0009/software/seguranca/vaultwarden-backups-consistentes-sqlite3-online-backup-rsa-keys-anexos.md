---
id: software.seguranca.tranche14.001329
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
fontes: ["https://raw.githubusercontent.com/dani-garcia/vaultwarden/main/README.md", "https://raw.githubusercontent.com/dani-garcia/vaultwarden/main/.env.template"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Estratégia de **Backup e Disaster Recovery** do Vaultwarden: Backup Online Atômico do **SQLite (`sqlite3 .backup`)**, Chaves **`rsa_key*`**, `attachments` e Criptografia **`age` / `GPG`**

## Em uma frase
Quais arquivos dentro do diretório `/data` do **Vaultwarden** são estritamente obrigatórios para restaurar 100% da instância em outro servidor, e por que simplesmente copiar `db.sqlite3` com `cp` enquanto o servidor está gravando em modo WAL (`db.sqlite3-wal`) pode gerar um backup corrompido?

## Por que importa
Quando o SQLite opera em modo **WAL (`ENABLE_DB_WAL=true`)**, transações recentes podem estar no arquivo `.sqlite3-wal` ainda não consolidadas no arquivo principal. Para criar um snapshot 100% atômico e consistente do banco SQLite com o Vaultwarden rodando online sem parar o container, utilize sempre o comando nativo **`sqlite3 /data/db.sqlite3 ".backup '/backup/db.sqlite3'"`**!

## Como funciona
E além do **`db.sqlite3`**, o seu pacote de backup do `/data` **DEVE incluir obrigatoriamente**: **(1) As chaves privadas/públicas `rsa_key.pem` e `rsa_key.pub.pem`** (usadas pelo Vaultwarden para assinar tokens Bearer JWT de sessão); **(2) O arquivo `config.json`** (se houver configurações salvas via `/admin`) e o `.env`; **(3) A pasta `attachments/`** (anexos cifrados dos cofres); e **(4) A pasta `sends/`**!

## Exemplo
```bash
# Realizar backup online atomico do banco SQLite3 do Vaultwarden, empacotar com chaves/anexos e cifrar com 'age' antes de enviar para S3/offsite
sqlite3 ./data/db.sqlite3 ".backup './data/db_backup_atomico.sqlite3'"
tar -czf - ./data/db_backup_atomico.sqlite3 ./data/rsa_key* ./data/attachments ./data/config.json \
  | age -r age1ql3z7hjy54pw3hyww5ayyfg7zqgvc7w3j2elw8zmrj2kg5sfn9aqmcac8p > ./backup_vaultwarden_$(date +%F).tar.gz.age
rm -f ./data/db_backup_atomico.sqlite3
```

## Limites e trade-offs
Embora os dados dos cofres dentro de `db.sqlite3` e `attachments/` já estejam cifrados client-side com as chaves dos usuários, o banco contém metadados em texto claro (como os endereços de e-mail dos usuários cadastrados, nomes de Organizações, IPs de login e `rsa_key.pem`): por isso, **sempre cifre o arquivo `.tar.gz` de backup com `age` ou `GPG` antes de enviá-lo para armazenamento em nuvem (S3 / Backblaze / Restic)**!

## Como verificar
Teste mensalmente a restauração do backup em um container isolado para validar tanto a integridade do `db.sqlite3` quanto a disponibilidade da chave privada de recuperação do `age`.

## Conexões
- [[vaultwarden-automacao-cli-bw-api-keys-ssh-agent-pipelines-devops]] — Veja também: Automação com **Bitwarden CLI (`bw`)**, **Personal API Keys (`client_id` / `client_secret`)** e **SSH Agent** Conectados ao Vaultwarden.
- [[vaultwarden-sso-directory-connector-ldap-scim-emergencia-enterprise]] — Veja também: Provisionamento Corporativo no Vaultwarden: **Bitwarden Directory Connector (LDAP / Active Directory / Entra ID / Okta)**, Notificações Push e Hardening de Container.
- [[vaultwarden-arquitetura-bitwarden-rust-zero-knowledge-sqlite-postgres]] — Referência cruzada direta com vaultwarden-arquitetura-bitwarden-rust-zero-knowledge-sqlite-postgres.
- [[kanidm-operacao-cli-kanidmd-certificados-backups-migracoes-json]] — Referência cruzada direta com kanidm-operacao-cli-kanidmd-certificados-backups-migracoes-json.

## Fontes
- [Vaultwarden Official GitHub Repository (`dani-garcia/vaultwarden`)](https://raw.githubusercontent.com/dani-garcia/vaultwarden/main/README.md) — repositório oficial do servidor Vaultwarden em Rust cobrindo compatibilidade com clientes Bitwarden, Organizations, Send, 2FA WebAuthn, Emergency Access e requisito HTTPS/Web Crypto API; consultado em 2026-10-03.
- [Vaultwarden Official Configuration Template (`.env.template`)](https://raw.githubusercontent.com/dani-garcia/vaultwarden/main/.env.template) — referência oficial de configuração `.env.template` do Vaultwarden cobrindo `ADMIN_TOKEN` Argon2 PHC, `SIGNUPS_ALLOWED`, `ENABLE_DB_WAL`, `IP_HEADER`, Rate Limiting e `ORG_EVENTS_ENABLED`; consultado em 2026-10-03.
