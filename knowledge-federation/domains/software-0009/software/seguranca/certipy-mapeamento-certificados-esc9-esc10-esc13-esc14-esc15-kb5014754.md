---
id: software.seguranca.tranche12.001136
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

# Mapeamento Fraco de Certificados e Novas Classes (**`ESC9`, `ESC10`, `ESC13`, `ESC14`, `ESC15`/`EKUwu`, `ESC16` e `ESC17`**) e o Patch **`KB5014754`**

## Em uma frase
Por que um certificado emitido para uma conta modificada conseguia se autenticar como outra conta no Active Directory, e o que são as classes avançadas **`ESC9` a `ESC17`** suportadas pelo Certipy v5+?

## Por que importa
Para impedir ataques de falsificação de identidade via certificado (`CVE-2022-26923`), a Microsoft introduziu no patch **`KB5014754`** a extensão criptográfica **`szOID_NTDS_CA_SECURITY_EXT` (`1.3.6.1.4.1.311.25.2`)**, que grava o `objectSid` real do solicitante dentro do certificado emitido, além das chaves de registro **`StrongCertificateBindingEnforcement`** (no KDC) e **`CertificateMappingMethods`** (no Schannel). Quando o template possui a flag `CT_FLAG_NO_SECURITY_EXTENSION` (**`ESC9`**), quando o registro do DC permite mapeamento fraco por UPN/DNS no Schannel (**`ESC10`**), ou quando a própria CA está configurada para omitir a extensão de segurança globalmente (**`ESC16`**), um atacante que controla uma conta intermediária (ex.: permissão `GenericWrite` sobre uma conta `victimA`) pode renomear o `userPrincipalName` ou `dNSHostName` de `victimA` para `Administrator`, pedir um certificado e personificar o `Administrator`!

## Como funciona
Além disso, o Certipy detecta **`ESC13`** (templates que vinculam uma *Issuance Policy* OID a um grupo privilegiado do AD via atributo `msDS-OIDToGroupLink`), **`ESC14`** (abuso de mapeamentos explícitos fracos `altSecurityIdentities` como `X509:<I>...<SR>...`), **`ESC15` (`EKUwu` / `CVE-2024-49019`)** (injeção de Application Policies arbitrárias em templates de Schema Version 1) e **`ESC17`**!

## Exemplo
```bash
# Verificar em um Domain Controller via PowerShell se o StrongCertificateBindingEnforcement (KB5014754) esta em modo Full Enforcement (valor 2)
# (Execute no Domain Controller para validar a mitigacao de ESC6/ESC9/ESC10/ESC16)
reg query "HKLM\SYSTEM\CurrentControlSet\Services\Kdc" /v StrongCertificateBindingEnforcement
reg query "HKLM\SYSTEM\CurrentControlSet\Control\SecurityProviders\Schannel" /v CertificateMappingMethods
```

## Limites e trade-offs
Certifique-se de que todos os Domain Controllers da sua floresta estão atualizados com os patches cumulativos do **`KB5014754`** e operando em **Full Enforcement Mode (`StrongCertificateBindingEnforcement = 2`)**, onde o KDC rejeita qualquer certificado que não possua mapeamento forte por SID (`1.3.6.1.4.1.311.25.2`) ou mapeamento explícito forte por hash SHA-1/Emissor+Serial!

## Como verificar
Desative ou migre imediatamente quaisquer *Certificate Templates* legados ainda em **Schema Version 1** para eliminar a superfície do **`ESC15` (`CVE-2024-49019`)**.

## Conexões
- [[certipy-ataques-configuracao-ca-relay-esc6-esc8-esc11-epa-https]] — Veja também: Configurações Inseguras da CA e **NTLM Relay para AD CS (`ESC6`, `ESC8` e `ESC11`)**: Flag `EDITF_ATTRIBUTESUBJECTALTNAME2`, Web Enrollment HTTP e RPC.
- [[certipy-shadow-credentials-msds-keycredentiallink-whfb-pkinit]] — Veja também: Auditoria e Abuso de **Shadow Credentials (`msDS-KeyCredentialLink`)** com **`certipy shadow`**: Como Funciona o **Windows Hello for Business (WHfB)** no AD.
- [[certipy-arquitetura-auditoria-active-directory-certificate-services-adcs]] — Referência cruzada direta com certipy-arquitetura-auditoria-active-directory-certificate-services-adcs.
- [[certipy-autenticacao-pkinit-schannel-certipy-auth-unpac-the-hash]] — Referência cruzada direta com certipy-autenticacao-pkinit-schannel-certipy-auth-unpac-the-hash.

## Fontes
- [Certipy Official GitHub — Active Directory Certificate Services (AD CS) Attack & Enumeration Toolkit](https://raw.githubusercontent.com/ly4k/Certipy/main/README.md) — repositório oficial do Certipy cobrindo descoberta de CAs/Templates, identificação de vulnerabilidades ESC1–ESC17, Shadow Credentials e Golden Certificates; consultado em 2026-10-03.
- [Certipy Official Package & Architecture Specification (`pyproject.toml`)](https://raw.githubusercontent.com/ly4k/Certipy/main/pyproject.toml) — especificação técnica do pacote `certipy-ad` v5.1+ (`impacket`, `ldap3`, `cryptography`, `asn1crypto`, `neo4j`/BloodHound); consultado em 2026-10-03.
