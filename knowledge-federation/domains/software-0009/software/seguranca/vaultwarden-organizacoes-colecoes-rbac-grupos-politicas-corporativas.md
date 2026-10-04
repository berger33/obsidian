---
id: software.seguranca.tranche14.001323
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

# Compartilhamento Corporativo no Vaultwarden: **Organizations**, **Collections**, Papéis RBAC (`Owner`, `Admin`, `Manager`, `User`), **Groups** e **Organization Policies**

## Em uma frase
Como estruturar o compartilhamento seguro de segredos entre equipes diferentes (ex.: `SRE`, `Backend`, `Financeiro`, `Marketing`) dentro do **Vaultwarden** garantindo o **Princípio do Privilégio Mínimo** e exigindo que todos os funcionários usem 2FA e senhas mestras fortes?

## Por que importa
Através da hierarquia de **Organizations & Collections** do Vaultwarden: **(1) Organization** é o contêiner corporativo que reúne os membros da empresa e aplica as **Organization Policies**; **(2) Collections** são as pastas criptografadas compartilhadas dentro da Organização (ex.: `Infra/Producao`, `Infra/Homolog`, `Financeiro/Bancos`), onde cada Collection possui sua permissão granular (`Read-Only`, `Hide Passwords`, `Can Edit`, `Can Manage`) atribuída a **Groups** ou usuários individuais!

## Como funciona
Nos **Member Roles**: **`Owner`** e **`Admin`** gerenciam toda a organização; **`Manager`** gerencia apenas as Collections às quais foi atribuído; e **`User`** acessa apenas as Collections liberadas para o seu grupo! E nas **Organization Policies**, você deve ativar obrigatoriamente: **`Two-step login` (exige 2FA ativo para entrar na Organização!)**, **`Master password requirements`** e **`Single organization`**!

## Exemplo
```bash
# Auditar via Bitwarden CLI (bw) conectada ao Vaultwarden a lista de Collections e membros da Organizacao
bw config server https://cofre.exemplo.br
bw list org-collections --organizationid "${ORG_UUID}" | jq .
```

## Limites e trade-offs
Como funciona a criptografia de uma **Organization** sem quebrar o modelo Zero-Knowledge? Quando a Organização é criada, o cliente gera uma **Chave Simétrica da Organização (`Org Symmetric Key`)** e um par de chaves RSA da Organização; para cada membro convidado e confirmado, a `Org Symmetric Key` é cifrada com a **Chave Pública RSA individual daquele membro**! Assim, nem mesmo o banco de dados do servidor Vaultwarden consegue ler os itens compartilhados da Organização!

## Como verificar
Use o recurso **Admin Password Reset (*Account Recovery*)** da Organização com extrema cautela e governança dual-control, pois ele permite que administradores designados redefinam a senha mestra de um funcionário que perdeu suas credenciais.

## Conexões
- [[vaultwarden-blindagem-painel-admin-token-argon2-phc-signups-allowed]] — Veja também: Hardening Crítico do **Vaultwarden**: Desabilitando Cadastros Abertos (**`SIGNUPS_ALLOWED=false`**), Convites e Protegendo o **`ADMIN_TOKEN` com Argon2id PHC**.
- [[vaultwarden-autenticacao-2fa-webauthn-fido2-yubikey-totp-duo-email]] — Veja também: Autenticação Multifator (**2FA**) e Derivação de Chave (**Argon2id Client-Side**) no Vaultwarden: **FIDO2 WebAuthn**, **YubiKey OTP**, **TOTP** e **Duo**.
- [[vaultwarden-arquitetura-bitwarden-rust-zero-knowledge-sqlite-postgres]] — Referência cruzada direta com vaultwarden-arquitetura-bitwarden-rust-zero-knowledge-sqlite-postgres.
- [[keepassxc-compartilhamento-equipes-keeshare-assinatura-merge-git]] — Referência cruzada direta com keepassxc-compartilhamento-equipes-keeshare-assinatura-merge-git.

## Fontes
- [Vaultwarden Official GitHub Repository (`dani-garcia/vaultwarden`)](https://raw.githubusercontent.com/dani-garcia/vaultwarden/main/README.md) — repositório oficial do servidor Vaultwarden em Rust cobrindo compatibilidade com clientes Bitwarden, Organizations, Send, 2FA WebAuthn, Emergency Access e requisito HTTPS/Web Crypto API; consultado em 2026-10-03.
- [Vaultwarden Official Configuration Template (`.env.template`)](https://raw.githubusercontent.com/dani-garcia/vaultwarden/main/.env.template) — referência oficial de configuração `.env.template` do Vaultwarden cobrindo `ADMIN_TOKEN` Argon2 PHC, `SIGNUPS_ALLOWED`, `ENABLE_DB_WAL`, `IP_HEADER`, Rate Limiting e `ORG_EVENTS_ENABLED`; consultado em 2026-10-03.
