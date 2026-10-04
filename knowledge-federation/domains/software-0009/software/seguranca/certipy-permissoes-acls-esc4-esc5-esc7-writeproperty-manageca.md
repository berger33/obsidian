---
id: software.seguranca.tranche12.001134
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

# Controle de Acesso no AD CS (**`ESC4`, `ESC5` e `ESC7`**): ACLs Perigosas em Templates (`certipy template`) e na Autoridade Certificadora (`ManageCA` / `ManageCertificates`)

## Em uma frase
E se todos os seus *Certificate Templates* estiverem configurados de forma segura (sem `ESC1`, `ESC2` ou `ESC3`), mas a **Lista de Controle de Acesso (DACL)** do próprio objeto do Template no Active Directory ou do servidor da CA conceder permissões de escrita a um grupo não-privilegiado?

## Por que importa
É exatamente isso que o Certipy detecta como **`ESC4`**, **`ESC5`** e **`ESC7`**: **`ESC4`** ocorre quando um usuário ou grupo não-administrativo possui permissões de modificação sobre o objeto LDAP de um Certificate Template (**`FullControl`**, **`WriteOwner`**, **`WriteDacl`** ou **`WriteProperty`**) — permitindo que um atacante use o comando **`certipy template -template <Nome> -save-old`** para alterar temporariamente as flags do template no AD (transformando-o em `ESC1`), emitir o certificado de `Domain Admin` e restaurar a configuração original segundos depois (`-configuration <arquivo.json>`)!

## Como funciona
**`ESC5`** abrange permissões inseguras na infraestrutura subjacente da PKI (servidor da CA, objetos PKI no container `CN=Public Key Services`), enquanto **`ESC7`** ocorre quando um usuário possui os direitos **`ManageCA`** (*CA Administrator*) ou **`ManageCertificates`** (*Certificate Officer*) diretamente na Autoridade Certificadora (permitindo habilitar o template `SubCA` ou aprovar manualmente a própria solicitação pendente via **`certipy ca -issue-request <ID>`**)!

## Exemplo
```bash
# Auditar no JSON do certipy find as permissoes de acesso (Access Rights) da Enterprise CA e identificar quem possui ManageCA ou ManageCertificates
jq '.["Certificate Authorities"] | to_entries[] | {ca_name: .value["CA Name"], access_rights: .value["Access Rights"], vulnerabilities: .value["[!] Vulnerabilities"]}' \
  ./*_Certipy.json
```

## Limites e trade-offs
A lição arquitetural da Microsoft para proteger contra `ESC4`, `ESC5` e `ESC7` é clara: **trate todo o servidor AD CS e todos os objetos de Certificate Templates como ativos de Tier 0 (mesmo nível de criticidade de um Domain Controller!)**, removendo quaisquer grupos de Tier 1/Tier 2 (como *Server Operators* ou *Helpdesk*) das ACLs dos templates e da segurança da CA (`certsrv.msc` -> *Properties* -> *Security*)!

## Como verificar
Monitore alterações em objetos `pKICertificateTemplate` no Active Directory (Event ID **`5136`** — *Directory Service Object Modified*, e Event ID **`4899`** / **`4900`** na CA).

## Conexões
- [[certipy-vulnerabilidades-templates-esc1-esc2-esc3-san-eku-enrollment]] — Veja também: Anatomia e Mitigação de **`ESC1`, `ESC2` e `ESC3`**: Abuso de **`ENROLLEE_SUPPLIES_SUBJECT` (SAN)**, **Any Purpose EKU** e **Enrollment Agent**.
- [[certipy-ataques-configuracao-ca-relay-esc6-esc8-esc11-epa-https]] — Veja também: Configurações Inseguras da CA e **NTLM Relay para AD CS (`ESC6`, `ESC8` e `ESC11`)**: Flag `EDITF_ATTRIBUTESUBJECTALTNAME2`, Web Enrollment HTTP e RPC.
- [[certipy-arquitetura-auditoria-active-directory-certificate-services-adcs]] — Referência cruzada direta com certipy-arquitetura-auditoria-active-directory-certificate-services-adcs.
- [[certipy-enumeracao-find-vulnerable-bloodhound-templates-cas-ldap]] — Referência cruzada direta com certipy-enumeracao-find-vulnerable-bloodhound-templates-cas-ldap.

## Fontes
- [Certipy Official GitHub — Active Directory Certificate Services (AD CS) Attack & Enumeration Toolkit](https://raw.githubusercontent.com/ly4k/Certipy/main/README.md) — repositório oficial do Certipy cobrindo descoberta de CAs/Templates, identificação de vulnerabilidades ESC1–ESC17, Shadow Credentials e Golden Certificates; consultado em 2026-10-03.
- [Certipy Official Package & Architecture Specification (`pyproject.toml`)](https://raw.githubusercontent.com/ly4k/Certipy/main/pyproject.toml) — especificação técnica do pacote `certipy-ad` v5.1+ (`impacket`, `ldap3`, `cryptography`, `asn1crypto`, `neo4j`/BloodHound); consultado em 2026-10-03.
