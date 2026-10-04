---
id: software.seguranca.tranche12.001137
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

# Auditoria e Abuso de **Shadow Credentials (`msDS-KeyCredentialLink`)** com **`certipy shadow`**: Como Funciona o **Windows Hello for Business (WHfB)** no AD

## Em uma frase
Você sabia que um atacante com permissão de escrita (`GenericAll`, `GenericWrite` ou `WriteProperty`) sobre um objeto de usuário ou computador no Active Directory pode obter um TGT Kerberos e o hash NTLM daquela conta **mesmo sem existir nenhuma Autoridade Certificadora (AD CS) instalada no domínio**, desde que exista pelo menos um Domain Controller Windows Server 2016+ com certificado KDC?

## Por que importa
Essa técnica, descoberta por Elad Shamir e implementada nativamente no subcomando **`certipy shadow`**, abusa do atributo LDAP **`msDS-KeyCredentialLink`** — criado pela Microsoft para suportar autenticação sem senha do **Windows Hello for Business (WHfB)**!

## Como funciona
Quando você executa **`certipy shadow auto -u atacante@corp.interno -p ... -account vitima$`**, o Certipy gera localmente um par de chaves RSA e um certificado X.509 autoassinado, anexa a chave pública no atributo `msDS-KeyCredentialLink` da conta alvo via LDAP, autentica-se imediatamente via **Kerberos PKINIT** usando o certificado recém-registrado para recuperar o hash NT da conta (via *UnPAC-the-hash*) e, ao final do modo `auto`, **remove a entrada que adicionou do `msDS-KeyCredentialLink`** para não deixar rastros!

## Exemplo
```bash
# Auditar via LDAP (ldapsearch ou PowerShell) quais contas do dominio possuem entradas configuradas no atributo msDS-KeyCredentialLink
# Em ambientes que NAO utilizam Windows Hello for Business, esse atributo deve estar vazio!
ldapsearch -x -H ldap://10.10.10.5 \
  -D "auditor@corp.interno" -W \
  -b "DC=corp,DC=interno" \
  "(msDS-KeyCredentialLink=*)" sAMAccountName msDS-KeyCredentialLink
```

## Limites e trade-offs
Como detectar e prevenir **Shadow Credentials** no seu SOC? **(1)** Monitore no SIEM o **Event ID `5136`** (*A directory service object was modified*) sempre que o atributo **`AttributeLDAPDisplayName = msDS-KeyCredentialLink`** for modificado (especialmente se a sua organização não usa Windows Hello for Business on-premises!); e **(2)** Audite com BloodHound quem possui permissões `WriteProperty` / `AddKeyCredentialLink` sobre contas privilegiadas e computadores!

## Como verificar
Lembre-se de que por padrão a ACL `KeyCredentialLink` permite que contas de computador modifiquem seu próprio atributo `msDS-KeyCredentialLink` quando o WHfB está habilitado — o que torna ataques de NTLM Relay para LDAP (quando LDAP Signing / Channel Binding não estão exigidos!) altamente críticos.

## Conexões
- [[certipy-mapeamento-certificados-esc9-esc10-esc13-esc14-esc15-kb5014754]] — Veja também: Mapeamento Fraco de Certificados e Novas Classes (**`ESC9`, `ESC10`, `ESC13`, `ESC14`, `ESC15`/`EKUwu`, `ESC16` e `ESC17`**) e o Patch **`KB5014754`**.
- [[certipy-autenticacao-pkinit-schannel-certipy-auth-unpac-the-hash]] — Veja também: Autenticação via Certificado com **`certipy auth`**: **Kerberos PKINIT (`EventID 4768`)**, **UnPAC-the-Hash (`PAC_CREDENTIAL_INFO`)** e **LDAPS Schannel**.
- [[certipy-arquitetura-auditoria-active-directory-certificate-services-adcs]] — Referência cruzada direta com certipy-arquitetura-auditoria-active-directory-certificate-services-adcs.
- [[hayabusa-deteccao-ataques-active-directory-dcsync-kerberoasting-golden-ticket]] — Referência cruzada direta com hayabusa-deteccao-ataques-active-directory-dcsync-kerberoasting-golden-ticket.

## Fontes
- [Certipy Official GitHub — Active Directory Certificate Services (AD CS) Attack & Enumeration Toolkit](https://raw.githubusercontent.com/ly4k/Certipy/main/README.md) — repositório oficial do Certipy cobrindo descoberta de CAs/Templates, identificação de vulnerabilidades ESC1–ESC17, Shadow Credentials e Golden Certificates; consultado em 2026-10-03.
- [Certipy Official Package & Architecture Specification (`pyproject.toml`)](https://raw.githubusercontent.com/ly4k/Certipy/main/pyproject.toml) — especificação técnica do pacote `certipy-ad` v5.1+ (`impacket`, `ldap3`, `cryptography`, `asn1crypto`, `neo4j`/BloodHound); consultado em 2026-10-03.
