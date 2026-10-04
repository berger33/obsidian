---
id: software.seguranca.tranche14.001313
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

# Autenticação Criptográfica no Kanidm: **Passkeys (WebAuthn)**, **Attested Passkeys (Verificação de Fabricante FIDO)** e Políticas de Credenciais por Grupo

## Em uma frase
O Kanidm foi projetado desde o primeiro dia ao redor de **Passkeys (WebAuthn / FIDO2)** como cidadão de primeira classe (mantendo inclusive a biblioteca oficial `webauthn-rs` do ecossistema Rust!). Qual é a diferença no Kanidm entre uma **Passkey padrão** e uma **Attested Passkey**, e como o Kanidm protege contas de alto privilégio?

## Por que importa
Uma **Passkey padrão** permite que o usuário se autentique sem senha usando qualquer autenticador WebAuthn (TouchID/FaceID do notebook/celular, gerenciador de senhas como KeePassXC/Bitwarden ou chave USB). Já uma **Attested Passkey** exige **Atestação Criptográfica de Hardware (*WebAuthn Attestation*)**: durante o registro da chave, o chip seguro da chave física (ex.: **YubiKey 5 FIPS** ou **Nitrokey**) apresenta um certificado X.509 de fábrica assinado pelo fabricante; o Kanidm verifica essa assinatura contra sua lista de autoridades de dispositivos confiáveis e **bloqueia o cadastro de qualquer autenticador emulado por software ou modelo de hardware não autorizado**!

## Como funciona
Além disso, através das **Credential Policies** associadas a grupos, você pode exigir automaticamente que membros de grupos sensíveis usem exclusivamente **Attested Passkeys** ou **MFA obrigatório**!

## Exemplo
```bash
# Gerar um token de sessao interativo de cadastro de credencial (Passkey / Attested Passkey / TOTP + Senha) para um usuario via CLI do Kanidm
kanidm person credential create-reset-token ana.silva --ttl 3600 -D idm_admin
kanidm person credential status ana.silva -D idm_admin
```

## Limites e trade-offs
Veja como o fluxo de onboarding de credenciais no Kanidm (`kanidm person credential create-reset-token`) é seguro: em vez de um administrador definir uma "senha temporária fraca" por telefone ou chat, o Kanidm gera um código/QR Code de uso único e duração curta (`--ttl 3600`) com o qual a própria usuária registra diretamente sua Passkey e seu MFA!

## Como verificar
Use **`kanidm person credential status <usuario>`** para auditar quais tipos de credenciais estão ativos na conta e se a conta atende às políticas de segurança dos grupos aos quais pertence.

## Conexões
- [[kanidm-configuracao-server-toml-domain-origin-zfs-backups-online]] — Veja também: Configuração Segura do **`server.toml`** no Kanidm: Consistência Estrita **`domain` / `origin` (WebAuthn)**, `http_client_address_info` (`proxy-v2`) e `[online_backup]`.
- [[kanidm-modelo-privilegios-separacao-admin-idm-admin-reauth-sudo]] — Veja também: Modelo de Privilégio Mínimo e **Reautenticação (`re-auth` Estilo `sudo`)** no Kanidm: Por que `admin` e `idm_admin` São Estritamente Separados?.
- [[kanidm-arquitetura-idm-rust-banco-transacional-estrategia-zero-trust]] — Referência cruzada direta com kanidm-arquitetura-idm-rust-banco-transacional-estrategia-zero-trust.
- [[authentik-autenticacao-webauthn-passkeys-totp-duo-mfa-obrigatorio]] — Referência cruzada direta com authentik-autenticacao-webauthn-passkeys-totp-duo-mfa-obrigatorio.
- [[keepassxc-integracao-navegador-nativa-nacl-passkeys-anti-phishing]] — Referência cruzada direta com keepassxc-integracao-navegador-nativa-nacl-passkeys-anti-phishing.

## Fontes
- [Kanidm Official GitHub Repository (`kanidm/kanidm`)](https://raw.githubusercontent.com/kanidm/kanidm/master/README.md) — repositório oficial do servidor de gerenciamento de identidade Kanidm em Rust cobrindo WebAuthn/Passkeys, OAuth2/OIDC, LDAPS, RADIUS e clientes POSIX; consultado em 2026-10-03.
- [Kanidm Official Server Configuration Reference (`examples/server.toml`)](https://raw.githubusercontent.com/kanidm/kanidm/master/examples/server.toml) — especificação oficial de configuração do `kanidmd` (`server.toml`) cobrindo `bindaddress`, `ldapbindaddress`, TLS, `domain`, `origin`, `online_backup` e `trust_x_forward_for`; consultado em 2026-10-03.
