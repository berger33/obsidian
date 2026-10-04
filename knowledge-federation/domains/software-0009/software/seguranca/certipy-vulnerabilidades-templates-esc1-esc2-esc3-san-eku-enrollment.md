---
id: software.seguranca.tranche12.001133
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
fontes: ["https://raw.githubusercontent.com/ly4k/Certipy/main/README.md", "https://raw.githubusercontent.com/ly4k/Certipy/main/pyproject.toml"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Anatomia e Mitigação de **`ESC1`, `ESC2` e `ESC3`**: Abuso de **`ENROLLEE_SUPPLIES_SUBJECT` (SAN)**, **Any Purpose EKU** e **Enrollment Agent**

## Em uma frase
As três vulnerabilidades mais clássicas de configuração de *Certificate Templates* no AD CS são **`ESC1`**, **`ESC2`** e **`ESC3`**, e todas permitem que um usuário de baixo privilégio escale instantaneamente para `Domain Admin` se o template conceder direito de `Enroll` para `Domain Users` ou `Authenticated Users`!

## Por que importa
**`ESC1`** ocorre quando um template combina: **(a)** permissão de `Enroll` para usuários comuns, **(b)** `Manager Approval` desativado, **(c)** nenhuma exigência de assinatura prévia (`Authorized Signatures = 0`), **(d)** EKU (*Extended Key Usage*) que permite autenticação no domínio (`Client Authentication 1.3.6.1.5.5.7.3.2`, `Smart Card Logon`, `PKINIT Client Authentication` ou `Any Purpose`), e **(e)** a flag fatal **`CT_FLAG_ENROLLEE_SUPPLIES_SUBJECT`** ativa — que permite ao solicitante especificar um **Subject Alternative Name (SAN / `-upn administrator@corp.interno`)** arbitrário no CSR!

## Como funciona
**`ESC2`** ocorre quando o template define o EKU como **`Any Purpose` (`2.5.29.37.0`)** ou não define nenhum EKU (*SubCA*), enquanto **`ESC3`** abusa de templates que emitem certificados de **`Certificate Request Agent` (`1.3.6.1.4.1.311.20.2.1`)**, permitindo que o portador solicite um segundo certificado em nome de qualquer outro usuário do domínio (`-on-behalf-of`)!

## Exemplo
```bash
# Auditar no JSON gerado pelo certipy find quais templates possuem Enrollee Supplies Subject ativo sem aprovacao de gerente
jq '.["Certificate Templates"] | to_entries[] | select(.value["Enrollee Supplies Subject"] == true and .value["CA Certificate Manager Approval"] == false) | {template: .value["Template Name"], vulnerabilities: .value["[!] Vulnerabilities"]}' \
  ./*_Certipy.json
```

## Limites e trade-offs
Como remediar definitivamente **`ESC1`, `ESC2` e `ESC3`** no console `certtmpl.msc` da sua PKI? **(1)** Nunca habilite *"Supply in the request"* na aba *Subject Name* para templates acessíveis a usuários ou máquinas comuns (ou exija obrigatoriamente **`CA certificate manager approval`** na aba *Issuance Requirements*!); **(2)** Restrinja a DACL de `Enroll` exclusivamente ao grupo específico que precisa do certificado; e **(3)** Despublique da Enterprise CA templates legados perigosos como `SubCA`!

## Como verificar
Monitore o Event ID **`4886`** e **`4887`** no log de Segurança da CA (com auditoria de AD CS ativada) verificando certificados emitidos cujo `Subject Alternative Name (SAN)` difere da conta solicitante (`Requester`).

## Conexões
- [[certipy-enumeracao-find-vulnerable-bloodhound-templates-cas-ldap]] — Veja também: Enumeração e Diagnóstico de AD CS com **`certipy find`**: Flag **`-vulnerable`**, Saída JSON/Stdout e Integração com **BloodHound**.
- [[certipy-permissoes-acls-esc4-esc5-esc7-writeproperty-manageca]] — Veja também: Controle de Acesso no AD CS (**`ESC4`, `ESC5` e `ESC7`**): ACLs Perigosas em Templates (`certipy template`) e na Autoridade Certificadora (`ManageCA` / `ManageCertificates`).
- [[certipy-arquitetura-auditoria-active-directory-certificate-services-adcs]] — Referência cruzada direta com certipy-arquitetura-auditoria-active-directory-certificate-services-adcs.
- [[certipy-autenticacao-pkinit-schannel-certipy-auth-unpac-the-hash]] — Referência cruzada direta com certipy-autenticacao-pkinit-schannel-certipy-auth-unpac-the-hash.

## Fontes
- [Certipy Official GitHub — Active Directory Certificate Services (AD CS) Attack & Enumeration Toolkit](https://raw.githubusercontent.com/ly4k/Certipy/main/README.md) — repositório oficial do Certipy cobrindo descoberta de CAs/Templates, identificação de vulnerabilidades ESC1–ESC17, Shadow Credentials e Golden Certificates; consultado em 2026-10-03.
- [Certipy Official Package & Architecture Specification (`pyproject.toml`)](https://raw.githubusercontent.com/ly4k/Certipy/main/pyproject.toml) — especificação técnica do pacote `certipy-ad` v5.1+ (`impacket`, `ldap3`, `cryptography`, `asn1crypto`, `neo4j`/BloodHound); consultado em 2026-10-03.
